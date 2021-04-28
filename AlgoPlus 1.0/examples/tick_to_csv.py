# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from AlgoPlus.CTP.MdApi import run_mdrecorder
from AlgoPlus.CTP.FutureAccount import FutureAccount, get_simnow_account


if __name__ == '__main__':
    # 账户配置
    instrument_id_list = [b'rb2010']  # 需要订阅的合约列表
    future_account = get_simnow_account(
        investor_id=b'',  # SimNow账户
        password=b'',  # SimNow账户密码
        instrument_id_list=instrument_id_list,  # 合约列表
        server_name='TEST'  # 电信1、电信2、移动、TEST
    )

    #
    run_mdrecorder(future_account)
