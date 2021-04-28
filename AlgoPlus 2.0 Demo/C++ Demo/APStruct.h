#ifndef AP_STRUCT_H__
#define AP_STRUCT_H__


#include <cstring>
#include "APDataType.h"


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 登录
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct CAPLoginField
{
	CAPLoginField() { memset(this, 0, sizeof(*this)); };

	///许可证
	TAPLicenseType License;
	///客户类型
	TAPUserTypeType UserType;
	///客户号
	TAPUserIDType UserID;
	///投资者代码
	TAPInvestorIDType InvestorID;
	///密码
	TAPPasswordType Password;
	///交易前置（tcp://127.0.0.1:22222）
	TAPFrontAddressType TraderFront;
	///行情交易（tcp://127.0.0.1:22222）
	TAPFrontAddressType MdFront;
	///登录超时设置
	TAPTimeAnchorType ConnectTimeout;
	///账户任务执行间隔
	TAPTimeAnchorType TaskExecuteGap;
	///循环线程间隔
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
	///终端信息
	TAPTerminalInfoType TerminalInfo;
};

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 实时行情
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct CAPMarketDataField
{
	CAPMarketDataField() = delete;

	///交易日
	TAPDateType TradingDay;
	///标准交易代码
	TAPStandardIDType StandardID;
	///交易所代码
	TAPExchangeIDType ExchangeID;
	///昨收盘价
	TAPPriceType PreClosePrice;
	///今开盘价
	TAPPriceType OpenPrice;
	///行情产品实时状态
	TAPStandardStatusType StandardStatus;
	///成交笔数
	TAPCountType TradingCount;
	///更新时间
	TAPTimeType UpdateTime;
	///更新毫秒
	TAPMillisecType UpdateMillisec;
	///持仓量
	TAPLargeVolumeType OpenInterest;
	///成交量
	TAPLongVolumeType Volume;
	///成交金额
	TAPMoneyType Turnover;
	///当日均价
	TAPPriceType AveragePrice;
	///最新价
	TAPPriceType LastPrice;
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
};

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 持仓
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct CAPPositionField
{
	CAPPositionField() = delete;

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
};

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 订单
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct CAPOrderField
{
	CAPOrderField() = delete;

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
	///请求编号
	TAPRequestIDType RequestID;
	///报单引用
	TAPOrderIDType OrderID;
	///报单引用
	TAPOrderIDType NextOrderID;
	///订单备注
	TAPOrderMarkType OrderMark;
	///交易所
	TAPExchangeIDType ExchangeID;
	///标准交易代码
	TAPStandardIDType StandardID;
	///买
	TAPBoolType IsBuyFromMarket;
	///
	TAPOrderDirectionType Direction;
	///订单类型
	TAPOrderTypeType OrderType;
	///是否是限价单
	TAPBoolType IsLimitOrder;
	///
	TAPPriceTypeType PriceType;
	///
	TAPTimeConditionType TimeCondition;
	///
	TAPVolumeConditionType VolumeCondition;
	///
	TAPContingentConditionType ContingentCondition;
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
	TAPVolumeType CancelVolume;
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
	///信用头寸编号(两融专用)
	TAPQuotaIDType	CreditQuotaID;
	///头寸类型(两融专用)
	TAPCreditQuotaTypeType	CreditQuotaType;
	///信用负债编号(两融专用)
	TAPCreditDebtIDType	CreditDebtID;
	///错误代码
	TAPErrorIDType ErrorID;
	///信息
	TAPMessageType Message;
};


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 行情事件回调方法
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPOnMarketDataFunctionType)(CAPMarketDataField*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 订单事件回调方法
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPOnOrderFunctionType)(TAPOrderEventIDType, const CAPOrderField*, const CAPPositionField*, double);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 其他事件回调方法
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPOnEventFunctionType)(TAPEventIDType, const void*, bool, TAPErrorIDType, const char*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// 轮询
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void (*FAPOnLoopFunctionType)();


#endif //
