# encoding:utf-8
# distutils: language=c++

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from cpython     cimport PyObject
from libc.string cimport const_char
from libcpp      cimport bool
from libc.stdlib cimport malloc, free

import os
import ctypes
from datetime import datetime

from .cython2c.ThostFtdcUserApiStruct cimport *
from .cython2c.cMdApi                 cimport CMdSpi, CMdApi, CreateFtdcMdApi

from .ApiStruct import *

from ..utils.check_service import check_service
from ..utils.base_field    import to_bytes, to_str


cdef class MdApiBase:
    cdef CMdApi *__api
    cdef CMdSpi *__spi

    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    def __cinit__(self, broker_id, md_server, investor_id, password, app_id, auth_code, instrument_id_list, md_queue_list=None,
                        page_dir='', using_udp=False, multicast=False):
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
            md_server = to_bytes(md_server)
            self.md_server = md_server if md_server.startswith(b'tcp://') else (b'tcp://' + md_server)
            self.broker_id = to_bytes(broker_id)
            self.investor_id = to_bytes(investor_id)
            self.password = to_bytes(password)
            self.app_id = to_bytes(app_id)
            self.auth_code = to_bytes(auth_code)

            # ############################################################################# #
            page_dir = os.path.join(to_str(page_dir), to_str(investor_id))
            self.page_dir = page_dir if page_dir.endswith(os.path.sep) else (page_dir + os.path.sep)
            flow_path = self.page_dir + 'md.con'
            tmp_dir = ''
            for dir in flow_path.split(os.path.sep):
                tmp_dir = os.path.join(tmp_dir, dir) + os.path.sep
                if not os.path.exists(tmp_dir):
                    os.mkdir(tmp_dir)

            self.using_udp = using_udp
            self.multicast = multicast

            # ############################################################################# #
            if self.__init_base() != 0:
                raise Exception('__init_base || 创建MdApi与MdSpi失败！')

            # ############################################################################# #
            info_list = self.md_server.split(b':')
            ip = to_str(info_list[1][2:])
            port = int(info_list[2])
            if not check_service(ip, port):
                raise Exception(f'check_service || 服务器{self.md_server}未开启！')

            # ############################################################################# #
            self.md_queue_list = md_queue_list if isinstance(md_queue_list, list) else []
            self.instrument_id_list = []
            if isinstance(instrument_id_list, list):
                for instrument_id in instrument_id_list:
                    self.instrument_id_list.append(to_bytes(instrument_id))

            # ############################################################################# #
            self.init_extra()

            # ############################################################################# #
            # 初始化运行环境，只有调用后，接口才开始发起前置的连接请求。
            if self.__init_net() != 0:
                raise Exception('__init_net || 行情初始化失败！')

        except Exception as err_msg:
            self.write_log('__cinit__', err_msg)

    # ############################################################################# #
    def init_extra(self):
        pass

    # ############################################################################# #
    def write_log(self, *args, sep=' || '):
        local_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{local_time}{sep}{self.investor_id}.md{sep}{sep.join(map(str, args))}')

    # ############################################################################# #
    def __dealloc__(self):
        try:
            self.Release()
        except Exception as err_msg:
            self.write_log('__dealloc__', err_msg)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///创建MdApi
    def __init_base(self):
        cdef int bInit = -1
        try:
            self.__api = CreateFtdcMdApi(to_bytes(self.page_dir + 'md.con' + os.path.sep), self.using_udp, self.multicast)
            if self.__api is NULL:
                raise MemoryError()
            self.__spi = new CMdSpi(<PyObject *> self)
            if self.__spi is NULL:
                raise MemoryError()
            bInit=0
        except Exception as err_msg:
            self.write_log('__init_base', err_msg)
        finally:
          return bInit

    # ############################################################################# #
    # ///void RegisterSpi()
    # ///注册回调接口
    # ///void Init()
    # ///初始化
    def __init_net(self):
        cdef int bInit=-1
        try:
            if self.__api is NULL or self.__spi is NULL:
                raise Exception('行情接口未注册！')
            self.__api.RegisterSpi(self.__spi)
            if self.RegisterFront(self.md_server) == 0:
                # 初始化成功后OnFrontConnected会被回调
                self.__api.Init()
                bInit=0
        except Exception as err_msg:
            self.write_log('__init_net', err_msg)
        finally:
          return bInit

    # ############################################################################# #
    def __inc_req_id(self):
        self.__request_id += 1
        return self.__request_id



    # ############################################################################# #
    # ############################################################################# #
    # ///获取API的版本信息
    @staticmethod
    def GetApiVersion(self):
        cdef const_char *result = ''
        try:
            result = CMdApi.GetApiVersion()
        except Exception as err_msg:
            self.write_log('GetApiVersion', err_msg)
        finally:
            return result

    # ############################################################################# #
    # ///获取当前交易日
    def GetTradingDay(self):
        cdef const_char *result = ''
        try:
            if self.__api is NULL:
                raise Exception('只有登录成功后,才能得到正确的交易日！')
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
          self.write_log('OnFrontConnected', '重连成功！')

    # ///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
    def OnFrontDisconnected(self, nReason):
        self.status = -2
        self.write_log('OnFrontDisconnected', nReason)

    # ///心跳超时警告。当长时间未收到报文时，该方法被调用。
    def OnHeartBeatWarning(self, nTimeLapse):
        self.write_log('OnHeartBeatWarning', nTimeLapse)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///用户登录请求
    def ReqUserLogin(self, pReqUserLoginField):
        cdef int result = -1
        cdef size_t address = 0
        cdef int nRequestID
        try:
            nRequestID = self.__inc_req_id()
            if self.__api is not NULL:
                address = addressof(pReqUserLoginField)
                with nogil:
                    result = self.__api.ReqUserLogin(<CThostFtdcReqUserLoginField *> address, nRequestID)
        except Exception as err_msg:
            self.write_log('ReqUserLogin', err_msg)
        finally:
            return result

    # ///登录请求响应
    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspUserLogin', pRspUserLogin)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///登出请求
    def ReqUserLogout(self, size_t pUserLogout):
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

    # ///登出请求响应
    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspUserLogout', pUserLogout)



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///订阅行情。
    def SubscribeMarketData(self, pInstrumentID):
        cdef int result = -1
        cdef Py_ssize_t count
        cdef char **InstrumentIDs
        try:
            if self.__api is not NULL:
                count = len(pInstrumentID)
                if count > 0:
                    InstrumentIDs = <char **> malloc(sizeof(char*) * count)
                    try:
                        for i from 0 <= i < count:
                            InstrumentIDs[i] = pInstrumentID[i]
                        with nogil:
                            result = self.__api.SubscribeMarketData(InstrumentIDs, <int>count)
                    finally:
                        free(InstrumentIDs)
        except Exception as err_msg:
            self.write_log('SubscribeMarketData', err_msg)
        finally:
            return result

    # ///订阅行情应答
    def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspSubMarketData', pSpecificInstrument)

    # ############################################################################# #
    # ///退订行情。
    def UnSubscribeMarketData(self, pInstrumentID):
        cdef int result = -1
        cdef Py_ssize_t count
        cdef char **InstrumentIDs
        try:
            if self.__api is not NULL:
                count = len(pInstrumentID)
                InstrumentIDs = <char **> malloc(sizeof(char*) * count)
                try:
                    for i from 0 <= i < count:
                        InstrumentIDs[i] = pInstrumentID[i]
                    with nogil:
                        result = self.__api.UnSubscribeMarketData(InstrumentIDs, <int>count)
                finally:
                    free(InstrumentIDs)
        except Exception as err_msg:
            self.write_log('UnSubscribeMarketData', err_msg)
        finally:
            return result

    # ///取消订阅行情应答
    def OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspUnSubMarketData', pSpecificInstrument)

    # ///深度行情通知
    def OnRtnDepthMarketData(self, pDepthMarketData):
        pass



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///订阅询价。
    def SubscribeForQuoteRsp(self, pInstrumentID):
        cdef int result = -1
        cdef Py_ssize_t count
        cdef char **InstrumentIDs
        try:
            if self.__api is not NULL:
                count = len(pInstrumentID)
                InstrumentIDs = <char **> malloc(sizeof(char*) * count)
                try:
                    for i from 0 <= i < count:
                        InstrumentIDs[i] = pInstrumentID[i]
                    with nogil:
                        result = self.__api.SubscribeForQuoteRsp(InstrumentIDs, <int>count)
                finally:
                    free(InstrumentIDs)
        except Exception as err_msg:
            self.write_log('SubscribeForQuoteRsp', err_msg)
        finally:
            return result

    # ///订阅询价应答
    def OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspSubForQuoteRsp', pSpecificInstrument)

    # ############################################################################# #
    # ///退订询价。
    def UnSubscribeForQuoteRsp(self, pInstrumentID):
        cdef int result = -1
        cdef Py_ssize_t count
        cdef char **InstrumentIDs
        try:
            if self.__api is not NULL:
                count = len(pInstrumentID)
                InstrumentIDs = <char **> malloc(sizeof(char*) * count)
                try:
                    for i from 0 <= i < count:
                        InstrumentIDs[i] = pInstrumentID[i]
                    with nogil:
                        result = self.__api.UnSubscribeForQuoteRsp(InstrumentIDs, <int>count)
                finally:
                    free(InstrumentIDs)
        except Exception as err_msg:
            self.write_log('UnSubscribeForQuoteRsp', err_msg)
        finally:
            return result

    # ///取消订阅询价应答
    def OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspUnSubForQuoteRsp', pSpecificInstrument)

    # ///询价通知
    def OnRtnForQuoteRsp(self, pForQuoteRsp):
        pass



    # ############################################################################# #
    # ############################################################################# #
    # ############################################################################# #
    # ///错误应答
    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        self.write_log('OnRspError', pRspInfo)



# ############################################################################# #
# ############################################################################# #
# ############################################################################# #
# ///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
cdef extern int   MdSpi_OnFrontConnected(self) except -1:
    try:
        req_user_login = ReqUserLoginField(BrokerID=self.broker_id,
                                           UserID=self.investor_id,
                                           Password=self.password)
        if self.ReqUserLogin(req_user_login) != 0:
            self.write_log('ReqUserLogin', '登录行情账户失败！', req_user_login)
        self.OnFrontConnected()
    except Exception as err_msg:
        self.write_log('MdSpi_OnFrontConnected', err_msg)
    return 0

# ############################################################################# #
# ///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
cdef extern int   MdSpi_OnFrontDisconnected(self, int nReason) except -1:
    try:
        self.OnFrontDisconnected(nReason)
    except Exception as err_msg:
        self.write_log('MdSpi_OnFrontDisconnected', err_msg)
    return 0

# ############################################################################# #
# ///心跳超时警告。当长时间未收到报文时，该方法被调用。
cdef extern int   MdSpi_OnHeartBeatWarning(self, int nTimeLapse) except -1:
    try:
        self.OnHeartBeatWarning(nTimeLapse)
    except Exception as err_msg:
        self.write_log('MdSpi_OnHeartBeatWarning', err_msg)
    return 0



# ############################################################################# #
# ############################################################################# #
# ############################################################################# #
# ///登录请求响应
cdef extern int   MdSpi_OnRspUserLogin(self, CThostFtdcRspUserLoginField *pRspUserLogin,
                                             CThostFtdcRspInfoField *pRspInfo,
                                             int nRequestID,
                                             bool bIsLast) except -1:
    try:
        if pRspUserLogin is not NULL:
            rsp_user_login = RspUserLoginField.from_address(<size_t> pRspUserLogin).to_dict()
            if pRspInfo is not NULL:
                rsp_info = RspInfoField.from_address(<size_t> pRspInfo).to_str_dict()
                if rsp_info['ErrorID'] == 0:
                    if self.instrument_id_list and self.SubscribeMarketData(self.instrument_id_list) != 0:
                        self.write_log('SubscribeMarketData', f'订阅行情失败！', f'instrument_id_list:{self.instrument_id_list}')
                    else:
                      self.status = 0
                      self.write_log('MdSpi_OnRspUserLogin', '行情启动完毕！', f'CTP版本号：{self.GetApiVersion(self)}', f'交易日:{self.GetTradingDay()}',
                                      f'server:{self.md_server}', f'broker_id:{self.broker_id}', f'instrument_id_list:{self.instrument_id_list}')
                else:
                    self.write_log('MdSpi_OnRspUserLogin', '登录行情账户失败！', rsp_info)
            else:
                rsp_info = {}
                self.write_log('MdSpi_OnRspUserLogin', '响应信息异常！')
        else:
            rsp_user_login = {}

        self.OnRspUserLogin(rsp_user_login,
                            rsp_info,
                            nRequestID,
                            bIsLast)
    except Exception as err_msg:
        self.write_log('MdSpi_OnRspUserLogin', err_msg)
    return 0

# ############################################################################# #
# ///登出请求响应
cdef extern int   MdSpi_OnRspUserLogout(self, CThostFtdcUserLogoutField *pUserLogout,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID,
                                              bool bIsLast) except -1:
    try:
        self.OnRspUserLogout({} if pUserLogout is NULL else UserLogoutField.from_address(<size_t> pUserLogout).to_dict(),
                             {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                             nRequestID,
                             bIsLast)
    except Exception as err_msg:
        self.write_log('MdSpi_OnRspUserLogout', err_msg)
    return 0



# ############################################################################# #
# ############################################################################# #
# ############################################################################# #
# ///订阅行情应答
cdef extern int   MdSpi_OnRspSubMarketData(self, CThostFtdcSpecificInstrumentField *pSpecificInstrument,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 bool bIsLast) except -1:
    try:
        self.OnRspSubMarketData({} if pSpecificInstrument is NULL else SpecificInstrumentField.from_address(<size_t> pSpecificInstrument).to_dict(),
                                {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                nRequestID,
                                bIsLast)
    except Exception as err_msg:
        self.write_log('MdSpi_OnRspSubMarketData', err_msg)
    return 0

# ############################################################################# #
# ///取消订阅行情应答
cdef extern int   MdSpi_OnRspUnSubMarketData(self, CThostFtdcSpecificInstrumentField *pSpecificInstrument,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   bool bIsLast) except -1:
    try:
        self.OnRspUnSubMarketData({} if pSpecificInstrument is NULL else SpecificInstrumentField.from_address(<size_t> pSpecificInstrument).to_dict(),
                                  {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                  nRequestID,
                                  bIsLast)
    except Exception as err_msg:
        self.write_log('MdSpi_OnRspUnSubMarketData', err_msg)
    return 0

# ############################################################################# #
# ///深度行情通知
cdef extern int   MdSpi_OnRtnDepthMarketData(self, CThostFtdcDepthMarketDataField *pDepthMarketData) except -1:
    try:
        self.OnRtnDepthMarketData({} if pDepthMarketData is NULL else DepthMarketDataField.from_address(<size_t> pDepthMarketData).to_dict())
    except Exception as err_msg:
        self.write_log('MdSpi_OnRtnDepthMarketData', err_msg)
    return 0



# ############################################################################# #
# ############################################################################# #
# ############################################################################# #
# ///订阅询价应答
cdef extern int   MdSpi_OnRspSubForQuoteRsp(self, CThostFtdcSpecificInstrumentField *pSpecificInstrument,
                                                  CThostFtdcRspInfoField *pRspInfo,
                                                  int nRequestID,
                                                  bool bIsLast) except -1:
    try:
        self.OnRspSubForQuoteRsp({} if pSpecificInstrument is NULL else SpecificInstrumentField.from_address(<size_t> pSpecificInstrument).to_dict(),
                                 {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                 nRequestID,
                                 bIsLast)
    except Exception as err_msg:
        self.write_log('MdSpi_OnRspSubForQuoteRsp', err_msg)
    return 0

# ############################################################################# #
# ///取消订阅询价应答
cdef extern int   MdSpi_OnRspUnSubForQuoteRsp(self, CThostFtdcSpecificInstrumentField *pSpecificInstrument,
                                                    CThostFtdcRspInfoField *pRspInfo,
                                                    int nRequestID,
                                                    bool bIsLast) except -1:
    try:
        self.OnRspUnSubForQuoteRsp({} if pSpecificInstrument is NULL else SpecificInstrumentField.from_address(<size_t> pSpecificInstrument).to_dict(),
                                   {} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                                   nRequestID,
                                   bIsLast)
    except Exception as err_msg:
        self.write_log('MdSpi_OnRspUnSubForQuoteRsp', err_msg)
    return 0

# ############################################################################# #
# ///询价通知
cdef extern int   MdSpi_OnRtnForQuoteRsp(self, CThostFtdcForQuoteRspField *pForQuoteRsp) except -1:
    try:
        self.OnRtnForQuoteRsp({} if pForQuoteRsp is NULL else ForQuoteRspField.from_address(<size_t> pForQuoteRsp).to_dict())
    except Exception as err_msg:
        self.write_log('MdSpi_OnRtnForQuoteRsp', err_msg)
    return 0



# ############################################################################# #
# ############################################################################# #
# ############################################################################# #
# ///错误应答
cdef extern int   MdSpi_OnRspError(self, CThostFtdcRspInfoField *pRspInfo,
                                         int nRequestID,
                                         bool bIsLast) except -1:
    try:
        self.OnRspError({} if pRspInfo is NULL else RspInfoField.from_address(<size_t> pRspInfo).to_str_dict(),
                        nRequestID,
                        bIsLast)
    except Exception as err_msg:
        self.write_log('MdSpi_OnRspError', err_msg)
    return 0

# ############################################################################# #
# ############################################################################# #
# ############################################################################# #
