#ifndef AP_UTILIIES_H__
#define AP_UTILIIES_H__

#ifdef UTILITIES_EXPORT
#ifdef _WIN32
#define UTILITIES_DLL_EXPORT __declspec(dllexport)
#else
#define UTILITIES_DLL_EXPORT __attribute__ ((visibility("default")))
#endif
#else
#define UTILITIES_DLL_EXPORT
#endif

#include <map>
#include "APStruct.h"
#include "ThostFtdcUserApiStruct.h"

#define EVENTSTRUCT__(eventid) EventCallbackStruct_##eventid
#define EVENTSTRUCT(eventid) EVENTSTRUCT__(eventid)

typedef std::map<std::string, std::string> TAPStructKeyValueMap;

class UTILITIES_DLL_EXPORT CAPPrintHelper
{
public:
	static const char* toText(CAPLoginField* pLoginField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CAPLoginField* pLoginField, int nPrecision = 2);

	static const char* toText(CAPSimpleMarketDataField* pSimpleMarketDataField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CAPSimpleMarketDataField* pSimpleMarketDataField, int nPrecision = 2);

	static const char* toText(CAPMarketDataField* pMarketDataField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CAPMarketDataField* pMarketDataField, int nPrecision = 2);

	static const char* toText(CAPDetailDataField* pDetailDataField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CAPDetailDataField* pDetailDataField, int nPrecision = 2);

	static const char* toText(CAPCreditDebtField* pCreditDebtField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CAPCreditDebtField* pCreditDebtField, int nPrecision = 2);

	static const char* toText(CAPPositionField* pPositionField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CAPPositionField* pPositionField, int nPrecision = 2);

	static const char* toText(CAPOrderField* pOrderField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CAPOrderField* pOrderField, int nPrecision = 2);

	static const char* toText(CAPTransferAssetField* pTransferAssetField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CAPTransferAssetField* pTransferAssetField, int nPrecision = 2);

	static const char* toText(CAPQueryCommandField* pQueryCommandField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CAPQueryCommandField* pQueryCommandField, int nPrecision = 2);

	static const char* toText(CThostFtdcRspUserLoginField* pRspUserLoginField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcRspUserLoginField* pRspUserLoginField, int nPrecision = 2);

	static const char* toText(CThostFtdcRspAuthenticateField* pRspAuthenticateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcRspAuthenticateField* pRspAuthenticateField, int nPrecision = 2);

	static const char* toText(CThostFtdcExchangeField* pExchangeField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcExchangeField* pExchangeField, int nPrecision = 2);

	static const char* toText(CThostFtdcProductField* pProductField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcProductField* pProductField, int nPrecision = 2);

	static const char* toText(CThostFtdcInstrumentField* pInstrumentField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInstrumentField* pInstrumentField, int nPrecision = 2);

	static const char* toText(CThostFtdcInvestorField* pInvestorField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInvestorField* pInvestorField, int nPrecision = 2);

	static const char* toText(CThostFtdcTradingCodeField* pTradingCodeField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcTradingCodeField* pTradingCodeField, int nPrecision = 2);

	static const char* toText(CThostFtdcTradingAccountField* pTradingAccountField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcTradingAccountField* pTradingAccountField, int nPrecision = 2);

	static const char* toText(CThostFtdcInvestorPositionField* pInvestorPositionField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInvestorPositionField* pInvestorPositionField, int nPrecision = 2);

	static const char* toText(CThostFtdcInstrumentMarginRateField* pInstrumentMarginRateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInstrumentMarginRateField* pInstrumentMarginRateField, int nPrecision = 2);

	static const char* toText(CThostFtdcInstrumentCommissionRateField* pInstrumentCommissionRateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInstrumentCommissionRateField* pInstrumentCommissionRateField, int nPrecision = 2);

	static const char* toText(CThostFtdcDepthMarketDataField* pDepthMarketDataField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcDepthMarketDataField* pDepthMarketDataField, int nPrecision = 2);

	static const char* toText(CThostFtdcSettlementInfoField* pSettlementInfoField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcSettlementInfoField* pSettlementInfoField, int nPrecision = 2);

	static const char* toText(CThostFtdcExchangeMarginRateField* pExchangeMarginRateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcExchangeMarginRateField* pExchangeMarginRateField, int nPrecision = 2);

	static const char* toText(CThostFtdcExchangeMarginRateAdjustField* pExchangeMarginRateAdjustField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcExchangeMarginRateAdjustField* pExchangeMarginRateAdjustField, int nPrecision = 2);

	static const char* toText(CThostFtdcExchangeRateField* pExchangeRateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcExchangeRateField* pExchangeRateField, int nPrecision = 2);

	static const char* toText(CThostFtdcUserPasswordUpdateField* pUserPasswordUpdateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcUserPasswordUpdateField* pUserPasswordUpdateField, int nPrecision = 2);

	static const char* toText(CThostFtdcOrderField* pOrderField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcOrderField* pOrderField, int nPrecision = 2);

	static const char* toText(CThostFtdcTradeField* pTradeField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcTradeField* pTradeField, int nPrecision = 2);

	static const char* toText(CThostFtdcSettlementInfoConfirmField* pSettlementInfoConfirmField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcSettlementInfoConfirmField* pSettlementInfoConfirmField, int nPrecision = 2);

	static const char* toText(CThostFtdcOptionInstrCommRateField* pOptionInstrCommRateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcOptionInstrCommRateField* pOptionInstrCommRateField, int nPrecision = 2);

	static const char* toText(CThostFtdcOptionInstrTradeCostField* pOptionInstrTradeCostField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcOptionInstrTradeCostField* pOptionInstrTradeCostField, int nPrecision = 2);

	static const char* toText(CThostFtdcExecOrderField* pExecOrderField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcExecOrderField* pExecOrderField, int nPrecision = 2);

	static const char* toText(CThostFtdcForQuoteField* pForQuoteField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcForQuoteField* pForQuoteField, int nPrecision = 2);

	static const char* toText(CThostFtdcQuoteField* pQuoteField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcQuoteField* pQuoteField, int nPrecision = 2);

	static const char* toText(CThostFtdcCombInstrumentGuardField* pCombInstrumentGuardField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcCombInstrumentGuardField* pCombInstrumentGuardField, int nPrecision = 2);

	static const char* toText(CThostFtdcCombActionField* pCombActionField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcCombActionField* pCombActionField, int nPrecision = 2);

	static const char* toText(CThostFtdcProductExchRateField* pProductExchRateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcProductExchRateField* pProductExchRateField, int nPrecision = 2);

	static const char* toText(CThostFtdcMMOptionInstrCommRateField* pMMOptionInstrCommRateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcMMOptionInstrCommRateField* pMMOptionInstrCommRateField, int nPrecision = 2);

	static const char* toText(CThostFtdcMMInstrumentCommissionRateField* pMMInstrumentCommissionRateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcMMInstrumentCommissionRateField* pMMInstrumentCommissionRateField, int nPrecision = 2);

	static const char* toText(CThostFtdcInstrumentOrderCommRateField* pInstrumentOrderCommRateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInstrumentOrderCommRateField* pInstrumentOrderCommRateField, int nPrecision = 2);

	static const char* toText(CThostFtdcOptionSelfCloseField* pOptionSelfCloseField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcOptionSelfCloseField* pOptionSelfCloseField, int nPrecision = 2);

	static const char* toText(CThostFtdcSecAgentCheckModeField* pSecAgentCheckModeField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcSecAgentCheckModeField* pSecAgentCheckModeField, int nPrecision = 2);

	static const char* toText(CThostFtdcSecAgentTradeInfoField* pSecAgentTradeInfoField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcSecAgentTradeInfoField* pSecAgentTradeInfoField, int nPrecision = 2);

	static const char* toText(CThostFtdcSpecificInstrumentField* pSpecificInstrumentField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcSpecificInstrumentField* pSpecificInstrumentField, int nPrecision = 2);

	static const char* toText(CThostFtdcInstrumentStatusField* pInstrumentStatusField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInstrumentStatusField* pInstrumentStatusField, int nPrecision = 2);

	static const char* toText(CThostFtdcTransferBankField* pTransferBankField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcTransferBankField* pTransferBankField, int nPrecision = 2);

	static const char* toText(CThostFtdcInvestorPositionDetailField* pInvestorPositionDetailField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInvestorPositionDetailField* pInvestorPositionDetailField, int nPrecision = 2);

	static const char* toText(CThostFtdcNoticeField* pNoticeField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcNoticeField* pNoticeField, int nPrecision = 2);

	static const char* toText(CThostFtdcTradingAccountPasswordUpdateField* pTradingAccountPasswordUpdateField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcTradingAccountPasswordUpdateField* pTradingAccountPasswordUpdateField, int nPrecision = 2);

	static const char* toText(CThostFtdcContractBankField* pContractBankField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcContractBankField* pContractBankField, int nPrecision = 2);

	static const char* toText(CThostFtdcInvestorPositionCombineDetailField* pInvestorPositionCombineDetailField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInvestorPositionCombineDetailField* pInvestorPositionCombineDetailField, int nPrecision = 2);

	static const char* toText(CThostFtdcParkedOrderField* pParkedOrderField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcParkedOrderField* pParkedOrderField, int nPrecision = 2);

	static const char* toText(CThostFtdcParkedOrderActionField* pParkedOrderActionField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcParkedOrderActionField* pParkedOrderActionField, int nPrecision = 2);

	static const char* toText(CThostFtdcTradingNoticeInfoField* pTradingNoticeInfoField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcTradingNoticeInfoField* pTradingNoticeInfoField, int nPrecision = 2);

	static const char* toText(CThostFtdcTradingNoticeField* pTradingNoticeField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcTradingNoticeField* pTradingNoticeField, int nPrecision = 2);

	static const char* toText(CThostFtdcBrokerTradingParamsField* pBrokerTradingParamsField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcBrokerTradingParamsField* pBrokerTradingParamsField, int nPrecision = 2);

	static const char* toText(CThostFtdcBrokerTradingAlgosField* pBrokerTradingAlgosField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcBrokerTradingAlgosField* pBrokerTradingAlgosField, int nPrecision = 2);

	static const char* toText(CThostFtdcCFMMCTradingAccountKeyField* pCFMMCTradingAccountKeyField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcCFMMCTradingAccountKeyField* pCFMMCTradingAccountKeyField, int nPrecision = 2);

	static const char* toText(CThostFtdcEWarrantOffsetField* pEWarrantOffsetField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcEWarrantOffsetField* pEWarrantOffsetField, int nPrecision = 2);

	static const char* toText(CThostFtdcInvestorProductGroupMarginField* pInvestorProductGroupMarginField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcInvestorProductGroupMarginField* pInvestorProductGroupMarginField, int nPrecision = 2);

	static const char* toText(CThostFtdcCFMMCTradingAccountTokenField* pCFMMCTradingAccountTokenField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcCFMMCTradingAccountTokenField* pCFMMCTradingAccountTokenField, int nPrecision = 2);

	static const char* toText(CThostFtdcProductGroupField* pProductGroupField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcProductGroupField* pProductGroupField, int nPrecision = 2);

	static const char* toText(CThostFtdcBulletinField* pBulletinField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcBulletinField* pBulletinField, int nPrecision = 2);

	static const char* toText(CThostFtdcRspTransferField* pRspTransferField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcRspTransferField* pRspTransferField, int nPrecision = 2);

	static const char* toText(CThostFtdcNotifyQueryAccountField* pNotifyQueryAccountField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcNotifyQueryAccountField* pNotifyQueryAccountField, int nPrecision = 2);

	static const char* toText(CThostFtdcTransferSerialField* pTransferSerialField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcTransferSerialField* pTransferSerialField, int nPrecision = 2);

	static const char* toText(CThostFtdcAccountregisterField* pAccountregisterField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcAccountregisterField* pAccountregisterField, int nPrecision = 2);

	static const char* toText(CThostFtdcSecAgentACIDMapField* pSecAgentACIDMapField, bool bWithFieldName = false, std::string strSeparator = " || ", int nPrecision = 2);

	static void toMap(TAPStructKeyValueMap& mStructKeyValueMap, CThostFtdcSecAgentACIDMapField* pSecAgentACIDMapField, int nPrecision = 2);

};

#endif
