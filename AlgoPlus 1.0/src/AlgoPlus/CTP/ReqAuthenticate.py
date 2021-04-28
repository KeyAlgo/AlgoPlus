# encoding:utf-8

# AlgoPlus量化投资开源框架范例
# 微信公众号：AlgoPlus
# 项目网址：http://www.algo.plus

import time
from AlgoPlus.CTP.TraderApiBase import TraderApiBase
from AlgoPlus.CTP.FutureAccount import FutureAccount


class ReqAuthenticate(TraderApiBase):
    def __init__(self, broker_id, td_server, investor_id, password, app_id, auth_code, md_queue=None,
                 page_dir='', private_resume_type=2, public_resume_type=2):
        pass

    def init_extra(self):
        """
        初始化策略参数
        :return:
        """
        # {
        #     'ExchangeID': b'',  # 交易所
        #     'InstrumentID': b'',  # 合约代码
        #     'UpperLimitPrice': 0.0,  # 涨停板
        #     'LowerLimitPrice': 0.0,  # 跌停板
        #     'Volume': 1,  # 报单手数
        # }
        self.parameter_dict = self.md_queue.get(block=False)

    # ############################################################################# #
    def OnRtnOrder(self, pOrder):
        # self.write_log('OnRtnOrder', pOrder)
        pass

    # ############################################################################# #
    def OnRtnTrade(self, pTrade):
        # self.write_log('OnRtnTrade', pTrade)
        pass

    def OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        if bIsLast:
            self.write_log('OnRspQryOrder', "查询结果，避免内容太长不输出。")

    def OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        if bIsLast:
            self.write_log('OnRspQryTrade', "查询结果，避免内容太长不输出。")

    def OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        if bIsLast:
            self.write_log('OnRspQryInvestorPosition', "查询结果，避免内容太长不输出。")

    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        if bIsLast:
            self.write_log('OnRspQryTradingAccount', "查询结果，避免内容太长不输出。")

    def Join(self):
        while True:
            if self.status >= 0 and isinstance(self.parameter_dict, dict):
                # ############################################################################# #
                # 连续5次买开 - 卖平
                ikk = 0
                while ikk < 5:
                    ikk += 1
                    self.buy_open(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.parameter_dict['UpperLimitPrice'], self.parameter_dict['Volume'])
                    self.write_log(f"=>{ikk}=>发出涨停买开仓请求！")
                    time.sleep(3)

                    # 跌停卖平仓
                    self.sell_close(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.parameter_dict['LowerLimitPrice'], self.parameter_dict['Volume'], True)
                    self.write_log(f"=>{ikk}=>发出跌停卖平仓请求！")

                # ############################################################################# #
                # 连续5次卖开 - 买平
                ikk = 0
                while ikk < 5:
                    ikk += 1
                    # 跌停卖开仓
                    self.sell_open(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.parameter_dict['LowerLimitPrice'], self.parameter_dict['Volume'])
                    self.write_log(f"=>{ikk}=>发出跌停卖开仓请求！")
                    time.sleep(3)

                    # 涨停买平仓
                    self.buy_close(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.parameter_dict['UpperLimitPrice'], self.parameter_dict['Volume'], True)
                    self.write_log(f"=>{ikk}=>发出涨停买平仓请求！")

                # ############################################################################# #
                # 买开 - 撤单
                self.buy_open(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.parameter_dict['LowerLimitPrice'], self.parameter_dict['Volume'])
                self.write_log(f"=>发出涨停买开仓请求！")
                time.sleep(3)

                # 撤单
                self.req_order_action(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.order_ref)
                self.write_log(f"=>发出撤单请求！")

                # ############################################################################# #
                # 卖开 - 撤单
                self.sell_open(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.parameter_dict['UpperLimitPrice'], self.parameter_dict['Volume'])
                self.write_log(f"=>发出跌停卖开仓请求！")
                time.sleep(3)

                # 撤单
                self.req_order_action(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.order_ref)
                self.write_log(f"=>发出撤单请求！")

                # ############################################################################# #
                # 查询订单
                self.req_qry_order()
                self.write_log(f"=>发出查询订单请求！")
                time.sleep(3)

                # ############################################################################# #
                # 查询成交
                self.req_qry_trade()
                self.write_log(f"=>发出查询成交请求！")
                time.sleep(3)

                # ############################################################################# #
                # 查询持仓
                self.req_qry_investor_position()
                self.write_log(f"=>发出查询持仓请求！")
                time.sleep(3)

                # ############################################################################# #
                # 查询资金
                self.req_qry_trading_account()
                self.write_log(f"=>发出查询资金请求！")
                time.sleep(3)

                # ############################################################################# #
                print("看穿式监管认证仿真交易已经完成！可联系期货公司！")
                break

            time.sleep(1)


def run_req_authenticate(account, md_queue):
    if isinstance(account, FutureAccount):
        trader_engine = ReqAuthenticate(
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
