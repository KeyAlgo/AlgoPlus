# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

import os
import csv
from AlgoPlus.CTP.MdApiBase import MdApiBase
from AlgoPlus.CTP.FutureAccount import FutureAccount
from AlgoPlus.ta.time_bar import tick_to_bar
from AlgoPlus.utils.base_field import to_str, to_bytes
from AlgoPlus.CTP.ApiStruct import DepthMarketDataField


class TickEngine(MdApiBase):
    def __init__(self, broker_id, md_server, investor_id, password, app_id, auth_code, instrument_id_list, md_queue_list=None,
                 page_dir='', using_udp=False, multicast=False):
        pass

    def OnRtnDepthMarketData(self, pDepthMarketData):
        # 将行情放入共享队列
        for md_queue in self.md_queue_list:
            md_queue.put(pDepthMarketData)


class BarEngine(MdApiBase):
    def __init__(self, md_server, broker_id, investor_id, password, app_id, auth_code, instrument_id_list, md_queue_list=None,
                 page_dir='', using_udp=False, multicast=False):
        pass

    def init_extra(self):
        # Bar字段
        bar_cache = {
            "InstrumentID": b"",
            "UpdateTime": b"99:99:99",
            "LastPrice": 0.0,
            "HighPrice": 0.0,
            "LowPrice": 0.0,
            "OpenPrice": 0.0,
            "BarVolume": 0,
            "BarTurnover": 0.0,
            "BarSettlement": 0.0,
            "BVolume": 0,
            "SVolume": 0,
            "FVolume": 0,
            "DayVolume": 0,
            "DayTurnover": 0.0,
            "DaySettlement": 0.0,
            "OpenInterest": 0.0,
            "LastVolume": 0,
            "TradingDay": b"99999999",
        }

        self.bar_dict = {}  # Bar字典容器
        # 遍历订阅列表
        for instrument_id in self.instrument_id_list:
            # 将str转为byte
            if not isinstance(instrument_id, bytes):
                instrument_id = to_bytes(instrument_id.encode('utf-8'))

            # 初始化Bar字段
            bar_cache["InstrumentID"] = instrument_id
            self.bar_dict[instrument_id] = bar_cache.copy()

    # ///深度行情通知
    def OnRtnDepthMarketData(self, pDepthMarketData):
        last_update_time = self.bar_dict[pDepthMarketData['InstrumentID']]["UpdateTime"]
        is_new_1minute = (pDepthMarketData['UpdateTime'][:-2] != last_update_time[:-2]) and pDepthMarketData['UpdateTime'] != b'21:00:00'  # 1分钟K线条件
        # is_new_5minute = is_new_1minute and int(pDepthMarketData['UpdateTime'][-4]) % 5 == 0  # 5分钟K线条件
        # is_new_10minute = is_new_1minute and pDepthMarketData['UpdateTime'][-4] == b"0"  # 10分钟K线条件
        # is_new_10minute = is_new_1minute and int(pDepthMarketData['UpdateTime'][-5:-3]) % 15 == 0  # 15分钟K线条件
        # is_new_30minute = is_new_1minute and int(pDepthMarketData['UpdateTime'][-5:-3]) % 30 == 0  # 30分钟K线条件
        # is_new_hour = is_new_1minute and int(pDepthMarketData['UpdateTime'][-5:-3]) % 60 == 0  # 60分钟K线条件

        # # 新K线开始
        if is_new_1minute and self.bar_dict[pDepthMarketData['InstrumentID']]["UpdateTime"] != b"99:99:99":
            for md_queue in self.md_queue_list:
                md_queue.put(self.bar_dict[pDepthMarketData['InstrumentID']])

        # 将Tick池化为Bar
        tick_to_bar(self.bar_dict[pDepthMarketData['InstrumentID']], pDepthMarketData, is_new_1minute)


class MdRecorder(MdApiBase):
    def __init__(self, broker_id, md_server, investor_id, password, app_id, auth_code, instrument_id_list, md_queue_list=None, page_dir='', using_udp=False, multicast=False):
        pass

    def init_extra(self):
        self.csv_file_dict = {}
        self.csv_writer = {}
        # 深度行情结构体字段名列表
        header = list(DepthMarketDataField().to_dict())
        for instrument_id in self.instrument_id_list:
            instrument_id = to_str(instrument_id)
            # file object
            file_dir = os.path.join(self.page_dir, f'{instrument_id}-{to_str(self.GetTradingDay())}.csv')
            self.csv_file_dict[instrument_id] = open(file_dir, 'a', newline='')
            # writer object
            self.csv_writer[instrument_id] = csv.DictWriter(self.csv_file_dict[instrument_id], header)
            # 写入表头
            self.csv_writer[instrument_id].writeheader()
            self.csv_file_dict[instrument_id].flush()

    # ///深度行情通知
    def OnRtnDepthMarketData(self, pDepthMarketData):
        try:
            for key in pDepthMarketData.keys():
                pDepthMarketData[key] = to_str(pDepthMarketData[key])
            # 写入行情
            self.csv_writer[pDepthMarketData['InstrumentID']].writerow(pDepthMarketData)
            self.csv_file_dict[pDepthMarketData['InstrumentID']].flush()
        except Exception as err_msg:
            self.write_log(err_msg, pDepthMarketData)


def run_api(api_cls, account, md_queue_list=None):
    if isinstance(account, FutureAccount):
        tick_engine = api_cls(
            account.broker_id,
            account.server_dict['MDServer'],
            account.investor_id,
            account.password,
            account.app_id,
            account.auth_code,
            account.instrument_id_list,
            md_queue_list,
            account.md_page_dir
        )
        tick_engine.Join()


def run_tick_engine(account, md_queue_list):
    run_api(TickEngine, account, md_queue_list)


def run_bar_engine(account, md_queue_list):
    run_api(BarEngine, account, md_queue_list)


def run_mdrecorder(account):
    run_api(MdRecorder, account, None)
