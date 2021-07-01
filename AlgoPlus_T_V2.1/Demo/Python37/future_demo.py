import sys
import AlgoPlus as ap


# #######
@ap.marketdata_callback_wraps
def future_marketdata_callback1(event_id, data):
    # print("=======")
    # print(event_id)
    # print(data)
    # print("=======")
    pass


def future_marketdata_callback2(event_id, data):
    # data = ap.decode_marketdata_field(data)
    pass


# #######
@ap.order_callback_wraps
def future_order_callback1(event_id, order, position, cash):
    print("=======")
    print(event_id)
    print(order)
    print(position)
    print(cash)
    print("=======")


def future_order_callback2(event_id, order, position, cash):
    order = ap.decode_order_field(order)
    position = ap.decode_position_field(position)


# #######
@ap.flexible_callback_wraps
def future_flexible_callback1(event_id, field, islast, user_id, error_id, error_msg):
    # print("=======")
    # print(event_id, islast, user_id, error_id, error_msg)
    # print(field)
    # print("=======")
    pass


def future_flexible_callback2(event_id, field, islast, user_id, error_id, error_msg):
    field = ap.decode_event_field(event_id, field)


# #######
def future_loop_callback():
    global my_strategy

    unit_amount = 20000
    step = 100
    my_strategy.count += 1

    if my_strategy.count % step == 0:
        print('loop', my_strategy.count)

    if my_strategy.count == step * 1:
        ap.buyOpen(my_strategy.trader, my_strategy.instrument_id, 8, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    # elif my_strategy.count == step * 2:
    #     ap.sellClose(my_strategy.trader, my_strategy.instrument_id, 2, ap.ENUM_OrderType_FrontierLimitAndWait, 0, 0, None, ap.ENUM_Direction_Sell, ap.ENUM_OffsetFlag_CloseHistory)
    elif my_strategy.count == step * 3:
        ap.sellClose(my_strategy.trader, my_strategy.instrument_id, 2, ap.ENUM_OrderType_FrontierLimitAndWait, 0, 0, None, ap.ENUM_Direction_Sell, ap.ENUM_OffsetFlag_CloseToday)
    elif my_strategy.count == step * 4:
        ap.sellOpen(my_strategy.trader, my_strategy.instrument_id, 8, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    # elif my_strategy.count == step * 5:
    #     ap.buyClose(my_strategy.trader, my_strategy.instrument_id, 2, ap.ENUM_OrderType_FrontierLimitAndWait, 0, 0, None, ap.ENUM_Direction_Buy, ap.ENUM_OffsetFlag_CloseHistory)
    elif my_strategy.count == step * 6:
        ap.buyClose(my_strategy.trader, my_strategy.instrument_id, 2, ap.ENUM_OrderType_FrontierLimitAndWait, 0, 0, None, ap.ENUM_Direction_Buy, ap.ENUM_OffsetFlag_CloseToday)
    elif my_strategy.count == step * 7:
        ap.buy(my_strategy.trader, my_strategy.instrument_id, 30, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    elif my_strategy.count == step * 8:
        ap.buyAmount(my_strategy.trader, my_strategy.instrument_id, unit_amount, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    elif my_strategy.count == step * 9:
        ap.sell(my_strategy.trader, my_strategy.instrument_id, 24, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    elif my_strategy.count == step * 10:
        ap.sellAmount(my_strategy.trader, my_strategy.instrument_id, unit_amount, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    elif my_strategy.count == step * 11:
        ap.balanceToShortVolume(my_strategy.trader, my_strategy.instrument_id, 10, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    elif my_strategy.count == step * 12:
        ap.balanceToLongValue(my_strategy.trader, my_strategy.instrument_id, unit_amount, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    elif my_strategy.count == step * 13:
        ap.balanceToLongVolume(my_strategy.trader, my_strategy.instrument_id, 10, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    elif my_strategy.count == step * 14:
        ap.closeLong(my_strategy.trader, my_strategy.instrument_id, 1, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
    elif my_strategy.count == step * 15:
        ap.closeLong(my_strategy.trader, my_strategy.instrument_id, 9999, ap.ENUM_OrderType_FrontierLimitAndWait, 0)


class Strategy:
    def __init__(self, instrument_id):
        self.login_field = ap.CAPLoginField()
        self.trader = None
        self.instrument_id = instrument_id
        self.subscribe_list = [instrument_id]
        self.count = 0


if __name__ == '__main__':

    my_strategy = Strategy('au2112')

    # 加QQ号2565657639(注明AlgoPlus授权)，或者公众号AlgoPlus后台留言，免费申请模拟交易授权。
    my_strategy.login_field.License = ""
    my_strategy.login_field.UserType = ap.ENUM_UserType_SIMNOWFuture
    my_strategy.login_field.UserID = ""
    my_strategy.login_field.Password = ""
    my_strategy.login_field.TraderFront = "tcp://180.168.146.187:10201"
    my_strategy.login_field.MdFront = "tcp://180.168.146.187:10211"
    my_strategy.login_field.BrokerID = "9999"
    my_strategy.login_field.AppID = "simnow_client_test"
    my_strategy.login_field.AuthCode = "0000000000000000"

    my_strategy.trader = ap.init(1, my_strategy.login_field, None, None, future_loop_callback, None)
    if my_strategy.trader is not None:
        ap.subscribe(my_strategy.trader, my_strategy.subscribe_list)
        ap.loop()
    else:
        init_error_id = ap.getInitError()
        print(f"future init errors:{init_error_id}")
        sys.exit(1)
