# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from multiprocessing import Process, Queue
from AlgoPlus.CTP.TraderApi import req_instrument
from AlgoPlus.CTP.MdApi import run_mdrecorder
from AlgoPlus.CTP.FutureAccount import get_simnow_account


if __name__ == '__main__':
    # 账户配置
    future_account = get_simnow_account(
        investor_id='',  # SimNow账户
        password='',  # SimNow账户密码
        server_name=''  # 电信1、电信2、移动、TEST
    )

    # 查询所有期货合约
    future_account.instrument_id_list = req_instrument(future_account)

    # 订阅并保存行情为csv文件
    run_mdrecorder(future_account)
