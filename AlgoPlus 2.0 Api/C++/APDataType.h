#ifndef AP_DATETYPE_H__
#define AP_DATETYPE_H__


/////////////////////////////////////////////////////////////////////////
/// 常量
/////////////////////////////////////////////////////////////////////////
/// 零
const int ZERO_INT = 0;
/// int无效值
const int MAX_INT = 999999999;
/// double无效值
const double MAX_DOUBLE = 999999999999.99;
/// 空字符串
const char NULL_CSTRING[2] = "";

/////////////////////////////////////////////////////////////////////////
/// TAPTimeAnchorType是一个时间间隔类型
/////////////////////////////////////////////////////////////////////////
#ifdef _WIN32
typedef __int64 TAPTimeAnchorType;
#else
typedef long long int TAPTimeAnchorType;
#endif
/// 秒与微秒的换算单位
const TAPTimeAnchorType MICROSECONDS_IN_SECOND = 1000000;

/////////////////////////////////////////////////////////////////////////
/// TAPApiStatusType是一个接口状态类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPApiStatusType;
/// 退出
const TAPApiStatusType ENUM_ApiStatus_Exit = '0';
/// 未初始化
const TAPApiStatusType ENUM_ApiStatus_Null = '1';
/// 断开链接
const TAPApiStatusType ENUM_ApiStatus_Disconnected = '2';
/// 正在初始化
const TAPApiStatusType ENUM_ApiStatus_Initializing = '3';
/// 正常工作
const TAPApiStatusType ENUM_ApiStatus_Working = '4';

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPOrderStatusType是一个订单状态类型
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPOrderStatusType;
/// 未发出
const TAPOrderStatusType ENUM_OrderStatus_Null = '0';
/// 本地发出报单指令
const TAPOrderStatusType ENUM_OrderStatus_Ordering = '1';
/// 本地发出撤单指令
const TAPOrderStatusType ENUM_OrderStatus_Canceling = '2';
/// 可撤销（未成交、部分成交）
const TAPOrderStatusType ENUM_OrderStatus_Revocable = '3';
/// 不可撤销（部成部撤、全部撤销）
const TAPOrderStatusType ENUM_OrderStatus_Irrevocable = '4';
/// 错误（柜台拒绝、交易所拒绝）
const TAPOrderStatusType ENUM_OrderStatus_Error = '5';

/////////////////////////////////////////////////////////////////////////
/// TAPOrderEventIDType是一个订单事件ID类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPOrderEventIDType;
/// 部分成交，只更新成交量数据
const TAPOrderEventIDType ENUM_OrderEventID_PartTraded = 10001;
/// 更新成交量数据，且更新成本数据
const TAPOrderEventIDType ENUM_OrderEventID_TradedAndUpdateCost = 10002;
/// 全部成交，只更新成交量数据
const TAPOrderEventIDType ENUM_OrderEventID_AllTraded = 10003;
/// 剩余撤单，且更新成交量数据
const TAPOrderEventIDType ENUM_OrderEventID_TradedAndCanceled = 10004;
/// 剩余撤单
const TAPOrderEventIDType ENUM_OrderEventID_Canceled = 10005;
/// 报单失败
const TAPOrderEventIDType ENUM_OrderEventID_Error = 10006;
/// 更新成本数据
const TAPOrderEventIDType ENUM_OrderEventID_UpdateCost = 10007;
/// 排队
const TAPOrderEventIDType ENUM_OrderEventID_Waiting = 10008;
/// 预埋
const TAPOrderEventIDType ENUM_OrderEventID_Cached = 10009;
/// 撤单失败
const TAPOrderEventIDType ENUM_OrderEventID_FailToCancel = 10010;
/// 撤单失败
const TAPOrderEventIDType ENUM_OrderEventID_IPO = 10011;

/////////////////////////////////////////////////////////////////////////
/// TAPEventIDType是一个事件ID类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPEventIDType;
/// 建立TraderApi连接失败
const TAPEventIDType ENUM_EventID_FailToCreateTrader = 10001;
/// 初始化失败
const TAPEventIDType ENUM_EventID_FailToInitialize = 10002;
/// TraderApi连接断开
const TAPEventIDType ENUM_EventID_TraderDisconnected = 10003;
/// 建立MdApi连接失败
const TAPEventIDType ENUM_EventID_FailToCreateMd = 10004;
/// MdApi连接断开
const TAPEventIDType ENUM_EventID_MdDisconnected = 10005;
/// 订阅行情失败
const TAPEventIDType ENUM_EventID_FailToSubscribeMarketData = 10006;
/// 退订行情失败
const TAPEventIDType ENUM_EventID_FailToUnsubscribeMarketData = 10007;
/// 切换交易日
const TAPEventIDType ENUM_EventID_DayRolling = 10008;
/// 初始化完成
const TAPEventIDType ENUM_EventID_Ready = 10009;
/// 查询订单
const TAPEventIDType ENUM_EventID_QryOrder = 10010;
/// 查询成交
const TAPEventIDType ENUM_EventID_QryTrade = 10011;
/// 查询持仓
const TAPEventIDType ENUM_EventID_QryPosition = 10012;
/// 查询资金
const TAPEventIDType ENUM_EventID_QryBalance = 10013;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPOrderTypeType是一个报单类型类型
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPOrderTypeType;
/// <summary>
/// 通用
/// </summary>
/// 限价，等待成交
const TAPOrderTypeType ENUM_OrderType_LimitAndWait = '0';
/// 最优对方限价，等待成交
const TAPOrderTypeType ENUM_OrderType_BestLimitAndWait = '1';
/// 最优本方限价，等待成交
const TAPOrderTypeType ENUM_OrderType_HomeBestLimitAndWait = '2';
/// 极限价格限价，等待成交
const TAPOrderTypeType ENUM_OrderType_FrontierLimitAndWait = '3';
/// 最新成交限价，等待成交
const TAPOrderTypeType ENUM_OrderType_LastLimitAndWait = '4';
/// 最优五档限价，等待成交
const TAPOrderTypeType ENUM_OrderType_FiveBestLimitAndWait = '5';
/// <summary>
/// 股票订单
/// </summary>
/// 限价，等待成交
const TAPOrderTypeType ENUM_OrderType_SSE_LimitAndWait = 'a';
/// 最优五档，等待成交
const TAPOrderTypeType ENUM_OrderType_SSE_FiveAndWait = 'b';
/// 最优五档，剩余立即撤销
const TAPOrderTypeType ENUM_OrderType_SSE_FiveAndKill = 'c';
/// 最优对方，等待成交
const TAPOrderTypeType ENUM_OrderType_SSEKC_BestAndWait = 'd';
/// 最优本方，等待成交
const TAPOrderTypeType ENUM_OrderType_SSEKC_HomeBestAndWait = 'e';
const TAPOrderTypeType ENUM_OrderType_SSEKC_Fix = 'f';
const TAPOrderTypeType ENUM_OrderType_SSEOPTION_LimitOrKill = 'g';
const TAPOrderTypeType ENUM_OrderType_SSEOPTION_AnyAndWait = 'h';
const TAPOrderTypeType ENUM_OrderType_SSEOPTION_AnyAndKill = 'i';
const TAPOrderTypeType ENUM_OrderType_SSEOPTION_AnyOrKill = 'j';
/// 限价，等待成交
const TAPOrderTypeType ENUM_OrderType_SZSE_LimitAndWait = 'k';
/// 最优对方，等待成交
const TAPOrderTypeType ENUM_OrderType_SZSE_BestAndWait = 'l';
/// 最优本方，等待成交
const TAPOrderTypeType ENUM_OrderType_SZSE_HomeBestAndWait = 'm';
/// 市价，剩余撤销
const TAPOrderTypeType ENUM_OrderType_SZSE_AnyAndKill = 'n';
/// 市价，全部成交否则全部撤销
const TAPOrderTypeType ENUM_OrderType_SZSE_AnyOrKill = 'o';
/// 最优五档，剩余撤销
const TAPOrderTypeType ENUM_OrderType_SZSE_FiveAndKill = 'p';
const TAPOrderTypeType ENUM_OrderType_SZSESGT_AuctionLimit = 'q';
const TAPOrderTypeType ENUM_OrderType_SZSEOPTION_LimitOrKill = 'r';
/// <summary>
/// 期货订单
/// </summary>
/// 限价，不撤销
const TAPOrderTypeType ENUM_OrderType_CZCE_LimitAndWait = 'A';
/// 限价，剩余撤销
const TAPOrderTypeType ENUM_OrderType_CZCE_LimitAndKill = 'B';
/// 市价，等待成交
const TAPOrderTypeType ENUM_OrderType_CZCE_AnyAndWait = 'C';
/// 市价，剩余撤销
const TAPOrderTypeType ENUM_OrderType_CZCE_AnyAndKill = 'D';
/// 限价，全部成交否则全部撤销
const TAPOrderTypeType ENUM_OrderType_CZCEOPTION_LimitOrKill = 'E';
/// 市价，全部成交否则全部撤销
const TAPOrderTypeType ENUM_OrderType_CZCEOPTION_AnyOrKill = 'F';
/// 限价，等待成交
const TAPOrderTypeType ENUM_OrderType_DCE_LimitAndWait = 'G';
/// 限价，剩余撤销
const TAPOrderTypeType ENUM_OrderType_DCE_LimitAndKill = 'H';
/// 限价，全部成交否则全部撤销
const TAPOrderTypeType ENUM_OrderType_DCE_LimitOrKill = 'I';
/// 市价，等待成交
const TAPOrderTypeType ENUM_OrderType_DCE_AnyAndWait = 'J';
/// 市价，剩余撤销
const TAPOrderTypeType ENUM_OrderType_DCE_AnyAndKill = 'K';
/// 市价，全部成交否则全部撤销
const TAPOrderTypeType ENUM_OrderType_DCE_AnyOrKill = 'L';
const TAPOrderTypeType ENUM_OrderType_DCE_AnyTouchAndWait = 'M';
const TAPOrderTypeType ENUM_OrderType_DCE_AnyTouchProfitAndWait = 'N';
/// 限价，等待成交
const TAPOrderTypeType ENUM_OrderType_SHFE_LimitAndWait = 'O';
/// 限价，剩余撤销
const TAPOrderTypeType ENUM_OrderType_SHFE_LimitAndKill = 'P';
const TAPOrderTypeType ENUM_OrderType_SHFE_LimitAndKillAndLimit = 'Q';
/// 限价，全部成交否则全部撤销
const TAPOrderTypeType ENUM_OrderType_SHFE_LimitOrKill = 'R';
/// 限价，等待成交
const TAPOrderTypeType ENUM_OrderType_CFFEX_LimitAndWait = 'S';
/// 限价，剩余撤销
const TAPOrderTypeType ENUM_OrderType_CFFEX_LimitAndKill = 'T';
const TAPOrderTypeType ENUM_OrderType_CFFEX_LimitAndKillAndLimit = 'U';
/// 限价，全部成交否则全部撤销
const TAPOrderTypeType ENUM_OrderType_CFFEX_LimitOrKill = 'V';
/// 最优五档，剩余撤销
const TAPOrderTypeType ENUM_OrderType_CFFEX_FiveAndKill = 'W';
/// 最优五档，等待成交
const TAPOrderTypeType ENUM_OrderType_CFFEX_FiveAndWait = 'X';
/// 最优对方，剩余撤销
const TAPOrderTypeType ENUM_OrderType_CFFEX_BestAndKill = 'Y';
/// 最优对方，等待成交
const TAPOrderTypeType ENUM_OrderType_CFFEX_BestAndWait = 'Z';

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPCloseTypeType是一个平仓类型类型
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPCloseTypeType;
/// 禁止平今
const TAPCloseTypeType ENUM_CloseType_HistoryOnly = '0';
/// 先开先平
const TAPCloseTypeType ENUM_CloseType_FIFO = '1';
/// 平今或者平昨
const TAPCloseTypeType ENUM_CloseType_Either = '2';

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPPositionDirectionType是一个持仓多空类型
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPPositionDirectionType;
/// 多头
const TAPPositionDirectionType ENUM_PositionDirection_Long = '0';
/// 空头
const TAPPositionDirectionType ENUM_PositionDirection_Short = '1';

/////////////////////////////////////////////////////////////////////////
/// TAPOrderDirectionType是一个Direction类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPOrderDirectionType[3];
/// 买入
const TAPOrderDirectionType ENUM_OrderDirection_Buy = "00";
/// 卖出
const TAPOrderDirectionType ENUM_OrderDirection_Sell = "11";
/// ETF申购
const TAPOrderDirectionType ENUM_OrderDirection_ETFPur = "2";
/// ETF赎回
const TAPOrderDirectionType ENUM_OrderDirection_ETFRed = "3";
/// 新股申购
const TAPOrderDirectionType ENUM_OrderDirection_IPO = "4";
/// 正回购
const TAPOrderDirectionType ENUM_OrderDirection_Repurchase = "5";
/// 逆回购
const TAPOrderDirectionType ENUM_OrderDirection_ReverseRepur = "60";
/// 开放式基金申购
const TAPOrderDirectionType ENUM_OrderDirection_OeFundPur = "8";
/// 开放式基金赎回
const TAPOrderDirectionType ENUM_OrderDirection_OeFundRed = "9";
/// 担保品划入
const TAPOrderDirectionType ENUM_OrderDirection_CollateralIn = "a";
/// 担保品划出
const TAPOrderDirectionType ENUM_OrderDirection_CollateralOut = "b";
/// 质押入库
const TAPOrderDirectionType ENUM_OrderDirection_PledgeIn = "d";
/// 质押出库
const TAPOrderDirectionType ENUM_OrderDirection_PledgeOut = "e";
/// 配股配债
const TAPOrderDirectionType ENUM_OrderDirection_Rationed = "f";
/// 基金拆分
const TAPOrderDirectionType ENUM_OrderDirection_Split = "g";
/// 基金合并
const TAPOrderDirectionType ENUM_OrderDirection_Merge = "h";
/// 融资买入
const TAPOrderDirectionType ENUM_OrderDirection_CreditBuy = "i0";
/// 融券卖出
const TAPOrderDirectionType ENUM_OrderDirection_CreditSell = "j0";
/// 卖券还款
const TAPOrderDirectionType ENUM_OrderDirection_SellRepay = "k1";
/// 买券还券
const TAPOrderDirectionType ENUM_OrderDirection_BuyRepay = "l1";
/// 还券划转
const TAPOrderDirectionType ENUM_OrderDirection_RepayTransfer = "m";
/// 余券划转
const TAPOrderDirectionType ENUM_OrderDirection_SurplusTransfer = "n";
/// 源券划转
const TAPOrderDirectionType ENUM_OrderDirection_SourceTransfer = "o";
/// 债券转股
const TAPOrderDirectionType ENUM_OrderDirection_BondConvertStock = "t";
/// 债券回售
const TAPOrderDirectionType ENUM_OrderDirection_BondPutback = "u";
/// ETF实物申购
const TAPOrderDirectionType ENUM_OrderDirection_ETFOtPur = "v";
/// ETF实物赎回
const TAPOrderDirectionType ENUM_OrderDirection_ETFOtRed = "w";
/// 回售撤销
const TAPOrderDirectionType ENUM_OrderDirection_PutbackRelieve = "x";
/// 意向买入
const TAPOrderDirectionType ENUM_OrderDirection_IOIBuy = "A";
/// 意向卖出
const TAPOrderDirectionType ENUM_OrderDirection_IOISell = "B";
/// 成交确认买入
const TAPOrderDirectionType ENUM_OrderDirection_TCRBuy = "C";
/// 成交确认卖出
const TAPOrderDirectionType ENUM_OrderDirection_TCRSell = "D";
/// 买开仓
const TAPOrderDirectionType ENUM_OrderDirection_BuyOpen = "00";
/// 卖平
const TAPOrderDirectionType ENUM_OrderDirection_SellClose = "11";
/// 卖平今
const TAPOrderDirectionType ENUM_OrderDirection_SellCloseToday = "13";
/// 买平昨
const TAPOrderDirectionType ENUM_OrderDirection_SellCloseHistory = "14";
/// 卖开仓
const TAPOrderDirectionType ENUM_OrderDirection_SellOpen = "10";
/// 买平仓
const TAPOrderDirectionType ENUM_OrderDirection_BuyClose = "01";
/// 买平今
const TAPOrderDirectionType ENUM_OrderDirection_BuyCloseToday = "03";
/// 买平昨
const TAPOrderDirectionType ENUM_OrderDirection_BuyCloseHistory = "04";
/// 备兑开仓
const TAPOrderDirectionType ENUM_OrderDirection_CoveredOpen = "E";
/// 备兑平仓
const TAPOrderDirectionType ENUM_OrderDirection_CoveredClose = "F";
/// 行权
const TAPOrderDirectionType ENUM_OrderDirection_ExecOrder = "G";

/////////////////////////////////////////////////////////////////////////
/// TAPPriceTypeType是一个报单价格条件类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPPriceTypeType;

/////////////////////////////////////////////////////////////////////////
/// TAPTimeConditionType是一个有效期类型类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPTimeConditionType;

/////////////////////////////////////////////////////////////////////////
/// TAPVolumeConditionType是一个成交量类型类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPVolumeConditionType;

/////////////////////////////////////////////////////////////////////////
/// TAPContingentConditionType是一个触发条件类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPContingentConditionType;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPExchangeIDType是一个交易所类型
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPExchangeIDType[9];
/// 未知
const TAPExchangeIDType ENUM_ExchangeID_Unknown = "U";
/// 上海交易所
const TAPExchangeIDType ENUM_ExchangeID_SSE = "1";
/// 深圳交易所
const TAPExchangeIDType ENUM_ExchangeID_SZSE = "2";
/// 香港交易所
const TAPExchangeIDType ENUM_ExchangeID_HK = "3";
/// 中国金融期货交易所
const TAPExchangeIDType ENUM_ExchangeID_CFFEX = "CFFEX";
/// 上海期货交易所
const TAPExchangeIDType ENUM_ExchangeID_SHFE = "SHFE";
/// 上海国际能源交易中心股份有限公司
const TAPExchangeIDType ENUM_ExchangeID_INE = "INE";
/// 大连商品交易所
const TAPExchangeIDType ENUM_ExchangeID_DCE = "DCE";
/// 郑州商品交易所
const TAPExchangeIDType ENUM_ExchangeID_CZCE = "CZCE";

/////////////////////////////////////////////////////////////////////////
/// TAPStandardStatusType是一个行情证券状态类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPStandardStatusType;
/// 开盘前
const TAPStandardStatusType ENUM_StandardStatus_PreOpen = '0';
/// 集合竞价
const TAPStandardStatusType ENUM_StandardStatus_CallAuction = '1';
/// 连续交易
const TAPStandardStatusType ENUM_StandardStatus_Continous = '2';
/// 休市
const TAPStandardStatusType ENUM_StandardStatus_Pause = '3';
/// 停牌
const TAPStandardStatusType ENUM_StandardStatus_Suspend = '4';
/// 长期停牌
const TAPStandardStatusType ENUM_StandardStatus_LongSuspend = '5';
/// 波动性中断
const TAPStandardStatusType ENUM_StandardStatus_UndulationInt = '6';
/// 熔断可恢复
const TAPStandardStatusType ENUM_StandardStatus_CircuitBreak = '7';
/// 熔断不可恢复
const TAPStandardStatusType ENUM_StandardStatus_CircuitBreakU = '8';
/// 闭市
const TAPStandardStatusType ENUM_StandardStatus_Close = '9';
/// 其它
const TAPStandardStatusType ENUM_StandardStatus_Other = 'a';
/// 收盘集合竞价
const TAPStandardStatusType ENUM_StandardStatus_CloseCallAuction = 'b';
/// 集中撮合(盘后定价)
const TAPStandardStatusType ENUM_StandardStatus_CallMatch = 'c';
/// 连续交易(盘后定价)
const TAPStandardStatusType ENUM_StandardStatus_PostContinous = 'd';
/// 闭市(盘后定价)
const TAPStandardStatusType ENUM_StandardStatus_PostClose = 'e';
/// 开盘前(盘后定价)
const TAPStandardStatusType ENUM_StandardStatus_PrePostOpen = 'f';

/////////////////////////////////////////////////////////////////////////
/// TAPBoolType是一个布尔型类型
/////////////////////////////////////////////////////////////////////////
typedef bool TAPBoolType;

/////////////////////////////////////////////////////////////////////////
/// TAPCountType是一个计数类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPCountType;

/////////////////////////////////////////////////////////////////////////
/// TAPDateType是一个日期类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPDateType[9];

/////////////////////////////////////////////////////////////////////////
/// TAPTimeType是一个时间类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPTimeType[9];

/////////////////////////////////////////////////////////////////////////
/// TAPDateTimeType是一个日期时间类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPDateTimeType[18];

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPLicenseType是一个许可证类型
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPLicenseType[256];

/////////////////////////////////////////////////////////////////////////
/// TAPUserTypeType是一个客户类型类型
/////////////////////////////////////////////////////////////////////////
typedef unsigned int TAPUserTypeType;
/// CTP用户实盘
const TAPUserTypeType ENUM_UserType_CTP = 10001;
/// 奇点普通股票用户实盘
const TAPUserTypeType ENUM_UserType_TORAStock = 10002;
/// 奇点信用股票用户实盘
const TAPUserTypeType ENUM_UserType_TORACredit = 10003;
/// 奇点股票期权用户实盘
const TAPUserTypeType ENUM_UserType_TORAOption = 10004;

/// N视界模拟环境期货用户
const TAPUserTypeType ENUM_UserType_NSIGHTFuture = 20001;
/// N视界模拟环境普通股票用户
const TAPUserTypeType ENUM_UserType_NSIGHTStock = 20002;
/// N视界模拟环境信用股票用户
const TAPUserTypeType ENUM_UserType_NSIGHTCredit = 20003;
/// N视界模拟环境股票期权用户
const TAPUserTypeType ENUM_UserType_NSIGHTOption = 20004;
/// SimNow模拟环境用户
const TAPUserTypeType ENUM_UserType_SIMNOWFuture = 20005;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPUserIDType是一个客户号类型
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPUserIDType[16];

/////////////////////////////////////////////////////////////////////////
/// TAPPasswordType是一个密码类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPPasswordType[41];

/////////////////////////////////////////////////////////////////////////
/// TAPInvestorIDType是一个投资者代码类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPInvestorIDType[16];

/////////////////////////////////////////////////////////////////////////
/// TAPShareholderIDType是一个股东账户代码类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPShareholderIDType[11];

/////////////////////////////////////////////////////////////////////////
/// TAPFrontAddressType是一个前置地址类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPFrontAddressType[32];

/////////////////////////////////////////////////////////////////////////
/// TAPFilePathType是一个文件路径类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPFilePathType[128];

/////////////////////////////////////////////////////////////////////////
/// TAPBrokerIDType是一个经纪公司代码类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPBrokerIDType[11];

/////////////////////////////////////////////////////////////////////////
/// TAPAppIDType是一个AppID类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPAppIDType[33];

/////////////////////////////////////////////////////////////////////////
/// TAPAuthCodeType是一个客户端认证码类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPAuthCodeType[17];

/////////////////////////////////////////////////////////////////////////
/// TAPHDSerialType是一个硬盘序列号类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPHDSerialType[33];

/////////////////////////////////////////////////////////////////////////
/// TAPMacAddressType是一个Mac地址类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPMacAddressType[21];

/////////////////////////////////////////////////////////////////////////
/// TAPIPAddressType是一个IP地址类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPIPAddressType[16];

/////////////////////////////////////////////////////////////////////////
/// TAPPortType是一个端口号类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPPortType;

/////////////////////////////////////////////////////////////////////////
/// TAPTerminalInfoType是一个终端信息类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPTerminalInfoType[256];

/////////////////////////////////////////////////////////////////////////
/// TAPFrontIDType是一个前置编号类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPFrontIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPSessionIDType是一个会话编号类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPSessionIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPStandardIDType是一个标准标的代码类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPStandardIDType[31];

/////////////////////////////////////////////////////////////////////////
/// TAPStandardNameType是一个标准标的名称类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPStandardNameType[81];

/////////////////////////////////////////////////////////////////////////
/// TAPOrderMarkType是一个报单标记类型
/////////////////////////////////////////////////////////////////////////
typedef short TAPOrderMarkType;

/////////////////////////////////////////////////////////////////////////
/// TAPOrderIDType是一个报单ID类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPOrderIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPOrderSysIDType是一个报单编号类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPOrderSysIDType[21];

/////////////////////////////////////////////////////////////////////////
/// TAPVolumeType是一个数量类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPVolumeType;

/////////////////////////////////////////////////////////////////////////
/// TAPLongVolumeType是一个LongVolume类型
/////////////////////////////////////////////////////////////////////////
#ifdef _WIN32
typedef __int64 TAPLongVolumeType;
#else
typedef long long int TAPLongVolumeType;
#endif

/////////////////////////////////////////////////////////////////////////
/// TAPLargeVolumeType是一个LargeVolume类型
/////////////////////////////////////////////////////////////////////////
typedef double TAPLargeVolumeType;

/////////////////////////////////////////////////////////////////////////
/// TAPMoneyType是一个资金类型
/////////////////////////////////////////////////////////////////////////
typedef double TAPMoneyType;

/////////////////////////////////////////////////////////////////////////
/// TAPPriceType是一个价格类型
/////////////////////////////////////////////////////////////////////////
typedef double TAPPriceType;

/////////////////////////////////////////////////////////////////////////
/// TAPErrorIDType是一个错误代码类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPErrorIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPMessageType是一个信息类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPMessageType[256];

/////////////////////////////////////////////////////////////////////////
/// TAPMarketIDType是一个市场代码类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPMarketIDType;
/// 上海A股
const TAPMarketIDType ENUM_MarketID_SHA = '1';
/// 深圳A股
const TAPMarketIDType ENUM_MarketID_SZA = '2';
/// 上海B股
const TAPMarketIDType ENUM_MarketID_SHB = '3';
/// 深圳B股
const TAPMarketIDType ENUM_MarketID_SZB = '4';
/// 深圳三版A股
const TAPMarketIDType ENUM_MarketID_SZThreeA = '5';
/// 深圳三版B股
const TAPMarketIDType ENUM_MarketID_SZThreeB = '6';
/// 境外市场
const TAPMarketIDType ENUM_MarketID_Foreign = '7';
/// 深圳港股通市场
const TAPMarketIDType ENUM_MarketID_SZHK = '8';
/// 上海港股通市场
const TAPMarketIDType ENUM_MarketID_SHHK = '9';

/////////////////////////////////////////////////////////////////////////
/// TAPProductIDType是一个证券品种代码类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPProductIDType;
/// 通用(内部使用)
const TAPProductIDType ENUM_ProductID_COMMON = '0';
/// 上海股票
const TAPProductIDType ENUM_ProductID_SHStock = '1';
/// 上海基金
const TAPProductIDType ENUM_ProductID_SHFund = '3';
/// 上海债券
const TAPProductIDType ENUM_ProductID_SHBond = '4';
/// 上海标准券
const TAPProductIDType ENUM_ProductID_SHStandard = '5';
/// 上海质押式回购
const TAPProductIDType ENUM_ProductID_SHRepurchase = '6';
/// 深圳股票
const TAPProductIDType ENUM_ProductID_SZStock = '7';
/// 深圳基金
const TAPProductIDType ENUM_ProductID_SZFund = '9';
/// 深圳债券
const TAPProductIDType ENUM_ProductID_SZBond = 'a';
/// 深圳标准券
const TAPProductIDType ENUM_ProductID_SZStandard = 'b';
/// 深圳质押式回购
const TAPProductIDType ENUM_ProductID_SZRepurchase = 'c';
/// 深港通港股主板
const TAPProductIDType ENUM_ProductID_SZSEHKMain = 'd';
/// 深港通港股创业板
const TAPProductIDType ENUM_ProductID_SZSEHKGEM = 'e';
/// 深港通港股扩充交易证券
const TAPProductIDType ENUM_ProductID_SZSEHKETS = 'f';
/// 深港通港股NasdaqAMX市场
const TAPProductIDType ENUM_ProductID_SZSEHKNasdaqAMX = 'g';
/// 上海科创板
const TAPProductIDType ENUM_ProductID_SHKC = 'i';
/// 上海个股期权
const TAPProductIDType ENUM_ProductID_SHStockOption = 'u';
/// 深圳个股期权
const TAPProductIDType ENUM_ProductID_SZStockOption = 'v';
/// 期货
const TAPProductIDType ENUM_ProductID_Futures = 'B';
/// 期货期权
const TAPProductIDType ENUM_ProductID_Options = 'C';
/// 组合
const TAPProductIDType ENUM_ProductID_Combination = 'D';
/// 即期
const TAPProductIDType ENUM_ProductID_Spot = 'E';
/// 期转现
const TAPProductIDType ENUM_ProductID_EFP = 'F';
/// 现货期权
const TAPProductIDType ENUM_ProductID_SpotOption = 'G';
/// TAS合约
const TAPProductIDType ENUM_ProductID_TAS = 'H';
/// 金属指数
const TAPProductIDType ENUM_ProductID_MI = 'Z';

/////////////////////////////////////////////////////////////////////////
/// TAPStandardTypeType是一个标的类别类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPStandardTypeType;
/// 通用(内部使用)
const TAPStandardTypeType ENUM_StandardType_COMMON = '0';
/// 上海A股
const TAPStandardTypeType ENUM_StandardType_SHAShares = 'a';
/// 上海单市场股票ETF
const TAPStandardTypeType ENUM_StandardType_SHSingleMarketStockETF = 'b';
/// 上海单市场实物债券ETF
const TAPStandardTypeType ENUM_StandardType_SHSingleMarketBondETF = 'c';
/// 上海黄金ETF
const TAPStandardTypeType ENUM_StandardType_SHGoldETF = 'd';
/// 上海货币ETF
const TAPStandardTypeType ENUM_StandardType_SHTradableMonetaryFund = 'e';
/// 上海国债地方债
const TAPStandardTypeType ENUM_StandardType_SHBondNation = 'f';
/// 上海企业债
const TAPStandardTypeType ENUM_StandardType_SHBondCorporation = 'g';
/// 上海公司债
const TAPStandardTypeType ENUM_StandardType_SHBondCompany = 'h';
/// 上海可转债
const TAPStandardTypeType ENUM_StandardType_SHBondConversion = 'i';
/// 上海分离债
const TAPStandardTypeType ENUM_StandardType_SHBondSeparation = 'j';
/// 上海标准券
const TAPStandardTypeType ENUM_StandardType_SHStandard = 'o';
/// 上海质押式回购
const TAPStandardTypeType ENUM_StandardType_SHRepo = 'p';
/// 上海封闭式基金
const TAPStandardTypeType ENUM_StandardType_SHCEFund = 'q';
/// 上海开放式基金
const TAPStandardTypeType ENUM_StandardType_SHOEFund = 'r';
/// 上海跨市场ETF
const TAPStandardTypeType ENUM_StandardType_SHCrossMarketStockETF = 's';
/// 上海跨境ETF
const TAPStandardTypeType ENUM_StandardType_SHCrossBorderETF = 't';
/// 上海分级母基金
const TAPStandardTypeType ENUM_StandardType_SHMontherStructFund = 'u';
/// 上海分级子基金
const TAPStandardTypeType ENUM_StandardType_SHSubStructFund = 'v';
/// 上海实时申赎货币基金
const TAPStandardTypeType ENUM_StandardType_SHRealTimeMonetaryFund = 'w';
/// 上海可交换债
const TAPStandardTypeType ENUM_StandardType_SHExchangeableBond = 'x';
/// 上海标准LOF基金
const TAPStandardTypeType ENUM_StandardType_SHLOF = 'A';
/// 深圳主板A股
const TAPStandardTypeType ENUM_StandardType_SZMainAShares = 'B';
/// 深圳中小企业板
const TAPStandardTypeType ENUM_StandardType_SZSME = 'C';
/// 深圳国债、地方债
const TAPStandardTypeType ENUM_StandardType_SZBondNation = 'D';
/// 深圳企业债
const TAPStandardTypeType ENUM_StandardType_SZBondCorporation = 'E';
/// 深圳公司债
const TAPStandardTypeType ENUM_StandardType_SZBondCompany = 'F';
/// 深圳可转债
const TAPStandardTypeType ENUM_StandardType_SZBondConversion = 'G';
/// 深圳分离债
const TAPStandardTypeType ENUM_StandardType_SZBondSeparation = 'H';
/// 深圳创业板(注册制)
const TAPStandardTypeType ENUM_StandardType_SZGEMReg = 'I';
/// 深圳创业板可转债(注册制)
const TAPStandardTypeType ENUM_StandardType_SZGEMBondConversionReg = 'J';
/// 深圳跨境ETF
const TAPStandardTypeType ENUM_StandardType_SZCrossBorderETF = 'K';
/// 深圳黄金ETF
const TAPStandardTypeType ENUM_StandardType_SZGoldETF = 'L';
/// 深圳现金债券ETF
const TAPStandardTypeType ENUM_StandardType_SZCashBondETF = 'M';
/// 深圳单市场股票ETF
const TAPStandardTypeType ENUM_StandardType_SZSingleMarketStockETF = 'N';
/// 深圳单市场实物债券ETF
const TAPStandardTypeType ENUM_StandardType_SZSingleMarketBondETF = 'O';
/// 深圳货币ETF
const TAPStandardTypeType ENUM_StandardType_SZMonetaryFundETF = 'P';
/// 深圳创业板
const TAPStandardTypeType ENUM_StandardType_SZGEM = 'Q';
/// 深圳创业板可交换债
const TAPStandardTypeType ENUM_StandardType_SZGEMExchangeableBond = 'R';
/// 深圳创业板可交换债(注册制)
const TAPStandardTypeType ENUM_StandardType_SZGEMExchangeableBondReg = 'S';
/// 深圳标准券
const TAPStandardTypeType ENUM_StandardType_SZStandard = 'T';
/// 深圳质押式回购
const TAPStandardTypeType ENUM_StandardType_SZRepo = 'U';
/// 深圳封闭式基金
const TAPStandardTypeType ENUM_StandardType_SZCEFund = 'V';
/// 深圳开放式基金
const TAPStandardTypeType ENUM_StandardType_SZOEFund = 'W';
/// 深圳跨境开放式基金
const TAPStandardTypeType ENUM_StandardType_SZCrossBorderOEFund = 'X';
/// 深圳跨市场股票ETF
const TAPStandardTypeType ENUM_StandardType_SZCrossMarketStockETF = 'Y';
/// 深圳标准LOF基金
const TAPStandardTypeType ENUM_StandardType_SZLOF = 'Z';
/// 深圳跨境LOF基金
const TAPStandardTypeType ENUM_StandardType_SZCrossBorderLOF = '1';
/// 深圳传统分级母基金
const TAPStandardTypeType ENUM_StandardType_SZMontherStructFund = '2';
/// 深圳传统分级子基金
const TAPStandardTypeType ENUM_StandardType_SZSubStructFund = '3';
/// 深圳跨境分级母基金
const TAPStandardTypeType ENUM_StandardType_SZMontherCrossBorderStructFund = '4';
/// 深圳跨境分级子基金
const TAPStandardTypeType ENUM_StandardType_SZSubCrossBorderStructFund = '5';
/// 深圳可交换债
const TAPStandardTypeType ENUM_StandardType_SZExchangeableBond = '6';
/// 深圳创业板可转债
const TAPStandardTypeType ENUM_StandardType_SZGEMBondConversion = '7';
/// 深港通港股债券
const TAPStandardTypeType ENUM_StandardType_SZSEHKBond = '8';
/// 深港通港股一篮子权证
const TAPStandardTypeType ENUM_StandardType_SZSEHKBasketWarrant = '9';
/// 深港通港股股本
const TAPStandardTypeType ENUM_StandardType_SZSEHKEquity = 'y';
/// 深港通港股信托
const TAPStandardTypeType ENUM_StandardType_SZSEHKTrust = 'z';
/// 深港通港股权证
const TAPStandardTypeType ENUM_StandardType_SZSEHKWarrant = '#';
/// 上海存托凭证
const TAPStandardTypeType ENUM_StandardType_SHCDR = '+';
/// 上海科创板股票
const TAPStandardTypeType ENUM_StandardType_SHKC = '*';
/// 科创板产品（上市后前5个交易日）
const TAPStandardTypeType ENUM_StandardType_SHKC1 = '^';
/// 上海科创板存托凭证
const TAPStandardTypeType ENUM_StandardType_SHKCCDR = '-';
/// 深圳主板、中小板创新企业股票或存托凭证
const TAPStandardTypeType ENUM_StandardType_SZCDR = 'k';
/// 深圳创业板创新企业股票或存托凭证
const TAPStandardTypeType ENUM_StandardType_SZGEMCDR = 'l';
/// 深圳创业板创新企业股票或存托凭证(注册制)
const TAPStandardTypeType ENUM_StandardType_SZGEMCDRReg = 'm';
/// 深圳商品期货ETF
const TAPStandardTypeType ENUM_StandardType_SZCommFuturesETF = 'n';
/// 深圳基础设施基金
const TAPStandardTypeType ENUM_StandardType_SZInfrastructureFund = '=';
/// 上海科创板ETF
const TAPStandardTypeType ENUM_StandardType_SHKCETF = '@';
/// 上海科创板LOF
const TAPStandardTypeType ENUM_StandardType_SHKCLOF = '%';
/// 上海科创板可转债
const TAPStandardTypeType ENUM_StandardType_SHKCBondConversion = '$';
/// 上海定向可转债
const TAPStandardTypeType ENUM_StandardType_SHOrientedConversionBond = '<';
/// 深圳定向可转债
const TAPStandardTypeType ENUM_StandardType_SZOrientedConversionBond = '>';
/// 上海股票型看涨期权
const TAPStandardTypeType ENUM_StandardType_SHCallAStockOption = char(1);
/// 上海股票型看跌期权
const TAPStandardTypeType ENUM_StandardType_SHPullAStockOption = char(2);
/// 上海基金型看涨期权
const TAPStandardTypeType ENUM_StandardType_SHCallFundStockOption = char(3);
/// 上海基金型看跌期权
const TAPStandardTypeType ENUM_StandardType_SHPullFundStockOption = char(4);
/// 深圳股票型看涨期权
const TAPStandardTypeType ENUM_StandardType_SZCallAStockOption = char(5);
/// 深圳股票型看跌期权
const TAPStandardTypeType ENUM_StandardType_SZPullAStockOption = char(6);
/// 深圳基金型看涨期权
const TAPStandardTypeType ENUM_StandardType_SZCallFundStockOption = char(7);
/// 深圳基金型看跌期权
const TAPStandardTypeType ENUM_StandardType_SZPullFundStockOption = char(8);
/// 上海组合期权
const TAPStandardTypeType ENUM_StandardType_SHCombOption = char(9);
/// 深圳组合期权
const TAPStandardTypeType ENUM_StandardType_SZCombOption = char(10);

/////////////////////////////////////////////////////////////////////////
/// TAPCombinationTypeType是一个组合类型类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPCombinationTypeType;
/// 期货组合
const TAPCombinationTypeType ENUM_CombinationType_Future = '0';
/// 垂直价差BUL
const TAPCombinationTypeType ENUM_CombinationType_BUL = '1';
/// 垂直价差BER
const TAPCombinationTypeType ENUM_CombinationType_BER = '2';
/// 跨式组合
const TAPCombinationTypeType ENUM_CombinationType_STD = '3';
/// 宽跨式组合
const TAPCombinationTypeType ENUM_CombinationType_STG = '4';
/// 备兑组合
const TAPCombinationTypeType ENUM_CombinationType_PRT = '5';
/// 时间价差组合
const TAPCombinationTypeType ENUM_CombinationType_CAS = '6';
/// 期权对锁组合
const TAPCombinationTypeType ENUM_CombinationType_OPL = '7';
/// 买备兑组合
const TAPCombinationTypeType ENUM_CombinationType_BFO = '8';
/// 买入期权垂直价差组合
const TAPCombinationTypeType ENUM_CombinationType_BLS = '9';
/// 卖出期权垂直价差组合
const TAPCombinationTypeType ENUM_CombinationType_BES = 'a';

/////////////////////////////////////////////////////////////////////////
/// TAPVolumeMultipleType是一个基础商品乘数类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPVolumeMultipleType;

/////////////////////////////////////////////////////////////////////////
/// TAPUnderlyingMultipleType是一个基础商品乘数类型
/////////////////////////////////////////////////////////////////////////
typedef double TAPUnderlyingMultipleType;

/////////////////////////////////////////////////////////////////////////
/// TAPOptionsTypeType是一个期权类型类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPOptionsTypeType;
/// 看涨
const TAPOptionsTypeType ENUM_OptionsType_CallOptions = '1';
/// 看跌
const TAPOptionsTypeType ENUM_OptionsType_PutOptions = '2';

/////////////////////////////////////////////////////////////////////////
/// TAPMaxMarginSideAlgorithmType是一个大额单边保证金算法类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPMaxMarginSideAlgorithmType;
/// 不使用大额单边保证金算法
const TAPMaxMarginSideAlgorithmType ENUM_MaxMarginSideAlgorithm_NO = '0';
/// 使用大额单边保证金算法
const TAPMaxMarginSideAlgorithmType ENUM_MaxMarginSideAlgorithm_YES = '1';

/////////////////////////////////////////////////////////////////////////
/// TAPRatioType是一个比率类型
/////////////////////////////////////////////////////////////////////////
typedef double TAPRatioType;

/////////////////////////////////////////////////////////////////////////
/// TAPPositionDateTypeType是一个持仓日期类型类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPPositionDateTypeType;
/// 使用历史持仓
const TAPPositionDateTypeType ENUM_PositionDateType_UseHistory = '1';
/// 不使用历史持仓
const TAPPositionDateTypeType ENUM_PositionDateType_NoUseHistory = '2';

/////////////////////////////////////////////////////////////////////////
/// TAPPositionTypeType是一个持仓类型类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPPositionTypeType;
/// 净持仓
const TAPPositionTypeType ENUM_PositionType_Net = '1';
/// 综合持仓
const TAPPositionTypeType ENUM_PositionType_Gross = '2';

/////////////////////////////////////////////////////////////////////////
/// TAPStrikeModeType是一个执行方式类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPStrikeModeType;
/// 欧式
const TAPStrikeModeType ENUM_StrikeMode_Continental = '0';
/// 美式
const TAPStrikeModeType ENUM_StrikeMode_American = '1';
/// 百慕大
const TAPStrikeModeType ENUM_StrikeMode_Bermuda = '2';

/////////////////////////////////////////////////////////////////////////
/// TAPInterestType是一个利息类型
/////////////////////////////////////////////////////////////////////////
typedef double TAPInterestType;

/////////////////////////////////////////////////////////////////////////
/// TAPParValueType是一个面值类型
/////////////////////////////////////////////////////////////////////////
typedef double TAPParValueType;

/////////////////////////////////////////////////////////////////////////
/// TAPMillisecType是一个时间（毫秒）类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPMillisecType;

/////////////////////////////////////////////////////////////////////////
/// TAPQuotaIDType是一个额度编号类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPQuotaIDType[17];

/////////////////////////////////////////////////////////////////////////
/// TAPCreditQuotaTypeType是一个信用头寸类型类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPCreditQuotaTypeType;
/// 普通
const TAPCreditQuotaTypeType ENUM_CreditQuotaType_Normal = '0';
/// 专项
const TAPCreditQuotaTypeType ENUM_CreditQuotaType_Special = '1';

/////////////////////////////////////////////////////////////////////////
/// TAPCreditDebtIDType是一个信用负债编号类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPCreditDebtIDType[21];

/////////////////////////////////////////////////////////////////////////
/// TAPFloatInfoType是一个浮点型附加信息类型
/////////////////////////////////////////////////////////////////////////
typedef double TAPFloatInfoType;

/////////////////////////////////////////////////////////////////////////
/// TAPIntInfoType是一个整形附加信息类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPIntInfoType;

/////////////////////////////////////////////////////////////////////////
/// TAPRequestIDType是一个请求编号类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPRequestIDType;


#endif
