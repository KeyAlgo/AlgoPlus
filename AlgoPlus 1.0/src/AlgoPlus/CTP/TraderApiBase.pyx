# encoding:utf-8
# distutils: language=c++

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from cpython     cimport PyObject
from libc.string cimport const_char
from libcpp      cimport bool

import os
import ctypes
from datetime import datetime

from .cython2c.ThostFtdcUserApiStruct cimport *
from .cython2c.cTraderApi             cimport CTraderSpi, CTraderApi, CreateFtdcTraderApi

from .ApiStruct import *
from .ApiConst import *

from ..utils.check_service import check_service
from ..utils.base_field    import to_bytes, to_str



cdef class TraderApiBase:
    cdef CTraderApi *__api
    cdef CTraderSpi *__spi

    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    def __cinit__(self, broker_id, td_server, investor_id, password, app_id, auth_code, md_queue=None, 
                        page_dir='', private_resume_type=2, public_resume_type=2):
        try:
            # ############################################################################# #
            # 状态
            self.status = -1

            # ############################################################################# #
            self.__api = NULL
            self.__spi = NULL

            # ############################################################################# #
            self.__request_id = 0

            # ############################################################################# #
            self.front_id = None
            self.session_id = None

            # ############################################################################# #
            td_server = to_bytes(td_server)
            self.td_server = td_server if td_server.startswith(b'tcp://') else (b'tcp://' + td_server)
            self.broker_id = to_bytes(broker_id)
            self.investor_id = to_bytes(investor_id)
            self.password = to_bytes(password)
            self.app_id = to_bytes(app_id)
            self.auth_code = to_bytes(auth_code)

            # ############################################################################# #
            page_dir = os.path.join(to_str(page_dir), to_str(investor_id))
            self.page_dir = page_dir if page_dir.endswith(os.path.sep) else (page_dir + os.path.sep)
            flow_path = self.page_dir + 'td.con'
            tmp_dir = ''
            for dir in flow_path.split(os.path.sep):
                tmp_dir = os.path.join(tmp_dir, dir) + os.path.sep
                if not os.path.exists(tmp_dir):
                    os.mkdir(tmp_dir)

            self.private_resume_type = private_resume_type
            self.public_resume_type = public_resume_type

            # ############################################################################# #
            if self.__init_base() != 0:
                raise Exception('__init_base || 创建TraderApi与TraderSpi失败！')

            # ############################################################################# #
            info_list = self.td_server.split(b':')
            ip = to_str(info_list[1][2:])
            port = int(info_list[2])
            if not check_service(ip, port):
                raise Exception(f'check_service || 服务器{self.td_server}未开启！')

            # ############################################################################# #
            self.md_queue = md_queue
            self.order_ref = 0

            # ############################################################################# #
            self.init_extra()

            # ############################################################################# #
            if self.__init_net() != 0:
                raise Exception('__init_net || 交易初始化失败！')

        except Exception as err_msg:
            self.write_log('__cinit__', err_msg)

    # ############################################################################# #
    def init_extra(self):
        pass

    # ############################################################################# #
    def write_log(self, *args, sep=' || '):
        local_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{local_time}{sep}{self.investor_id}.td{sep}{sep.join(map(str, args))}')

    # ############################################################################# #
    def __dealloc__(self):
        try:
            self.Release()
        except Exception as err_msg:
            self.write_log('__dealloc__', err_msg)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    def req_qry_order(self):
        """
        查询订单。
        :return:
        """
        qry_order_field = QryOrderField(BrokerID=self.broker_id,
                                        InvestorID=self.investor_id)
        return self.ReqQryOrder(qry_order_field)

    def req_qry_trade(self):
        """
        查询成交。
        :return:
        """
        qry_trade_field = QryTradeField(BrokerID=self.broker_id,
                                        InvestorID=self.investor_id)
        return self.ReqQryTrade(qry_trade_field)

    def req_qry_investor_position(self):
        """
        查询持仓。
        :return:
        """
        qry_investor_position_field = QryInvestorPositionField(BrokerID=self.broker_id,
                                                               InvestorID=self.investor_id)
        return self.ReqQryInvestorPosition(qry_investor_position_field)

    def req_qry_investor_position_detail(self):
        """
        查询持仓明细。
        :return:
        """
        qry_investor_position_detail_field = QryInvestorPositionDetailField(BrokerID=self.broker_id,
                                                                            InvestorID=self.investor_id)
        return self.ReqQryInvestorPositionDetail(qry_investor_position_detail_field)

    def req_qry_trading_account(self):
        """
        查询资金。
        :return:
        """
        qry_trading_account_field = QryTradingAccountField(BrokerID=self.broker_id,
                                                           AccountID=self.investor_id,
                                                           CurrencyID=b'CNY',
                                                           BizType=BizType_Future)
        return self.ReqQryTradingAccount(qry_trading_account_field)

    def req_qry_instrument(self):
        qry_instrument_field = QryInstrumentField()
        self.ReqQryInstrument(qry_instrument_field)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    def inc_order_ref(self):
        """
        增加报单引用，用来标识订单。
        :return:
        """
        self.order_ref += 1

    def buy_open(self, exchange_id, instrument_id, order_price, order_vol):
        """
        买开仓。与卖平仓为一组对应交易。
        :param exchange_id: 交易所
        :param instrument_id: 合约
        :param order_price: 价格
        :param order_vol: 数量
        :return:
        """
        return self.req_order_insert(exchange_id, instrument_id, order_price, order_vol, Direction_Buy, OffsetFlag_Open)

    def sell_close(self, exchange_id, instrument_id, order_price, order_vol, is_today=True):
        """
        卖平仓。与买开仓为一组对应交易。SHFE与INE区分平今与平昨。
        :param exchange_id:
        :param instrument_id:
        :param order_price:
        :param order_vol:
        :param is_today:
        :return:
        """
        offset_flag = (OffsetFlag_CloseToday if is_today else OffsetFlag_CloseYesterday) if (exchange_id == b'SHFE' or exchange_id == b'INE') else OffsetFlag_Close
        return self.req_order_insert(exchange_id, instrument_id, order_price, order_vol, Direction_Sell, offset_flag)

    def sell_open(self, exchange_id, instrument_id, order_price, order_vol):
        """
        卖开仓。与买平仓为一组对应交易。
        :param exchange_id:
        :param instrument_id:
        :param order_price:
        :param order_vol:
        :return:
        """
        return self.req_order_insert(exchange_id, instrument_id, order_price, order_vol, Direction_Sell, OffsetFlag_Open)

    def buy_close(self, exchange_id, instrument_id, order_price, order_vol, is_today=True):
        """
        买平仓。与卖开仓为一组对应交易。SHFE与INE区分平今与平昨。
        :param exchange_id:
        :param instrument_id:
        :param order_price:
        :param order_vol:
        :param is_today:
        :return:
        """
        offset_flag = (OffsetFlag_CloseToday if is_today else OffsetFlag_CloseYesterday) if (exchange_id == b'SHFE' or exchange_id == b'INE') else OffsetFlag_Close
        return self.req_order_insert(exchange_id, instrument_id, order_price, order_vol, Direction_Buy, offset_flag)

    def req_order_insert(self, exchange_id, instrument_id, order_price, order_vol, direction, offset_flag):
        """
        录入报单请求。将订单结构体参数传递给父类方法ReqOrderInsert执行。
        :param exchange_id:交易所ID。
        :param instrument_id:合约ID。
        :param order_price:报单价格。
        :param order_vol:报单手数。
        :param direction:买卖方向。
        (‘买 : 0’,)
        (‘卖 : 1’,)
        :param offset_flag:开平标志，只有SHFE和INE区分平今、平昨。
        (‘开仓 : 0’,)
        (‘平仓 : 1’,)
        (‘强平 : 2’,)
        (‘平今 : 3’,)
        (‘平昨 : 4’,)
        (‘强减 : 5’,)
        (‘本地强平 : 6’,)
        :return:
        """
        result = -1
        try:
            self.inc_order_ref()
            input_order_field = InputOrderField(
                BrokerID=self.broker_id,
                InvestorID=self.investor_id,
                ExchangeID=exchange_id,
                InstrumentID=instrument_id,
                UserID=self.investor_id,
                OrderPriceType=OrderPriceType_LimitPrice,
                Direction=direction,
                CombOffsetFlag=offset_flag,
                CombHedgeFlag=HedgeFlag_Speculation,
                LimitPrice=order_price,
                VolumeTotalOriginal=order_vol,
                TimeCondition=TimeCondition_GFD,
                VolumeCondition=VolumeCondition_AV,
                MinVolume=1,
                ContingentCondition=ContingentCondition_Immediately,
                StopPrice=0,
                ForceCloseReason=ForceCloseReason_NotForceClose,
                IsAutoSuspend=0,
                OrderRef=to_bytes(self.order_ref),
            )
            result = self.ReqOrderInsert(input_order_field)
        except Exception as err_msg:
            self.write_log('req_order_insert', err_msg)
        finally:
            return result

    def req_order_action(self, exchange_id, instrument_id, order_ref, order_sysid=b''):
        """
        撤单请求。将撤单结构体参数传递给父类方法ReqOrderAction执行。
        :param exchange_id:交易所ID
        :param instrument_id:合约ID
        :param order_ref:报单引用，用来标识订单来源。根据该标识撤单。
        :param order_sysid:系统ID，当录入成功时，可在回报/通知中获取该字段。
        :return:
        """
        result = -1
        try:
            self.inc_order_ref()
            input_order_action_field = InputOrderActionField(
                BrokerID=self.broker_id,
                InvestorID=self.investor_id,
                OrderActionRef=self.order_ref,
                OrderRef=to_bytes(order_ref),
                FrontID=self.front_id,
                SessionID=self.session_id,
                ExchangeID=exchange_id,
                OrderSysID=order_sysid,
                ActionFlag=ActionFlag_Delete,
                UserID=self.investor_id,
                InstrumentID=instrument_id,
            )
            result = self.ReqOrderAction(input_order_action_field)
        except Exception as err_msg:
            self.write_log('req_order_action', err_msg)
        finally:
            return result



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///void CreateFtdcTraderApi
    # ///创建TraderApi
    # ///void Init()
    # ///初始化
    def __init_base(self):
        cdef int result = -1
        try:
            self.__api = CreateFtdcTraderApi(to_bytes(self.page_dir + 'td.con' + os.path.sep))
            if self.__api is NULL:
                raise MemoryError()
            self.__spi = new CTraderSpi(<PyObject *> self)
            if self.__spi is NULL:
                raise MemoryError()
            result = 0
        except Exception as err_msg:
            self.write_log('__init_base', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///注册回调接口
    def __init_net(self):
        cdef int result = -1
        try:
            if self.__api is NULL or self.__spi is NULL:
                raise Exception('交易接口未注册！')
            self.__api.RegisterSpi(self.__spi)
            self.SubscribePrivateTopic(self.private_resume_type)
            self.SubscribePublicTopic( self.public_resume_type)
            self.RegisterFront(self.td_server)
            # 初始化成功后OnFrontConnected会被回调
            self.__api.Init()
            result = 0
        except Exception as err_msg:
            self.write_log('__init_net', err_msg)
        finally:
            return result

    # ############################################################################# #
    def __inc_req_id(self):
        self.__request_id += 1
        return self.__request_id



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///获取API的版本信息
    @staticmethod
    def GetApiVersion(self):
        cdef const_char *result = ''
        try:
            result = CTraderApi.GetApiVersion()
        except Exception as err_msg:
            self.write_log('GetApiVersion', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///获取当前交易日
    def GetTradingDay(self):
        cdef const_char *result = ''
        try:
            with nogil:
                result = self.__api.GetTradingDay()
        except Exception as err_msg:
            self.write_log('GetTradingDay', err_msg)
        finally:
            return result



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///删除接口对象本身
    def Release(self):
        try:
            if self.__api is not NULL:
                self.__api.RegisterSpi(NULL)
                self.__api.Release()
                self.__api = NULL
                self.__spi = NULL
        except Exception as err_msg:
            self.write_log('Release', err_msg)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///等待接口线程结束运行
    def Join(self):
        cdef int result = -1
        try:
            if self.__api is not NULL:
                with nogil:
                    result = self.__api.Join()
        except Exception as err_msg:
            self.write_log('Join', err_msg)
        finally:
            return result



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///订阅私有流。
    def SubscribePrivateTopic(self, THOST_TE_RESUME_TYPE nResumeType):
        cdef int result = -1
        try:
            if self.__api is not NULL:
                with nogil:
                    self.__api.SubscribePrivateTopic(nResumeType)
                    result = 0
        except Exception as err_msg:
            self.write_log('SubscribePrivateTopic', err_msg)
        finally:
            return result

    # ############################################################################# #
    def SubscribePublicTopic(self, THOST_TE_RESUME_TYPE nResumeType):
        cdef int result = -1
        try:
            if self.__api is not NULL:
                with nogil:
                    self.__api.SubscribePublicTopic(nResumeType)
                    result = 0
        except Exception as err_msg:
            self.write_log('SubscribePublicTopic', err_msg)
        finally:
            return result


    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///注册前置机网络地址
    def RegisterFront(self, char *pszFrontAddress):
        cdef int result = -1
        try:
            if self.__api is not NULL:
                with nogil:
                    self.__api.RegisterFront(pszFrontAddress)
                    result = 0
        except Exception as err_msg:
            self.write_log('RegisterFront', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///注册名字服务器网络地址
    def RegisterNameServer(self, char *pszNsAddress):
        cdef int result = -1
        try:
            if self.__api is not NULL:
                with nogil:
                    self.__api.RegisterNameServer(pszNsAddress)
                    result = 0
        except Exception as err_msg:
            self.write_log('RegisterNameServer', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///注册名字服务器用户信息
    def RegisterFensUserInfo(self, pFensUserInfo):
        cdef int result = -1
        cdef size_t address = 0
        try:
            if self.__api is not NULL:
                address = addressof(pFensUserInfo)
                with nogil:
                    self.__api.RegisterFensUserInfo(<CThostFtdcFensUserInfoField *> address)
                    result = 0
        except Exception as err_msg:
            self.write_log('RegisterFensUserInfo', err_msg)
        finally:
            return result



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
    def OnFrontConnected(self):
        if self.status == -2:
            self.write_log('OnFrontConnected')

    # ############################################################################# #
    # ///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
    def OnFrontDisconnected(self, nReason):
        self.status = -2
        self.write_log('OnFrontDisconnected', nReason)

    # ############################################################################# #
    # ///心跳超时警告。当长时间未收到报文时，该方法被调用。
    def OnHeartBeatWarning(self, nTimeLapse):
        self.write_log('OnHeartBeatWarning', nTimeLapse)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///客户端认证请求
    def ReqAuthenticate(self, pReqAuthenticateField):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqAuthenticateField)
                with nogil:
                    result = self.__api.ReqAuthenticate(<CThostFtdcReqAuthenticateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqAuthenticate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///客户端认证响应
    def OnRspAuthenticate(self, pRspAuthenticateField, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspAuthenticate', pRspAuthenticateField)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///查询用户当前支持的认证模式
    def ReqUserAuthMethod(self, pReqUserAuthMethod):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqUserAuthMethod)
                with nogil:
                    result = self.__api.ReqUserAuthMethod(<CThostFtdcReqUserAuthMethodField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqUserAuthMethod', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///查询用户当前支持的认证模式的回复
    def OnRspUserAuthMethod(self, pRspUserAuthMethod, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspUserAuthMethod', pRspUserAuthMethod)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///注册用户终端信息，用于中继服务器多连接模式
    def RegisterUserSystemInfo(self, pUserSystemInfo):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pUserSystemInfo)
                with nogil:
                    result = self.__api.RegisterUserSystemInfo(<CThostFtdcUserSystemInfoField *> address)
        except Exception as err_msg:
            self.write_log('RegisterUserSystemInfo', err_msg)
        finally:
            return result



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///上报用户终端信息，用于中继服务器操作员登录模式
    def SubmitUserSystemInfo(self, pUserSystemInfo):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pUserSystemInfo)
                with nogil:
                    result = self.__api.SubmitUserSystemInfo(<CThostFtdcUserSystemInfoField *> address)
        except Exception as err_msg:
            self.write_log('SubmitUserSystemInfo', err_msg)
        finally:
            return result



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///用户登录请求
    def ReqUserLogin(self, pReqUserLogin):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqUserLogin)
                with nogil:
                    result = self.__api.ReqUserLogin(<CThostFtdcReqUserLoginField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqUserLogin', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///用户发出带有图片验证码的登陆请求
    def ReqUserLoginWithCaptcha(self, pReqUserLoginWithCaptcha):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqUserLoginWithCaptcha)
                with nogil:
                    result = self.__api.ReqUserLoginWithCaptcha(<CThostFtdcReqUserLoginWithCaptchaField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqUserLoginWithCaptcha', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///用户发出带有短信验证码的登陆请求
    def ReqUserLoginWithText(self, pReqUserLoginWithText):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqUserLoginWithText)
                with nogil:
                    result = self.__api.ReqUserLoginWithText(<CThostFtdcReqUserLoginWithTextField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqUserLoginWithText', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///用户发出带有动态口令的登陆请求
    def ReqUserLoginWithOTP(self, pReqUserLoginWithOTP):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqUserLoginWithOTP)
                with nogil:
                    result = self.__api.ReqUserLoginWithOTP(<CThostFtdcReqUserLoginWithOTPField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqUserLoginWithOTP', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///登录请求响应
    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspUserLogin', pRspUserLogin)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///用户发出获取图形验证码请求
    def ReqGenUserCaptcha(self, pReqGenUserCaptcha):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqGenUserCaptcha)
                with nogil:
                    result = self.__api.ReqGenUserCaptcha(<CThostFtdcReqGenUserCaptchaField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqGenUserCaptcha', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///获取图形验证码请求的回复
    def OnRspGenUserCaptcha(self, pRspGenUserCaptcha, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspGenUserCaptcha', pRspGenUserCaptcha)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///用户发出获取短信验证码请求
    def ReqGenUserText(self, pReqGenUserText):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqGenUserText)
                with nogil:
                    result = self.__api.ReqGenUserText(<CThostFtdcReqGenUserTextField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqGenUserText', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///获取短信验证码请求的回复
    def OnRspGenUserText(self, pRspGenUserText, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspGenUserText', pRspGenUserText)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///登出请求
    def ReqUserLogout(self, pUserLogout):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pUserLogout)
                with nogil:
                    result = self.__api.ReqUserLogout(<CThostFtdcUserLogoutField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqUserLogout', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///登出请求响应
    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspUserLogout', pUserLogout)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询投资者
    def ReqQryInvestor(self, pQryInvestor):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInvestor)
                with nogil:
                    result = self.__api.ReqQryInvestor(<CThostFtdcQryInvestorField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInvestor', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询投资者响应
    def OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInvestor', pInvestor)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///用户口令更新请求
    def ReqUserPasswordUpdate(self, pUserPasswordUpdate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pUserPasswordUpdate)
                with nogil:
                    result = self.__api.ReqUserPasswordUpdate(<CThostFtdcUserPasswordUpdateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqUserPasswordUpdate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///用户口令更新请求响应
    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspUserPasswordUpdate', pUserPasswordUpdate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///资金账户口令更新请求
    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pTradingAccountPasswordUpdate)
                with nogil:
                    result = self.__api.ReqTradingAccountPasswordUpdate(<CThostFtdcTradingAccountPasswordUpdateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqTradingAccountPasswordUpdate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///资金账户口令更新请求响应
    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspTradingAccountPasswordUpdate', pTradingAccountPasswordUpdate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询监控中心用户令牌
    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQueryCFMMCTradingAccountToken)
                with nogil:
                    result = self.__api.ReqQueryCFMMCTradingAccountToken(<CThostFtdcQueryCFMMCTradingAccountTokenField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQueryCFMMCTradingAccountToken', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询监控中心用户令牌
    def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQueryCFMMCTradingAccountToken', pQueryCFMMCTradingAccountToken)

    # ############################################################################# #
    # ///保证金监控中心用户令牌
    def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken):
        self.write_log('OnRtnCFMMCTradingAccountToken', pCFMMCTradingAccountToke)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///投资者结算结果确认
    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pSettlementInfoConfirm)
                with nogil:
                    result = self.__api.ReqSettlementInfoConfirm(<CThostFtdcSettlementInfoConfirmField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqSettlementInfoConfirm', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///投资者结算结果确认响应
    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspSettlementInfoConfirm', pSettlementInfoConfirm)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询结算信息确认
    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQrySettlementInfoConfirm)
                with nogil:
                    result = self.__api.ReqQrySettlementInfoConfirm(<CThostFtdcQrySettlementInfoConfirmField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQrySettlementInfoConfirm', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询结算信息确认响应
    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQrySettlementInfoConfirm', pSettlementInfoConfirm)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询投资者结算结果
    def ReqQrySettlementInfo(self, pQrySettlementInfo):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQrySettlementInfo)
                with nogil:
                    result = self.__api.ReqQrySettlementInfo(<CThostFtdcQrySettlementInfoField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQrySettlementInfo', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询投资者结算结果响应
    def OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQrySettlementInfo', pSettlementInfo)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///合约交易状态通知
    def OnRtnInstrumentStatus(self, pInstrumentStatus):
        self.write_log('OnRtnInstrumentStatus', pInstrumentStatus)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///错误应答
    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspError', pRspInfo)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///报单录入请求
    def ReqOrderInsert(self, pInputOrder):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputOrder)
                with nogil:
                    result = self.__api.ReqOrderInsert(<CThostFtdcInputOrderField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqOrderInsert', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///报单录入请求响应
    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspOrderInsert', pInputOrder)

    # ############################################################################# #
    # ///报单通知
    def OnRtnOrder(self, pOrder):
        self.write_log('OnRtnOrder', pOrder)

    # ############################################################################# #
    # ///成交通知
    def OnRtnTrade(self, pTrade):
        self.write_log('OnRtnTrade', pTrade)

    # ############################################################################# #
    # ///报单录入错误回报
    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        self.write_log('OnErrRtnOrderInsert', pRspInfo, pInputOrder)

    # ############################################################################# #
    # ///提示条件单校验错误
    def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder):
        self.write_log('OnRtnErrorConditionalOrder', pRspInfo, pErrorConditionalOrder)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询报单
    def ReqQryOrder(self, pQryOrder):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryOrder)
                with nogil:
                    result = self.__api.ReqQryOrder(<CThostFtdcQryOrderField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryOrder', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询报单响应
    def OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryOrder', pOrder)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询成交
    def ReqQryTrade(self, pQryTrade):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryTrade)
                with nogil:
                    result = self.__api.ReqQryTrade(<CThostFtdcQryTradeField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryTrade', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询成交响应
    def OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryTrade', pTrade)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///报单操作请求
    def ReqOrderAction(self, pInputOrderAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputOrderAction)
                with nogil:
                    result = self.__api.ReqOrderAction(<CThostFtdcInputOrderActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqOrderAction', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///撤单操作请求响应
    def OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspOrderAction', pInputOrderAction)

    # ############################################################################# #
    # ///撤单操作错误回报
    def OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        self.write_log('OnErrRtnOrderAction', pRspInfo, pOrderAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///批量报单操作请求
    def ReqBatchOrderAction(self, pInputBatchOrderAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputBatchOrderAction)
                with nogil:
                    result = self.__api.ReqBatchOrderAction(<CThostFtdcInputBatchOrderActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqBatchOrderAction', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///批量报单操作请求响应
    def OnRspBatchOrderAction(self, pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspBatchOrderAction', pInputBatchOrderAction)

    # ############################################################################# #
    # ///批量报单操作错误回报
    def OnErrRtnBatchOrderAction(self, pBatchOrderAction, pRspInfo):
        self.write_log('OnErrRtnBatchOrderAction', pRspInfo, pBatchOrderAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///预埋单录入请求
    def ReqParkedOrderInsert(self, pParkedOrder):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pParkedOrder)
                with nogil:
                    result = self.__api.ReqParkedOrderInsert(<CThostFtdcParkedOrderField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqParkedOrderInsert', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///预埋单录入请求响应
    def OnRspParkedOrderInsert(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspParkedOrderInsert', pParkedOrder)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询预埋单
    def ReqQryParkedOrder(self, pQryParkedOrder):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryParkedOrder)
                with nogil:
                    result = self.__api.ReqQryParkedOrder(<CThostFtdcQryParkedOrderField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryParkedOrder', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询预埋单响应
    def OnRspQryParkedOrder(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryParkedOrder', pParkedOrder)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求删除预埋单
    def ReqRemoveParkedOrder(self, pRemoveParkedOrder):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pRemoveParkedOrder)
                with nogil:
                    result = self.__api.ReqRemoveParkedOrder(<CThostFtdcRemoveParkedOrderField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqRemoveParkedOrder', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///删除预埋单响应
    def OnRspRemoveParkedOrder(self, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspRemoveParkedOrder', pRemoveParkedOrder)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///预埋撤单录入请求
    def ReqParkedOrderAction(self, pParkedOrderAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pParkedOrderAction)
                with nogil:
                    result = self.__api.ReqParkedOrderAction(<CThostFtdcParkedOrderActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqParkedOrderAction', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///预埋撤单录入请求响应
    def OnRspParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspParkedOrderAction', pParkedOrderAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询预埋撤单
    def ReqQryParkedOrderAction(self, pQryParkedOrderAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryParkedOrderAction)
                with nogil:
                    result = self.__api.ReqQryParkedOrderAction(<CThostFtdcQryParkedOrderActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryParkedOrderAction', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询预埋撤单响应
    def OnRspQryParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryParkedOrderAction', pParkedOrderAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求删除预埋撤单
    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pRemoveParkedOrderAction)
                with nogil:
                    result = self.__api.ReqRemoveParkedOrderAction(<CThostFtdcRemoveParkedOrderActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqRemoveParkedOrderAction', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///删除预埋撤单响应
    def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspRemoveParkedOrderAction', pRemoveParkedOrderAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///申请组合录入请求
    def ReqCombActionInsert(self, pInputCombAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputCombAction)
                with nogil:
                    result = self.__api.ReqCombActionInsert(<CThostFtdcInputCombActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqCombActionInsert', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///申请组合录入请求响应
    def OnRspCombActionInsert(self, pInputCombAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspCombActionInsert', pInputCombAction)

    # ############################################################################# #
    # ///申请组合通知
    def OnRtnCombAction(self, pCombAction):
        self.write_log('OnRtnCombAction', pCombAction)

    # ############################################################################# #
    # ///申请组合录入错误回报
    def OnErrRtnCombActionInsert(self, pInputCombAction, pRspInfo):
        self.write_log('OnErrRtnCombActionInsert', pRspInfo, pInputCombAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询申请组合
    def ReqQryCombAction(self, pQryCombAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryCombAction)
                with nogil:
                    result = self.__api.ReqQryCombAction(<CThostFtdcQryCombActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryCombAction', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询申请组合响应
    def OnRspQryCombAction(self, pCombAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryCombAction', pCombAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询资金账户
    def ReqQryTradingAccount(self, pQryTradingAccount):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryTradingAccount)
                with nogil:
                    result = self.__api.ReqQryTradingAccount(<CThostFtdcQryTradingAccountField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryTradingAccount', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询资金账户响应
    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryTradingAccount', pTradingAccount)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询资金账户
    def ReqQrySecAgentTradingAccount(self, pQryTradingAccount):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryTradingAccount)
                with nogil:
                    result = self.__api.ReqQrySecAgentTradingAccount(<CThostFtdcQryTradingAccountField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQrySecAgentTradingAccount', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询资金账户响应
    def OnRspQrySecAgentTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQrySecAgentTradingAccount', pTradingAccount)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询投资者持仓
    def ReqQryInvestorPosition(self, pQryInvestorPosition):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInvestorPosition)
                with nogil:
                    result = self.__api.ReqQryInvestorPosition(<CThostFtdcQryInvestorPositionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInvestorPosition', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询投资者持仓响应
    def OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInvestorPosition', pInvestorPosition)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询投资者持仓明细
    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInvestorPositionDetail)
                with nogil:
                    result = self.__api.ReqQryInvestorPositionDetail(<CThostFtdcQryInvestorPositionDetailField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInvestorPositionDetail', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询投资者持仓明细响应
    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInvestorPositionDetail', pInvestorPositionDetail)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询投资者持仓明细
    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInvestorPositionCombineDetail)
                with nogil:
                    result = self.__api.ReqQryInvestorPositionCombineDetail(<CThostFtdcQryInvestorPositionCombineDetailField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInvestorPositionCombineDetail', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询投资者持仓明细响应
    def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInvestorPositionCombineDetail', pInvestorPositionCombineDetail)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///报价录入请求
    def ReqQuoteInsert(self, pInputQuote):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputQuote)
                with nogil:
                    result = self.__api.ReqQuoteInsert(<CThostFtdcInputQuoteField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQuoteInsert', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///报价录入请求响应
    def OnRspQuoteInsert(self, pInputQuote, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQuoteInsert', pInputQuote)

    # ############################################################################# #
    # ///报价通知
    def OnRtnQuote(self, pQuote):
        self.write_log('OnRtnQuote', pQuote)

    # ############################################################################# #
    # ///报价录入错误回报
    def OnErrRtnQuoteInsert(self, pInputQuote, pRspInfo):
        self.write_log('OnErrRtnQuoteInsert', pRspInfo, pInputQuote)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询报价
    def ReqQryQuote(self, pQryQuote):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryQuote)
                with nogil:
                    result = self.__api.ReqQryQuote(<CThostFtdcQryQuoteField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryQuote', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询报价响应
    def OnRspQryQuote(self, pQuote, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryQuote', pQuote)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///报价操作请求
    def ReqQuoteAction(self, pInputQuoteAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputQuoteAction)
                with nogil:
                    result = self.__api.ReqQuoteAction(<CThostFtdcInputQuoteActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQuoteAction', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///报价操作请求响应
    def OnRspQuoteAction(self, pInputQuoteAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQuoteAction', pInputQuoteAction)

    # ############################################################################# #
    # ///报价操作错误回报
    def OnErrRtnQuoteAction(self, pQuoteAction, pRspInfo):
        self.write_log('OnErrRtnQuoteAction', pRspInfo, pQuoteAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///询价录入请求
    def ReqForQuoteInsert(self, pInputForQuote):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputForQuote)
                with nogil:
                    result = self.__api.ReqForQuoteInsert(<CThostFtdcInputForQuoteField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqForQuoteInsert', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///询价录入请求响应
    def OnRspForQuoteInsert(self, pInputForQuote, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspForQuoteInsert', pInputForQuote)

    # ############################################################################# #
    # ///询价通知
    def OnRtnForQuoteRsp(self, pForQuoteRsp):
        self.write_log('OnRtnForQuoteRsp', pForQuoteRsp)

    # ############################################################################# #
    # ///询价录入错误回报
    def OnErrRtnForQuoteInsert(self, pInputForQuote, pRspInfo):
        self.write_log('OnErrRtnForQuoteInsert', pRspInfo, pInputForQuote)



    # ############################################################################# #
    # ///请求查询询价
    def ReqQryForQuote(self, pQryForQuote):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryForQuote)
                with nogil:
                    result = self.__api.ReqQryForQuote(<CThostFtdcQryForQuoteField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryForQuote', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询询价响应
    def OnRspQryForQuote(self, pForQuote, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryForQuote', pForQuote)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///执行宣告录入请求
    def ReqExecOrderInsert(self, pInputExecOrder):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputExecOrder)
                with nogil:
                    result = self.__api.ReqExecOrderInsert(<CThostFtdcInputExecOrderField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqExecOrderInsert', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///执行宣告录入请求响应
    def OnRspExecOrderInsert(self, pInputExecOrder, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspExecOrderInsert', pInputExecOrder)

    # ############################################################################# #
    # ///执行宣告通知
    def OnRtnExecOrder(self, pExecOrder):
        self.write_log('OnRtnExecOrder', pExecOrder)

    # ############################################################################# #
    # ///执行宣告录入错误回报
    def OnErrRtnExecOrderInsert(self, pInputExecOrder, pRspInfo):
        self.write_log('OnErrRtnExecOrderInsert', pRspInfo, pInputExecOrder)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询执行宣告
    def ReqQryExecOrder(self, pQryExecOrder):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryExecOrder)
                with nogil:
                    result = self.__api.ReqQryExecOrder(<CThostFtdcQryExecOrderField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryExecOrder', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询执行宣告响应
    def OnRspQryExecOrder(self, pExecOrder, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryExecOrder', pExecOrder)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///执行宣告操作请求
    def ReqExecOrderAction(self, pInputExecOrderAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputExecOrderAction)
                with nogil:
                    result = self.__api.ReqExecOrderAction(<CThostFtdcInputExecOrderActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqExecOrderAction', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///执行宣告操作请求响应
    def OnRspExecOrderAction(self, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspExecOrderAction', pInputExecOrderAction)

    # ############################################################################# #
    # ///执行宣告操作错误回报
    def OnErrRtnExecOrderAction(self, pExecOrderAction, pRspInfo):
        self.write_log('OnErrRtnExecOrderAction', pRspInfo, pExecOrderAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///期权自对冲录入请求
    def ReqOptionSelfCloseInsert(self, pInputOptionSelfClose):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputOptionSelfClose)
                with nogil:
                    result = self.__api.ReqOptionSelfCloseInsert(<CThostFtdcInputOptionSelfCloseField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqOptionSelfCloseInsert', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///期权自对冲录入请求响应
    def OnRspOptionSelfCloseInsert(self, pInputOptionSelfClose, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspOptionSelfCloseInsert', pInputOptionSelfClose)

    # ############################################################################# #
    # ///期权自对冲通知
    def OnRtnOptionSelfClose(self, pOptionSelfClose):
        self.write_log('OnRtnOptionSelfClose', pOptionSelfClose)

    # ############################################################################# #
    # ///期权自对冲录入错误回报
    def OnErrRtnOptionSelfCloseInsert(self, pInputOptionSelfClose, pRspInfo):
        self.write_log('OnErrRtnOptionSelfCloseInsert', pRspInfo, pInputOptionSelfClose)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询期权自对冲
    def ReqQryOptionSelfClose(self, pQryOptionSelfClose):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryOptionSelfClose)
                with nogil:
                    result = self.__api.ReqQryOptionSelfClose(<CThostFtdcQryOptionSelfCloseField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryOptionSelfClose', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询期权自对冲响应
    def OnRspQryOptionSelfClose(self, pOptionSelfClose, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryOptionSelfClose', pOptionSelfClose)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///期权自对冲操作请求
    def ReqOptionSelfCloseAction(self, pInputOptionSelfCloseAction):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pInputOptionSelfCloseAction)
                with nogil:
                    result = self.__api.ReqOptionSelfCloseAction(<CThostFtdcInputOptionSelfCloseActionField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqOptionSelfCloseAction', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///期权自对冲操作请求响应
    def OnRspOptionSelfCloseAction(self, pInputOptionSelfCloseAction, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspOptionSelfCloseAction', pInputOptionSelfCloseAction)

    # ############################################################################# #
    # ///期权自对冲操作错误回报
    def OnErrRtnOptionSelfCloseAction(self, pOptionSelfCloseAction, pRspInfo):
        self.write_log('OnErrRtnOptionSelfCloseAction', pRspInfo, pOptionSelfCloseAction)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///期货发起银行资金转期货请求
    def ReqFromBankToFutureByFuture(self, pReqTransfer):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqTransfer)
                with nogil:
                    result = self.__api.ReqFromBankToFutureByFuture(<CThostFtdcReqTransferField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqFromBankToFutureByFuture', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///期货发起银行资金转期货应答
    def OnRspFromBankToFutureByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspFromBankToFutureByFuture', pReqTransfer)

    # ############################################################################# #
    # ///期货发起银行资金转期货通知
    def OnRtnFromBankToFutureByFuture(self, pRspTransfer):
        self.write_log('OnRtnFromBankToFutureByFuture', pRspTransfer)

    # ############################################################################# #
    # ///期货发起银行资金转期货错误回报
    def OnErrRtnBankToFutureByFuture(self, pReqTransfer, pRspInfo):
        self.write_log('OnErrRtnBankToFutureByFuture', pRspInfo, pReqTransfer)

    # ############################################################################# #
    # ///期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal):
        self.write_log('OnRtnRepealFromBankToFutureByFuture', pRspRepeal)

    # ############################################################################# #
    # ///系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal):
        self.write_log('OnRtnRepealFromBankToFutureByFutureManual', pRspRepeal)

    # ############################################################################# #
    # ///系统运行时期货端手工发起冲正银行转期货错误回报
    def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal, pRspInfo):
        self.write_log('OnErrRtnRepealBankToFutureByFutureManual', pRspInfo, pReqRepeal)

    # ############################################################################# #
    # ///银行发起银行资金转期货通知
    def OnRtnFromBankToFutureByBank(self, pRspTransfer):
        self.write_log('OnRtnFromBankToFutureByBank', pRspTransfer)

    # ############################################################################# #
    # ///银行发起冲正银行转期货通知
    def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal):
        self.write_log('OnRtnRepealFromBankToFutureByBank', pRspRepeal)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///期货发起期货资金转银行请求
    def ReqFromFutureToBankByFuture(self, pReqTransfer):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqTransfer)
                with nogil:
                    result = self.__api.ReqFromFutureToBankByFuture(<CThostFtdcReqTransferField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqFromFutureToBankByFuture', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///期货发起期货资金转银行应答
    def OnRspFromFutureToBankByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspFromFutureToBankByFuture', pReqTransfer)

    # ############################################################################# #
    # ///期货发起期货资金转银行通知
    def OnRtnFromFutureToBankByFuture(self, pRspTransfer):
        self.write_log('OnRtnFromFutureToBankByFuture', pRspTransfer)

    # ############################################################################# #
    # ///期货发起期货资金转银行错误回报
    def OnErrRtnFutureToBankByFuture(self, pReqTransfer, pRspInfo):
        self.write_log('OnErrRtnFutureToBankByFuture', pReqTransfer)

    # ############################################################################# #
    # ///期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal):
        self.write_log('OnRtnRepealFromFutureToBankByFuture', pRspRepeal)

    # ############################################################################# #
    # ///系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal):
        self.write_log('OnRtnRepealFromFutureToBankByFutureManual', pRspRepeal)

    # ############################################################################# #
    # ///系统运行时期货端手工发起冲正期货转银行错误回报
    def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal, pRspInfo):
        self.write_log('OnErrRtnRepealFutureToBankByFutureManual', pRspInfo, pReqRepeal)

    # ############################################################################# #
    # ///银行发起期货资金转银行通知
    def OnRtnFromFutureToBankByBank(self, pRspTransfer):
        self.write_log('OnRtnFromFutureToBankByBank', pRspTransfer)

    # ############################################################################# #
    # ///银行发起冲正期货转银行通知
    def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal):
        self.write_log('OnRtnRepealFromFutureToBankByBank', pRspRepeal)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///期货发起查询银行余额请求
    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqQueryAccount)
                with nogil:
                    result = self.__api.ReqQueryBankAccountMoneyByFuture(<CThostFtdcReqQueryAccountField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQueryBankAccountMoneyByFuture', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///期货发起查询银行余额应答
    def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQueryBankAccountMoneyByFuture', pReqQueryAccount)

    # ############################################################################# #
    # ///期货发起查询银行余额通知
    def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount):
        self.write_log('OnRtnQueryBankBalanceByFuture', pNotifyQueryAccount)

    # ############################################################################# #
    # ///期货发起查询银行余额错误回报
    def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount, pRspInfo):
        self.write_log('OnErrRtnQueryBankBalanceByFuture', pRspInfo, pReqQueryAccount)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询转帐流水
    def ReqQryTransferSerial(self, pQryTransferSerial):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryTransferSerial)
                with nogil:
                    result = self.__api.ReqQryTransferSerial(<CThostFtdcQryTransferSerialField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryTransferSerial', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询转帐流水响应
    def OnRspQryTransferSerial(self, pTransferSerial, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryTransferSerial', pTransferSerial)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询转帐银行
    def ReqQryTransferBank(self, pQryTransferBank):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryTransferBank)
                with nogil:
                    result = self.__api.ReqQryTransferBank(<CThostFtdcQryTransferBankField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryTransferBank', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询转帐银行响应
    def OnRspQryTransferBank(self, pTransferBank, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryTransferBank', pTransferBank)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询签约银行
    def ReqQryContractBank(self, pQryContractBank):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryContractBank)
                with nogil:
                    result = self.__api.ReqQryContractBank(<CThostFtdcQryContractBankField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryContractBank', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询签约银行响应
    def OnRspQryContractBank(self, pContractBank, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryContractBank', pContractBank)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询银期签约关系
    def ReqQryAccountregister(self, pQryAccountregister):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryAccountregister)
                with nogil:
                    result = self.__api.ReqQryAccountregister(<CThostFtdcQryAccountregisterField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryAccountregister', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询银期签约关系响应
    def OnRspQryAccountregister(self, pAccountregister, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryAccountregister', pAccountregister)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///银行发起银期开户通知
    def OnRtnOpenAccountByBank(self, pOpenAccount):
        self.write_log('OnRtnOpenAccountByBank', pOpenAccount)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///银行发起银期销户通知
    def OnRtnCancelAccountByBank(self, pCancelAccount):
        self.write_log('OnRtnCancelAccountByBank', pCancelAccount)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///银行发起变更银行账号通知
    def OnRtnChangeAccountByBank(self, pChangeAccount):
        self.write_log('OnRtnChangeAccountByBank', pChangeAccount)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询合约保证金率
    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInstrumentMarginRate)
                with nogil:
                    result = self.__api.ReqQryInstrumentMarginRate(<CThostFtdcQryInstrumentMarginRateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInstrumentMarginRate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询合约保证金率响应
    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInstrumentMarginRate', pInstrumentMarginRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询投资者品种/跨品种保证金
    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInvestorProductGroupMargin)
                with nogil:
                    result = self.__api.ReqQryInvestorProductGroupMargin(<CThostFtdcQryInvestorProductGroupMarginField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInvestorProductGroupMargin', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询投资者品种/跨品种保证金响应
    def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInvestorProductGroupMargin', pInvestorProductGroupMargin)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询交易所保证金率
    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryExchangeMarginRate)
                with nogil:
                    result = self.__api.ReqQryExchangeMarginRate(<CThostFtdcQryExchangeMarginRateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryExchangeMarginRate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询交易所保证金率响应
    def OnRspQryExchangeMarginRate(self, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryExchangeMarginRate', pExchangeMarginRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询交易所调整保证金率
    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryExchangeMarginRateAdjust)
                with nogil:
                    result = self.__api.ReqQryExchangeMarginRateAdjust(<CThostFtdcQryExchangeMarginRateAdjustField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryExchangeMarginRateAdjust', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询交易所调整保证金率响应
    def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryExchangeMarginRateAdjust', pExchangeMarginRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询合约手续费率
    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInstrumentCommissionRate)
                with nogil:
                    result = self.__api.ReqQryInstrumentCommissionRate(<CThostFtdcQryInstrumentCommissionRateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInstrumentCommissionRate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询合约手续费率响应
    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInstrumentCommissionRate', pInstrumentCommissionRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询做市商合约手续费率
    def ReqQryMMInstrumentCommissionRate(self, pQryMMInstrumentCommissionRate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryMMInstrumentCommissionRate)
                with nogil:
                    result = self.__api.ReqQryMMInstrumentCommissionRate(<CThostFtdcQryMMInstrumentCommissionRateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryMMInstrumentCommissionRate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询做市商合约手续费率响应
    def OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryMMInstrumentCommissionRate', pMMInstrumentCommissionRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询报单手续费
    def ReqQryInstrumentOrderCommRate(self, pQryInstrumentOrderCommRate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInstrumentOrderCommRate)
                with nogil:
                    result = self.__api.ReqQryInstrumentOrderCommRate(<CThostFtdcQryInstrumentOrderCommRateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInstrumentOrderCommRate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询报单手续费响应
    def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInstrumentOrderCommRate', pInstrumentOrderCommRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询期权合约手续费
    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryOptionInstrCommRate)
                with nogil:
                    result = self.__api.ReqQryOptionInstrCommRate(<CThostFtdcQryOptionInstrCommRateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryOptionInstrCommRate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询期权合约手续费响应
    def OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryOptionInstrCommRate', pOptionInstrCommRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询做市商期权合约手续费
    def ReqQryMMOptionInstrCommRate(self, pQryMMOptionInstrCommRate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryMMOptionInstrCommRate)
                with nogil:
                    result = self.__api.ReqQryMMOptionInstrCommRate(<CThostFtdcQryMMOptionInstrCommRateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryMMOptionInstrCommRate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询做市商期权合约手续费响应
    def OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryMMOptionInstrCommRate', pMMOptionInstrCommRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询期权交易成本
    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryOptionInstrTradeCost)
                with nogil:
                    result = self.__api.ReqQryOptionInstrTradeCost(<CThostFtdcQryOptionInstrTradeCostField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryOptionInstrTradeCost', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询期权交易成本
    def OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryOptionInstrTradeCost', pOptionInstrTradeCost)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询交易所
    def ReqQryExchange(self, pQryExchange):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryExchange)
                with nogil:
                    result = self.__api.ReqQryExchange(<CThostFtdcQryExchangeField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryExchange', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询交易所响应
    def OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryExchange', pExchange)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询合约
    def ReqQryInstrument(self, pQryInstrument):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInstrument)
                with nogil:
                    result = self.__api.ReqQryInstrument(<CThostFtdcQryInstrumentField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInstrument', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询合约响应
    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInstrument', pInstrument)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询交易编码
    def ReqQryTradingCode(self, pQryTradingCode):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryTradingCode)
                with nogil:
                    result = self.__api.ReqQryTradingCode(<CThostFtdcQryTradingCodeField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryTradingCode', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询交易编码响应
    def OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryTradingCode', pTradingCode)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询产品
    def ReqQryProduct(self, pQryProduct):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryProduct)
                with nogil:
                    result = self.__api.ReqQryProduct(<CThostFtdcQryProductField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryProduct', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询产品响应
    def OnRspQryProduct(self, pProduct, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryProduct', pProduct)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询产品报价汇率
    def ReqQryProductExchRate(self, pQryProductExchRate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryProductExchRate)
                with nogil:
                    result = self.__api.ReqQryProductExchRate(<CThostFtdcQryProductExchRateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryProductExchRate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询产品报价汇率
    def OnRspQryProductExchRate(self, pProductExchRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryProductExchRate', pProductExchRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询产品组
    def ReqQryProductGroup(self, pQryProductGroup):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryProductGroup)
                with nogil:
                    result = self.__api.ReqQryProductGroup(<CThostFtdcQryProductGroupField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryProductGroup', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询产品组响应
    def OnRspQryProductGroup(self, pProductGroup, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryProductGroup', pProductGroup)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询投资单元
    def ReqQryInvestUnit(self, pQryInvestUnit):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryInvestUnit)
                with nogil:
                    result = self.__api.ReqQryInvestUnit(<CThostFtdcQryInvestUnitField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryInvestUnit', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询投资单元响应
    def OnRspQryInvestUnit(self, pInvestUnit, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryInvestUnit', pInvestUnit)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询组合合约安全系数
    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryCombInstrumentGuard)
                with nogil:
                    result = self.__api.ReqQryCombInstrumentGuard(<CThostFtdcQryCombInstrumentGuardField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryCombInstrumentGuard', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询组合合约安全系数响应
    def OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryCombInstrumentGuard', pCombInstrumentGuard)



    # ############################################################################# #
    # ///交易所公告通知
    def OnRtnBulletin(self, pBulletin):
        self.write_log('OnRtnBulletin', pBulletin)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询行情
    def ReqQryDepthMarketData(self, pQryDepthMarketData):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryDepthMarketData)
                with nogil:
                    result = self.__api.ReqQryDepthMarketData(<CThostFtdcQryDepthMarketDataField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryDepthMarketData', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询行情响应
    def OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryDepthMarketData', pDepthMarketData)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///查询最大报单数量请求
    def ReqQueryMaxOrderVolume(self, pQueryMaxOrderVolume):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQueryMaxOrderVolume)
                with nogil:
                    result = self.__api.ReqQueryMaxOrderVolume(<CThostFtdcQueryMaxOrderVolumeField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQueryMaxOrderVolume', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///查询最大报单数量响应
    def OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQueryMaxOrderVolume', pQueryMaxOrderVolume)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询仓单折抵信息
    def ReqQryEWarrantOffset(self, pQryEWarrantOffset):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryEWarrantOffset)
                with nogil:
                    result = self.__api.ReqQryEWarrantOffset(<CThostFtdcQryEWarrantOffsetField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryEWarrantOffset', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询仓单折抵信息响应
    def OnRspQryEWarrantOffset(self, pEWarrantOffset, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryEWarrantOffset', pEWarrantOffset)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询汇率
    def ReqQryExchangeRate(self, pQryExchangeRate):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryExchangeRate)
                with nogil:
                    result = self.__api.ReqQryExchangeRate(<CThostFtdcQryExchangeRateField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryExchangeRate', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询汇率响应
    def OnRspQryExchangeRate(self, pExchangeRate, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryExchangeRate', pExchangeRate)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询客户通知
    def ReqQryNotice(self, pQryNotice):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryNotice)
                with nogil:
                    result = self.__api.ReqQryNotice(<CThostFtdcQryNoticeField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryNotice', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询客户通知响应
    def OnRspQryNotice(self, pNotice, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryNotice', pNotice)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询交易通知
    def ReqQryTradingNotice(self, pQryTradingNotice):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryTradingNotice)
                with nogil:
                    result = self.__api.ReqQryTradingNotice(<CThostFtdcQryTradingNoticeField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryTradingNotice', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询交易通知响应
    def OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryTradingNotice', pTradingNotice)

    # ############################################################################# #
    # ///交易通知
    def OnRtnTradingNotice(self, pTradingNoticeInfo):
        self.write_log('OnRtnTradingNotice', pTradingNoticeInfo)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询保证金监管系统经纪公司资金账户密钥
    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryCFMMCTradingAccountKey)
                with nogil:
                    result = self.__api.ReqQryCFMMCTradingAccountKey(<CThostFtdcQryCFMMCTradingAccountKeyField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryCFMMCTradingAccountKey', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///查询保证金监管系统经纪公司资金账户密钥响应
    def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryCFMMCTradingAccountKey', pCFMMCTradingAccountKey)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询经纪公司交易参数
    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryBrokerTradingParams)
                with nogil:
                    result = self.__api.ReqQryBrokerTradingParams(<CThostFtdcQryBrokerTradingParamsField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryBrokerTradingParams', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询经纪公司交易参数响应
    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryBrokerTradingParams', pBrokerTradingParams)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询经纪公司交易算法
    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQryBrokerTradingAlgos)
                with nogil:
                    result = self.__api.ReqQryBrokerTradingAlgos(<CThostFtdcQryBrokerTradingAlgosField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQryBrokerTradingAlgos', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询经纪公司交易算法响应
    def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQryBrokerTradingAlgos', pBrokerTradingAlgos)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询二级代理商信息
    def ReqQrySecAgentTradeInfo(self, pQrySecAgentTradeInfo):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQrySecAgentTradeInfo)
                with nogil:
                    result = self.__api.ReqQrySecAgentTradeInfo(<CThostFtdcQrySecAgentTradeInfoField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQrySecAgentTradeInfo', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询二级代理商信息响应
    def OnRspQrySecAgentTradeInfo(self, pSecAgentTradeInfo, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQrySecAgentTradeInfo', pSecAgentTradeInfo)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询二级代理商资金校验模式
    def ReqQrySecAgentCheckMode(self, pQrySecAgentCheckMode):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQrySecAgentCheckMode)
                with nogil:
                    result = self.__api.ReqQrySecAgentCheckMode(<CThostFtdcQrySecAgentCheckModeField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQrySecAgentCheckMode', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询二级代理商资金校验模式响应
    def OnRspQrySecAgentCheckMode(self, pSecAgentCheckMode, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQrySecAgentCheckMode', pSecAgentCheckMode)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///请求查询二级代理操作员银期权限
    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pQrySecAgentACIDMap)
                with nogil:
                    result = self.__api.ReqQrySecAgentACIDMap(<CThostFtdcQrySecAgentACIDMapField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqQrySecAgentACIDMap', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///请求查询二级代理操作员银期权限响应
    def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspQrySecAgentACIDMap', pSecAgentACIDMap)



# ///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
cdef extern int   TraderSpi_OnFrontConnected(self) except -1:
    try:
        req_authenticate = ReqAuthenticateField(BrokerID=self.broker_id,
                                                UserID=self.investor_id,
                                                AppID=self.app_id,
                                                AuthCode=self.auth_code)
        if self.ReqAuthenticate(req_authenticate) != 0:
            self.write_log('ReqAuthenticate', '认证申请失败！', req_authenticate)
        self.OnFrontConnected()
    except Exception as err_msg:
        self.write_log('OnFrontConnected', err_msg)
    return 0

# ///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
# ///@param nReason 错误原因
# ///        0x1001 网络读失败
# ///        0x1002 网络写失败
# ///        0x2001 接收心跳超时
# ///        0x2002 发送心跳失败
# ///        0x2003 收到错误报文
cdef extern int   TraderSpi_OnFrontDisconnected(self, int nReason) except -1:
    try:
        self.OnFrontDisconnected(nReason)
    except Exception as err_msg:
        self.write_log('OnFrontDisconnected', err_msg)
    return 0

# ///心跳超时警告。当长时间未收到报文时，该方法被调用。
# ///@param nTimeLapse 距离上次接收报文的时间
cdef extern int   TraderSpi_OnHeartBeatWarning(self, int nTimeLapse) except -1:
    try:
        self.OnHeartBeatWarning(nTimeLapse)
    except Exception as err_msg:
        self.write_log('OnHeartBeatWarning', err_msg)
    return 0

# ///客户端认证响应
cdef extern int   TraderSpi_OnRspAuthenticate(self, CThostFtdcRspAuthenticateField *pRspAuthenticateField,
                                                    CThostFtdcRspInfoField *pRspInfo,
                                                    int nRequestID,
                                                    bool bIsLast) except -1:
    try:
        if pRspAuthenticateField is not NULL:
            rsp_authenticate = RspAuthenticateField.from_address(<size_t> pRspAuthenticateField).to_dict()
            if pRspInfo is not NULL:
                rsp_info = RspInfoField.from_address(<size_t> pRspInfo).to_str_dict()
                if rsp_info['ErrorID'] == 0:
                    self.write_log('OnRspAuthenticate', f'认证成功:{rsp_authenticate}')
                    req_user_login = ReqUserLoginField(BrokerID=self.broker_id,
                                                       UserID=self.investor_id,
                                                       Password=self.password)
                    if self.ReqUserLogin(req_user_login) != 0:
                        self.write_log('ReqUserLogin', '登录交易账户失败！', req_user_login)
                else:
                    self.write_log('OnRspAuthenticate', f'认证失败:{rsp_info}')
            else:
                rsp_info = {}
        else:
            rsp_authenticate = {}

        self.OnRspAuthenticate(rsp_authenticate,
                               rsp_info,
                               nRequestID,
                               bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspAuthenticate', err_msg)
    return 0

# ///查询用户当前支持的认证模式的回复
cdef extern int   TraderSpi_OnRspUserAuthMethod(self, CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      bool bIsLast) except -1:
    try:
        self.OnRspUserAuthMethod({} if pRspUserAuthMethod is NULL else RspUserAuthMethodField.from_address(<size_t> pRspUserAuthMethod).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                 nRequestID,
                                 bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspUserAuthMethod', err_msg)
    return 0

# ///登录请求响应
cdef extern int   TraderSpi_OnRspUserLogin(self, CThostFtdcRspUserLoginField *pRspUserLogin,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 bool bIsLast) except -1:
    try:
        if pRspUserLogin is not NULL:
            rsp_user_login = RspUserLoginField.from_address(<size_t> pRspUserLogin).to_dict()
            if pRspInfo is not NULL:
              rsp_info = RspInfoField.from_address(<size_t> pRspInfo).to_str_dict()
              if rsp_info['ErrorID'] == 0:
                  self.front_id = rsp_user_login['FrontID']
                  self.session_id = rsp_user_login['SessionID']
                  req_settlement_info_confirm = SettlementInfoConfirmField(BrokerID=self.broker_id,
                                                                           InvestorID=self.investor_id)
                  if self.ReqSettlementInfoConfirm(req_settlement_info_confirm) != 0:
                      self.write_log('ReqSettlementInfoConfirm', '确认结算单失败！', req_settlement_info_confirm)
              else:
                  self.write_log('OnRspUserLogin', '登录交易账户失败！', rsp_info)
            else:
                rsp_info = {}
        else:
            rsp_user_login = {}

        self.OnRspUserLogin(rsp_user_login,
                            rsp_info,
                            nRequestID,
                            bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspUserLogin', err_msg)
    return 0

# ///获取图形验证码请求的回复
cdef extern int   TraderSpi_OnRspGenUserCaptcha(self, CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      bool bIsLast) except -1:
    try:
        self.OnRspGenUserCaptcha({} if pRspGenUserCaptcha is NULL else RspGenUserCaptchaField.from_address(<size_t> pRspGenUserCaptcha).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                 nRequestID,
                                 bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspGenUserCaptcha', err_msg)
    return 0

# ///获取短信验证码请求的回复
cdef extern int   TraderSpi_OnRspGenUserText(self, CThostFtdcRspGenUserTextField *pRspGenUserText,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   bool bIsLast) except -1:
    try:
        self.OnRspGenUserText({} if pRspGenUserText is NULL else RspGenUserTextField.from_address(<size_t> pRspGenUserText).to_dict(),
                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                              nRequestID,
                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspGenUserText', err_msg)
    return 0

# ///登出请求响应
cdef extern int   TraderSpi_OnRspUserLogout(self, CThostFtdcUserLogoutField *pUserLogout,
                                                  CThostFtdcRspInfoField *pRspInfo,
                                                  int nRequestID,
                                                  bool bIsLast) except -1:
    try:
        self.OnRspUserLogout({} if pUserLogout is NULL else UserLogoutField.from_address(<size_t> pUserLogout).to_dict(),
                             {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                             nRequestID,
                             bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspUserLogout', err_msg)
    return 0

# ///请求查询投资者响应
cdef extern int   TraderSpi_OnRspQryInvestor(self, CThostFtdcInvestorField *pInvestor,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   bool bIsLast) except -1:
    try:
        self.OnRspQryInvestor({} if pInvestor is NULL else InvestorField.from_address(<size_t> pInvestor).to_dict(),
                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                              nRequestID,
                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInvestor', err_msg)
    return 0

# ///用户口令更新请求响应
cdef extern int   TraderSpi_OnRspUserPasswordUpdate(self, CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate,
                                                          CThostFtdcRspInfoField *pRspInfo,
                                                          int nRequestID,
                                                          bool bIsLast) except -1:
    try:
        self.OnRspUserPasswordUpdate({} if pUserPasswordUpdate is NULL else UserPasswordUpdateField.from_address(<size_t> pUserPasswordUpdate).to_dict(),
                                     {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                     nRequestID,
                                     bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspUserPasswordUpdate', err_msg)
    return 0

# ///资金账户口令更新请求响应
cdef extern int   TraderSpi_OnRspTradingAccountPasswordUpdate(self, CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate,
                                                                    CThostFtdcRspInfoField *pRspInfo,
                                                                    int nRequestID,
                                                                    bool bIsLast) except -1:
    try:
        self.OnRspTradingAccountPasswordUpdate({} if pTradingAccountPasswordUpdate is NULL else TradingAccountPasswordUpdateField.from_address(<size_t> pTradingAccountPasswordUpdate).to_dict(),
                                               {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                               nRequestID,
                                               bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspTradingAccountPasswordUpdate', err_msg)
    return 0

# ///请求查询监控中心用户令牌
cdef extern int   TraderSpi_OnRspQueryCFMMCTradingAccountToken(self, CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken,
                                                                     CThostFtdcRspInfoField *pRspInfo,
                                                                     int nRequestID,
                                                                     bool bIsLast) except -1:
    try:
        self.OnRspQueryCFMMCTradingAccountToken({} if pQueryCFMMCTradingAccountToken is NULL else QueryCFMMCTradingAccountTokenField.from_address(<size_t> pQueryCFMMCTradingAccountToken).to_dict(),
                                                {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                                nRequestID,
                                                bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQueryCFMMCTradingAccountToken', err_msg)
    return 0

# ///保证金监控中心用户令牌
cdef extern int   TraderSpi_OnRtnCFMMCTradingAccountToken(self, CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) except -1:
    try:
        self.OnRtnCFMMCTradingAccountToken({} if pCFMMCTradingAccountToken is NULL else CFMMCTradingAccountTokenField.from_address(<size_t> pCFMMCTradingAccountToken).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnCFMMCTradingAccountToken', err_msg)
    return 0

# ///投资者结算结果确认响应
cdef extern int   TraderSpi_OnRspSettlementInfoConfirm(self, CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                                             CThostFtdcRspInfoField *pRspInfo,
                                                             int nRequestID,
                                                             bool bIsLast) except -1:
    try:
        if pSettlementInfoConfirm is not NULL:
            rsp_settlement_info_confirm = SettlementInfoConfirmField.from_address(<size_t> pSettlementInfoConfirm).to_dict()
            if pRspInfo is not NULL:
                rsp_info = RspInfoField.from_address(<size_t> pRspInfo).to_dict()
                if rsp_info['ErrorID'] == 0:
                    # 启动完成
                    self.status = 0
                    self.write_log('交易启动完毕', f'CTP版本号：{self.GetApiVersion(self)}', f'交易日:{self.GetTradingDay()}',
                                    f'server:{self.td_server}', f'broker_id:{self.broker_id}', f'investor_id:{self.investor_id}')
                else:
                    self.write_log('OnRspSettlementInfoConfirm', '确认结算单失败！', f'CTP版本号：{self.GetApiVersion(self)}', f'交易日:{self.GetTradingDay()}',
                                    f'server:{self.td_server}', f'broker_id:{self.broker_id}', f'investor_id:{self.investor_id}', rsp_settlement_info_confirm)
            else:
                rsp_info = {}
        else:
            rsp_settlement_info_confirm = {}

        self.OnRspSettlementInfoConfirm(rsp_settlement_info_confirm,
                                        rsp_info,
                                        nRequestID,
                                        bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspSettlementInfoConfirm', err_msg)
    return 0

# ///请求查询结算信息确认响应
cdef extern int   TraderSpi_OnRspQrySettlementInfoConfirm(self, CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                                                CThostFtdcRspInfoField *pRspInfo,
                                                                int nRequestID,
                                                                bool bIsLast) except -1:
    try:
        self.OnRspQrySettlementInfoConfirm({} if pSettlementInfoConfirm is NULL else SettlementInfoConfirmField.from_address(<size_t> pSettlementInfoConfirm).to_dict(),
                                           {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                           nRequestID,
                                           bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQrySettlementInfoConfirm', err_msg)
    return 0

# ///请求查询投资者结算结果响应
cdef extern int   TraderSpi_OnRspQrySettlementInfo(self, CThostFtdcSettlementInfoField *pSettlementInfo,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         bool bIsLast) except -1:
    try:
        self.OnRspQrySettlementInfo({} if pSettlementInfo is NULL else SettlementInfoField.from_address(<size_t> pSettlementInfo).to_dict(),
                                    {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                    nRequestID,
                                    bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQrySettlementInfo', err_msg)
    return 0

# ///合约交易状态通知
cdef extern int   TraderSpi_OnRtnInstrumentStatus(self, CThostFtdcInstrumentStatusField *pInstrumentStatus) except -1:
    try:
        self.OnRtnInstrumentStatus({} if pInstrumentStatus is NULL else InstrumentStatusField.from_address(<size_t> pInstrumentStatus).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnInstrumentStatus', err_msg)
    return 0

# ///错误应答
cdef extern int   TraderSpi_OnRspError(self, CThostFtdcRspInfoField *pRspInfo,
                                             int nRequestID,
                                             bool bIsLast) except -1:
    try:
        self.OnRspError({} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                        nRequestID,
                        bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspError', err_msg)
    return 0

# ///报单录入请求响应
cdef extern int   TraderSpi_OnRspOrderInsert(self, CThostFtdcInputOrderField *pInputOrder,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   bool bIsLast) except -1:
    try:
        self.OnRspOrderInsert({} if pInputOrder is NULL else InputOrderField.from_address(<size_t> pInputOrder).to_dict(),
                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                              nRequestID,
                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspOrderInsert', err_msg)
    return 0

# ///报单通知
cdef extern int   TraderSpi_OnRtnOrder(self, CThostFtdcOrderField *pOrder) except -1:
    try:
        self.OnRtnOrder({} if pOrder is NULL else OrderField.from_address(<size_t> pOrder).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnOrder', err_msg)
    return 0

# ///成交通知
cdef extern int   TraderSpi_OnRtnTrade(self, CThostFtdcTradeField *pTrade) except -1:
    try:
        self.OnRtnTrade({} if pTrade is NULL else TradeField.from_address(<size_t> pTrade).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnTrade', err_msg)
    return 0

# ///报单录入错误回报
cdef extern int   TraderSpi_OnErrRtnOrderInsert(self, CThostFtdcInputOrderField *pInputOrder,
                                                      CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnOrderInsert({} if pInputOrder is NULL else InputOrderField.from_address(<size_t> pInputOrder).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnOrderInsert', err_msg)
    return 0

# ///提示条件单校验错误
cdef extern int   TraderSpi_OnRtnErrorConditionalOrder(self, CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) except -1:
    try:
        self.OnRtnErrorConditionalOrder({} if pErrorConditionalOrder is NULL else ErrorConditionalOrderField.from_address(<size_t> pErrorConditionalOrder).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnErrorConditionalOrder', err_msg)
    return 0

# ///请求查询报单响应
cdef extern int   TraderSpi_OnRspQryOrder(self, CThostFtdcOrderField *pOrder,
                                                CThostFtdcRspInfoField *pRspInfo,
                                                int nRequestID,
                                                bool bIsLast) except -1:
    try:
        self.OnRspQryOrder({} if pOrder is NULL else OrderField.from_address(<size_t> pOrder).to_dict(),
                           {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                           nRequestID,
                           bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryOrder', err_msg)
    return 0

# ///请求查询成交响应
cdef extern int   TraderSpi_OnRspQryTrade(self, CThostFtdcTradeField *pTrade,
                                                CThostFtdcRspInfoField *pRspInfo,
                                                int nRequestID,
                                                bool bIsLast) except -1:
    try:
        self.OnRspQryTrade({} if pTrade is NULL else TradeField.from_address(<size_t> pTrade).to_dict(),
                           {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                           nRequestID,
                           bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryTrade', err_msg)
    return 0

# ///报单操作请求响应
cdef extern int   TraderSpi_OnRspOrderAction(self, CThostFtdcInputOrderActionField *pInputOrderAction,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   bool bIsLast) except -1:
    try:
        self.OnRspOrderAction({} if pInputOrderAction is NULL else InputOrderActionField.from_address(<size_t> pInputOrderAction).to_dict(),
                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                              nRequestID,
                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspOrderAction', err_msg)
    return 0

# ///报单操作错误回报
cdef extern int   TraderSpi_OnErrRtnOrderAction(self, CThostFtdcOrderActionField *pOrderAction,
                                                      CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnOrderAction({} if pOrderAction is NULL else OrderActionField.from_address(<size_t> pOrderAction).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnOrderAction', err_msg)
    return 0

# ///批量报单操作请求响应
cdef extern int   TraderSpi_OnRspBatchOrderAction(self, CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction,
                                                        CThostFtdcRspInfoField *pRspInfo,
                                                        int nRequestID,
                                                        bool bIsLast) except -1:
    try:
        self.OnRspBatchOrderAction({} if pInputBatchOrderAction is NULL else InputBatchOrderActionField.from_address(<size_t> pInputBatchOrderAction).to_dict(),
                                   {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                   nRequestID,
                                   bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspBatchOrderAction', err_msg)
    return 0

# ///批量报单操作错误回报
cdef extern int   TraderSpi_OnErrRtnBatchOrderAction(self, CThostFtdcBatchOrderActionField *pBatchOrderAction,
                                                           CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnBatchOrderAction({} if pBatchOrderAction is NULL else BatchOrderActionField.from_address(<size_t> pBatchOrderAction).to_dict(),
                                      {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnBatchOrderAction', err_msg)
    return 0

# ///预埋单录入请求响应
cdef extern int   TraderSpi_OnRspParkedOrderInsert(self, CThostFtdcParkedOrderField *pParkedOrder,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         bool bIsLast) except -1:
    try:
        self.OnRspParkedOrderInsert({} if pParkedOrder is NULL else ParkedOrderField.from_address(<size_t> pParkedOrder).to_dict(),
                                    {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                    nRequestID,
                                    bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspParkedOrderInsert', err_msg)
    return 0

# ///请求查询预埋单响应
cdef extern int   TraderSpi_OnRspQryParkedOrder(self, CThostFtdcParkedOrderField *pParkedOrder,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      bool bIsLast) except -1:
    try:
        self.OnRspQryParkedOrder({} if pParkedOrder is NULL else ParkedOrderField.from_address(<size_t> pParkedOrder).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                 nRequestID,
                                 bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryParkedOrder', err_msg)
    return 0

# ///删除预埋单响应
cdef extern int   TraderSpi_OnRspRemoveParkedOrder(self, CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         bool bIsLast) except -1:
    try:
        self.OnRspRemoveParkedOrder({} if pRemoveParkedOrder is NULL else RemoveParkedOrderField.from_address(<size_t> pRemoveParkedOrder).to_dict(),
                                    {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                    nRequestID,
                                    bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspRemoveParkedOrder', err_msg)
    return 0

# ///预埋撤单录入请求响应
cdef extern int   TraderSpi_OnRspParkedOrderAction(self, CThostFtdcParkedOrderActionField *pParkedOrderAction,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         bool bIsLast) except -1:
    try:
        self.OnRspParkedOrderAction({} if pParkedOrderAction is NULL else ParkedOrderActionField.from_address(<size_t> pParkedOrderAction).to_dict(),
                                    {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                    nRequestID,
                                    bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspParkedOrderAction', err_msg)
    return 0

# ///请求查询预埋撤单响应
cdef extern int   TraderSpi_OnRspQryParkedOrderAction(self, CThostFtdcParkedOrderActionField *pParkedOrderAction,
                                                            CThostFtdcRspInfoField *pRspInfo,
                                                            int nRequestID,
                                                            bool bIsLast) except -1:
    try:
        self.OnRspQryParkedOrderAction({} if pParkedOrderAction is NULL else ParkedOrderActionField.from_address(<size_t> pParkedOrderAction).to_dict(),
                                       {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                       nRequestID,
                                       bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryParkedOrderAction', err_msg)
    return 0

# ///删除预埋撤单响应
cdef extern int   TraderSpi_OnRspRemoveParkedOrderAction(self, CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction,
                                                               CThostFtdcRspInfoField *pRspInfo,
                                                               int nRequestID,
                                                               bool bIsLast) except -1:
    try:
        self.OnRspRemoveParkedOrderAction({} if pRemoveParkedOrderAction is NULL else RemoveParkedOrderActionField.from_address(<size_t> pRemoveParkedOrderAction).to_dict(),
                                          {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                          nRequestID,
                                          bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspRemoveParkedOrderAction', err_msg)
    return 0

# ///申请组合录入请求响应
cdef extern int   TraderSpi_OnRspCombActionInsert(self, CThostFtdcInputCombActionField *pInputCombAction,
                                                        CThostFtdcRspInfoField *pRspInfo,
                                                        int nRequestID,
                                                        bool bIsLast) except -1:
    try:
        self.OnRspCombActionInsert({} if pInputCombAction is NULL else InputCombActionField.from_address(<size_t> pInputCombAction).to_dict(),
                                   {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                   nRequestID,
                                   bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspCombActionInsert', err_msg)
    return 0

# ///申请组合通知
cdef extern int   TraderSpi_OnRtnCombAction(self, CThostFtdcCombActionField *pCombAction) except -1:
    try:
        self.OnRtnCombAction({} if pCombAction is NULL else CombActionField.from_address(<size_t> pCombAction)).to_dict()
    except Exception as err_msg:
        self.write_log('OnRtnCombAction', err_msg)
    return 0

# ///申请组合录入错误回报
cdef extern int   TraderSpi_OnErrRtnCombActionInsert(self, CThostFtdcInputCombActionField *pInputCombAction,
                                                           CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnCombActionInsert({} if pInputCombAction is NULL else InputCombActionField.from_address(<size_t> pInputCombAction).to_dict(),
                                      {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnCombActionInsert', err_msg)
    return 0

# ///请求查询申请组合响应
cdef extern int   TraderSpi_OnRspQryCombAction(self, CThostFtdcCombActionField *pCombAction,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     bool bIsLast) except -1:
    try:
        self.OnRspQryCombAction({} if pCombAction is NULL else CombActionField.from_address(<size_t> pCombAction).to_dict(),
                                {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                nRequestID,
                                bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryCombAction', err_msg)
    return 0

# ///请求查询资金账户响应
cdef extern int   TraderSpi_OnRspQryTradingAccount(self, CThostFtdcTradingAccountField *pTradingAccount,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         bool bIsLast) except -1:
    try:
        self.OnRspQryTradingAccount({} if pTradingAccount is NULL else TradingAccountField.from_address(<size_t> pTradingAccount).to_dict(),
                                    {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                    nRequestID,
                                    bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryTradingAccount', err_msg)
    return 0

# ///请求查询资金账户响应
cdef extern int   TraderSpi_OnRspQrySecAgentTradingAccount(self, CThostFtdcTradingAccountField *pTradingAccount,
                                                                 CThostFtdcRspInfoField *pRspInfo,
                                                                 int nRequestID,
                                                                 bool bIsLast) except -1:
    try:
        self.OnRspQrySecAgentTradingAccount({} if pTradingAccount is NULL else TradingAccountField.from_address(<size_t> pTradingAccount).to_dict(),
                                            {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                            nRequestID,
                                            bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQrySecAgentTradingAccount', err_msg)
    return 0

# ///请求查询投资者持仓响应
cdef extern int   TraderSpi_OnRspQryInvestorPosition(self, CThostFtdcInvestorPositionField *pInvestorPosition,
                                                           CThostFtdcRspInfoField *pRspInfo,
                                                           int nRequestID,
                                                           bool bIsLast) except -1:
    try:
        self.OnRspQryInvestorPosition({} if pInvestorPosition is NULL else InvestorPositionField.from_address(<size_t> pInvestorPosition).to_dict(),
                                      {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                      nRequestID,
                                      bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInvestorPosition', err_msg)
    return 0

# ///请求查询投资者持仓明细响应
cdef extern int   TraderSpi_OnRspQryInvestorPositionDetail(self, CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail,
                                                                 CThostFtdcRspInfoField *pRspInfo,
                                                                 int nRequestID,
                                                                 bool bIsLast) except -1:
    try:
        self.OnRspQryInvestorPositionDetail({} if pInvestorPositionDetail is NULL else InvestorPositionDetailField.from_address(<size_t> pInvestorPositionDetail).to_dict(),
                                            {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                            nRequestID,
                                            bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInvestorPositionDetail', err_msg)
    return 0

# ///请求查询投资者持仓明细响应
cdef extern int   TraderSpi_OnRspQryInvestorPositionCombineDetail(self, CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail,
                                                                        CThostFtdcRspInfoField *pRspInfo,
                                                                        int nRequestID,
                                                                        bool bIsLast) except -1:
    try:
        self.OnRspQryInvestorPositionCombineDetail({} if pInvestorPositionCombineDetail is NULL else InvestorPositionCombineDetailField.from_address(<size_t> pInvestorPositionCombineDetail).to_dict(),
                                                   {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                                   nRequestID,
                                                   bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInvestorPositionCombineDetail', err_msg)
    return 0

# ///报价录入请求响应
cdef extern int   TraderSpi_OnRspQuoteInsert(self, CThostFtdcInputQuoteField *pInputQuote,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   bool bIsLast) except -1:
    try:
        self.OnRspQuoteInsert({} if pInputQuote is NULL else InputQuoteField.from_address(<size_t> pInputQuote).to_dict(),
                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                              nRequestID,
                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQuoteInsert', err_msg)
    return 0

# ///报价通知
cdef extern int   TraderSpi_OnRtnQuote(self, CThostFtdcQuoteField *pQuote) except -1:
    try:
        self.OnRtnQuote({} if pQuote is NULL else QuoteField.from_address(<size_t> pQuote).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnQuote', err_msg)
    return 0

# ///报价录入错误回报
cdef extern int   TraderSpi_OnErrRtnQuoteInsert(self, CThostFtdcInputQuoteField *pInputQuote,
                                                      CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnQuoteInsert({} if pInputQuote is NULL else InputQuoteField.from_address(<size_t> pInputQuote).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnQuoteInsert', err_msg)
    return 0

# ///请求查询报价响应
cdef extern int   TraderSpi_OnRspQryQuote(self, CThostFtdcQuoteField *pQuote,
                                                CThostFtdcRspInfoField *pRspInfo,
                                                int nRequestID,
                                                bool bIsLast) except -1:
    try:
        self.OnRspQryQuote({} if pQuote is NULL else QuoteField.from_address(<size_t> pQuote).to_dict(),
                           {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                           nRequestID,
                           bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryQuote', err_msg)
    return 0

# ///报价操作请求响应
cdef extern int   TraderSpi_OnRspQuoteAction(self, CThostFtdcInputQuoteActionField *pInputQuoteAction,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   bool bIsLast) except -1:
    try:
        self.OnRspQuoteAction({} if pInputQuoteAction is NULL else InputQuoteActionField.from_address(<size_t> pInputQuoteAction).to_dict(),
                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                              nRequestID,
                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQuoteAction', err_msg)
    return 0

# ///报价操作错误回报
cdef extern int   TraderSpi_OnErrRtnQuoteAction(self, CThostFtdcQuoteActionField *pQuoteAction,
                                                      CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnQuoteAction({} if pQuoteAction is NULL else QuoteActionField.from_address(<size_t> pQuoteAction).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnQuoteAction', err_msg)
    return 0

# ///询价录入请求响应
cdef extern int   TraderSpi_OnRspForQuoteInsert(self, CThostFtdcInputForQuoteField *pInputForQuote,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      bool bIsLast) except -1:
    try:
        self.OnRspForQuoteInsert({} if pInputForQuote is NULL else InputForQuoteField.from_address(<size_t> pInputForQuote).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                 nRequestID,
                                 bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspForQuoteInsert', err_msg)
    return 0

# ///询价通知
cdef extern int   TraderSpi_OnRtnForQuoteRsp(self, CThostFtdcForQuoteRspField *pForQuoteRsp) except -1:
    try:
        self.OnRtnForQuoteRsp({} if pForQuoteRsp is NULL else ForQuoteRspField.from_address(<size_t> pForQuoteRsp).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnForQuoteRsp', err_msg)
    return 0

# ///询价录入错误回报
cdef extern int   TraderSpi_OnErrRtnForQuoteInsert(self, CThostFtdcInputForQuoteField *pInputForQuote,
                                                         CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnForQuoteInsert({} if pInputForQuote is NULL else InputForQuoteField.from_address(<size_t> pInputForQuote).to_dict(),
                                    {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnForQuoteInsert', err_msg)
    return 0

# ///请求查询询价响应
cdef extern int   TraderSpi_OnRspQryForQuote(self, CThostFtdcForQuoteField *pForQuote,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   bool bIsLast) except -1:
    try:
        self.OnRspQryForQuote({} if pForQuote is NULL else ForQuoteField.from_address(<size_t> pForQuote).to_dict(),
                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                              nRequestID,
                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryForQuote', err_msg)
    return 0

# ///执行宣告录入请求响应
cdef extern int   TraderSpi_OnRspExecOrderInsert(self, CThostFtdcInputExecOrderField *pInputExecOrder,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       bool bIsLast) except -1:
    try:
        self.OnRspExecOrderInsert({} if pInputExecOrder is NULL else InputExecOrderField.from_address(<size_t> pInputExecOrder).to_dict(),
                                  {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                  nRequestID,
                                  bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspExecOrderInsert', err_msg)
    return 0

# ///执行宣告通知
cdef extern int   TraderSpi_OnRtnExecOrder(self, CThostFtdcExecOrderField *pExecOrder) except -1:
    try:
        self.OnRtnExecOrder({} if pExecOrder is NULL else ExecOrderField.from_address(<size_t> pExecOrder).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnExecOrder', err_msg)
    return 0

# ///执行宣告录入错误回报
cdef extern int   TraderSpi_OnErrRtnExecOrderInsert(self, CThostFtdcInputExecOrderField *pInputExecOrder,
                                                          CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnExecOrderInsert({} if pInputExecOrder is NULL else InputExecOrderField.from_address(<size_t> pInputExecOrder).to_dict(),
                                     {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnExecOrderInsert', err_msg)
    return 0

# ///请求查询执行宣告响应
cdef extern int   TraderSpi_OnRspQryExecOrder(self, CThostFtdcExecOrderField *pExecOrder,
                                                    CThostFtdcRspInfoField *pRspInfo,
                                                    int nRequestID,
                                                    bool bIsLast) except -1:
    try:
        self.OnRspQryExecOrder({} if pExecOrder is NULL else ExecOrderField.from_address(<size_t> pExecOrder).to_dict(),
                               {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                               nRequestID,
                               bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryExecOrder', err_msg)
    return 0

# ///执行宣告操作请求响应
cdef extern int   TraderSpi_OnRspExecOrderAction(self, CThostFtdcInputExecOrderActionField *pInputExecOrderAction,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       bool bIsLast) except -1:
    try:
        self.OnRspExecOrderAction({} if pInputExecOrderAction is NULL else InputExecOrderActionField.from_address(<size_t> pInputExecOrderAction).to_dict(),
                                  {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                  nRequestID,
                                  bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspExecOrderAction', err_msg)
    return 0

# ///执行宣告操作错误回报
cdef extern int   TraderSpi_OnErrRtnExecOrderAction(self, CThostFtdcExecOrderActionField *pExecOrderAction,
                                                          CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnExecOrderAction({} if pExecOrderAction is NULL else ExecOrderActionField.from_address(<size_t> pExecOrderAction).to_dict(),
                                     {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnExecOrderAction', err_msg)
    return 0

# ///期权自对冲录入请求响应
cdef extern int   TraderSpi_OnRspOptionSelfCloseInsert(self, CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose,
                                                             CThostFtdcRspInfoField *pRspInfo,
                                                             int nRequestID,
                                                             bool bIsLast) except -1:
    try:
        self.OnRspOptionSelfCloseInsert({} if pInputOptionSelfClose is NULL else InputOptionSelfCloseField.from_address(<size_t> pInputOptionSelfClose).to_dict(),
                                        {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                        nRequestID,
                                        bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspOptionSelfCloseInsert', err_msg)
    return 0

# ///期权自对冲通知
cdef extern int   TraderSpi_OnRtnOptionSelfClose(self, CThostFtdcOptionSelfCloseField *pOptionSelfClose) except -1:
    try:
        self.OnRtnOptionSelfClose({} if pOptionSelfClose is NULL else OptionSelfCloseField.from_address(<size_t> pOptionSelfClose).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnOptionSelfClose', err_msg)
    return 0

# ///期权自对冲录入错误回报
cdef extern int   TraderSpi_OnErrRtnOptionSelfCloseInsert(self, CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose,
                                                                CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnOptionSelfCloseInsert({} if pInputOptionSelfClose is NULL else InputOptionSelfCloseField.from_address(<size_t> pInputOptionSelfClose).to_dict(),
                                           {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnOptionSelfCloseInsert', err_msg)
    return 0

# ///请求查询期权自对冲响应
cdef extern int   TraderSpi_OnRspQryOptionSelfClose(self, CThostFtdcOptionSelfCloseField *pOptionSelfClose,
                                                          CThostFtdcRspInfoField *pRspInfo,
                                                          int nRequestID,
                                                          bool bIsLast) except -1:
    try:
        self.OnRspQryOptionSelfClose({} if pOptionSelfClose is NULL else OptionSelfCloseField.from_address(<size_t> pOptionSelfClose).to_dict(),
                                     {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                     nRequestID,
                                     bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryOptionSelfClose', err_msg)
    return 0

# ///期权自对冲操作请求响应
cdef extern int   TraderSpi_OnRspOptionSelfCloseAction(self, CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction,
                                                             CThostFtdcRspInfoField *pRspInfo,
                                                             int nRequestID,
                                                             bool bIsLast) except -1:
    try:
        self.OnRspOptionSelfCloseAction({} if pInputOptionSelfCloseAction is NULL else InputOptionSelfCloseActionField.from_address(<size_t> pInputOptionSelfCloseAction).to_dict(),
                                        {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                        nRequestID,
                                        bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspOptionSelfCloseAction', err_msg)
    return 0

# ///期权自对冲操作错误回报
cdef extern int   TraderSpi_OnErrRtnOptionSelfCloseAction(self, CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction,
                                                                CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnOptionSelfCloseAction({} if pOptionSelfCloseAction is NULL else OptionSelfCloseActionField.from_address(<size_t> pOptionSelfCloseAction).to_dict(),
                                           {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnOptionSelfCloseAction', err_msg)
    return 0

# ///期货发起银行资金转期货应答
cdef extern int   TraderSpi_OnRspFromBankToFutureByFuture(self, CThostFtdcReqTransferField *pReqTransfer,
                                                                CThostFtdcRspInfoField *pRspInfo,
                                                                int nRequestID,
                                                                bool bIsLast) except -1:
    try:
        self.OnRspFromBankToFutureByFuture({} if pReqTransfer is NULL else ReqTransferField.from_address(<size_t> pReqTransfer).to_dict(),
                                           {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                           nRequestID,
                                           bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspFromBankToFutureByFuture', err_msg)
    return 0

# ///期货发起银行资金转期货通知
cdef extern int   TraderSpi_OnRtnFromBankToFutureByFuture(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    try:
        self.OnRtnFromBankToFutureByFuture({} if pRspTransfer is NULL else RspTransferField.from_address(<size_t> pRspTransfer).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnFromBankToFutureByFuture', err_msg)
    return 0

# ///期货发起银行资金转期货错误回报
cdef extern int   TraderSpi_OnErrRtnBankToFutureByFuture(self, CThostFtdcReqTransferField *pReqTransfer,
                                                               CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnBankToFutureByFuture({} if pReqTransfer is NULL else ReqTransferField.from_address(<size_t> pReqTransfer).to_dict(),
                                          {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo)).to_dict()
    except Exception as err_msg:
        self.write_log('OnErrRtnBankToFutureByFuture', err_msg)
    return 0

# ///期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
cdef extern int   TraderSpi_OnRtnRepealFromBankToFutureByFuture(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    try:
        self.OnRtnRepealFromBankToFutureByFuture({} if pRspRepeal is NULL else RspRepealField.from_address(<size_t> pRspRepeal).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnRepealFromBankToFutureByFuture', err_msg)
    return 0

# ///系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
cdef extern int   TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    try:
        self.OnRtnRepealFromBankToFutureByFutureManual({} if pRspRepeal is NULL else RspRepealField.from_address(<size_t> pRspRepeal).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnRepealFromBankToFutureByFutureManual', err_msg)
    return 0

# ///系统运行时期货端手工发起冲正银行转期货错误回报
cdef extern int   TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(self, CThostFtdcReqRepealField *pReqRepeal,
                                                                           CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnRepealBankToFutureByFutureManual({} if pReqRepeal is NULL else ReqRepealField.from_address(<size_t> pReqRepeal).to_dict(),
                                                      {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnRepealBankToFutureByFutureManual', err_msg)
    return 0

# ///银行发起银行资金转期货通知
cdef extern int   TraderSpi_OnRtnFromBankToFutureByBank(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    try:
        self.OnRtnFromBankToFutureByBank({} if pRspTransfer is NULL else RspTransferField.from_address(<size_t> pRspTransfer).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnFromBankToFutureByBank', err_msg)
    return 0

# ///银行发起冲正银行转期货通知
cdef extern int   TraderSpi_OnRtnRepealFromBankToFutureByBank(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    try:
        self.OnRtnRepealFromBankToFutureByBank({} if pRspRepeal is NULL else RspRepealField.from_address(<size_t> pRspRepeal).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnRepealFromBankToFutureByBank', err_msg)
    return 0

# ///期货发起期货资金转银行应答
cdef extern int   TraderSpi_OnRspFromFutureToBankByFuture(self, CThostFtdcReqTransferField *pReqTransfer,
                                                                CThostFtdcRspInfoField *pRspInfo,
                                                                int nRequestID,
                                                                bool bIsLast) except -1:
    try:
        self.OnRspFromFutureToBankByFuture({} if pReqTransfer is NULL else ReqTransferField.from_address(<size_t> pReqTransfer).to_dict(),
                                           {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                           nRequestID,
                                           bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspFromFutureToBankByFuture', err_msg)
    return 0

# ///期货发起期货资金转银行通知
cdef extern int   TraderSpi_OnRtnFromFutureToBankByFuture(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    try:
        self.OnRtnFromFutureToBankByFuture({} if pRspTransfer is NULL else RspTransferField.from_address(<size_t> pRspTransfer).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnFromFutureToBankByFuture', err_msg)
    return 0

# ///期货发起期货资金转银行错误回报
cdef extern int   TraderSpi_OnErrRtnFutureToBankByFuture(self, CThostFtdcReqTransferField *pReqTransfer,
                                                               CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnFutureToBankByFuture({} if pReqTransfer is NULL else ReqTransferField.from_address(<size_t> pReqTransfer).to_dict(),
                                          {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnFutureToBankByFuture', err_msg)
    return 0

# ///期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
cdef extern int   TraderSpi_OnRtnRepealFromFutureToBankByFuture(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    try:
        self.OnRtnRepealFromFutureToBankByFuture({} if pRspRepeal is NULL else RspRepealField.from_address(<size_t> pRspRepeal).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnRepealFromFutureToBankByFuture', err_msg)
    return 0

# ///系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
cdef extern int   TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    try:
        self.OnRtnRepealFromFutureToBankByFutureManual({} if pRspRepeal is NULL else RspRepealField.from_address(<size_t> pRspRepeal).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnRepealFromFutureToBankByFutureManual', err_msg)
    return 0

# ///系统运行时期货端手工发起冲正期货转银行错误回报
cdef extern int   TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(self, CThostFtdcReqRepealField *pReqRepeal,
                                                                           CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnRepealFutureToBankByFutureManual({} if pReqRepeal is NULL else ReqRepealField.from_address(<size_t> pReqRepeal).to_dict(),
                                                      {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnRepealFutureToBankByFutureManual', err_msg)
    return 0

# ///银行发起期货资金转银行通知
cdef extern int   TraderSpi_OnRtnFromFutureToBankByBank(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    try:
        self.OnRtnFromFutureToBankByBank({} if pRspTransfer is NULL else RspTransferField.from_address(<size_t> pRspTransfer).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnFromFutureToBankByBank', err_msg)
    return 0

# ///银行发起冲正期货转银行通知
cdef extern int   TraderSpi_OnRtnRepealFromFutureToBankByBank(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    try:
        self.OnRtnRepealFromFutureToBankByBank({} if pRspRepeal is NULL else RspRepealField.from_address(<size_t> pRspRepeal).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnRepealFromFutureToBankByBank', err_msg)
    return 0

# ///期货发起查询银行余额应答
cdef extern int   TraderSpi_OnRspQueryBankAccountMoneyByFuture(self, CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                                                     CThostFtdcRspInfoField *pRspInfo,
                                                                     int nRequestID,
                                                                     bool bIsLast) except -1:
    try:
        self.OnRspQueryBankAccountMoneyByFuture({} if pReqQueryAccount is NULL else ReqQueryAccountField.from_address(<size_t> pReqQueryAccount).to_dict(),
                                                {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                                nRequestID,
                                                bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQueryBankAccountMoneyByFuture', err_msg)
    return 0

# ///期货发起查询银行余额通知
cdef extern int   TraderSpi_OnRtnQueryBankBalanceByFuture(self, CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) except -1:
    try:
        self.OnRtnQueryBankBalanceByFuture({} if pNotifyQueryAccount is NULL else NotifyQueryAccountField.from_address(<size_t> pNotifyQueryAccount).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnQueryBankBalanceByFuture', err_msg)
    return 0

# ///期货发起查询银行余额错误回报
cdef extern int   TraderSpi_OnErrRtnQueryBankBalanceByFuture(self, CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                                                   CThostFtdcRspInfoField *pRspInfo) except -1:
    try:
        self.OnErrRtnQueryBankBalanceByFuture({} if pReqQueryAccount is NULL else ReqQueryAccountField.from_address(<size_t> pReqQueryAccount).to_dict(),
                                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict())
    except Exception as err_msg:
        self.write_log('OnErrRtnQueryBankBalanceByFuture', err_msg)
    return 0

# ///请求查询转帐流水响应
cdef extern int   TraderSpi_OnRspQryTransferSerial(self, CThostFtdcTransferSerialField *pTransferSerial,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         bool bIsLast) except -1:
    try:
        self.OnRspQryTransferSerial({} if pTransferSerial is NULL else TransferSerialField.from_address(<size_t> pTransferSerial).to_dict(),
                                    {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                    nRequestID,
                                    bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryTransferSerial', err_msg)
    return 0

# ///请求查询转帐银行响应
cdef extern int   TraderSpi_OnRspQryTransferBank(self, CThostFtdcTransferBankField *pTransferBank,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       bool bIsLast) except -1:
    try:
        self.OnRspQryTransferBank({} if pTransferBank is NULL else TransferBankField.from_address(<size_t> pTransferBank).to_dict(),
                                  {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                  nRequestID,
                                  bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryTransferBank', err_msg)
    return 0

# ///请求查询签约银行响应
cdef extern int   TraderSpi_OnRspQryContractBank(self, CThostFtdcContractBankField *pContractBank,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       bool bIsLast) except -1:
    try:
        self.OnRspQryContractBank({} if pContractBank is NULL else ContractBankField.from_address(<size_t> pContractBank).to_dict(),
                                  {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                  nRequestID,
                                  bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryContractBank', err_msg)
    return 0

# ///请求查询银期签约关系响应
cdef extern int   TraderSpi_OnRspQryAccountregister(self, CThostFtdcAccountregisterField *pAccountregister,
                                                          CThostFtdcRspInfoField *pRspInfo,
                                                          int nRequestID,
                                                          bool bIsLast) except -1:
    try:
        self.OnRspQryAccountregister({} if pAccountregister is NULL else AccountregisterField.from_address(<size_t> pAccountregister).to_dict(),
                                     {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                     nRequestID,
                                     bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryAccountregister', err_msg)
    return 0

# ///银行发起银期开户通知
cdef extern int   TraderSpi_OnRtnOpenAccountByBank(self, CThostFtdcOpenAccountField *pOpenAccount) except -1:
    try:
        self.OnRtnOpenAccountByBank({} if pOpenAccount is NULL else OpenAccountField.from_address(<size_t> pOpenAccount).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnOpenAccountByBank', err_msg)
    return 0

# ///银行发起银期销户通知
cdef extern int   TraderSpi_OnRtnCancelAccountByBank(self, CThostFtdcCancelAccountField *pCancelAccount) except -1:
    try:
        self.OnRtnCancelAccountByBank({} if pCancelAccount is NULL else CancelAccountField.from_address(<size_t> pCancelAccount).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnCancelAccountByBank', err_msg)
    return 0

# ///银行发起变更银行账号通知
cdef extern int   TraderSpi_OnRtnChangeAccountByBank(self, CThostFtdcChangeAccountField *pChangeAccount) except -1:
    try:
        self.OnRtnChangeAccountByBank({} if pChangeAccount is NULL else ChangeAccountField.from_address(<size_t> pChangeAccount).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnChangeAccountByBank', err_msg)
    return 0

# ///请求查询合约保证金率响应
cdef extern int   TraderSpi_OnRspQryInstrumentMarginRate(self, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate,
                                                               CThostFtdcRspInfoField *pRspInfo,
                                                               int nRequestID,
                                                               bool bIsLast) except -1:
    try:
        self.OnRspQryInstrumentMarginRate({} if pInstrumentMarginRate is NULL else InstrumentMarginRateField.from_address(<size_t> pInstrumentMarginRate).to_dict(),
                                          {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                          nRequestID,
                                          bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInstrumentMarginRate', err_msg)
    return 0

# ///请求查询投资者品种/跨品种保证金响应
cdef extern int   TraderSpi_OnRspQryInvestorProductGroupMargin(self, CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin,
                                                                     CThostFtdcRspInfoField *pRspInfo,
                                                                     int nRequestID,
                                                                     bool bIsLast) except -1:
    try:
        self.OnRspQryInvestorProductGroupMargin({} if pInvestorProductGroupMargin is NULL else InvestorProductGroupMarginField.from_address(<size_t> pInvestorProductGroupMargin).to_dict(),
                                                {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                                nRequestID,
                                                bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInvestorProductGroupMargin', err_msg)
    return 0

# ///请求查询交易所保证金率响应
cdef extern int   TraderSpi_OnRspQryExchangeMarginRate(self, CThostFtdcExchangeMarginRateField *pExchangeMarginRate,
                                                             CThostFtdcRspInfoField *pRspInfo,
                                                             int nRequestID,
                                                             bool bIsLast) except -1:
    try:
        self.OnRspQryExchangeMarginRate({} if pExchangeMarginRate is NULL else ExchangeMarginRateField.from_address(<size_t> pExchangeMarginRate).to_dict(),
                                        {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                        nRequestID,
                                        bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryExchangeMarginRate', err_msg)
    return 0

# ///请求查询交易所调整保证金率响应
cdef extern int   TraderSpi_OnRspQryExchangeMarginRateAdjust(self, CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust,
                                                                   CThostFtdcRspInfoField *pRspInfo,
                                                                   int nRequestID,
                                                                   bool bIsLast) except -1:
    try:
        self.OnRspQryExchangeMarginRateAdjust({} if pExchangeMarginRateAdjust is NULL else ExchangeMarginRateAdjustField.from_address(<size_t> pExchangeMarginRateAdjust).to_dict(),
                                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                              nRequestID,
                                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryExchangeMarginRateAdjust', err_msg)
    return 0

# ///请求查询合约手续费率响应
cdef extern int   TraderSpi_OnRspQryInstrumentCommissionRate(self, CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate,
                                                                   CThostFtdcRspInfoField *pRspInfo,
                                                                   int nRequestID,
                                                                   bool bIsLast) except -1:
    try:
        self.OnRspQryInstrumentCommissionRate({} if pInstrumentCommissionRate is NULL else InstrumentCommissionRateField.from_address(<size_t> pInstrumentCommissionRate).to_dict(),
                                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                              nRequestID,
                                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInstrumentCommissionRate', err_msg)
    return 0

# ///请求查询做市商合约手续费率响应
cdef extern int   TraderSpi_OnRspQryMMInstrumentCommissionRate(self, CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate,
                                                                     CThostFtdcRspInfoField *pRspInfo,
                                                                     int nRequestID,
                                                                     bool bIsLast) except -1:
    try:
        self.OnRspQryMMInstrumentCommissionRate({} if pMMInstrumentCommissionRate is NULL else MMInstrumentCommissionRateField.from_address(<size_t> pMMInstrumentCommissionRate).to_dict(),
                                                {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                                nRequestID,
                                                bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryMMInstrumentCommissionRate', err_msg)
    return 0

# ///请求查询报单手续费响应
cdef extern int   TraderSpi_OnRspQryInstrumentOrderCommRate(self, CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate,
                                                                  CThostFtdcRspInfoField *pRspInfo,
                                                                  int nRequestID,
                                                                  bool bIsLast) except -1:
    try:
        self.OnRspQryInstrumentOrderCommRate({} if pInstrumentOrderCommRate is NULL else InstrumentOrderCommRateField.from_address(<size_t> pInstrumentOrderCommRate).to_dict(),
                                             {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                             nRequestID,
                                             bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInstrumentOrderCommRate', err_msg)
    return 0

# ///请求查询期权合约手续费响应
cdef extern int   TraderSpi_OnRspQryOptionInstrCommRate(self, CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate,
                                                              CThostFtdcRspInfoField *pRspInfo,
                                                              int nRequestID,
                                                              bool bIsLast) except -1:
    try:
        self.OnRspQryOptionInstrCommRate({} if pOptionInstrCommRate is NULL else OptionInstrCommRateField.from_address(<size_t> pOptionInstrCommRate).to_dict(),
                                         {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                         nRequestID,
                                         bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryOptionInstrCommRate', err_msg)
    return 0

# ///请求查询做市商期权合约手续费响应
cdef extern int   TraderSpi_OnRspQryMMOptionInstrCommRate(self, CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate,
                                                                CThostFtdcRspInfoField *pRspInfo,
                                                                int nRequestID,
                                                                bool bIsLast) except -1:
    try:
        self.OnRspQryMMOptionInstrCommRate({} if pMMOptionInstrCommRate is NULL else MMOptionInstrCommRateField.from_address(<size_t> pMMOptionInstrCommRate).to_dict(),
                                           {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                           nRequestID,
                                           bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryMMOptionInstrCommRate', err_msg)
    return 0

# ///请求查询期权交易成本响应
cdef extern int   TraderSpi_OnRspQryOptionInstrTradeCost(self, CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost,
                                                               CThostFtdcRspInfoField *pRspInfo,
                                                               int nRequestID,
                                                               bool bIsLast) except -1:
    try:
        self.OnRspQryOptionInstrTradeCost({} if pOptionInstrTradeCost is NULL else OptionInstrTradeCostField.from_address(<size_t> pOptionInstrTradeCost).to_dict(),
                                          {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                          nRequestID,
                                          bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryOptionInstrTradeCost', err_msg)
    return 0

# ///请求查询交易所响应
cdef extern int   TraderSpi_OnRspQryExchange(self, CThostFtdcExchangeField *pExchange,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   bool bIsLast) except -1:
    try:
        self.OnRspQryExchange({} if pExchange is NULL else ExchangeField.from_address(<size_t> pExchange).to_dict(),
                              {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                              nRequestID,
                              bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryExchange', err_msg)
    return 0

# ///请求查询合约响应
cdef extern int   TraderSpi_OnRspQryInstrument(self, CThostFtdcInstrumentField *pInstrument,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     bool bIsLast) except -1:
    try:
        self.OnRspQryInstrument({} if pInstrument is NULL else InstrumentField.from_address(<size_t> pInstrument).to_dict(),
                                {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                nRequestID,
                                bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInstrument', err_msg)
    return 0

# ///请求查询交易编码响应
cdef extern int   TraderSpi_OnRspQryTradingCode(self, CThostFtdcTradingCodeField *pTradingCode,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      bool bIsLast) except -1:
    try:
        self.OnRspQryTradingCode({} if pTradingCode is NULL else TradingCodeField.from_address(<size_t> pTradingCode).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                 nRequestID,
                                 bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryTradingCode', err_msg)
    return 0

# ///请求查询产品响应
cdef extern int   TraderSpi_OnRspQryProduct(self, CThostFtdcProductField *pProduct,
                                                  CThostFtdcRspInfoField *pRspInfo,
                                                  int nRequestID,
                                                  bool bIsLast) except -1:
    try:
        self.OnRspQryProduct({} if pProduct is NULL else ProductField.from_address(<size_t> pProduct).to_dict(),
                             {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                             nRequestID,
                             bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryProduct', err_msg)
    return 0

# ///请求查询产品报价汇率
cdef extern int   TraderSpi_OnRspQryProductExchRate(self, CThostFtdcProductExchRateField *pProductExchRate,
                                                          CThostFtdcRspInfoField *pRspInfo,
                                                          int nRequestID,
                                                          bool bIsLast) except -1:
    try:
        self.OnRspQryProductExchRate({} if pProductExchRate is NULL else ProductExchRateField.from_address(<size_t> pProductExchRate).to_dict(),
                                     {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                     nRequestID,
                                     bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryProductExchRate', err_msg)
    return 0

# ///请求查询产品组
cdef extern int   TraderSpi_OnRspQryProductGroup(self, CThostFtdcProductGroupField *pProductGroup,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       bool bIsLast) except -1:
    try:
        self.OnRspQryProductGroup({} if pProductGroup is NULL else ProductGroupField.from_address(<size_t> pProductGroup).to_dict(),
                                  {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                  nRequestID,
                                  bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryProductGroup', err_msg)
    return 0

# ///请求查询投资单元响应
cdef extern int   TraderSpi_OnRspQryInvestUnit(self, CThostFtdcInvestUnitField *pInvestUnit,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     bool bIsLast) except -1:
    try:
        self.OnRspQryInvestUnit({} if pInvestUnit is NULL else InvestUnitField.from_address(<size_t> pInvestUnit).to_dict(),
                                {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                nRequestID,
                                bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryInvestUnit', err_msg)
    return 0

# ///请求查询组合合约安全系数响应
cdef extern int   TraderSpi_OnRspQryCombInstrumentGuard(self, CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard,
                                                              CThostFtdcRspInfoField *pRspInfo,
                                                              int nRequestID,
                                                              bool bIsLast) except -1:
    try:
        self.OnRspQryCombInstrumentGuard({} if pCombInstrumentGuard is NULL else CombInstrumentGuardField.from_address(<size_t> pCombInstrumentGuard).to_dict(),
                                         {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                         nRequestID,
                                         bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryCombInstrumentGuard', err_msg)
    return 0

# ///交易所公告通知
cdef extern int   TraderSpi_OnRtnBulletin(self, CThostFtdcBulletinField *pBulletin) except -1:
    try:
        self.OnRtnBulletin({} if pBulletin is NULL else BulletinField.from_address(<size_t> pBulletin).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnBulletin', err_msg)
    return 0

# ///请求查询行情响应
cdef extern int   TraderSpi_OnRspQryDepthMarketData(self, CThostFtdcDepthMarketDataField *pDepthMarketData,
                                                          CThostFtdcRspInfoField *pRspInfo,
                                                          int nRequestID,
                                                          bool bIsLast) except -1:
    try:
        self.OnRspQryDepthMarketData({} if pDepthMarketData is NULL else DepthMarketDataField.from_address(<size_t> pDepthMarketData).to_dict(),
                                     {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                     nRequestID,
                                     bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryDepthMarketData', err_msg)
    return 0

# ///查询最大报单数量响应
cdef extern int   TraderSpi_OnRspQueryMaxOrderVolume(self, CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume,
                                                           CThostFtdcRspInfoField *pRspInfo,
                                                           int nRequestID,
                                                           bool bIsLast) except -1:
    try:
        self.OnRspQueryMaxOrderVolume({} if pQueryMaxOrderVolume is NULL else QueryMaxOrderVolumeField.from_address(<size_t> pQueryMaxOrderVolume).to_dict(),
                                      {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                      nRequestID,
                                      bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQueryMaxOrderVolume', err_msg)
    return 0

# ///请求查询仓单折抵信息响应
cdef extern int   TraderSpi_OnRspQryEWarrantOffset(self, CThostFtdcEWarrantOffsetField *pEWarrantOffset,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         bool bIsLast) except -1:
    try:
        self.OnRspQryEWarrantOffset({} if pEWarrantOffset is NULL else EWarrantOffsetField.from_address(<size_t> pEWarrantOffset).to_dict(),
                                    {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                    nRequestID,
                                    bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryEWarrantOffset', err_msg)
    return 0

# ///请求查询汇率响应
cdef extern int   TraderSpi_OnRspQryExchangeRate(self, CThostFtdcExchangeRateField *pExchangeRate,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       bool bIsLast) except -1:
    try:
        self.OnRspQryExchangeRate({} if pExchangeRate is NULL else ExchangeRateField.from_address(<size_t> pExchangeRate).to_dict(),
                                  {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                  nRequestID,
                                  bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryExchangeRate', err_msg)
    return 0

# ///请求查询客户通知响应
cdef extern int   TraderSpi_OnRspQryNotice(self, CThostFtdcNoticeField *pNotice,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 bool bIsLast) except -1:
    try:
        self.OnRspQryNotice({} if pNotice is NULL else NoticeField.from_address(<size_t> pNotice).to_dict(),
                            {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                            nRequestID,
                            bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryNotice', err_msg)
    return 0

# ///请求查询交易通知响应
cdef extern int   TraderSpi_OnRspQryTradingNotice(self, CThostFtdcTradingNoticeField *pTradingNotice,
                                                        CThostFtdcRspInfoField *pRspInfo,
                                                        int nRequestID,
                                                        bool bIsLast) except -1:
    try:
        self.OnRspQryTradingNotice({} if pTradingNotice is NULL else TradingNoticeField.from_address(<size_t> pTradingNotice).to_dict(),
                                   {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                   nRequestID,
                                   bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryTradingNotice', err_msg)
    return 0

# ///交易通知
cdef extern int   TraderSpi_OnRtnTradingNotice(self, CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) except -1:
    try:
        self.OnRtnTradingNotice({} if pTradingNoticeInfo is NULL else TradingNoticeInfoField.from_address(<size_t> pTradingNoticeInfo).to_dict())
    except Exception as err_msg:
        self.write_log('OnRtnTradingNotice', err_msg)
    return 0

# ///查询保证金监管系统经纪公司资金账户密钥响应
cdef extern int   TraderSpi_OnRspQryCFMMCTradingAccountKey(self, CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey,
                                                                 CThostFtdcRspInfoField *pRspInfo,
                                                                 int nRequestID,
                                                                 bool bIsLast) except -1:
    try:
        self.OnRspQryCFMMCTradingAccountKey({} if pCFMMCTradingAccountKey is NULL else CFMMCTradingAccountKeyField.from_address(<size_t> pCFMMCTradingAccountKey).to_dict(),
                                            {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                            nRequestID,
                                            bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryCFMMCTradingAccountKey', err_msg)
    return 0

# ///请求查询经纪公司交易参数响应
cdef extern int   TraderSpi_OnRspQryBrokerTradingParams(self, CThostFtdcBrokerTradingParamsField *pBrokerTradingParams,
                                                              CThostFtdcRspInfoField *pRspInfo,
                                                              int nRequestID,
                                                              bool bIsLast) except -1:
    try:
        self.OnRspQryBrokerTradingParams({} if pBrokerTradingParams is NULL else BrokerTradingParamsField.from_address(<size_t> pBrokerTradingParams).to_dict(),
                                         {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                         nRequestID,
                                         bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryBrokerTradingParams', err_msg)
    return 0

# ///请求查询经纪公司交易算法响应
cdef extern int   TraderSpi_OnRspQryBrokerTradingAlgos(self, CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos,
                                                             CThostFtdcRspInfoField *pRspInfo,
                                                             int nRequestID,
                                                             bool bIsLast) except -1:
    try:
        self.OnRspQryBrokerTradingAlgos({} if pBrokerTradingAlgos is NULL else BrokerTradingAlgosField.from_address(<size_t> pBrokerTradingAlgos).to_dict(),
                                        {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                        nRequestID,
                                        bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQryBrokerTradingAlgos', err_msg)
    return 0

# ///请求查询二级代理商信息响应
cdef extern int   TraderSpi_OnRspQrySecAgentTradeInfo(self, CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo,
                                                            CThostFtdcRspInfoField *pRspInfo,
                                                            int nRequestID,
                                                            bool bIsLast) except -1:
    try:
        self.OnRspQrySecAgentTradeInfo({} if pSecAgentTradeInfo is NULL else SecAgentTradeInfoField.from_address(<size_t> pSecAgentTradeInfo).to_dict(),
                                       {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                       nRequestID,
                                       bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQrySecAgentTradeInfo', err_msg)
    return 0

# ///请求查询二级代理商资金校验模式响应
cdef extern int   TraderSpi_OnRspQrySecAgentCheckMode(self, CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode,
                                                            CThostFtdcRspInfoField *pRspInfo,
                                                            int nRequestID,
                                                            bool bIsLast) except -1:
    try:
        self.OnRspQrySecAgentCheckMode({} if pSecAgentCheckMode is NULL else SecAgentCheckModeField.from_address(<size_t> pSecAgentCheckMode).to_dict(),
                                       {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                       nRequestID,
                                       bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQrySecAgentCheckMode', err_msg)
    return 0

# ///请求查询二级代理操作员银期权限响应
cdef extern int   TraderSpi_OnRspQrySecAgentACIDMap(self, CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap,
                                                          CThostFtdcRspInfoField *pRspInfo,
                                                          int nRequestID,
                                                          bool bIsLast) except -1:
    try:
        self.OnRspQrySecAgentACIDMap({} if pSecAgentACIDMap is NULL else SecAgentACIDMapField.from_address(<size_t> pSecAgentACIDMap).to_dict(),
                                     {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                     nRequestID,
                                     bIsLast)
    except Exception as err_msg:
        self.write_log('OnRspQrySecAgentACIDMap', err_msg)
    return 0