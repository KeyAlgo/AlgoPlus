#ifndef AP_API_H__
#define AP_API_H__

#include <string>
#include "APStruct.h"

#ifdef APAPI_EXPORT
#ifdef _WIN32
#define APAPI_DLL_EXPORT __declspec(dllexport)
#else
#define APAPI_DLL_EXPORT __attribute__ ((visibility("default")))
#endif
#else
#define APAPI_DLL_EXPORT 
#endif

class CBaseTrader;

#ifdef __cplusplus
extern "C" {
#endif

	/// ��ʼ��
	APAPI_DLL_EXPORT CBaseTrader* init(short nRunID, CAPLoginField* pLoginField, FAPOrderEventCallbackType pOrderEventCallback = NULL, FAPFlexibleEventCallbackType pFlexibleEventCallback = NULL, FAPLoopEventCallbackType pLoopEventCallback = NULL, FAPSnapDataEventCallbackType pSnapDataEventCallback = NULL, FAPDetailDataEventCallbackType pDetailDataEventCallback = NULL);
	/// ��ѯ��ʼ������
	APAPI_DLL_EXPORT TAPErrorIDType getInitError();
	/// ��ѯ
	APAPI_DLL_EXPORT void loop();

	/// ��������ģʽ��Ĭ��Debugģʽ�����¼���ؽṹ��תΪ�ַ���������EventTextProcessor����
	APAPI_DLL_EXPORT TAPErrorIDType setRunMode(TAPRunModeType chRunMode);
	/// ���ô����¼��ַ����ķ�����Ĭ���������Ļ��
	APAPI_DLL_EXPORT TAPErrorIDType setEventTextProcessor(FAPEventTextProcessorType pTextProcessor);

	/// ���ñ����¼��ص�����
	APAPI_DLL_EXPORT TAPErrorIDType setOrderEventCallback(CBaseTrader* pAPTrader, TAPEventIDType nOrderEventID, FAPOrderEventCallbackType pOrderEventCallback);
	/// ���ÿ��������¼��ص�����
	APAPI_DLL_EXPORT TAPErrorIDType setSnapDataEventCallback(CBaseTrader* pAPTrader, TAPEventIDType nSnapDataEventID, FAPSnapDataEventCallbackType pSnapDataEventCallback);
	/// ����Level2��ϸ�����¼��ص�����
	APAPI_DLL_EXPORT TAPErrorIDType setDetailDataEventCallback(CBaseTrader* pAPTrader, TAPEventIDType nDetailDataEventID, FAPDetailDataEventCallbackType pDetailDataEventCallback);

	///// ���õ�����󱨵���
	//APAPI_DLL_EXPORT TAPErrorIDType setMaxOrderVolume(const char* szStandardID, int nMaxVolume, const char* szExchangeID = NULL);
	///// ���ñ�֤�����
	//APAPI_DLL_EXPORT TAPErrorIDType setMarginRate(const char* szStandardID, double dMarginRate, const char* szExchangeID = NULL);
	///// ������������
	//APAPI_DLL_EXPORT TAPErrorIDType setTurnoverFeeRate(const char* szStandardID, double dFeeRate, const char* szExchangeID = NULL);
	///// ���õ�λ�̶�������
	//APAPI_DLL_EXPORT TAPErrorIDType setVolumeConstFee(const char* szStandardID, double dConstFee, const char* szExchangeID = NULL);

	/// ��������
	APAPI_DLL_EXPORT TAPErrorIDType subscribeOne(CBaseTrader* pAPTrader, const char* szStandardID, const char* szExchangeID = NULL, char chMarketDataType = ENUM_MarketDataType_Snap);
	/// ������������
	APAPI_DLL_EXPORT TAPErrorIDType subscribe(CBaseTrader* pAPTrader, char** ppStandardID, int nCount, const char* szExchangeID = NULL, char chMarketDataType = ENUM_MarketDataType_Snap);
	/// �˶�����
	APAPI_DLL_EXPORT TAPErrorIDType unsubscribeOne(CBaseTrader* pAPTrader, const char* szStandardID, const char* szExchangeID = NULL, char chMarketDataType = ENUM_MarketDataType_Snap);
	/// �����˶�����
	APAPI_DLL_EXPORT TAPErrorIDType unsubscribe(CBaseTrader* pAPTrader, char** ppStandardID, int nCount, const char* szExchangeID = NULL, char chMarketDataType = ENUM_MarketDataType_Snap);

	/// ������
	APAPI_DLL_EXPORT CAPOrderField* buyOpen(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chDirection = ENUM_Direction_Buy);
	/// ��ƽ����
	APAPI_DLL_EXPORT CAPOrderField* sellClose(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chDirection = ENUM_Direction_Sell, char chOffsetFlag = '\0', const char* szCreditDebitID = NULL);
	/// ��������
	APAPI_DLL_EXPORT CAPOrderField* sellOpen(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chDirection = '\0', char chCreditQuotaType = '\0');
	/// ��ƽ����
	APAPI_DLL_EXPORT CAPOrderField* buyClose(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chDirection = '\0', char chOffsetFlag = '\0', const char* szCreditDebitID = NULL);
	/// ������
	APAPI_DLL_EXPORT CAPOrderField* buy(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// ����
	APAPI_DLL_EXPORT CAPOrderField* buyAmount(CBaseTrader* pAPTrader, const char* szStandardID, double dAmount, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// �����
	APAPI_DLL_EXPORT CAPOrderField* buyRatio(CBaseTrader* pAPTrader, const char* szStandardID, double dRatio, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// ������
	APAPI_DLL_EXPORT CAPOrderField* sell(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// �����
	APAPI_DLL_EXPORT CAPOrderField* sellAmount(CBaseTrader* pAPTrader, const char* szStandardID, double dAmount, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// ������
	APAPI_DLL_EXPORT CAPOrderField* sellRatio(CBaseTrader* pAPTrader, const char* szStandardID, double dRatio, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// ��ֶ�ͷ
	APAPI_DLL_EXPORT CAPOrderField* closeLong(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, bool bTodayFirst = false);
	/// ��ֿ�ͷ
	APAPI_DLL_EXPORT CAPOrderField* closeShort(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, bool bTodayFirst = false);
	/// ��������ͷĿ������
	APAPI_DLL_EXPORT CAPOrderField* balanceToLongValue(CBaseTrader* pAPTrader, const char* szStandardID, double dTargetValue, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��������ͷĿ����
	APAPI_DLL_EXPORT CAPOrderField* balanceToLongVolume(CBaseTrader* pAPTrader, const char* szStandardID, int nTargetVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��������ͷĿ������
	APAPI_DLL_EXPORT CAPOrderField* balanceToShortValue(CBaseTrader* pAPTrader, const char* szStandardID, double dTargetValue, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��������ͷĿ����
	APAPI_DLL_EXPORT CAPOrderField* balanceToShortVolume(CBaseTrader* pAPTrader, const char* szStandardID, int nTargetVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);

	/// ����
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrder(CBaseTrader* pAPTrader, const char* szExchangeID, const char* szStandardID, const char* szOrderSysID, int nOrderID, int nFrontID = 0, int nSessionID = 0);
	/// ����
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByOrderID(CBaseTrader* pAPTrader, int nOrderID);
	/// �Ա�ĳ���
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByStandardID(CBaseTrader* pAPTrader, const char* szStandardID, const char* szExchangeID = NULL);
	/// �Խ���������
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByExchangeID(CBaseTrader* pAPTrader, const char* szExchangeID);
	/// �������ж���
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderAll(CBaseTrader* pAPTrader);

	/// ��ѯ�����ʽ�
	APAPI_DLL_EXPORT TAPMoneyType getUsableCash(CBaseTrader* pAPTrader);
	/// ��ѯ����
	APAPI_DLL_EXPORT CAPOrderField* getOrder(CBaseTrader* pAPTrader, int nOrderID = 0);
	/// ��ѯ�ֲ�
	APAPI_DLL_EXPORT CAPPositionField* getPosition(CBaseTrader* pAPTrader, const char* szStandardID = NULL, const char* szExchangeID = NULL);

	/// ��ת�ʽ�
	APAPI_DLL_EXPORT CAPTransferAssetField* transferCash(CBaseTrader* pAPTrader, char chTransferDirection, double dAmount, const char* szAccountPassword, const char* szBankID, const char* szBankPassword, const char* szNodeID = NULL, const char* szCreditDebtID = NULL);
	/// ��ת�ֲ�
	APAPI_DLL_EXPORT CAPTransferAssetField* transferPosition(CBaseTrader* pAPTrader, char chTransferDirection, int nVolume, const char* szStandardID, const char* szNodeID = NULL, const char* szCreditDebtID = NULL, const char* szExchangeID = NULL);
	/// ��ѯ���п����
	APAPI_DLL_EXPORT TAPErrorIDType queryBankAccountCash(CBaseTrader* pAPTrader, const char* szAccountPassword, const char* szBankID, const char* szBankPassword);
	/// �޸�����
	APAPI_DLL_EXPORT TAPErrorIDType updatePassword(CBaseTrader* pAPTrader, char chPasswordFlag, const char* szOldPassword, const char* szNewPassword);

	/// �������
	APAPI_DLL_EXPORT TAPErrorIDType addTask(CBaseTrader* pAPTrader, TAPEventIDType nEventID, CAPQueryCommandField* pQueryCommandField = NULL, int nMaxExecuteCount = 1, TAPTimeAnchorType nExecuteGap = -1, bool bRefuseError = false, TAPTimeAnchorType nExecuteTimeout = -1);

	/// ����ʱ��ê
	APAPI_DLL_EXPORT TAPTimeAnchorType setTimeAnchor();
	/// ����ʱ���
	APAPI_DLL_EXPORT TAPTimeAnchorType getTimeElapse(TAPTimeAnchorType nTimeAnchor = 0);

	/// �˳�
	APAPI_DLL_EXPORT void exitX(CBaseTrader* pAPTrader = NULL);

#ifdef __cplusplus
}
#endif

#endif
