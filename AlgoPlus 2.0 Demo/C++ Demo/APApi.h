#ifndef AP_API_H__
#define AP_API_H__

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

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
	APAPI_DLL_EXPORT CBaseTrader* init(short nRunID, CAPLoginField* pLoginField, FAPOnMarketDataFunctionType pMarketDataCallback, FAPOnOrderFunctionType pOrderCallback, FAPOnEventFunctionType pEventCallback, FAPOnLoopFunctionType pLoopCallback = NULL);
	/// ��ѯ��ʼ������
	APAPI_DLL_EXPORT TAPErrorIDType getInitError();
	/// ��ѯ
	APAPI_DLL_EXPORT void loop();

	/// ��������
	APAPI_DLL_EXPORT TAPErrorIDType subscribe(CBaseTrader* pAPTrader, char** ppStandardID, int nCount, const char* szExchangeID = NULL);
	/// �˶�����
	APAPI_DLL_EXPORT TAPErrorIDType unsubscribe(CBaseTrader* pAPTrader, char** ppStandardID, int nCount, const char* szExchangeID = NULL);

	/// ������
	APAPI_DLL_EXPORT CAPOrderField* buy(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ����
	APAPI_DLL_EXPORT CAPOrderField* buyAmount(CBaseTrader* pAPTrader, const char* szStandardID, double dAmount, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// �����
	APAPI_DLL_EXPORT CAPOrderField* buyRatio(CBaseTrader* pAPTrader, const char* szStandardID, double dRatio, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ������
	APAPI_DLL_EXPORT CAPOrderField* sell(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// �����
	APAPI_DLL_EXPORT CAPOrderField* sellAmount(CBaseTrader* pAPTrader, const char* szStandardID, double dAmount, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ������
	APAPI_DLL_EXPORT CAPOrderField* sellRatio(CBaseTrader* pAPTrader, const char* szStandardID, double dRatio, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ������
	APAPI_DLL_EXPORT CAPOrderField* buyOpen(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��ƽ����
	APAPI_DLL_EXPORT CAPOrderField* sellClose(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��ƽ����
	APAPI_DLL_EXPORT CAPOrderField* sellCloseTodayFirst(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��������
	APAPI_DLL_EXPORT CAPOrderField* sellOpen(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��ƽ����
	APAPI_DLL_EXPORT CAPOrderField* buyClose(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��ƽ����
	APAPI_DLL_EXPORT CAPOrderField* buyCloseTodayFirst(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��ֶ�ͷ
	APAPI_DLL_EXPORT CAPOrderField* closeLong(CBaseTrader* pAPTrader, const char* szStandardID, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��ֿ�ͷ
	APAPI_DLL_EXPORT CAPOrderField* closeShort(CBaseTrader* pAPTrader, const char* szStandardID, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��������ͷĿ������
	APAPI_DLL_EXPORT CAPOrderField* balanceToLongValue(CBaseTrader* pAPTrader, const char* szStandardID, double dTargetValue, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��������ͷĿ����
	APAPI_DLL_EXPORT CAPOrderField* balanceToLongVolume(CBaseTrader* pAPTrader, const char* szStandardID, int nTargetVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��������ͷĿ������
	APAPI_DLL_EXPORT CAPOrderField* balanceToShortValue(CBaseTrader* pAPTrader, const char* szStandardID, double dTargetValue, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// ��������ͷĿ����
	APAPI_DLL_EXPORT CAPOrderField* balanceToShortVolume(CBaseTrader* pAPTrader, const char* szStandardID, int nTargetVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);

	/// �����Զ��屨���ṹ��
	APAPI_DLL_EXPORT CAPOrderField* newAPOrderField();
	/// ʹ���Զ��屨���ṹ��ֱ�ӱ���
	APAPI_DLL_EXPORT CAPOrderField* insertOrder(CAPOrderField* pApOrderField);

	/// ����
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrder(CBaseTrader* pAPTrader, int nOrderID);
	/// �Ա�ĳ���
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByStandardID(CBaseTrader* pAPTrader, const char* szStandardID, const char* szExchangeID = NULL);
	/// �Խ���������
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByExchangeID(CBaseTrader* pAPTrader, const char* szExchangeID);
	/// �������ж���
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderAll(CBaseTrader* pAPTrader);

	/// �������
	APAPI_DLL_EXPORT TAPErrorIDType addTask(CBaseTrader* pAPTrader, TAPEventIDType nEventID, bool bRefuseError = true, int nMaxExecuteCount = 1, TAPTimeAnchorType nExecuteGap = MICROSECONDS_IN_SECOND, TAPTimeAnchorType nExecuteTimeout = MICROSECONDS_IN_SECOND, const char* pContentField = NULL);
	/// ��ѯ�����ʽ�
	APAPI_DLL_EXPORT TAPMoneyType getUsableCash(CBaseTrader* pAPTrader);
	/// ��ѯ����
	APAPI_DLL_EXPORT CAPOrderField* getOrder(CBaseTrader* pAPTrader, int nOrderID = 0);
	/// ��ѯ�ֲ�
	APAPI_DLL_EXPORT CAPPositionField* getPosition(CBaseTrader* pAPTrader, const char* szStandardID = NULL, const char* szExchangeID = NULL);

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