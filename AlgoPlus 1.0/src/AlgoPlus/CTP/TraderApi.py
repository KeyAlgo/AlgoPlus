# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from time import sleep, perf_counter as timer
from AlgoPlus.CTP.TraderApiBase import TraderApiBase
from AlgoPlus.CTP.FutureAccount import FutureAccount
from AlgoPlus.utils.base_field import to_bytes, to_str
from AlgoPlus.CTP.ApiStruct import *
from AlgoPlus.CTP.ApiConst import *


class TraderApi(TraderApiBase):
    # ############################################################################# #
    def __init__(self, broker_id, td_server, investor_id, password, app_id, auth_code, md_queue=None,
                 page_dir='', private_resume_type=2, public_resume_type=2):
        pass

    # ############################################################################# #
    def init_extra(self):
        """
        初始化策略参数
        :return:
        """

        self.rtn_order_list = []
        self.last_rtn_order_index = 0  # 已处理报单ID
        self.rtn_trade_list = []
        self.last_rtn_trade_index = 0  # 已处理成交ID

        '''
        {'InstrumentID': ,}
        # '''
        self.md_dict = {}

        '''
        {'InstrumentID': [b'00:00:00', b'00:00:00'], }
        # '''
        self.server_time_dict = {}

        '''
        {'InstrumentID':
            {
                'LongVolume': 0, 'LongVolumeToday': 0, 'LongVolumeYesterday': 0, 'LongPositionDetailList': []
                , 'ShortVolume': 0, 'ShortVolumeToday': 0, 'ShortVolumeYesterday': 0, 'ShortPositionDetailList': []
            }
        }
        # '''
        self.local_position_dict = {}

        '''
        {'InstrumentID': 0}
        #'''
        self.action_num_dict = {}  # 撤单次数 #

        """
        {"InstrumentID": {'0': [], '1': []}}
        #"""
        self.pl_parameter_dict = {}  # 止盈止损参数

        parameter_dict = self.md_queue.get(block=False)  # 策略参数结构体
        self.id = parameter_dict['StrategyID']
        self.order_ref = self.id * 10000
        self.order_ref_range = [self.order_ref, self.order_ref + 10000]
        self.pl_parameter_dict = parameter_dict['ProfitLossParameter']

    # ############################################################################# #
    def get_price(self, instrument_id, direction, price_type=0):
        """
        :param instrument_id:合约
        :param direction:持仓方向
        :param price_type:0->对手价, 1->排队价, 2->市价
        :return:报单价格
        """
        result = None
        try:
            md = self.md_dict[instrument_id]
            if price_type == 0:  # 对手价
                result = md['BidPrice1'] if direction == Direction_Sell else md['AskPrice1']
            elif price_type == 1:  # 排队价
                result = md['AskPrice1'] if direction == Direction_Sell else md['BidPrice1']
            elif price_type == 2:  # 市价
                result = md['LowerLimitPrice'] if direction == Direction_Sell else md['UpperLimitPrice']
        except Exception as err_msg:
            self.write_log('get_default_price', err_msg)
        finally:
            return result

    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        """
        录入撤单回报。不适宜在回调函数里做比较耗时的操作。可参考OnRtnOrder的做法。
        :param pInputOrder: AlgoPlus.CTP.ApiStruct中InputOrderField的实例。
        :param pRspInfo: AlgoPlus.CTP.ApiStruct中RspInfoField的实例。包含错误代码ErrorID和错误信息ErrorMsg
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        if self.is_my_order(pInputOrder['OrderRef']):
            if pRspInfo['ErrorID'] != 0:
                self.on_order_insert_fail(pInputOrder)
            self.write_log(pRspInfo, pInputOrder)

    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        """
        订单错误通知。不适宜在回调函数里做比较耗时的操作。可参考OnRtnOrder的做法。
        :param pInputOrder: AlgoPlus.CTP.ApiStruct中的InputOrderField实例。
        :param pRspInfo: AlgoPlus.CTP.ApiStruct中RspInfoField的实例。包含错误代码ErrorID和错误信息ErrorMsg
        :return:
        """
        if self.is_my_order(pInputOrder['OrderRef']):
            if pRspInfo['ErrorID'] != 0:
                self.on_order_insert_fail(pInputOrder)
            self.write_log(pRspInfo, pInputOrder)

    def on_order_insert_fail(self, pOrder):
        """
        报单失败处理逻辑。不适宜在回调函数里做比较耗时的操作。可参考OnRtnOrder的做法。
        :param pInputOrder: AlgoPlus.CTP.ApiStruct中的InputOrderField实例。
        :return:
        """
        pass

    # ############################################################################# #
    def OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        """
        录入撤单回报。不适宜在回调函数里做比较耗时的操作。可参考OnRtnOrder的做法。
        :param pInputOrderAction: AlgoPlus.CTP.ApiStruct中InputOrderActionField的实例。
        :param pRspInfo: AlgoPlus.CTP.ApiStruct中RspInfoField的实例。包含错误代码ErrorID和错误信息ErrorMsg。
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        if self.is_my_order(pInputOrderAction['OrderRef']):
            if pRspInfo['ErrorID'] != 0:
                self.on_order_action_fail(pInputOrderAction)
            self.write_log(pRspInfo, pInputOrderAction)

    def on_order_action_fail(self, pInputOrderAction):
        """
        撤单失败处理逻辑。不适宜在回调函数里做比较耗时的操作。可参考OnRtnOrder的做法。
        :param pInputOrderAction: AlgoPlus.CTP.ApiStruct中InputOrderActionField的实例。
        :return:
        """
        pass

    # ############################################################################# #
    def is_my_order(self, order_ref):
        """
        以order_ref标识本策略订单。
        """
        return True

    def OnRtnOrder(self, pOrder):
        """
        当收到订单状态变化时，可以在本方法中获得通知。不适宜在回调函数里做比较耗时的操作。可参考OnRtnOrder的做法。
        根据pOrder['OrderStatus']的取值调用适应的交易算法。
        :param pOrder: AlgoPlus.CTP.ApiStruct中OrderField的实例。
        OrderField的OrderStatus字段枚举值及含义：
        (‘全部成交 : 0’,)
        (‘部分成交还在队列中 : 1’,)
        (‘部分成交不在队列中 : 2’,)
        (‘未成交还在队列中 : 3’,)
        (‘未成交不在队列中 : 4’,)
        (‘撤单 : 5’,)
        (‘未知 : a’,)
        (‘尚未触发 : b’,)
        (‘已触发 : c’,)
        OrderField的OrderSubmitStatus字段枚举值及含义：
        (‘已经提交 : 0’,)
        (‘撤单已经提交 : 1’,)
        (‘修改已经提交 : 2’,)
        (‘已经接受 : 3’,)
        (‘报单已经被拒绝 : 4’,)
        (‘撤单已经被拒绝 : 5’,)
        (‘改单已经被拒绝 : 6’,)
        :return:
        """
        # # 延时计时结束
        if self.is_my_order(pOrder['OrderRef']):
            self.rtn_order_list.append(pOrder)

    def process_rtn_order(self):
        try:
            last_rtn_order_index = len(self.rtn_order_list)
            for rtn_order in self.rtn_order_list[self.last_rtn_order_index:last_rtn_order_index]:
                # 未成交
                if rtn_order['OrderStatus'] == OrderStatus_NoTradeQueueing:
                    pass

                # 全部成交
                elif rtn_order['OrderStatus'] == OrderStatus_AllTraded or rtn_order['OrderStatus'] == OrderStatus_PartTradedQueueing:
                    self.on_order_traded(rtn_order)

                # 撤单成功
                elif rtn_order['OrderStatus'] == OrderStatus_Canceled:
                    if rtn_order['InstrumentID'] in self.action_num_dict.keys():
                        self.action_num_dict[rtn_order['InstrumentID']] += 1
                    else:
                        self.action_num_dict[rtn_order['InstrumentID']] = 1
                    self.on_order_action(rtn_order)

                # 委托失败
                elif rtn_order['OrderSubmitStatus'] == OrderSubmitStatus_InsertRejected:
                    self.on_order_insert_fail(rtn_order)

                # 撤单失败
                elif rtn_order['OrderSubmitStatus'] == OrderSubmitStatus_CancelRejected:
                    self.on_order_action_fail(rtn_order)

                self.write_log(to_str(rtn_order['StatusMsg']), rtn_order)
            self.last_rtn_order_index = last_rtn_order_index
        except Exception as err_msg:
            self.write_log('process_rtn_order', err_msg.__doc__)

    def on_order_traded(self, pOrder):
        pass

    def on_order_action(self, pOrder):
        pass

    # ############################################################################# #
    def OnRtnTrade(self, pTrade):
        """
        当报单成交时，可以在本方法中获得通知。不适宜在回调函数里做比较耗时的操作。可参考OnRtnOrder的做法。
        TradeField包含成交价格，而OrderField则没有。
        如果不需要成交价格，可忽略该通知，使用OrderField。
        :param pTrade: AlgoPlus.CTP.ApiStruct中的TradeField实例。
        :return:
        """
        if self.is_my_order(pTrade['OrderRef']):
            self.rtn_trade_list.append(pTrade)

    def process_rtn_trade(self):
        """
        从上次订单ID位置开始处理订单数据。
        :return:
        """
        try:
            last_rtn_trade_index = len(self.rtn_trade_list)
            for rtn_trade in self.rtn_trade_list[self.last_rtn_trade_index:last_rtn_trade_index]:

                rtn_trade['IsLock'] = False
                rtn_trade['AnchorTime'] = timer()
                rtn_trade['StopProfitDict'] = {}
                rtn_trade['StopLossDict'] = {}
                if rtn_trade['InstrumentID'] not in self.local_position_dict.keys():
                    self.local_position_dict[rtn_trade['InstrumentID']] = {'LongVolume': 0, 'LongVolumeToday': 0, 'LongVolumeYesterday': 0, 'LongPositionList': [],
                                                                           'ShortVolume': 0, 'ShortVolumeToday': 0, 'ShortVolumeYesterday': 0, 'ShortPositionList': []}
                local_position = self.local_position_dict[rtn_trade['InstrumentID']]

                if rtn_trade['OffsetFlag'] == OffsetFlag_Open:
                    self.update_stop_price(rtn_trade)
                    if rtn_trade['Direction'] == Direction_Buy:
                        local_position['LongVolume'] += rtn_trade['Volume']
                        local_position['LongPositionList'].append(rtn_trade)
                    elif rtn_trade['Direction'] == Direction_Sell:
                        local_position['ShortVolume'] += rtn_trade['Volume']
                        local_position['ShortPositionList'].append(rtn_trade)
                elif rtn_trade['Direction'] == Direction_Buy:
                    local_position['ShortVolume'] = max(local_position['ShortVolume'] - rtn_trade['Volume'], 0)
                elif rtn_trade['Direction'] == Direction_Sell:
                    local_position['LongVolume'] = max(local_position['LongVolume'] - rtn_trade['Volume'], 0)

            self.last_rtn_trade_index = last_rtn_trade_index
        except Exception as err_msg:
            self.write_log('process_rtn_trade', err_msg)

    def update_stop_price(self, position):
        """
        获取止盈止损阈值。止损类型参考https://7jia.com/1002.html
        :param position: 持仓信息
        :return:
        """
        try:
            if position['InstrumentID'] in self.pl_parameter_dict.keys():
                pl_dict = self.pl_parameter_dict[position['InstrumentID']]
                for pl_type, delta in pl_dict.items():
                    # 固定止盈
                    sgn = 1 if position['Direction'] == Direction_Buy else -1
                    if pl_type == '0':
                        position['StopProfitDict']['0'] = position['Price'] + delta[0] * sgn
                    # 固定止损
                    elif pl_type == '1':
                        position['StopLossDict']['1'] = position['Price'] - delta[0] * sgn
        except Exception as err_msg:
            self.write_log('update_stop_price', err_msg)

    # ############################################################################# #
    def check_position(self):
        """
        检查所有持仓是否触发持仓阈值。
        """
        try:
            for instrument_id, position in self.local_position_dict.items():
                if instrument_id not in self.md_dict.keys():
                    break
                md = self.md_dict[instrument_id]
                for long_position in position['LongPositionList']:
                    if not long_position['IsLock']:
                        trigger = False
                        for stop_profit in long_position['StopProfitDict'].values():
                            if md['LastPrice'] > stop_profit:
                                trigger = True
                                break

                        if not trigger:
                            for stop_loss in long_position['StopLossDict'].values():
                                if md['LastPrice'] < stop_loss:
                                    trigger = True
                                    break

                        if trigger:
                            order_price = self.get_price(instrument_id, Direction_Sell)
                            if order_price is not None:
                                self.sell_close(long_position['ExchangeID'], instrument_id, order_price, long_position['Volume'])
                                long_position['IsLock'] = True

                for short_position in position['ShortPositionList']:
                    if not short_position['IsLock']:
                        trigger = False
                        for stop_profit in short_position['StopProfitDict'].values():
                            if md['LastPrice'] < stop_profit:
                                trigger = True
                                break

                        if not trigger:
                            for stop_loss in short_position['StopLossDict'].values():
                                if md['LastPrice'] > stop_loss:
                                    trigger = True
                                    break

                        if trigger:
                            order_price = self.get_price(instrument_id, Direction_Buy)
                            if order_price is not None:
                                self.buy_close(short_position['ExchangeID'], instrument_id, order_price, short_position['Volume'])
                                short_position['IsLock'] = True
        except Exception as err:
            self.write_log(err)

    # ############################################################################# #
    def Join(self):
        while True:
            if self.status == 0:
                if self.md_queue is not None:
                    while not self.md_queue.empty():
                        last_md = self.md_queue.get(block=False)
                        self.md_dict[last_md['InstrumentID']] = last_md

                self.process_rtn_order()
                self.process_rtn_trade()
                self.check_position()
            else:
                sleep(1)


def run_traderapi(account, md_queue=None):
    if isinstance(account, FutureAccount):
        trader_engine = TraderApi(
            account.broker_id,
            account.server_dict['TDServer'],
            account.investor_id,
            account.password,
            account.app_id,
            account.auth_code,
            md_queue,
            account.td_page_dir
        )
        trader_engine.Join()


class ReqInstrumentApi(TraderApiBase):
    def __init__(self, broker_id, td_server, investor_id, password, app_id, auth_code, md_queue=None,
                 page_dir='', private_resume_type=2, public_resume_type=2):
        self.instrument_id_list = []

    def req_qry_instrumrent_id(self):
        qry_instrument_field = QryInstrumentField()
        self.ReqQryInstrument(qry_instrument_field)

    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        if not pRspInfo or pRspInfo['ErrorID'] == 0:
            if pInstrument \
                and (pInstrument['InstrumentID'][-4:].isdigit() and pInstrument['InstrumentID'][:-4].isalpha()
                     or pInstrument['InstrumentID'][-3:].isdigit() and pInstrument['InstrumentID'][:-3].isalpha()):
                self.instrument_id_list.append(pInstrument['InstrumentID'])

            self.status += bIsLast

    def Join(self):
        while True:
            if self.status == 0:
                self.req_qry_instrumrent_id()
                self.status = 1
            elif self.status == 2:
                return self.instrument_id_list
            sleep(1)


def req_instrument(account):
    if isinstance(account, FutureAccount):
        trader_engine = ReqInstrumentApi(account.broker_id,
                                         account.server_dict['TDServer'],
                                         account.investor_id,
                                         account.password,
                                         account.app_id,
                                         account.auth_code,
                                         None,
                                         account.td_page_dir)
        return trader_engine.Join()
