# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

import os

BASE_LOCATION = "."
MD_LOCATION = BASE_LOCATION + os.path.sep + "MarketData"
TD_LOCATION = BASE_LOCATION + os.path.sep + "TradingData"
SD_LOCATION = BASE_LOCATION + os.path.sep + "StrategyData"


SIMNOW_SERVER = {
    '电信1': {'TDServer': "180.168.146.187:10100", 'MDServer': '180.168.146.187:10110'},
    '电信2': {'TDServer': "180.168.146.187:10101", 'MDServer': '180.168.146.187:10111'},
    '移动': {'TDServer': "218.202.237.33:10102", 'MDServer': '218.202.237.33:10112'},
    'TEST': {'TDServer': "180.168.146.187:10130", 'MDServer': '180.168.146.187:10131'},
}


class FutureAccount:
    def __init__(self, broker_id, server_dict, reserve_server_dict, investor_id, password, app_id, auth_code, instrument_id_list, md_page_dir=MD_LOCATION, td_page_dir=TD_LOCATION):
        self.broker_id = broker_id  # 期货公司BrokerID
        self.server_dict = server_dict  # 登录的服务器地址
        self.reserve_server_dict = reserve_server_dict  # 备用服务器地址
        self.investor_id = investor_id  # 账户
        self.password = password  # 密码
        self.app_id = app_id  # 认证使用AppID
        self.auth_code = auth_code  # 认证使用授权码
        self.instrument_id_list = instrument_id_list  # 订阅合约列表[]
        self.md_page_dir = md_page_dir  # MdApi流文件存储地址，默认MD_LOCATION
        self.td_page_dir = td_page_dir  # TraderApi流文件存储地址，默认TD_LOCATION


def get_simnow_account(investor_id, password, instrument_id_list=None, server_name='电信1', md_page_dir=MD_LOCATION, td_page_dir=TD_LOCATION):
    if server_name not in SIMNOW_SERVER.keys():
        print(f'{server_name}不在可选列表[电信1, 电信2, 移动, TEST]中，默认使用电信1。')
        server_name = '电信1'

    if instrument_id_list is None:
        instrument_id_list = []

    investor_id = investor_id if isinstance(investor_id, bytes) else investor_id.encode(encoding='utf-8')
    password = password if isinstance(password, bytes) else password.encode(encoding='utf-8')
    return FutureAccount(
        broker_id='9999',  # 期货公司BrokerID
        server_dict=SIMNOW_SERVER[server_name],  # TDServer为交易服务器，MDServer为行情服务器。服务器地址格式为"ip:port。"
        reserve_server_dict={},
        investor_id=investor_id,  # 账户
        password=password,  # 密码
        app_id='simnow_client_test',  # 认证使用AppID
        auth_code='0000000000000000',  # 认证使用授权码
        instrument_id_list=instrument_id_list,  # 订阅合约列表
        md_page_dir=md_page_dir,  # MdApi流文件存储地址，默认MD_LOCATION
        td_page_dir=td_page_dir  # TraderApi流文件存储地址，默认TD_LOCATION
    )
