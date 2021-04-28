# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from multiprocessing import Queue
from AlgoPlus.CTP.ReqAuthenticate import run_req_authenticate
from AlgoPlus.CTP.FutureAccount import get_simnow_account

if __name__ == '__main__':
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
    run_req_authenticate(account, share_queue)
