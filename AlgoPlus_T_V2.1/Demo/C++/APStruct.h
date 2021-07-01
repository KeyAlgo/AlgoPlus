#ifndef AP_STRUCT_H__
#define AP_STRUCT_H__

#include <cstring>
#include "APDataType.h"

/// ��¼
struct CAPLoginField
{
	CAPLoginField() { memset(this, 0, sizeof(*this)); TaskExecuteGap = -1; LoopGap = -1; };
	CAPLoginField(CAPLoginField* pLoginField) { memcpy(this, pLoginField, sizeof(*this)); };

	///���֤
	TAPLicenseType License;
	///�ͻ�����
	TAPUserTypeType UserType;
	///�ͻ���
	TAPUserIDType UserID;
	///����
	TAPPasswordType Password;
	///Ͷ���ߴ��룬���δ������ʹ��UserID
	TAPInvestorIDType InvestorID;
	///�ʽ��˻�����������
	TAPAccountIDType AccountID;
	///���Ŵ��룬��������
	TAPDepartmentIDType DepartmentID;
	///����ǰ�õ�ַ��tcp://127.0.0.1:22222��
	TAPFrontAddressType TraderFront;
	///����ǰ�õ�ַ��tcp://127.0.0.1:22222��
	TAPFrontAddressType MdFront;
	///��ʼ����ʱ�˳���΢�룩
	TAPTimeAnchorType ConnectTimeout;
	///�˻�����ִ�м����΢�룩
	TAPTimeAnchorType TaskExecuteGap;
	///�˻�����ִ�г�ʱ��΢�룩��δ���û���С��10��ʱ��10����ֵ
	TAPTimeAnchorType TaskExecuteTimeout;
	///Loop�̼߳����΢�룩
	TAPTimeAnchorType LoopGap;
	///�ļ�·��
	TAPFilePathType BasePath;
	///BrokerID���ڻ�ר�ã�
	TAPBrokerIDType BrokerID;
	///AppID���ڻ�ר�ã�
	TAPAppIDType AppID;
	///AuthCode���ڻ�ר�ã�
	TAPAuthCodeType AuthCode;
	///Ӳ�����к�
	TAPHDSerialType HDSerial;
	///Mac��ַ
	TAPMacAddressType MacAddress;
	///����IP��ַ
	TAPIPAddressType OuterIPAddress;
	///����IP�˿ں�
	TAPPortType OuterPort;
	///����IP��ַ
	TAPIPAddressType InnerIPAddress;
	//��Ʒ��Ϣ
	TAPProductInfoType UserProductInfo;
	///�ն���Ϣ
	TAPTerminalInfoType TerminalInfo;
};

/// ����ʵʱ��������
struct CAPSimpleMarketDataField
{
	CAPSimpleMarketDataField() { memset(this, 0, sizeof(*this)); };

	///������
	TAPDateType TradingDay;
	///������
	TAPExchangeIDType ExchangeID;
	///��׼���״���
	TAPStandardIDType StandardID;
	///����״̬
	TAPMarketDataStatusType MarketDataStatus;
	///����
	TAPCountType TradingCount;
	///����ʱ��
	TAPTimeType UpdateTime;
	///���º���
	TAPMillisecType UpdateMillisec;
	///ʱ���
	TAPTimeStampType TimeStamp;
	///���¼�
	TAPPriceType LastPrice;
	///�����̼�
	TAPPriceType PreClosePrice;
	///������
	TAPPriceType PreSettlementPrice;
	///���̼�
	TAPPriceType OpenPrice;
	///��߼�
	TAPPriceType HighestPrice;
	///��ͼ�
	TAPPriceType LowestPrice;
	///��1��
	TAPPriceType BidPrice1;
	///��1��
	TAPVolumeType BidVolume1;
	///��1��
	TAPPriceType AskPrice1;
	///��1��
	TAPVolumeType AskVolume1;
	///��ͣ��
	TAPPriceType UpperLimitPrice;
	///��ͣ��
	TAPPriceType LowerLimitPrice;
	///�ֲ���
	TAPOpenInterestType OpenInterest;
	///��ֲ���
	TAPOpenInterestType PreOpenInterest;
	///�ɽ���
	TAPLongVolumeType Volume;
	///�ɽ����
	TAPMoneyType Turnover;
	///���վ���
	TAPPriceType AveragePrice;
	///ί����������
	TAPVolumeType	TotalBidVolume;
	///��Ȩƽ��ί����۸�
	TAPPriceType	AvgBidPrice;
	///ί����������
	TAPVolumeType	TotalAskVolume;
	///��Ȩƽ��ί�����۸�
	TAPPriceType	AvgAskPrice;
};

/// ʵʱ��������
struct CAPMarketDataField
{
	CAPMarketDataField() { memset(this, 0, sizeof(*this)); };

	///������
	TAPDateType TradingDay;
	///������
	TAPExchangeIDType ExchangeID;
	///��׼���״���
	TAPStandardIDType StandardID;
	///����״̬
	TAPMarketDataStatusType MarketDataStatus;
	///����
	TAPCountType TradingCount;
	///����ʱ��
	TAPTimeType UpdateTime;
	///���º���
	TAPMillisecType UpdateMillisec;
	///ʱ���
	TAPTimeStampType TimeStamp;
	///���¼�
	TAPPriceType LastPrice;
	///�����̼�
	TAPPriceType PreClosePrice;
	///������
	TAPPriceType PreSettlementPrice;
	///���̼�
	TAPPriceType OpenPrice;
	///��߼�
	TAPPriceType HighestPrice;
	///��ͼ�
	TAPPriceType LowestPrice;
	///��1��
	TAPPriceType BidPrice1;
	///��1��
	TAPVolumeType BidVolume1;
	///��1��
	TAPPriceType AskPrice1;
	///��1��
	TAPVolumeType AskVolume1;
	///��ͣ��
	TAPPriceType UpperLimitPrice;
	///��ͣ��
	TAPPriceType LowerLimitPrice;
	///�ֲ���
	TAPOpenInterestType OpenInterest;
	///��ֲ���
	TAPOpenInterestType PreOpenInterest;
	///�ɽ���
	TAPLongVolumeType Volume;
	///�ɽ����
	TAPMoneyType Turnover;
	///���վ���
	TAPPriceType AveragePrice;
	///ί����������
	TAPVolumeType	TotalBidVolume;
	///��Ȩƽ��ί����۸�
	TAPPriceType	AvgBidPrice;
	///ί����������
	TAPVolumeType	TotalAskVolume;
	///��Ȩƽ��ί�����۸�
	TAPPriceType	AvgAskPrice;
	///��2��
	TAPPriceType BidPrice2;
	///��2��
	TAPVolumeType BidVolume2;
	///��2��
	TAPPriceType AskPrice2;
	///��2��
	TAPVolumeType AskVolume2;
	///��3��
	TAPPriceType BidPrice3;
	///��3��
	TAPVolumeType BidVolume3;
	///��3��
	TAPPriceType AskPrice3;
	///��3��
	TAPVolumeType AskVolume3;
	///��4��
	TAPPriceType BidPrice4;
	///��4��
	TAPVolumeType BidVolume4;
	///��4��
	TAPPriceType AskPrice4;
	///��4��
	TAPVolumeType AskVolume4;
	///��5��
	TAPPriceType BidPrice5;
	///��5��
	TAPVolumeType BidVolume5;
	///��5��
	TAPPriceType AskPrice5;
	///��5��
	TAPVolumeType AskVolume5;
	///��6��
	TAPPriceType BidPrice6;
	///��6��
	TAPVolumeType BidVolume6;
	///��6��
	TAPPriceType AskPrice6;
	///��6��
	TAPVolumeType AskVolume6;
	///��7��
	TAPPriceType BidPrice7;
	///��7��
	TAPVolumeType BidVolume7;
	///��7��
	TAPPriceType AskPrice7;
	///��7��
	TAPVolumeType AskVolume7;
	///��8��
	TAPPriceType BidPrice8;
	///��8��
	TAPVolumeType BidVolume8;
	///��8��
	TAPPriceType AskPrice8;
	///��8��
	TAPVolumeType AskVolume8;
	///��9��
	TAPPriceType BidPrice9;
	///��9��
	TAPVolumeType BidVolume9;
	///��9��
	TAPPriceType AskPrice9;
	///��9��
	TAPVolumeType AskVolume9;
	///��10��
	TAPPriceType BidPrice10;
	///��10��
	TAPVolumeType BidVolume10;
	///��10��
	TAPPriceType AskPrice10;
	///��10��
	TAPVolumeType AskVolume10;
	///�����ܱ���(ֻ���Ϻ�������Ч)
	TAPVolumeType	TotalBidNumber;
	///�����ܱ���(ֻ���Ϻ�������Ч)
	TAPVolumeType	TotalOfferNumber;
	///����ί�гɽ������ȴ�ʱ��(ֻ���Ϻ�������Ч)
	TAPVolumeType	BidTradeMaxDuration;
	///����ί�гɽ������ȴ�ʱ��(ֻ���Ϻ�������Ч)
	TAPVolumeType	OfferTradeMaxDuration;
	///����ʵʱ�ο���ֵ
	TAPPriceType	IOPV;
	///��һ������ί�б���
	TAPVolumeType	Ask1NumOrders;
	///��һ������ί�б���
	TAPVolumeType	Bid1NumOrders;
	///���������ί�б���
	TAPVolumeType	Ask2NumOrders;
	///����������ί�б���
	TAPVolumeType	Bid2NumOrders;
	///����������ί�б���
	TAPVolumeType	Ask3NumOrders;
	///����������ί�б���
	TAPVolumeType	Bid3NumOrders;
	///���ļ�����ί�б���
	TAPVolumeType	Ask4NumOrders;
	///���ļ�����ί�б���
	TAPVolumeType	Bid4NumOrders;
	///���������ί�б���
	TAPVolumeType	Ask5NumOrders;
	///���������ί�б���
	TAPVolumeType	Bid5NumOrders;
	///����������ί�б���
	TAPVolumeType	Ask6NumOrders;
	///����������ί�б���
	TAPVolumeType	Bid6NumOrders;
	///���߼�����ί�б���
	TAPVolumeType	Ask7NumOrders;
	///���߼�����ί�б���
	TAPVolumeType	Bid7NumOrders;
	///��˼�����ί�б���
	TAPVolumeType	Ask8NumOrders;
	///���˼�����ί�б���
	TAPVolumeType	Bid8NumOrders;
	///��ż�����ί�б���
	TAPVolumeType	Ask9NumOrders;
	///���ż�����ί�б���
	TAPVolumeType	Bid9NumOrders;
	///��ʮ������ί�б���
	TAPVolumeType	Ask10NumOrders;
	///��ʮ������ί�б���
	TAPVolumeType	Bid10NumOrders;
	///������Ϣ1
	TAPIntType	Info1;
	///������Ϣ2
	TAPIntType	Info2;
	///������Ϣ3
	TAPIntType	Info3;
};

/// Level2�����ϸ����
struct CAPDetailDataField
{
	CAPDetailDataField() { memset(this, 0, sizeof(*this)); };

	///������
	TAPExchangeIDType	ExchangeID;
	///��׼���״���
	TAPStandardIDType	StandardID;
	///��ϸ����ҵ������
	TAPDetailDataBusinessTypeType DetailDataBusinessType;
	///��ϸ���ݱ�־
	TAPDetailDataFlagType DetailDataFlag;
	///ʱ���
	TAPTimeStampType TimeStamp;
	///�۸�
	TAPPriceType Price;
	///����
	TAPVolumeType Volume;
	///�����
	TAPSequenceNoType	MainSequenceNo;
	///�����
	TAPLongSequenceType	SubSequenceNo;
	///��ί�����
	TAPLongSequenceType	BuyOrderNo;
	///����ί�����
	TAPLongSequenceType	SellOrderNo;
	///�������ֻ���������ί��������Ч��
	TAPOrderTypeType	OrderType;
	///ҵ����ţ�ֻ���Ϻ�������Ч��
	TAPLongSequenceType	BizIndex;
	///������Ϣ1
	TAPIntType	Info1;
	///������Ϣ2
	TAPIntType	Info2;
	///������Ϣ3
	TAPIntType	Info3;
};

/// ���ø�ծ
struct CAPCreditDebtField
{
	CAPCreditDebtField() { memset(this, 0, sizeof(*this)); };

	///���ø�ծ���
	TAPCreditDebtIDType	CreditDebtID;
	///���ø�ծ����
	TAPCreditDebtTypeType	CreditDebtType;
	///���ú�Լ״̬
	TAPCreditDebtStatusType	CreditDebtStatus;
	///ͷ������
	TAPCreditQuotaTypeType	CreditQuotaType;
	///����������
	TAPExchangeIDType ExchangeID;
	///֤ȯ����
	TAPStandardIDType StandardID;
	///��������
	TAPDateType OpenDate;
	///����ʱ��
	TAPTimeType OpenTime;
	///������
	TAPDateType ExpireDate;
	///����
	TAPVolumeType Volume;
	///���
	TAPMoneyType Amount;
	///δ��������
	TAPVolumeType UnpaidVolume;
	///δ�������
	TAPMoneyType UnpaidAmount;
	///δ�������׷��ã����ʣ�
	TAPMoneyType UnpaidTradingFee;
	///δ����Ϣ�ѣ�������Ϣ����ȯ���ã�
	TAPMoneyType UnpaidInterestFee;
	///��ȯδ�ɽ�����
	TAPVolumeType RepayUntradeVolume;
	///�ɳ�������
	TAPVolumeType ActiveVolume;
	///��չ�ڴ���
	TAPCountType ExtendCount;
	///�ճ�����
	TAPRatioType PreInterestRate;
	///����
	TAPRatioType InterestRate;
	///��Ϣ�ۿ�ȯ���
	TAPDiscountCouponIDType DiscountCouponID;
};

/// �ֲ�
struct CAPPositionField
{
	CAPPositionField() { memset(this, 0, sizeof(*this)); };

	///������
	TAPDateType TradingDay;
	///�ͻ���
	TAPUserIDType UserID;
	///������
	TAPExchangeIDType ExchangeID;
	///��׼���״���
	TAPStandardIDType StandardID;
	///��ͷ���
	TAPVolumeType LongVolumeHistory;
	///��ͷ�ֲֶ���
	TAPVolumeType LongVolumeHistoryFrozen;
	///��ͷ���
	TAPVolumeType LongVolumeToday;
	///��ͷ��ֶ���
	TAPVolumeType LongVolumeTodayFrozen;
	///��ͷ�ֲ�
	TAPVolumeType LongVolume;
	///��ͷ�ֲֶ���
	TAPVolumeType LongVolumeFrozen;
	///��ͷ���
	TAPVolumeType ShortVolumeHistory;
	///��ͷ�ֲ�
	TAPVolumeType ShortVolumeHistoryFrozen;
	///��ͷ���
	TAPVolumeType ShortVolumeToday;
	///��ͷ��ֶ���
	TAPVolumeType ShortVolumeTodayFrozen;
	///��ͷ�ֲ�
	TAPVolumeType ShortVolume;
	///��ͷ�ֲ�
	TAPVolumeType ShortVolumeFrozen;
	//��ͷ�ɽ����
	TAPMoneyType LongTurnover;
	//��ͷ����
	TAPPriceType LongAverageCost;
	//��ͷ�ɽ����
	TAPMoneyType ShortTurnover;
	//��ͷ����
	TAPPriceType ShortAverageCost;
	///���ö�ͷ���
	TAPVolumeType CreditLongVolumeToday;
	///���ö�ͷ���
	TAPVolumeType CreditLongVolumeHistory;
};

/// ����
struct CAPOrderField
{
	CAPOrderField() { memset(this, 0, sizeof(*this)); };

	///������
	TAPDateType TradingDay;
	///�ͻ���
	TAPUserIDType UserID;
	///�ɶ��˻�����
	TAPShareholderIDType ShareholderID;
	///�Ự��
	TAPSessionIDType SessionID;
	///ǰ�ú�
	TAPFrontIDType FrontID;
	///��������
	TAPOrderIDType OrderID;
	///������ע
	TAPOrderIDType OrderMark;
	///��һ������
	CAPOrderField* NextOrder;
	///������
	TAPExchangeIDType ExchangeID;
	///��׼���״���
	TAPStandardIDType StandardID;
	///��������
	TAPDirectionType Direction;
	///��ƽ��־
	TAPOffsetFlagType OffsetFlag;
	///��������
	TAPOrderTypeType OrderType;
	///�Ƿ�������
	TAPBoolType IsBuyFromMarket;
	///�Ƿ����޼۵�
	TAPBoolType IsLimitOrder;
	///�����۸�����
	TAPOrderPriceTypeType OrderPriceType;
	///��Ч��
	TAPTimeConditionType TimeCondition;
	///�ɽ���
	TAPVolumeConditionType VolumeCondition;
	///��������
	TAPContingentConditionType ContingentCondition;
	///ͷ������(����ר��)
	TAPCreditQuotaTypeType	CreditQuotaType;
	///���ø�ծ���(����ר��)
	TAPCreditDebtIDType	CreditDebtID;
	///��������
	TAPVolumeType OriginalVolume;
	///�����۸�
	TAPPriceType OriginalPrice;
	///���ر���ʱ��
	TAPTimeAnchorType OrderLocalTime;
	///ϵͳ���
	TAPOrderSysIDType OrderSysID;
	///�걨ʱ��
	TAPTimeType	InsertTime;
	///����������ʱ��
	TAPTimeType	UpdateTime;
	///����״̬
	TAPOrderStatusType OrderStatus;
	///�ɽ������仯
	TAPVolumeType TradedVolumeChange;
	///ȫ���ɽ�����
	TAPVolumeType TradedVolume;
	///ȫ����������
	TAPVolumeType CanceledVolume;
	///���һ�γɽ���
	TAPPriceType LastTradedPrice;
	///��ɽ����Ӧ�ĳɽ������仯
	TAPVolumeType TradedVolumeChangeOfTurnover;
	///��ɽ����Ӧ��ȫ���ɽ�����
	TAPVolumeType TradedVolumeOfTurnover;
	///�ɽ���
	TAPMoneyType TurnoverChange;
	///�ɽ���
	TAPMoneyType Turnover;
	///ƽ���ɱ�
	TAPPriceType AverageCost;
	///�������
	TAPErrorIDType ErrorID;
	///��Ϣ
	TAPMessageType Message;
};

/// �ʲ���ת
struct CAPTransferAssetField
{
	CAPTransferAssetField() { memset(this, 0, sizeof(*this)); };

	///������
	TAPDateType TradingDay;
	///�ͻ���
	TAPUserIDType UserID;
	///�ʲ���ת���
	TAPTransferIDType TransferID;
	///ת��״̬
	TAPTransferStatusType TransferStatus;
	///ת�Ʒ���
	TAPTransferDirectionType TransferDirection;
	///ת�ƽ��
	TAPMoneyType Amount;
	///ת������
	TAPVolumeType Volume;
	///������
	TAPExchangeIDType ExchangeID;
	///��׼���״���
	TAPStandardIDType StandardID;
	///ת�Ƴֲ�����
	TAPTransferPositionTypeType TransferPositionType;
	/// ��ծ���
	TAPCreditDebtIDType	CreditDebtID;
	///���д��루��֤ת��ʱ���
	TAPBankIDType BankID;
	///�ⲿ�ڵ���
	TAPNodeIDType ExternalNodeID;
	///ǰ�ñ��
	TAPFrontIDType FrontID;
	///�Ự���
	TAPSessionIDType SessionID;
	///ת����ˮ��
	TAPBusinessIDType BusinessID;
	///�������
	TAPErrorIDType ErrorID;
	///������Ϣ
	TAPMessageType Message;
};

/// ͨ�ò�ѯ
struct CAPQueryCommandField
{
	CAPQueryCommandField() { memset(this, 0, sizeof(*this)); };

	///������
	TAPDateType TradingDay;
	///�ͻ���
	TAPUserIDType UserID;
	///������
	TAPExchangeIDType ExchangeID;
	///��׼���״���
	TAPStandardIDType StandardID;
	///ҵ����ˮ��
	TAPBusinessIDType BusinessID;
	///ҵ���־���
	TAPCombineBusinessFlagType CombineBusinessFlag;
	///�۸�
	TAPPriceType Price;
	///����
	TAPVolumeType Volume;
	///��ʼʱ��
	TAPTimeType StartTime;
	///����ʱ��
	TAPTimeType EndTime;
	///��ʼ����
	TAPDateType StartDate;
	///��������
	TAPDateType EndDate;
	///���д���
	TAPBankIDType BankID;
	///�����˻�����
	TAPPasswordType BankPassword;
	///�ʽ��˻�����
	TAPPasswordType AccountPassword;
	///��̨�ڵ��
	TAPNodeIDType NodeID;
};

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// ��Ƭ�����¼��ص�
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPSnapDataEventCallbackType)(TAPEventIDType, CAPMarketDataField*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// ��������¼��ص�
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPDetailDataEventCallbackType)(TAPEventIDType, CAPDetailDataField*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// �����¼��ص�
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPOrderEventCallbackType)(TAPEventIDType, CAPOrderField*, CAPPositionField*, double);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// �����¼��ص�
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPFlexibleEventCallbackType)(TAPEventIDType, void*, bool, const char*, TAPErrorIDType, const char*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// �߳���ѯ�¼��ص�
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPLoopEventCallbackType)();

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// Ĭ��FlexibleEventCallback�������õ��ı������������δ�������������׼���
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPEventTextProcessorType)(const char*);

#endif
