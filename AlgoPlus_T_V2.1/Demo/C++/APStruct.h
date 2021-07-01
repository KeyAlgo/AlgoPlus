#ifndef AP_STRUCT_H__
#define AP_STRUCT_H__

#include <cstring>
#include "APDataType.h"

/// 登录
struct CAPLoginField
{
	CAPLoginField() { memset(this, 0, sizeof(*this)); TaskExecuteGap = -1; LoopGap = -1; };
	CAPLoginField(CAPLoginField* pLoginField) { memcpy(this, pLoginField, sizeof(*this)); };

	///许可证
	TAPLicenseType License;
	///客户类型
	TAPUserTypeType UserType;
	///客户号
	TAPUserIDType UserID;
	///密码
	TAPPasswordType Password;
	///投资者代码，如果未设置则使用UserID
	TAPInvestorIDType InvestorID;
	///资金账户，无需设置
	TAPAccountIDType AccountID;
	///部门代码，无需设置
	TAPDepartmentIDType DepartmentID;
	///交易前置地址（tcp://127.0.0.1:22222）
	TAPFrontAddressType TraderFront;
	///行情前置地址（tcp://127.0.0.1:22222）
	TAPFrontAddressType MdFront;
	///初始化超时退出（微秒）
	TAPTimeAnchorType ConnectTimeout;
	///账户任务执行间隔（微秒）
	TAPTimeAnchorType TaskExecuteGap;
	///账户任务执行超时（微秒），未设置或者小于10秒时以10秒阈值
	TAPTimeAnchorType TaskExecuteTimeout;
	///Loop线程间隔（微秒）
	TAPTimeAnchorType LoopGap;
	///文件路径
	TAPFilePathType BasePath;
	///BrokerID（期货专用）
	TAPBrokerIDType BrokerID;
	///AppID（期货专用）
	TAPAppIDType AppID;
	///AuthCode（期货专用）
	TAPAuthCodeType AuthCode;
	///硬盘序列号
	TAPHDSerialType HDSerial;
	///Mac地址
	TAPMacAddressType MacAddress;
	///公网IP地址
	TAPIPAddressType OuterIPAddress;
	///公网IP端口号
	TAPPortType OuterPort;
	///内网IP地址
	TAPIPAddressType InnerIPAddress;
	//产品信息
	TAPProductInfoType UserProductInfo;
	///终端信息
	TAPTerminalInfoType TerminalInfo;
};

/// 简明实时行情数据
struct CAPSimpleMarketDataField
{
	CAPSimpleMarketDataField() { memset(this, 0, sizeof(*this)); };

	///交易日
	TAPDateType TradingDay;
	///交易所
	TAPExchangeIDType ExchangeID;
	///标准交易代码
	TAPStandardIDType StandardID;
	///行情状态
	TAPMarketDataStatusType MarketDataStatus;
	///笔数
	TAPCountType TradingCount;
	///更新时间
	TAPTimeType UpdateTime;
	///更新毫秒
	TAPMillisecType UpdateMillisec;
	///时间戳
	TAPTimeStampType TimeStamp;
	///最新价
	TAPPriceType LastPrice;
	///昨收盘价
	TAPPriceType PreClosePrice;
	///昨结算价
	TAPPriceType PreSettlementPrice;
	///今开盘价
	TAPPriceType OpenPrice;
	///最高价
	TAPPriceType HighestPrice;
	///最低价
	TAPPriceType LowestPrice;
	///买1价
	TAPPriceType BidPrice1;
	///买1量
	TAPVolumeType BidVolume1;
	///卖1价
	TAPPriceType AskPrice1;
	///卖1量
	TAPVolumeType AskVolume1;
	///涨停价
	TAPPriceType UpperLimitPrice;
	///跌停价
	TAPPriceType LowerLimitPrice;
	///持仓量
	TAPOpenInterestType OpenInterest;
	///昨持仓量
	TAPOpenInterestType PreOpenInterest;
	///成交量
	TAPLongVolumeType Volume;
	///成交金额
	TAPMoneyType Turnover;
	///当日均价
	TAPPriceType AveragePrice;
	///委托买入总量
	TAPVolumeType	TotalBidVolume;
	///加权平均委托买价格
	TAPPriceType	AvgBidPrice;
	///委托卖出总量
	TAPVolumeType	TotalAskVolume;
	///加权平均委托卖价格
	TAPPriceType	AvgAskPrice;
};

/// 实时行情数据
struct CAPMarketDataField
{
	CAPMarketDataField() { memset(this, 0, sizeof(*this)); };

	///交易日
	TAPDateType TradingDay;
	///交易所
	TAPExchangeIDType ExchangeID;
	///标准交易代码
	TAPStandardIDType StandardID;
	///行情状态
	TAPMarketDataStatusType MarketDataStatus;
	///笔数
	TAPCountType TradingCount;
	///更新时间
	TAPTimeType UpdateTime;
	///更新毫秒
	TAPMillisecType UpdateMillisec;
	///时间戳
	TAPTimeStampType TimeStamp;
	///最新价
	TAPPriceType LastPrice;
	///昨收盘价
	TAPPriceType PreClosePrice;
	///昨结算价
	TAPPriceType PreSettlementPrice;
	///今开盘价
	TAPPriceType OpenPrice;
	///最高价
	TAPPriceType HighestPrice;
	///最低价
	TAPPriceType LowestPrice;
	///买1价
	TAPPriceType BidPrice1;
	///买1量
	TAPVolumeType BidVolume1;
	///卖1价
	TAPPriceType AskPrice1;
	///卖1量
	TAPVolumeType AskVolume1;
	///涨停价
	TAPPriceType UpperLimitPrice;
	///跌停价
	TAPPriceType LowerLimitPrice;
	///持仓量
	TAPOpenInterestType OpenInterest;
	///昨持仓量
	TAPOpenInterestType PreOpenInterest;
	///成交量
	TAPLongVolumeType Volume;
	///成交金额
	TAPMoneyType Turnover;
	///当日均价
	TAPPriceType AveragePrice;
	///委托买入总量
	TAPVolumeType	TotalBidVolume;
	///加权平均委托买价格
	TAPPriceType	AvgBidPrice;
	///委托卖出总量
	TAPVolumeType	TotalAskVolume;
	///加权平均委托卖价格
	TAPPriceType	AvgAskPrice;
	///买2价
	TAPPriceType BidPrice2;
	///买2量
	TAPVolumeType BidVolume2;
	///卖2价
	TAPPriceType AskPrice2;
	///卖2量
	TAPVolumeType AskVolume2;
	///买3价
	TAPPriceType BidPrice3;
	///买3量
	TAPVolumeType BidVolume3;
	///卖3价
	TAPPriceType AskPrice3;
	///卖3量
	TAPVolumeType AskVolume3;
	///买4价
	TAPPriceType BidPrice4;
	///买4量
	TAPVolumeType BidVolume4;
	///卖4价
	TAPPriceType AskPrice4;
	///卖4量
	TAPVolumeType AskVolume4;
	///买5价
	TAPPriceType BidPrice5;
	///买5量
	TAPVolumeType BidVolume5;
	///卖5价
	TAPPriceType AskPrice5;
	///卖5量
	TAPVolumeType AskVolume5;
	///买6价
	TAPPriceType BidPrice6;
	///买6量
	TAPVolumeType BidVolume6;
	///卖6价
	TAPPriceType AskPrice6;
	///卖6量
	TAPVolumeType AskVolume6;
	///买7价
	TAPPriceType BidPrice7;
	///买7量
	TAPVolumeType BidVolume7;
	///卖7价
	TAPPriceType AskPrice7;
	///卖7量
	TAPVolumeType AskVolume7;
	///买8价
	TAPPriceType BidPrice8;
	///买8量
	TAPVolumeType BidVolume8;
	///卖8价
	TAPPriceType AskPrice8;
	///卖8量
	TAPVolumeType AskVolume8;
	///买9价
	TAPPriceType BidPrice9;
	///买9量
	TAPVolumeType BidVolume9;
	///卖9价
	TAPPriceType AskPrice9;
	///卖9量
	TAPVolumeType AskVolume9;
	///买10价
	TAPPriceType BidPrice10;
	///买10量
	TAPVolumeType BidVolume10;
	///卖10价
	TAPPriceType AskPrice10;
	///卖10量
	TAPVolumeType AskVolume10;
	///买入总笔数(只有上海行情有效)
	TAPVolumeType	TotalBidNumber;
	///卖出总笔数(只有上海行情有效)
	TAPVolumeType	TotalOfferNumber;
	///买入委托成交量最大等待时间(只有上海行情有效)
	TAPVolumeType	BidTradeMaxDuration;
	///卖出委托成交量最大等待时间(只有上海行情有效)
	TAPVolumeType	OfferTradeMaxDuration;
	///基金实时参考净值
	TAPPriceType	IOPV;
	///买一价上总委托笔数
	TAPVolumeType	Ask1NumOrders;
	///卖一价上总委托笔数
	TAPVolumeType	Bid1NumOrders;
	///买二价上总委托笔数
	TAPVolumeType	Ask2NumOrders;
	///卖二价上总委托笔数
	TAPVolumeType	Bid2NumOrders;
	///买三价上总委托笔数
	TAPVolumeType	Ask3NumOrders;
	///卖三价上总委托笔数
	TAPVolumeType	Bid3NumOrders;
	///买四价上总委托笔数
	TAPVolumeType	Ask4NumOrders;
	///卖四价上总委托笔数
	TAPVolumeType	Bid4NumOrders;
	///买五价上总委托笔数
	TAPVolumeType	Ask5NumOrders;
	///卖五价上总委托笔数
	TAPVolumeType	Bid5NumOrders;
	///买六价上总委托笔数
	TAPVolumeType	Ask6NumOrders;
	///卖六价上总委托笔数
	TAPVolumeType	Bid6NumOrders;
	///买七价上总委托笔数
	TAPVolumeType	Ask7NumOrders;
	///卖七价上总委托笔数
	TAPVolumeType	Bid7NumOrders;
	///买八价上总委托笔数
	TAPVolumeType	Ask8NumOrders;
	///卖八价上总委托笔数
	TAPVolumeType	Bid8NumOrders;
	///买九价上总委托笔数
	TAPVolumeType	Ask9NumOrders;
	///卖九价上总委托笔数
	TAPVolumeType	Bid9NumOrders;
	///买十价上总委托笔数
	TAPVolumeType	Ask10NumOrders;
	///卖十价上总委托笔数
	TAPVolumeType	Bid10NumOrders;
	///附加信息1
	TAPIntType	Info1;
	///附加信息2
	TAPIntType	Info2;
	///附加信息3
	TAPIntType	Info3;
};

/// Level2逐笔明细数据
struct CAPDetailDataField
{
	CAPDetailDataField() { memset(this, 0, sizeof(*this)); };

	///交易所
	TAPExchangeIDType	ExchangeID;
	///标准交易代码
	TAPStandardIDType	StandardID;
	///明细数据业务类型
	TAPDetailDataBusinessTypeType DetailDataBusinessType;
	///明细数据标志
	TAPDetailDataFlagType DetailDataFlag;
	///时间戳
	TAPTimeStampType TimeStamp;
	///价格
	TAPPriceType Price;
	///数量
	TAPVolumeType Volume;
	///主序号
	TAPSequenceNoType	MainSequenceNo;
	///子序号
	TAPLongSequenceType	SubSequenceNo;
	///买方委托序号
	TAPLongSequenceType	BuyOrderNo;
	///卖方委托序号
	TAPLongSequenceType	SellOrderNo;
	///订单类别（只有深圳逐笔委托行情有效）
	TAPOrderTypeType	OrderType;
	///业务序号（只有上海行情有效）
	TAPLongSequenceType	BizIndex;
	///附加信息1
	TAPIntType	Info1;
	///附加信息2
	TAPIntType	Info2;
	///附加信息3
	TAPIntType	Info3;
};

/// 信用负债
struct CAPCreditDebtField
{
	CAPCreditDebtField() { memset(this, 0, sizeof(*this)); };

	///信用负债编号
	TAPCreditDebtIDType	CreditDebtID;
	///信用负债类型
	TAPCreditDebtTypeType	CreditDebtType;
	///信用合约状态
	TAPCreditDebtStatusType	CreditDebtStatus;
	///头寸类型
	TAPCreditQuotaTypeType	CreditQuotaType;
	///交易所代码
	TAPExchangeIDType ExchangeID;
	///证券代码
	TAPStandardIDType StandardID;
	///开仓日期
	TAPDateType OpenDate;
	///开仓时间
	TAPTimeType OpenTime;
	///到期日
	TAPDateType ExpireDate;
	///数量
	TAPVolumeType Volume;
	///金额
	TAPMoneyType Amount;
	///未偿还数量
	TAPVolumeType UnpaidVolume;
	///未偿还金额
	TAPMoneyType UnpaidAmount;
	///未偿还交易费用（融资）
	TAPMoneyType UnpaidTradingFee;
	///未偿还息费（融资利息、融券费用）
	TAPMoneyType UnpaidInterestFee;
	///还券未成交数量
	TAPVolumeType RepayUntradeVolume;
	///可偿还数量
	TAPVolumeType ActiveVolume;
	///已展期次数
	TAPCountType ExtendCount;
	///日初利率
	TAPRatioType PreInterestRate;
	///利率
	TAPRatioType InterestRate;
	///费息折扣券编号
	TAPDiscountCouponIDType DiscountCouponID;
};

/// 持仓
struct CAPPositionField
{
	CAPPositionField() { memset(this, 0, sizeof(*this)); };

	///交易日
	TAPDateType TradingDay;
	///客户号
	TAPUserIDType UserID;
	///交易所
	TAPExchangeIDType ExchangeID;
	///标准交易代码
	TAPStandardIDType StandardID;
	///多头昨仓
	TAPVolumeType LongVolumeHistory;
	///多头持仓冻结
	TAPVolumeType LongVolumeHistoryFrozen;
	///多头今仓
	TAPVolumeType LongVolumeToday;
	///多头今仓冻结
	TAPVolumeType LongVolumeTodayFrozen;
	///多头持仓
	TAPVolumeType LongVolume;
	///多头持仓冻结
	TAPVolumeType LongVolumeFrozen;
	///空头昨仓
	TAPVolumeType ShortVolumeHistory;
	///空头持仓
	TAPVolumeType ShortVolumeHistoryFrozen;
	///空头今仓
	TAPVolumeType ShortVolumeToday;
	///空头今仓冻结
	TAPVolumeType ShortVolumeTodayFrozen;
	///空头持仓
	TAPVolumeType ShortVolume;
	///空头持仓
	TAPVolumeType ShortVolumeFrozen;
	//多头成交金额
	TAPMoneyType LongTurnover;
	//多头均价
	TAPPriceType LongAverageCost;
	//空头成交金额
	TAPMoneyType ShortTurnover;
	//空头均价
	TAPPriceType ShortAverageCost;
	///信用多头今仓
	TAPVolumeType CreditLongVolumeToday;
	///信用多头昨仓
	TAPVolumeType CreditLongVolumeHistory;
};

/// 订单
struct CAPOrderField
{
	CAPOrderField() { memset(this, 0, sizeof(*this)); };

	///交易日
	TAPDateType TradingDay;
	///客户号
	TAPUserIDType UserID;
	///股东账户代码
	TAPShareholderIDType ShareholderID;
	///会话号
	TAPSessionIDType SessionID;
	///前置号
	TAPFrontIDType FrontID;
	///报单引用
	TAPOrderIDType OrderID;
	///订单备注
	TAPOrderIDType OrderMark;
	///下一个订单
	CAPOrderField* NextOrder;
	///交易所
	TAPExchangeIDType ExchangeID;
	///标准交易代码
	TAPStandardIDType StandardID;
	///订单方向
	TAPDirectionType Direction;
	///开平标志
	TAPOffsetFlagType OffsetFlag;
	///订单类型
	TAPOrderTypeType OrderType;
	///是否是买入
	TAPBoolType IsBuyFromMarket;
	///是否是限价单
	TAPBoolType IsLimitOrder;
	///报单价格条件
	TAPOrderPriceTypeType OrderPriceType;
	///有效期
	TAPTimeConditionType TimeCondition;
	///成交量
	TAPVolumeConditionType VolumeCondition;
	///触发条件
	TAPContingentConditionType ContingentCondition;
	///头寸类型(两融专用)
	TAPCreditQuotaTypeType	CreditQuotaType;
	///信用负债编号(两融专用)
	TAPCreditDebtIDType	CreditDebtID;
	///报单数量
	TAPVolumeType OriginalVolume;
	///报单价格
	TAPPriceType OriginalPrice;
	///本地报单时间
	TAPTimeAnchorType OrderLocalTime;
	///系统编号
	TAPOrderSysIDType OrderSysID;
	///申报时间
	TAPTimeType	InsertTime;
	///交易所接收时间
	TAPTimeType	UpdateTime;
	///订单状态
	TAPOrderStatusType OrderStatus;
	///成交数量变化
	TAPVolumeType TradedVolumeChange;
	///全部成交数量
	TAPVolumeType TradedVolume;
	///全部撤单数量
	TAPVolumeType CanceledVolume;
	///最近一次成交价
	TAPPriceType LastTradedPrice;
	///与成交额对应的成交数量变化
	TAPVolumeType TradedVolumeChangeOfTurnover;
	///与成交额对应的全部成交数量
	TAPVolumeType TradedVolumeOfTurnover;
	///成交额
	TAPMoneyType TurnoverChange;
	///成交额
	TAPMoneyType Turnover;
	///平均成本
	TAPPriceType AverageCost;
	///错误代码
	TAPErrorIDType ErrorID;
	///信息
	TAPMessageType Message;
};

/// 资产划转
struct CAPTransferAssetField
{
	CAPTransferAssetField() { memset(this, 0, sizeof(*this)); };

	///交易日
	TAPDateType TradingDay;
	///客户号
	TAPUserIDType UserID;
	///资产划转编号
	TAPTransferIDType TransferID;
	///转移状态
	TAPTransferStatusType TransferStatus;
	///转移方向
	TAPTransferDirectionType TransferDirection;
	///转移金额
	TAPMoneyType Amount;
	///转移数量
	TAPVolumeType Volume;
	///交易所
	TAPExchangeIDType ExchangeID;
	///标准交易代码
	TAPStandardIDType StandardID;
	///转移持仓类型
	TAPTransferPositionTypeType TransferPositionType;
	/// 负债编号
	TAPCreditDebtIDType	CreditDebtID;
	///银行代码（银证转账时必填）
	TAPBankIDType BankID;
	///外部节点编号
	TAPNodeIDType ExternalNodeID;
	///前置编号
	TAPFrontIDType FrontID;
	///会话编号
	TAPSessionIDType SessionID;
	///转移流水号
	TAPBusinessIDType BusinessID;
	///错误代码
	TAPErrorIDType ErrorID;
	///错误信息
	TAPMessageType Message;
};

/// 通用查询
struct CAPQueryCommandField
{
	CAPQueryCommandField() { memset(this, 0, sizeof(*this)); };

	///交易日
	TAPDateType TradingDay;
	///客户号
	TAPUserIDType UserID;
	///交易所
	TAPExchangeIDType ExchangeID;
	///标准交易代码
	TAPStandardIDType StandardID;
	///业务流水号
	TAPBusinessIDType BusinessID;
	///业务标志组合
	TAPCombineBusinessFlagType CombineBusinessFlag;
	///价格
	TAPPriceType Price;
	///数量
	TAPVolumeType Volume;
	///开始时间
	TAPTimeType StartTime;
	///结束时间
	TAPTimeType EndTime;
	///开始日期
	TAPDateType StartDate;
	///结束日期
	TAPDateType EndDate;
	///银行代码
	TAPBankIDType BankID;
	///银行账户密码
	TAPPasswordType BankPassword;
	///资金账户密码
	TAPPasswordType AccountPassword;
	///柜台节点号
	TAPNodeIDType NodeID;
};

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 切片行情事件回调
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPSnapDataEventCallbackType)(TAPEventIDType, CAPMarketDataField*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 逐笔行情事件回调
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPDetailDataEventCallbackType)(TAPEventIDType, CAPDetailDataField*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 订单事件回调
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPOrderEventCallbackType)(TAPEventIDType, CAPOrderField*, CAPPositionField*, double);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 其他事件回调
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPFlexibleEventCallbackType)(TAPEventIDType, void*, bool, const char*, TAPErrorIDType, const char*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 线程轮询事件回调
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPLoopEventCallbackType)();

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 默认FlexibleEventCallback方法调用的文本处理方法，如果未设置则输出到标准输出
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPEventTextProcessorType)(const char*);

#endif
