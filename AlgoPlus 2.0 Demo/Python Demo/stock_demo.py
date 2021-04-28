import AlgoPlus as ap

def stock_on_event(event_id, field, islast, error_id, error_msg):
    field = ap.decode_ctp_event_field(event_id, field)
    print(f"-------")
    print(f"on_event -> EventID:{event_id},LastFlag:{islast},ErrorID:{error_id},ErrorMsg:{error_msg}")
    print(f"on_event -> Content: {field}")
    print(f"-------")

@ap.ap_marketdata_callback_wraps
def stock_on_marketdata_event(data):
    print(f"-------")
    print(f"on_marketdata -> {data}")
    print(f"-------")

@ap.ap_order_callback_wraps
def stock_on_order_event(event_id, order, position, cash):
    print(f"-------")
    print(f"on_order -> EventID:{event_id},UsableCash:{cash}")
    print(f"on_order -> {order}")
    print(f"on_order -> {position}")
    print(f"-------")

def stock_on_loop():
    global counter
    global standard_list
    global trader
    global last_order

    counter += 1
    if counter == 1:
        ap.cancelOrderAll(trader)
        print(f"-------")
        print(f"loop:{counter} -> cancelOrderAll")
        print(f"-------")
    elif counter == 100:
        print(f"-------")
        for item in standard_list:
            order = ap.buy(trader, item, 100, ap.ENUM_OrderType_FrontierLimitAndWait, 0)
            if order is not None:
                print(f"loop:{counter} -> buy UpperLimitPrice -> ErrorID:{order.ErrorID},StandardID:{item},Volume:{100},Price:{order.OriginalPrice}")
        print(f"-------")
    elif counter == 150:
        print(f"-------")
        for item in standard_list:
            order = ap.buy(trader, item, 100, ap.ENUM_OrderType_HomeBestLimitAndWait, 0)
            if order is not None:
                print(f"loop:{counter} -> buy HomeBestPrice -> ErrorID:{order.ErrorID},StandardID:{item},Volume:{100},Price:{order.OriginalPrice}")
                if order.ErrorID == 0:
                    last_order = order
        print(f"-------")
    elif counter == 200:
        if last_order is not None:
            ap.cancelOrder(trader, last_order.OrderID)
            print(f"-------")
            print(f"loop:{counter} -> cancelOrder last_order -> StandardID:{last_order.StandardID}")
            print(f"-------")
    elif counter == 250:
        ap.cancelOrderAll(trader)
        print(f"-------")
        print(f"loop:{counter} -> cancelOrderAll")
        print(f"-------")

if __name__ == '__main__':

    login = ap.CAPLoginField()

    login.License = ""
    login.UserType = ap.ENUM_UserType_NSIGHTStock
    login.UserID = ""
    login.InvestorID = ""
    login.Password = ""
    login.TraderFront = "tcp://210.14.72.15:4400"
    login.MdFront = "tcp://210.14.72.15:4402"
    login.ConnectTimeout = 0
    login.TaskExecuteGap = ap.MICROSECONDS_IN_SECOND * 2
    login.BasePath = "./"

    last_order = None
    counter = 0
    standard_list = ["600000", "000001", "300001"]
    trader = ap.init(0, login, stock_on_marketdata_event, stock_on_order_event, stock_on_event, stock_on_loop)
    if trader is not None:
        ap.subscribe(trader, standard_list)
        ap.loop()
    else:
        init_error_id = ap.getInitError()
        print(f"init_error -> InitErrorID:{init_error_id}")
