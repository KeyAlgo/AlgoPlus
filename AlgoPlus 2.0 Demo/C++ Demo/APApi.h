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

	/// 初始化
	APAPI_DLL_EXPORT CBaseTrader* init(short nRunID, CAPLoginField* pLoginField, FAPOnMarketDataFunctionType pMarketDataCallback, FAPOnOrderFunctionType pOrderCallback, FAPOnEventFunctionType pEventCallback, FAPOnLoopFunctionType pLoopCallback = NULL);
	/// 查询初始化错误
	APAPI_DLL_EXPORT TAPErrorIDType getInitError();
	/// 轮询
	APAPI_DLL_EXPORT void loop();

	/// 订阅行情
	APAPI_DLL_EXPORT TAPErrorIDType subscribe(CBaseTrader* pAPTrader, char** ppStandardID, int nCount, const char* szExchangeID = NULL);
	/// 退订行情
	APAPI_DLL_EXPORT TAPErrorIDType unsubscribe(CBaseTrader* pAPTrader, char** ppStandardID, int nCount, const char* szExchangeID = NULL);

	/// 买数量
	APAPI_DLL_EXPORT CAPOrderField* buy(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 买金额
	APAPI_DLL_EXPORT CAPOrderField* buyAmount(CBaseTrader* pAPTrader, const char* szStandardID, double dAmount, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 买比例
	APAPI_DLL_EXPORT CAPOrderField* buyRatio(CBaseTrader* pAPTrader, const char* szStandardID, double dRatio, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 卖数量
	APAPI_DLL_EXPORT CAPOrderField* sell(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 卖金额
	APAPI_DLL_EXPORT CAPOrderField* sellAmount(CBaseTrader* pAPTrader, const char* szStandardID, double dAmount, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 卖比例
	APAPI_DLL_EXPORT CAPOrderField* sellRatio(CBaseTrader* pAPTrader, const char* szStandardID, double dRatio, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 买开数量
	APAPI_DLL_EXPORT CAPOrderField* buyOpen(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 卖平数量
	APAPI_DLL_EXPORT CAPOrderField* sellClose(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 卖平数量
	APAPI_DLL_EXPORT CAPOrderField* sellCloseTodayFirst(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 卖开数量
	APAPI_DLL_EXPORT CAPOrderField* sellOpen(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 买平数量
	APAPI_DLL_EXPORT CAPOrderField* buyClose(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 买平数量
	APAPI_DLL_EXPORT CAPOrderField* buyCloseTodayFirst(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 清仓多头
	APAPI_DLL_EXPORT CAPOrderField* closeLong(CBaseTrader* pAPTrader, const char* szStandardID, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 清仓空头
	APAPI_DLL_EXPORT CAPOrderField* closeShort(CBaseTrader* pAPTrader, const char* szStandardID, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 交易至多头目标数量
	APAPI_DLL_EXPORT CAPOrderField* balanceToLongValue(CBaseTrader* pAPTrader, const char* szStandardID, double dTargetValue, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 交易至多头目标金额
	APAPI_DLL_EXPORT CAPOrderField* balanceToLongVolume(CBaseTrader* pAPTrader, const char* szStandardID, int nTargetVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 交易至空头目标数量
	APAPI_DLL_EXPORT CAPOrderField* balanceToShortValue(CBaseTrader* pAPTrader, const char* szStandardID, double dTargetValue, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 交易至空头目标金额
	APAPI_DLL_EXPORT CAPOrderField* balanceToShortVolume(CBaseTrader* pAPTrader, const char* szStandardID, int nTargetVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);

	/// 创建自定义报单结构体
	APAPI_DLL_EXPORT CAPOrderField* newAPOrderField();
	/// 使用自定义报单结构体直接报单
	APAPI_DLL_EXPORT CAPOrderField* insertOrder(CAPOrderField* pApOrderField);

	/// 撤单
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrder(CBaseTrader* pAPTrader, int nOrderID);
	/// 以标的撤单
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByStandardID(CBaseTrader* pAPTrader, const char* szStandardID, const char* szExchangeID = NULL);
	/// 以交易所撤单
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByExchangeID(CBaseTrader* pAPTrader, const char* szExchangeID);
	/// 撤销所有订单
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderAll(CBaseTrader* pAPTrader);

	/// 添加任务
	APAPI_DLL_EXPORT TAPErrorIDType addTask(CBaseTrader* pAPTrader, TAPEventIDType nEventID, bool bRefuseError = true, int nMaxExecuteCount = 1, TAPTimeAnchorType nExecuteGap = MICROSECONDS_IN_SECOND, TAPTimeAnchorType nExecuteTimeout = MICROSECONDS_IN_SECOND, const char* pContentField = NULL);
	/// 查询可用资金
	APAPI_DLL_EXPORT TAPMoneyType getUsableCash(CBaseTrader* pAPTrader);
	/// 查询订单
	APAPI_DLL_EXPORT CAPOrderField* getOrder(CBaseTrader* pAPTrader, int nOrderID = 0);
	/// 查询持仓
	APAPI_DLL_EXPORT CAPPositionField* getPosition(CBaseTrader* pAPTrader, const char* szStandardID = NULL, const char* szExchangeID = NULL);

	/// 设置时间锚
	APAPI_DLL_EXPORT TAPTimeAnchorType setTimeAnchor();
	/// 计算时间差
	APAPI_DLL_EXPORT TAPTimeAnchorType getTimeElapse(TAPTimeAnchorType nTimeAnchor = 0);

	/// 退出
	APAPI_DLL_EXPORT void exitX(CBaseTrader* pAPTrader = NULL);

#ifdef __cplusplus
}
#endif

#endif