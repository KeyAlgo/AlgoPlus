# -*- coding: utf-8 -*-
# AlgoPlus量化投资开源框架范例
# 微信公众号：AlgoPlus
# 项目地址：http://gitee.com/AlgoPlus/AlgoPlus
# 项目网址：http://www.algo.plus
# 项目网址：http://www.ctp.plus
# 项目网址：http://www.7jia.com

import time
from multiprocessing import Queue
from AlgoPlus.CTP.TraderApiBase import TraderApiBase
from AlgoPlus.CTP.FutureAccount import get_simnow_account


class RollingTrade(TraderApiBase):
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

    def OnRtnTrade(self, pTrade):
        pass

    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        pass

    # 订单状态通知
    def OnRtnOrder(self, pOrder):
        if pOrder['OrderStatus'] == b"0":
            if self.order_ref < 300:
                self.buy_open(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.parameter_dict['UpperLimitPrice'], self.parameter_dict['Volume'])
            else:
                self.write_log("滚动交易（300笔）已经全部完成！")

    def Join(self):
        while True:
            if self.status >= 0 and self.order_ref == 0:
                self.buy_open(self.parameter_dict['ExchangeID'], self.parameter_dict['InstrumentID'], self.parameter_dict['UpperLimitPrice'], self.parameter_dict['Volume'])

            time.sleep(1)


if __name__ == "__main__":
    # 账户配置
    account = get_simnow_account(
        investor_id=b'',
        password=b'',
        server_name='TEST'
    )

    # 交易参数
    parameter_dict = {
        'ExchangeID': b'SHFE',  # 交易所
        'InstrumentID': b'rb2010',  # 合约代码
        'UpperLimitPrice': 3593,  # 涨停板
        'LowerLimitPrice': 3312,  # 跌停板
        'Volume': 1,  # 报单手数
    }

    # 共享队列
    share_queue = Queue(maxsize=100)
    share_queue.put(parameter_dict)

    #
    rolling_trade = RollingTrade(
        account.broker_id,
        account.server_dict['TDServer'],
        account.investor_id,
        account.password,
        account.app_id,
        account.auth_code,
        share_queue,
        account.td_page_dir
    )

    #
    rolling_trade.Join()
