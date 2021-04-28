# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from multiprocessing import Process, Queue
from AlgoPlus.CTP.MdApi import run_tick_engine
from AlgoPlus.CTP.FutureAccount import get_simnow_account,FutureAccount
from AlgoPlus.CTP.FutureAccount import SIMNOW_SERVER,MD_LOCATION,TD_LOCATION


def print_tick(md_queue):
    while True:
        if not md_queue.empty():
            print(md_queue.get(block=False))


if __name__ == '__main__':
    # 账户配置
    instrument_id_list = [b'IC2103',b'j2105']  # 需要订阅的合约列表
    # future_account = get_simnow_account(
    #     investor_id='',                   # SimNow账户
    #     password='',                     # SimNow账户密码
    #     instrument_id_list=instrument_id_list,  # 合约列表
    #     server_name='TEST'                      # 电信1、电信2、移动、TEST
    # )
    future_account = FutureAccount(
        broker_id='9999',  # 期货公司BrokerID
        server_dict={'TDServer': "180.168.146.187:10100", 'MDServer': '180.168.146.187:10110'},  # TDServer为交易服务器，MDServer为行情服务器。服务器地址格式为"ip:port。"
        reserve_server_dict={},
        investor_id="investor_id",  # 账户
        password="password",  # 密码
        app_id='simnow_client_test',  # 认证使用AppID
        auth_code='0000000000000000',  # 认证使用授权码
        instrument_id_list=instrument_id_list,  # 订阅合约列表
        md_page_dir=MD_LOCATION,  # MdApi流文件存储地址，默认MD_LOCATION
        td_page_dir=TD_LOCATION  # TraderApi流文件存储地址，默认TD_LOCATION
    )

    # 共享队列
    share_queue = Queue(maxsize=100)

    # 行情进程
    md_process = Process(target=run_tick_engine, args=(future_account, [share_queue]))
    # 交易进程
    print_process = Process(target=print_tick, args=(share_queue,))

    #
    md_process.start()
    print_process.start()

    #
    md_process.join()
    print_process.join()
