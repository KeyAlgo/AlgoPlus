# encoding:utf-8

# AlgoPlus量化投资开源框架范例
# 微信公众号：AlgoPlus
# 项目网址：http://www.algo.plus

# bar_cache = {
#     "InstrumentID": b"",
#     "UpdateTime": b"99:99:99",
#     "LastPrice": 0.0,
#     "HighPrice": 0.0,
#     "LowPrice": 0.0,
#     "OpenPrice": 0.0,
#     "BarVolume": 0,
#     "BarTurnover": 0.0,
#     "BarSettlement": 0.0,
#     "BVolume": 0,
#     "SVolume": 0,
#     "FVolume": 0,
#     "DayVolume": 0,
#     "DayTurnover": 0.0,
#     "DaySettlement": 0.0,
#     "OpenInterest": 0.0,
#     "LastVolume": 0,
#     "TradingDay": b"99999999",
# }


def tick_to_bar(bar_cache, raw_frame, is_new_bar):
    if raw_frame['TradingDay'] != bar_cache["TradingDay"]:
        bar_cache["LastVolume"] = 0  # Bar成交量
        bar_cache["DayVolume"] = 0  # Day成交量
        bar_cache["DayTurnover"] = 0.0  # Day成交额
        bar_cache["TradingDay"] = raw_frame['TradingDay']

    tick_volume = raw_frame['Volume'] - bar_cache["LastVolume"]  # Tick成交量
    bar_cache["LastVolume"] = raw_frame['Volume']
    bar_cache["UpdateTime"] = raw_frame['UpdateTime']  # 时间戳
    bar_cache["OpenInterest"] = raw_frame['OpenInterest']  # 持仓量

    if is_new_bar:
        # "B"为主动买，"S"为主动卖，"F"为模糊状态
        bar_cache["BVolume"] = 0
        bar_cache["SVolume"] = 0
        bar_cache["FVolume"] = 0

        bar_cache["BarVolume"] = 0  # Bar成交量
        bar_cache["BarTurnover"] = 0.0  # Bar成交额

    # 有成交
    if tick_volume > 0:
        tick_turnover = tick_volume * raw_frame['LastPrice']  # Tick成交额

        bar_cache["DayVolume"] += tick_volume  # Day成交量
        bar_cache["DayTurnover"] += tick_turnover  # Day成交额
        bar_cache["DaySettlement"] = bar_cache["DayTurnover"] / bar_cache["DayVolume"]  # Day均价

        # "B"为主动买，"S"为主动卖，"F"为模糊状态
        if raw_frame['LastPrice'] >= raw_frame['AskPrice1']:
            bar_cache["BVolume"] += tick_volume  # Bar主动买成交量
        elif raw_frame['LastPrice'] <= raw_frame['BidPrice1']:
            bar_cache["SVolume"] += tick_volume  # Bar主动卖成交量
        else:
            bar_cache["FVolume"] += tick_volume  # Bar模糊成交量

        if bar_cache["BarVolume"] == 0:
            bar_cache["LastPrice"] = raw_frame['LastPrice']  # Bar收盘价
            bar_cache["HighPrice"] = raw_frame['LastPrice']  # Bar最高价
            bar_cache["LowPrice"] = raw_frame['LastPrice']  # Bar最低价
            bar_cache["OpenPrice"] = raw_frame['LastPrice']  # Bar开盘价
            bar_cache["BarVolume"] = tick_volume  # Bar成交量
            bar_cache["BarTurnover"] = tick_turnover  # Bar成交额
            bar_cache["BarSettlement"] = raw_frame['LastPrice']  # Bar均价
        else:
            bar_cache["LastPrice"] = raw_frame['LastPrice']  # Bar收盘价
            bar_cache["HighPrice"] = max(raw_frame['LastPrice'], bar_cache["HighPrice"])  # Bar最高价
            bar_cache["LowPrice"] = min(raw_frame['LastPrice'], bar_cache["LowPrice"])  # Bar最低价
            bar_cache["BarVolume"] += tick_volume  # Bar成交量
            bar_cache["BarTurnover"] += tick_turnover  # Bar成交额
            bar_cache["BarSettlement"] = bar_cache["BarTurnover"] / bar_cache["BarVolume"]  # Bar均价
