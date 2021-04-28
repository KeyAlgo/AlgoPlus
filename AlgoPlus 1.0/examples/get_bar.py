# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from multiprocessing import Process, Queue
from AlgoPlus.CTP.MdApi import run_bar_engine
from AlgoPlus.CTP.FutureAccount import get_simnow_account


def print_bar(md_queue):
    while True:
        if not md_queue.empty():
            print(md_queue.get(block=False))


if __name__ == '__main__':
    instrument_id_list = [b'rb2010']
    future_account = get_simnow_account(
        investor_id='',                   # SimNow账户
        password='',                     # SimNow账户密码
        instrument_id_list=instrument_id_list,  # 合约列表
        server_name='TEST'                      # 电信1、电信2、移动、TEST
    )

    # 共享队列
    share_queue = Queue(maxsize=100)

    # 行情进程
    md_process = Process(target=run_bar_engine, args=(future_account, [share_queue]))
    # 交易进程
    print_process = Process(target=print_bar, args=(share_queue,))

    md_process.start()
    print_process.start()

    md_process.join()
    print_process.join()
