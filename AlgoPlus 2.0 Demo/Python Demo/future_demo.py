import sys
import AlgoPlus as ap


@ap.ap_marketdata_callback_wraps
def future_on_marketdata_event(data):
    print(data)


@ap.ap_order_callback_wraps
def future_on_order_event(event_id, order, position, cash):
    print(f"on_order {order}")


def future_on_event(event_id, field, islast, error_id, error_msg):
    field = ap.decode_ctp_event_field(event_id, field)
    if islast:
        print("event", event_id, field)


def future_on_loop():
    global future_counter
    global future_list
    global future_trader

    future_counter += 1
    print(f"loop:{future_counter}")
    if future_counter == 1:
        ap.cancelOrderAll(future_trader)
    elif future_counter == 100:
        for item in future_list:
            ap.buy(future_trader, item, 1, ap.ENUM_OrderType_FrontierLimitAndWait, 0)


if __name__ == '__main__':

    stock_counter = 0
    future_counter = 0

    future_login = ap.CAPLoginField()

    # 关于授权的说明：http://algo.plus/algoplus/0106001.html
    # 加QQ号2565657639(注明AlgoPlus授权)，或者公众号AlgoPlus后台留言，申请模拟交易授权。
    future_login.License = ""
    future_login.UserType = ap.ENUM_UserType_NSIGHTFuture
    future_login.UserID = ""
    future_login.InvestorID = ""
    future_login.Password = ""
    future_login.TraderFront = "tcp://210.14.72.12:4600"
    future_login.MdFront = "tcp://210.14.72.12:4602"
    future_login.ConnectTimeout = 0
    future_login.TaskExecuteGap = ap.MICROSECONDS_IN_SECOND * 2
    future_login.BasePath = "./"
    future_login.BrokerID = "10010"

    future_list = ["bu2106", "au2106", "fu2109", "ni2106"]
    future_trader = ap.init(0, future_login, future_on_marketdata_event, future_on_order_event, future_on_event, future_on_loop)

    if future_trader is not None:
        ap.subscribe(future_trader, future_list)
        ap.loop()
    else:
        init_error_id = ap.getInitError()
        print(f"future init errors:{init_error_id}")
        sys.exit(1)
