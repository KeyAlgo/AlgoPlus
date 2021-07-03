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

	/// 初始化
	APAPI_DLL_EXPORT CBaseTrader* init(short nRunID, CAPLoginField* pLoginField, FAPOrderEventCallbackType pOrderEventCallback = NULL, FAPFlexibleEventCallbackType pFlexibleEventCallback = NULL, FAPLoopEventCallbackType pLoopEventCallback = NULL, FAPSnapDataEventCallbackType pSnapDataEventCallback = NULL, FAPDetailDataEventCallbackType pDetailDataEventCallback = NULL);
	/// 查询初始化错误
	APAPI_DLL_EXPORT TAPErrorIDType getInitError();
	/// 轮询
	APAPI_DLL_EXPORT void loop();

	/// 设置运行模式。默认Debug模式：将事件相关结构体转为字符串，调用EventTextProcessor处理。
	APAPI_DLL_EXPORT TAPErrorIDType setRunMode(TAPRunModeType chRunMode);
	/// 设置处理事件字符串的方法。默认输出到屏幕。
	APAPI_DLL_EXPORT TAPErrorIDType setEventTextProcessor(FAPEventTextProcessorType pTextProcessor);

	/// 设置报单事件回调函数
	APAPI_DLL_EXPORT TAPErrorIDType setOrderEventCallback(CBaseTrader* pAPTrader, TAPEventIDType nOrderEventID, FAPOrderEventCallbackType pOrderEventCallback);
	/// 设置快照行情事件回调函数
	APAPI_DLL_EXPORT TAPErrorIDType setSnapDataEventCallback(CBaseTrader* pAPTrader, TAPEventIDType nSnapDataEventID, FAPSnapDataEventCallbackType pSnapDataEventCallback);
	/// 设置Level2明细行情事件回调函数
	APAPI_DLL_EXPORT TAPErrorIDType setDetailDataEventCallback(CBaseTrader* pAPTrader, TAPEventIDType nDetailDataEventID, FAPDetailDataEventCallbackType pDetailDataEventCallback);

	///// 设置单笔最大报单量
	//APAPI_DLL_EXPORT TAPErrorIDType setMaxOrderVolume(const char* szStandardID, int nMaxVolume, const char* szExchangeID = NULL);
	///// 设置保证金比例
	//APAPI_DLL_EXPORT TAPErrorIDType setMarginRate(const char* szStandardID, double dMarginRate, const char* szExchangeID = NULL);
	///// 设置手续费率
	//APAPI_DLL_EXPORT TAPErrorIDType setTurnoverFeeRate(const char* szStandardID, double dFeeRate, const char* szExchangeID = NULL);
	///// 设置单位固定手续费
	//APAPI_DLL_EXPORT TAPErrorIDType setVolumeConstFee(const char* szStandardID, double dConstFee, const char* szExchangeID = NULL);

	/// 订阅行情
	APAPI_DLL_EXPORT TAPErrorIDType subscribeOne(CBaseTrader* pAPTrader, const char* szStandardID, const char* szExchangeID = NULL, char chMarketDataType = ENUM_MarketDataType_Snap);
	/// 批量订阅行情
	APAPI_DLL_EXPORT TAPErrorIDType subscribe(CBaseTrader* pAPTrader, char** ppStandardID, int nCount, const char* szExchangeID = NULL, char chMarketDataType = ENUM_MarketDataType_Snap);
	/// 退订行情
	APAPI_DLL_EXPORT TAPErrorIDType unsubscribeOne(CBaseTrader* pAPTrader, const char* szStandardID, const char* szExchangeID = NULL, char chMarketDataType = ENUM_MarketDataType_Snap);
	/// 批量退订行情
	APAPI_DLL_EXPORT TAPErrorIDType unsubscribe(CBaseTrader* pAPTrader, char** ppStandardID, int nCount, const char* szExchangeID = NULL, char chMarketDataType = ENUM_MarketDataType_Snap);

	/// 买开数量
	APAPI_DLL_EXPORT CAPOrderField* buyOpen(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chDirection = ENUM_Direction_Buy);
	/// 卖平数量
	APAPI_DLL_EXPORT CAPOrderField* sellClose(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chDirection = ENUM_Direction_Sell, char chOffsetFlag = '\0', const char* szCreditDebitID = NULL);
	/// 卖开数量
	APAPI_DLL_EXPORT CAPOrderField* sellOpen(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chDirection = '\0', char chCreditQuotaType = '\0');
	/// 买平数量
	APAPI_DLL_EXPORT CAPOrderField* buyClose(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chDirection = '\0', char chOffsetFlag = '\0', const char* szCreditDebitID = NULL);
	/// 买数量
	APAPI_DLL_EXPORT CAPOrderField* buy(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// 买金额
	APAPI_DLL_EXPORT CAPOrderField* buyAmount(CBaseTrader* pAPTrader, const char* szStandardID, double dAmount, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// 买比例
	APAPI_DLL_EXPORT CAPOrderField* buyRatio(CBaseTrader* pAPTrader, const char* szStandardID, double dRatio, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// 卖数量
	APAPI_DLL_EXPORT CAPOrderField* sell(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// 卖金额
	APAPI_DLL_EXPORT CAPOrderField* sellAmount(CBaseTrader* pAPTrader, const char* szStandardID, double dAmount, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// 卖比例
	APAPI_DLL_EXPORT CAPOrderField* sellRatio(CBaseTrader* pAPTrader, const char* szStandardID, double dRatio, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, char chSmartOrderFlag = '\0');
	/// 清仓多头
	APAPI_DLL_EXPORT CAPOrderField* closeLong(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, bool bTodayFirst = false);
	/// 清仓空头
	APAPI_DLL_EXPORT CAPOrderField* closeShort(CBaseTrader* pAPTrader, const char* szStandardID, int nOrderVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL, bool bTodayFirst = false);
	/// 交易至多头目标数量
	APAPI_DLL_EXPORT CAPOrderField* balanceToLongValue(CBaseTrader* pAPTrader, const char* szStandardID, double dTargetValue, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 交易至多头目标金额
	APAPI_DLL_EXPORT CAPOrderField* balanceToLongVolume(CBaseTrader* pAPTrader, const char* szStandardID, int nTargetVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 交易至空头目标数量
	APAPI_DLL_EXPORT CAPOrderField* balanceToShortValue(CBaseTrader* pAPTrader, const char* szStandardID, double dTargetValue, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);
	/// 交易至空头目标金额
	APAPI_DLL_EXPORT CAPOrderField* balanceToShortVolume(CBaseTrader* pAPTrader, const char* szStandardID, int nTargetVolume, char chOrderType, double dOrderPrice, short nOrderMark = 0, const char* szExchangeID = NULL);

	/// 撤单
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrder(CBaseTrader* pAPTrader, const char* szExchangeID, const char* szStandardID, const char* szOrderSysID, int nOrderID, int nFrontID = 0, int nSessionID = 0);
	/// 撤单
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByOrderID(CBaseTrader* pAPTrader, int nOrderID);
	/// 以标的撤单
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByStandardID(CBaseTrader* pAPTrader, const char* szStandardID, const char* szExchangeID = NULL);
	/// 以交易所撤单
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderByExchangeID(CBaseTrader* pAPTrader, const char* szExchangeID);
	/// 撤销所有订单
	APAPI_DLL_EXPORT TAPErrorIDType cancelOrderAll(CBaseTrader* pAPTrader);

	/// 查询可用资金
	APAPI_DLL_EXPORT TAPMoneyType getUsableCash(CBaseTrader* pAPTrader);
	/// 查询订单
	APAPI_DLL_EXPORT CAPOrderField* getOrder(CBaseTrader* pAPTrader, int nOrderID = 0);
	/// 查询持仓
	APAPI_DLL_EXPORT CAPPositionField* getPosition(CBaseTrader* pAPTrader, const char* szStandardID = NULL, const char* szExchangeID = NULL);

	/// 划转资金
	APAPI_DLL_EXPORT CAPTransferAssetField* transferCash(CBaseTrader* pAPTrader, char chTransferDirection, double dAmount, const char* szAccountPassword, const char* szBankID, const char* szBankPassword, const char* szNodeID = NULL, const char* szCreditDebtID = NULL);
	/// 划转持仓
	APAPI_DLL_EXPORT CAPTransferAssetField* transferPosition(CBaseTrader* pAPTrader, char chTransferDirection, int nVolume, const char* szStandardID, const char* szNodeID = NULL, const char* szCreditDebtID = NULL, const char* szExchangeID = NULL);
	/// 查询银行卡余额
	APAPI_DLL_EXPORT TAPErrorIDType queryBankAccountCash(CBaseTrader* pAPTrader, const char* szAccountPassword, const char* szBankID, const char* szBankPassword);
	/// 修改密码
	APAPI_DLL_EXPORT TAPErrorIDType updatePassword(CBaseTrader* pAPTrader, char chPasswordFlag, const char* szOldPassword, const char* szNewPassword);

	/// 添加任务
	APAPI_DLL_EXPORT TAPErrorIDType addTask(CBaseTrader* pAPTrader, TAPEventIDType nEventID, CAPQueryCommandField* pQueryCommandField = NULL, int nMaxExecuteCount = 1, TAPTimeAnchorType nExecuteGap = -1, bool bRefuseError = false, TAPTimeAnchorType nExecuteTimeout = -1);

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
