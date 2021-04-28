#ifndef AP_STRUCT_H__
#define AP_STRUCT_H__


#include <cstring>
#include "APDataType.h"


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// ��¼
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct CAPLoginField
{
	CAPLoginField() { memset(this, 0, sizeof(*this)); };

	///���֤
	TAPLicenseType License;
	///�ͻ�����
	TAPUserTypeType UserType;
	///�ͻ���
	TAPUserIDType UserID;
	///Ͷ���ߴ���
	TAPInvestorIDType InvestorID;
	///����
	TAPPasswordType Password;
	///����ǰ�ã�tcp://127.0.0.1:22222��
	TAPFrontAddressType TraderFront;
	///���齻�ף�tcp://127.0.0.1:22222��
	TAPFrontAddressType MdFront;
	///��¼��ʱ����
	TAPTimeAnchorType ConnectTimeout;
	///�˻�����ִ�м��
	TAPTimeAnchorType TaskExecuteGap;
	///ѭ���̼߳��
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
	///�ն���Ϣ
	TAPTerminalInfoType TerminalInfo;
};

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// ʵʱ����
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct CAPMarketDataField
{
	CAPMarketDataField() = delete;

	///������
	TAPDateType TradingDay;
	///��׼���״���
	TAPStandardIDType StandardID;
	///����������
	TAPExchangeIDType ExchangeID;
	///�����̼�
	TAPPriceType PreClosePrice;
	///���̼�
	TAPPriceType OpenPrice;
	///�����Ʒʵʱ״̬
	TAPStandardStatusType StandardStatus;
	///�ɽ�����
	TAPCountType TradingCount;
	///����ʱ��
	TAPTimeType UpdateTime;
	///���º���
	TAPMillisecType UpdateMillisec;
	///�ֲ���
	TAPLargeVolumeType OpenInterest;
	///�ɽ���
	TAPLongVolumeType Volume;
	///�ɽ����
	TAPMoneyType Turnover;
	///���վ���
	TAPPriceType AveragePrice;
	///���¼�
	TAPPriceType LastPrice;
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
};

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// �ֲ�
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct CAPPositionField
{
	CAPPositionField() = delete;

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
};

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// ����
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct CAPOrderField
{
	CAPOrderField() = delete;

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
	///������
	TAPRequestIDType RequestID;
	///��������
	TAPOrderIDType OrderID;
	///��������
	TAPOrderIDType NextOrderID;
	///������ע
	TAPOrderMarkType OrderMark;
	///������
	TAPExchangeIDType ExchangeID;
	///��׼���״���
	TAPStandardIDType StandardID;
	///��
	TAPBoolType IsBuyFromMarket;
	///
	TAPOrderDirectionType Direction;
	///��������
	TAPOrderTypeType OrderType;
	///�Ƿ����޼۵�
	TAPBoolType IsLimitOrder;
	///
	TAPPriceTypeType PriceType;
	///
	TAPTimeConditionType TimeCondition;
	///
	TAPVolumeConditionType VolumeCondition;
	///
	TAPContingentConditionType ContingentCondition;
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
	TAPVolumeType CancelVolume;
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
	///����ͷ����(����ר��)
	TAPQuotaIDType	CreditQuotaID;
	///ͷ������(����ר��)
	TAPCreditQuotaTypeType	CreditQuotaType;
	///���ø�ծ���(����ר��)
	TAPCreditDebtIDType	CreditDebtID;
	///�������
	TAPErrorIDType ErrorID;
	///��Ϣ
	TAPMessageType Message;
};


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// �����¼��ص�����
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPOnMarketDataFunctionType)(CAPMarketDataField*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// �����¼��ص�����
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPOnOrderFunctionType)(TAPOrderEventIDType, const CAPOrderField*, const CAPPositionField*, double);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// �����¼��ص�����
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void(*FAPOnEventFunctionType)(TAPEventIDType, const void*, bool, TAPErrorIDType, const char*);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// ��ѯ
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef void (*FAPOnLoopFunctionType)();


#endif //
