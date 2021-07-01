#ifndef AP_EVENTTYPE_H__
#define AP_EVENTTYPE_H__

/////////////////////////////////////////////////////////////////////////
/// TAPEventIDType是一个事件ID类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPEventIDType;

////////////////////////////////////////////////////////////////////////
/// API状态事件
////////////////////////////////////////////////////////////////////////
/// 新交易日事件
#define ENUM_EventID_DayRolling 10001
/// 初始化完成事件
#define ENUM_EventID_Ready 10002

////////////////////////////////////////////////////////////////////////
/// 订单事件
////////////////////////////////////////////////////////////////////////
/// 订单事件，成交
#define ENUM_OrderEventID_Traded 10003
/// 订单事件，撤单
#define ENUM_OrderEventID_Canceled 10004
/// 订单事件，更新成本
#define ENUM_OrderEventID_UpdateCost 10005
/// 订单事件，排队
#define ENUM_OrderEventID_Accepted 10006
/// 订单事件，报单失败
#define ENUM_OrderEventID_InsertRejected 10007
/// 订单事件，撤单失败
#define ENUM_OrderEventID_CancelRejected 10008
/// 订单事件，预埋
#define ENUM_OrderEventID_Cached 10009

////////////////////////////////////////////////////////////////////////
/// 行情事件
////////////////////////////////////////////////////////////////////////
/// 行情事件，切片行情
#define ENUM_SnapDataEventID_MarketData 10010
/// 行情事件，Level2指数行情
#define ENUM_SnapDataEventID_IndexData 10011
/// 行情事件，Level2逐笔成交
#define ENUM_DetailDataEventID_DetailTransaction 10012
/// 行情事件，Level2逐笔委托
#define ENUM_DetailDataEventID_DetailOrder 10013
/// 行情事件，Level2重传逐笔成交
#define ENUM_DetailDataEventID_ResendDetailTransaction 10014
/// 行情事件，Level2重传逐笔委托
#define ENUM_DetailDataEventID_ResendDetailOrder 10015

////////////////////////////////////////////////////////////////////////
/// CTP事件
////////////////////////////////////////////////////////////////////////
#define ENUM_CTPEventID_CreateApiInstance 11001
#define ENUM_CTPEventID_TraderDisconnected 11002
#define ENUM_CTPEventID_MdDisconnected 11003
#define ENUM_CTPEventID_InstrumentStatus 11004
#define ENUM_CTPEventID_TradingNotice 11005
#define ENUM_CTPEventID_Bulletin 11006
#define ENUM_CTPEventID_SubscribeMarketData 11007
#define ENUM_CTPEventID_UnsubscribeMarketData 11008
#define ENUM_CTPEventID_UpdateUserPassword 11009
#define ENUM_CTPEventID_UpdateTradingAccountPassword 11010
#define ENUM_CTPEventID_TransferCash 11011
///
#define ENUM_CTPTaskID_LoginTrader 11101
#define ENUM_CTPTaskID_LoginMd 11102
#define ENUM_CTPTaskID_Authenticate 11103
#define ENUM_CTPTaskID_ConfirmSettlementInfo 11104
///
#define ENUM_CTPTaskID_QrySettlementInfo 11201
#define ENUM_CTPTaskID_QryOrder 11202
#define ENUM_CTPTaskID_QryInstrumentOrderCommRate 11203
#define ENUM_CTPTaskID_QryTrade 11204
#define ENUM_CTPTaskID_QryPosition 11205
#define ENUM_CTPTaskID_QryInvestorPositionDetail 11206
#define ENUM_CTPTaskID_QryTradingAccount 11207
#define ENUM_CTPTaskID_QryBankAccountCash 11208
#define ENUM_CTPTaskID_QryTransferCashDetail 11209
///
#define ENUM_CTPTaskID_QryExerciseOrder 11210
#define ENUM_CTPTaskID_QryForQuote 11211
#define ENUM_CTPTaskID_QryQuote 11212
#define ENUM_CTPTaskID_QryOptionSelfClose 11213
#define ENUM_CTPTaskID_QryParkedOrder 11214
#define ENUM_CTPTaskID_QryParkedOrderAction 11215
#define ENUM_CTPTaskID_QryCombAction 11216
#define ENUM_CTPTaskID_QryInvestorPositionCombineDetail 11217
///
#define ENUM_CTPTaskID_QryInvestor 11301
#define ENUM_CTPTaskID_QryTradingCode 11302
#define ENUM_CTPTaskID_QryCFMMCTradingAccountKey 11303
#define ENUM_CTPTaskID_QryCFMMCTradingAccountToken 11304
#define ENUM_CTPTaskID_QryAccountRegister 11305
#define ENUM_CTPTaskID_QryContractBank 11306
#define ENUM_CTPTaskID_QryMaxOrderVolume 11307
#define ENUM_CTPTaskID_QryTransferBank 11308
#define ENUM_CTPTaskID_QryOptionInstrTradeCost 11309
#define ENUM_CTPTaskID_QryInstrumentMarginRate 11310
#define ENUM_CTPTaskID_QryInvestorProductGroupMargin 11311
#define ENUM_CTPTaskID_QryInstrumentCommissionRate 11312
#define ENUM_CTPTaskID_QryOptionInstrCommRate 11313
#define ENUM_CTPTaskID_QryMMInstrumentCommissionRate 11314
#define ENUM_CTPTaskID_QryMMOptionInstrCommRate 11315
#define ENUM_CTPTaskID_QrySettlementInfoConfirm 11316
#define ENUM_CTPTaskID_QryTradingNotice 11317
///
#define ENUM_CTPTaskID_QrySecAgentACIDMap 11318
#define ENUM_CTPTaskID_QrySecAgentTradingAccount 11319
#define ENUM_CTPTaskID_QrySecAgentCheckMode 11320
#define ENUM_CTPTaskID_QrySecAgentTradeInfo 11321
#define ENUM_CTPTaskID_QryBrokerTradingParams 11322
#define ENUM_CTPTaskID_QryBrokerTradingAlgos 11323
///
#define ENUM_CTPTaskID_QryMarketData 11401
#define ENUM_CTPTaskID_QryInstrument 11402
#define ENUM_CTPTaskID_QryCombInstrumentGuard 11403
#define ENUM_CTPTaskID_QryProduct 11404
#define ENUM_CTPTaskID_QryProductGroup 11405
#define ENUM_CTPTaskID_QryExchange 11406
#define ENUM_CTPTaskID_QryExchangeMarginRate 11407
#define ENUM_CTPTaskID_QryExchangeMarginRateAdjust 11408
#define ENUM_CTPTaskID_QryNotice 11409
#define ENUM_CTPTaskID_QryEWarrantOffset 11410
#define ENUM_CTPTaskID_QryExchangeRate 11411
#define ENUM_CTPTaskID_QryProductExchRate 11412

////////////////////////////////////////////////////////////////////////
/// TORAStock事件
////////////////////////////////////////////////////////////////////////
///
#define ENUM_TORAStockEventID_CreateApiInstance 12001
#define ENUM_TORAStockEventID_Disconnected 12002
#define ENUM_TORAStockEventID_MarketStatus 12003
#define ENUM_TORAStockEventID_TradingNotice 12004
#define ENUM_TORAStockEventID_SubscribeMarketData 12005
#define ENUM_TORAStockEventID_UnsubscribeMarketData 12006
#define ENUM_TORAStockEventID_UpdateUserPassword 12007
#define ENUM_TORAStockEventID_TransferCash 12008
#define ENUM_TORAStockEventID_TransferPosition 12009
#define ENUM_TORAStockEventID_PeripheryTransferCash 12010
#define ENUM_TORAStockEventID_PeripheryTransferPosition 12011
///
#define ENUM_TORAStockTaskID_LoginTrader 12102
#define ENUM_TORAStockTaskID_LoginMd 12101
///
#define ENUM_TORAStockTaskID_QryOrder 12201
#define ENUM_TORAStockTaskID_QryOrderFundDetail 12202
#define ENUM_TORAStockTaskID_QryPrematurityRepoOrder 12203
#define ENUM_TORAStockTaskID_QryTrade 12204
#define ENUM_TORAStockTaskID_QryTradeConcentration 12205
#define ENUM_TORAStockTaskID_QryPosition 12206
#define ENUM_TORAStockTaskID_QryPledgePosition 12207
#define ENUM_TORAStockTaskID_QryStandardBondPosition 12208
#define ENUM_TORAStockTaskID_QryTradingAccount 12209
#define ENUM_TORAStockTaskID_QryJZCash 12210
#define ENUM_TORAStockTaskID_QryBankAccountCash 12211
#define ENUM_TORAStockTaskID_QryTransferCashDetail 12212
#define ENUM_TORAStockTaskID_QryTransferPositionDetail 12213
#define ENUM_TORAStockTaskID_QryPeripheryTransferCashDetail 12214
#define ENUM_TORAStockTaskID_QryPeripheryTransferPositionDetail 12215
///
#define ENUM_TORAStockTaskID_QryUser 12301
#define ENUM_TORAStockTaskID_QryBUProxy 12302
#define ENUM_TORAStockTaskID_QryInvestor 12303
#define ENUM_TORAStockTaskID_QryShareholderAccount 12304
#define ENUM_TORAStockTaskID_QryShareholderParam 12305
#define ENUM_TORAStockTaskID_QryShareholderSpecPrivilege 12306
#define ENUM_TORAStockTaskID_QryIPOQuota 12307
#define ENUM_TORAStockTaskID_QryIPONumberResult 12308
#define ENUM_TORAStockTaskID_QryIPOMatchNumberResult 12309
#define ENUM_TORAStockTaskID_QryMaxOrderVolume 12310
#define ENUM_TORAStockTaskID_QryInvestorPositionLimit 12311
#define ENUM_TORAStockTaskID_QryInvestorCondOrderLimitParam 12312
#define ENUM_TORAStockTaskID_QryInvestorTradingFee 12313
#define ENUM_TORAStockTaskID_QryTradingFee 12314
#define ENUM_TORAStockTaskID_QryTradingNotice 12315
#define ENUM_TORAStockTaskID_QryNodeFundAssignment 12316
#define ENUM_TORAStockTaskID_QryConnectionInfo 12317
///
#define ENUM_TORAStockTaskID_QryMarketData 12401
#define ENUM_TORAStockTaskID_QryPHMarketData 12402
#define ENUM_TORAStockTaskID_QrySecurity 12403
#define ENUM_TORAStockTaskID_QryIPOInfo 12404
#define ENUM_TORAStockTaskID_QryRationalInfo 12405
#define ENUM_TORAStockTaskID_QryPledgeInfo 12406
#define ENUM_TORAStockTaskID_QryBondConversionInfo 12407
#define ENUM_TORAStockTaskID_QryBondPutbackInfo 12408
#define ENUM_TORAStockTaskID_QryETFFile 12409
#define ENUM_TORAStockTaskID_QryETFBasket 12410
#define ENUM_TORAStockTaskID_QryLofFundInfo 12411
#define ENUM_TORAStockTaskID_QrySZSEImcParams 12412
#define ENUM_TORAStockTaskID_QrySZSEImcExchangeRate 12413
#define ENUM_TORAStockTaskID_QrySZSEHKPriceTickInfo 12414
#define ENUM_TORAStockTaskID_QryMarket 12415
#define ENUM_TORAStockTaskID_QryExchange 12416
#define ENUM_TORAStockTaskID_QrySystemNodeInfo 12417

////////////////////////////////////////////////////////////////////////
/// TORACredit事件
////////////////////////////////////////////////////////////////////////
///
#define ENUM_TORACreditEventID_CreateApiInstance 13001
#define ENUM_TORACreditEventID_Disconnected 13002
#define ENUM_TORACreditEventID_MarketStatus 13003
#define ENUM_TORACreditEventID_TradingNotice 13004
#define ENUM_TORACreditEventID_SubscribeMarketData 13005
#define ENUM_TORACreditEventID_UnsubscribeMarketData 13006
#define ENUM_TORACreditEventID_UpdateUserPassword 13007
#define ENUM_TORACreditEventID_TransferCash 13008
#define ENUM_TORACreditEventID_TransferPosition 13009
///
#define ENUM_TORACreditTaskID_LoginTrader 13101
#define ENUM_TORACreditTaskID_LoginMd 13102
///
#define ENUM_TORACreditTaskID_QryOrder 13201
#define ENUM_TORACreditTaskID_QryOrderFundDetail 13202
#define ENUM_TORACreditTaskID_QryTrade 13203
#define ENUM_TORACreditTaskID_QryPosition 13204
#define ENUM_TORACreditTaskID_QryStockPosition 13205
#define ENUM_TORACreditTaskID_QrySurplusPosition 13206
#define ENUM_TORACreditTaskID_QryTradingAccount 13207
#define ENUM_TORACreditTaskID_QryInvestorCreditInfo 13208
#define ENUM_TORACreditTaskID_QryJZCash 13209
#define ENUM_TORACreditTaskID_QryBankAccountCash 13210
#define ENUM_TORACreditTaskID_QryCreditDebt 13211
#define ENUM_TORACreditTaskID_QryCreditRepayment 13212
#define ENUM_TORACreditTaskID_QryTransferCashDetail 13213
#define ENUM_TORACreditTaskID_QryTransferPositionDetail 13214
#define ENUM_TORACreditTaskID_QryPeripheryTransferCashDetail 13215
#define ENUM_TORACreditTaskID_QryPeripheryTransferPositionDetail 13216
#define ENUM_TORACreditTaskID_QryTransferCredit 13217
#define ENUM_TORACreditTaskID_QryDebtExtend 13218
#define ENUM_TORACreditTaskID_QryInvestorRealTimeCreditInfo 13219
#define ENUM_TORACreditTaskID_QrySecurityCirculateAssetInfo 13220
///
#define ENUM_TORACreditTaskID_QryUser 13301
#define ENUM_TORACreditTaskID_QryBUProxy 13302
#define ENUM_TORACreditTaskID_QryInvestor 13303
#define ENUM_TORACreditTaskID_QryShareholderAccount 13304
#define ENUM_TORACreditTaskID_QryShareholderSpecPrivilege 13305
#define ENUM_TORACreditTaskID_QryShareholderSecurityBlackList 13306
#define ENUM_TORACreditTaskID_QryWhiteListSecurityCtrl 13307
#define ENUM_TORACreditTaskID_QryCreditFundQuota 13308
#define ENUM_TORACreditTaskID_QryCreditPositionQuota 13309
#define ENUM_TORACreditTaskID_QryIPOQuota 13310
#define ENUM_TORACreditTaskID_QryIPONumberResult 13311
#define ENUM_TORACreditTaskID_QryIPOMatchNumberResult 13312
#define ENUM_TORACreditTaskID_QryInvestorBusinessScaleConcentrationParam 13313
#define ENUM_TORACreditTaskID_QryMaxOrderVolume 13314
#define ENUM_TORACreditTaskID_QryInvestorCondOrderLimitParam 13315
#define ENUM_TORACreditTaskID_QryInvestorTradingFee 13316
#define ENUM_TORACreditTaskID_QryTradingFee 13317
#define ENUM_TORACreditTaskID_QryTradingNotice 13318
#define ENUM_TORACreditTaskID_QryInvestorCreditMarginRate 13319
#define ENUM_TORACreditTaskID_QryInvestorCreditInterestRate 13320
#define ENUM_TORACreditTaskID_QryInvestorCollateralRiskParam 13321
#define ENUM_TORACreditTaskID_QryInvestorCollateralConversionRate 13322
#define ENUM_TORACreditTaskID_QryInvestorCreditDiscountCoupon 13323
#define ENUM_TORACreditTaskID_QryInvestorCreditBenefitInterestRate 13324
#define ENUM_TORACreditTaskID_QryConnectionInfo 13325
///
#define ENUM_TORACreditTaskID_QryMarketData 13401
#define ENUM_TORACreditTaskID_QrySecurity 13402
#define ENUM_TORACreditTaskID_QrySecurityFairPrice 13403
#define ENUM_TORACreditTaskID_QrySecurityCirculateAssetParam 13404
#define ENUM_TORACreditTaskID_QryIPOInfo 13405
#define ENUM_TORACreditTaskID_QryRationInfo 13406
#define ENUM_TORACreditTaskID_QryBondConversionInfo 13407
#define ENUM_TORACreditTaskID_QryBondPutbackInfo 13408
#define ENUM_TORACreditTaskID_QryBrokerCreditSecurity 13409
#define ENUM_TORACreditTaskID_QryExchange 13410
#define ENUM_TORACreditTaskID_QryCreditPlanInfo 13411
#define ENUM_TORACreditTaskID_QryCreditDiscountCouponInfo 13412
#define ENUM_TORACreditTaskID_QryCreditRatingInfo 13413

////////////////////////////////////////////////////////////////////////
/// TORAOption事件
////////////////////////////////////////////////////////////////////////
#define ENUM_TORAOptionEventID_CreateApiInstance 14001
#define ENUM_TORAOptionEventID_Disconnected 14002
#define ENUM_TORAOptionEventID_MarketStatus 14003
#define ENUM_TORAOptionEventID_TradingNotice 14004
#define ENUM_TORAOptionEventID_SubscribeMarketData 14005
#define ENUM_TORAOptionEventID_UnsubscribeMarketData 14006
#define ENUM_TORAOptionEventID_UpdateUserPassword 14007
#define ENUM_TORAOptionEventID_TransferCash 14008
///
#define ENUM_TORAOptionTaskID_LoginTrader 14101
#define ENUM_TORAOptionTaskID_LoginMd 14102
///
#define ENUM_TORAOptionTaskID_QryOrder 14201
#define ENUM_TORAOptionTaskID_QryOrderFundDetail 14202
#define ENUM_TORAOptionTaskID_QryTrade 14203
#define ENUM_TORAOptionTaskID_QryPosition 14204
#define ENUM_TORAOptionTaskID_QryStockPosition 14205
#define ENUM_TORAOptionTaskID_QryTradingAccount 14206
#define ENUM_TORAOptionTaskID_QryJZCash 14207
#define ENUM_TORAOptionTaskID_QryBankAccountCash 14208
#define ENUM_TORAOptionTaskID_QryTransferCashDetail 14209
#define ENUM_TORAOptionTaskID_QryTransferPositionDetail 14210
#define ENUM_TORAOptionTaskID_QryTransferStockPositionDetail 14211
#define ENUM_TORAOptionTaskID_QryCondOrder 14212
#define ENUM_TORAOptionTaskID_QryCombOrder 14213
#define ENUM_TORAOptionTaskID_QryCombPosition 14214
#define ENUM_TORAOptionTaskID_QryCombPosDetail 14215
#define ENUM_TORAOptionTaskID_QryExercise 14216
#define ENUM_TORAOptionTaskID_QryExerciseAppointment 14217
#define ENUM_TORAOptionTaskID_QryCombExercise 14218
#define ENUM_TORAOptionTaskID_QryLock 14219
#define ENUM_TORAOptionTaskID_QryLockPosition 14220
#define ENUM_TORAOptionTaskID_QryStockDisposal 14221
#define ENUM_TORAOptionTaskID_QryInsufficientCoveredStockPosition 14222
#define ENUM_TORAOptionTaskID_QrySplitCombMarginDifference 14223
///
#define ENUM_TORAOptionTaskID_QryUser 14301
#define ENUM_TORAOptionTaskID_QryBUProxy 14302
#define ENUM_TORAOptionTaskID_QryInvestor 14303
#define ENUM_TORAOptionTaskID_QryShareholderAccount 14304
#define ENUM_TORAOptionTaskID_QryTradingFee 14305
#define ENUM_TORAOptionTaskID_QryInvestorTradingFee 14306
#define ENUM_TORAOptionTaskID_QryInvestorMarginFee 14307
#define ENUM_TORAOptionTaskID_QryTradingNotice 14308
#define ENUM_TORAOptionTaskID_QryInvestorLimitPosition 14309
#define ENUM_TORAOptionTaskID_QryInvestorLimitAmount 14310
///
#define ENUM_TORAOptionTaskID_QryMarketData 14401
#define ENUM_TORAOptionTaskID_QrySecurity 14402
#define ENUM_TORAOptionTaskID_QryCombSecurity 14403
#define ENUM_TORAOptionTaskID_QryExchange 14404

#endif
