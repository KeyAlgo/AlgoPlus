# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus


#///正常
ExchangeProperty_Normal = b'0'
#///根据成交生成报单
ExchangeProperty_GenOrderByTrade = b'1'
#///组织机构代码
IdCardType_EID = b'0'
#///中国公民身份证
IdCardType_IDCard = b'1'
#///军官证
IdCardType_OfficerIDCard = b'2'
#///警官证
IdCardType_PoliceIDCard = b'3'
#///士兵证
IdCardType_SoldierIDCard = b'4'
#///户口簿
IdCardType_HouseholdRegister =  b'5'
#///护照
IdCardType_Passport = b'6'
#///台胞证
IdCardType_TaiwanCompatriotIDCard = b'7'
#///回乡证
IdCardType_HomeComingCard = b'8'
#///营业执照号
IdCardType_LicenseNo = b'9'
#///税务登记号/当地纳税ID
IdCardType_TaxNo = b'A'
#///港澳居民来往内地通行证
IdCardType_HMMainlandTravelPermit = b'B'
#///台湾居民来往大陆通行证
IdCardType_TwMainlandTravelPermit = b'C'
#///驾照
IdCardType_DrivingLicense = b'D'
#///当地社保ID
IdCardType_SocialID = b'F'
#///当地身份证
IdCardType_LocalID = b'G'
#///商业登记证
IdCardType_BusinessRegistration = b'H'
#///港澳永久性居民身份证
IdCardType_HKMCIDCard = b'I'
#///人行开户许可证
IdCardType_AccountsPermits = b'J'
#///外国人永久居留证
IdCardType_FrgPrmtRdCard = b'K'
#///资管产品备案函
IdCardType_CptMngPrdLetter = b'L'
#///其他证件
IdCardType_OtherCard = b'x'
#///所有
InvestorRange_All = b'1'
#///投资者组
InvestorRange_Group = b'2'
#///单一投资者
InvestorRange_Single = b'3'
#///所有
DepartmentRange_All = b'1'
#///组织架构
DepartmentRange_Group = b'2'
#///单一投资者
DepartmentRange_Single = b'3'
#///未同步
DataSyncStatus_Asynchronous = b'1'
#///同步中
DataSyncStatus_Synchronizing = b'2'
#///已同步
DataSyncStatus_Synchronized = b'3'
#///已同步
BrokerDataSyncStatus_Synchronized = b'1'
#///同步中
BrokerDataSyncStatus_Synchronizing = b'2'
#///没有任何连接
ExchangeConnectStatus_NoConnection = b'1'
#///已经发出合约查询请求
ExchangeConnectStatus_QryInstrumentSent = b'2'
#///已经获取信息
ExchangeConnectStatus_GotInformation = b'9'
#///没有任何连接
TraderConnectStatus_NotConnected = b'1'
#///已经连接
TraderConnectStatus_Connected = b'2'
#///已经发出合约查询请求
TraderConnectStatus_QryInstrumentSent = b'3'
#///订阅私有流
TraderConnectStatus_SubPrivateFlow = b'4'
#///数据异步化
FunctionCode_DataAsync = b'1'
#///强制用户登出
FunctionCode_ForceUserLogout = b'2'
#///变更管理用户口令
FunctionCode_UserPasswordUpdate = b'3'
#///变更经纪公司口令
FunctionCode_BrokerPasswordUpdate = b'4'
#///变更投资者口令
FunctionCode_InvestorPasswordUpdate = b'5'
#///报单插入
FunctionCode_OrderInsert = b'6'
#///报单操作
FunctionCode_OrderAction = b'7'
#///同步系统数据
FunctionCode_SyncSystemData = b'8'
#///同步经纪公司数据
FunctionCode_SyncBrokerData = b'9'
#///批量同步经纪公司数据
FunctionCode_BachSyncBrokerData = b'A'
#///超级查询
FunctionCode_SuperQuery = b'B'
#///预埋报单插入
FunctionCode_ParkedOrderInsert = b'C'
#///预埋报单操作
FunctionCode_ParkedOrderAction = b'D'
#///同步动态令牌
FunctionCode_SyncOTP = b'E'
#///删除未知单
FunctionCode_DeleteOrder = b'F'
#///强制用户登出
BrokerFunctionCode_ForceUserLogout = b'1'
#///变更用户口令
BrokerFunctionCode_UserPasswordUpdate = b'2'
#///同步经纪公司数据
BrokerFunctionCode_SyncBrokerData = b'3'
#///批量同步经纪公司数据
BrokerFunctionCode_BachSyncBrokerData = b'4'
#///报单插入
BrokerFunctionCode_OrderInsert = b'5'
#///报单操作
BrokerFunctionCode_OrderAction = b'6'
#///全部查询
BrokerFunctionCode_AllQuery = b'7'
#///系统功能：登入/登出/修改密码等
BrokerFunctionCode_log = b'a'
#///基本查询：查询基础数据，如合约，交易所等常量
BrokerFunctionCode_BaseQry = b'b'
#///交易查询：如查成交，委托
BrokerFunctionCode_TradeQry = b'c'
#///交易功能：报单，撤单
BrokerFunctionCode_Trade = b'd'
#///银期转账
BrokerFunctionCode_Virement = b'e'
#///风险监控
BrokerFunctionCode_Risk = b'f'
#///查询/管理：查询会话，踢人等
BrokerFunctionCode_Session = b'g'
#///风控通知控制
BrokerFunctionCode_RiskNoticeCtl = b'h'
#///风控通知发送
BrokerFunctionCode_RiskNotice = b'i'
#///察看经纪公司资金权限
BrokerFunctionCode_BrokerDeposit = b'j'
#///资金查询
BrokerFunctionCode_QueryFund = b'k'
#///报单查询
BrokerFunctionCode_QueryOrder = b'l'
#///成交查询
BrokerFunctionCode_QueryTrade = b'm'
#///持仓查询
BrokerFunctionCode_QueryPosition = b'n'
#///行情查询
BrokerFunctionCode_QueryMarketData = b'o'
#///用户事件查询
BrokerFunctionCode_QueryUserEvent = b'p'
#///风险通知查询
BrokerFunctionCode_QueryRiskNotify = b'q'
#///出入金查询
BrokerFunctionCode_QueryFundChange = b'r'
#///投资者信息查询
BrokerFunctionCode_QueryInvestor = b's'
#///交易编码查询
BrokerFunctionCode_QueryTradingCode = b't'
#///强平
BrokerFunctionCode_ForceClose = b'u'
#///压力测试
BrokerFunctionCode_PressTest = b'v'
#///权益反算
BrokerFunctionCode_RemainCalc = b'w'
#///净持仓保证金指标
BrokerFunctionCode_NetPositionInd = b'x'
#///风险预算
BrokerFunctionCode_RiskPredict = b'y'
#///数据导出
BrokerFunctionCode_DataExport = b'z'
#///风控指标设置
BrokerFunctionCode_RiskTargetSetup = b'A'
#///行情预警
BrokerFunctionCode_MarketDataWarn = b'B'
#///业务通知查询
BrokerFunctionCode_QryBizNotice = b'C'
#///业务通知模板设置
BrokerFunctionCode_CfgBizNotice = b'D'
#///同步动态令牌
BrokerFunctionCode_SyncOTP = b'E'
#///发送业务通知
BrokerFunctionCode_SendBizNotice = b'F'
#///风险级别标准设置
BrokerFunctionCode_CfgRiskLevelStd = b'G'
#///交易终端应急功能
BrokerFunctionCode_TbCommand = b'H'
#///删除未知单
BrokerFunctionCode_DeleteOrder = b'J'
#///预埋报单插入
BrokerFunctionCode_ParkedOrderInsert = b'K'
#///预埋报单操作
BrokerFunctionCode_ParkedOrderAction = b'L'
#///资金不够仍允许行权
BrokerFunctionCode_ExecOrderNoCheck = b'M'
#///指定
BrokerFunctionCode_Designate = b'N'
#///证券处置
BrokerFunctionCode_StockDisposal = b'O'
#///席位资金预警
BrokerFunctionCode_BrokerDepositWarn = b'Q'
#///备兑不足预警
BrokerFunctionCode_CoverWarn = b'S'
#///行权试算
BrokerFunctionCode_PreExecOrder = b'T'
#///行权交收风险
BrokerFunctionCode_ExecOrderRisk = b'P'
#///持仓限额预警
BrokerFunctionCode_PosiLimitWarn = b'U'
#///持仓限额查询
BrokerFunctionCode_QryPosiLimit = b'V'
#///银期签到签退
BrokerFunctionCode_FBSign = b'W'
#///银期签约解约
BrokerFunctionCode_FBAccount = b'X'
#///已经提交
OrderActionStatus_Submitted = b'a'
#///已经接受
OrderActionStatus_Accepted = b'b'
#///已经被拒绝
OrderActionStatus_Rejected = b'c'
#///全部成交
OrderStatus_AllTraded = b'0'
#///部分成交还在队列中
OrderStatus_PartTradedQueueing = b'1'
#///部分成交不在队列中
OrderStatus_PartTradedNotQueueing = b'2'
#///未成交还在队列中
OrderStatus_NoTradeQueueing = b'3'
#///未成交不在队列中
OrderStatus_NoTradeNotQueueing = b'4'
#///撤单
OrderStatus_Canceled = b'5'
#///未知
OrderStatus_Unknown = b'a'
#///尚未触发
OrderStatus_NotTouched = b'b'
#///已触发
OrderStatus_Touched = b'c'
#///已经提交
OrderSubmitStatus_InsertSubmitted = b'0'
#///撤单已经提交
OrderSubmitStatus_CancelSubmitted = b'1'
#///修改已经提交
OrderSubmitStatus_ModifySubmitted = b'2'
#///已经接受
OrderSubmitStatus_Accepted = b'3'
#///报单已经被拒绝
OrderSubmitStatus_InsertRejected = b'4'
#///撤单已经被拒绝
OrderSubmitStatus_CancelRejected = b'5'
#///改单已经被拒绝
OrderSubmitStatus_ModifyRejected = b'6'
#///今日持仓
PositionDate_Today = b'1'
#///历史持仓
PositionDate_History = b'2'
#///使用历史持仓
PositionDateType_UseHistory = b'1'
#///不使用历史持仓
PositionDateType_NoUseHistory = b'2'
#///代理
TradingRole_Broker = b'1'
#///自营
TradingRole_Host = b'2'
#///做市商
TradingRole_Maker = b'3'
#///期货
ProductClass_Futures = b'1'
#///期货期权
ProductClass_Options = b'2'
#///组合
ProductClass_Combination = b'3'
#///即期
ProductClass_Spot = b'4'
#///期转现
ProductClass_EFP = b'5'
#///现货期权
ProductClass_SpotOption = b'6'
#///未上市
InstLifePhase_NotStart = b'0'
#///上市
InstLifePhase_Started = b'1'
#///停牌
InstLifePhase_Pause = b'2'
#///到期
InstLifePhase_Expired = b'3'
#///买
Direction_Buy = b'0'
#///卖
Direction_Sell = b'1'
#///净持仓
PositionType_Net = b'1'
#///综合持仓
PositionType_Gross = b'2'
#///净
PosiDirection_Net = b'1'
#///多头
PosiDirection_Long = b'2'
#///空头
PosiDirection_Short = b'3'
#///不活跃
SysSettlementStatus_NonActive = b'1'
#///启动
SysSettlementStatus_Startup = b'2'
#///操作
SysSettlementStatus_Operating = b'3'
#///结算
SysSettlementStatus_Settlement = b'4'
#///结算完成
SysSettlementStatus_SettlementFinished = b'5'
#///交易费率
RatioAttr_Trade = b'0'
#///结算费率
RatioAttr_Settlement = b'1'
#///投机
HedgeFlag_Speculation = b'1'
#///套利
HedgeFlag_Arbitrage = b'2'
#///套保
HedgeFlag_Hedge = b'3'
#///做市商
HedgeFlag_MarketMaker = b'5'
#///第一腿投机第二腿套保 大商所专用
HedgeFlag_SpecHedge = b'6'
#///第一腿套保第二腿投机  大商所专用
HedgeFlag_HedgeSpec = b'7'
#///投机
BillHedgeFlag_Speculation = b'1'
#///套利
BillHedgeFlag_Arbitrage = b'2'
#///套保
BillHedgeFlag_Hedge = b'3'
#///投机
ClientIDType_Speculation = b'1'
#///套利
ClientIDType_Arbitrage = b'2'
#///套保
ClientIDType_Hedge = b'3'
#///做市商
ClientIDType_MarketMaker = b'5'
#///任意价
OrderPriceType_AnyPrice = b'1'
#///限价
OrderPriceType_LimitPrice = b'2'
#///最优价
OrderPriceType_BestPrice = b'3'
#///最新价
OrderPriceType_LastPrice = b'4'
#///最新价浮动上浮1个ticks
OrderPriceType_LastPricePlusOneTicks = b'5'
#///最新价浮动上浮2个ticks
OrderPriceType_LastPricePlusTwoTicks = b'6'
#///最新价浮动上浮3个ticks
OrderPriceType_LastPricePlusThreeTicks = b'7'
#///卖一价
OrderPriceType_AskPrice1 = b'8'
#///卖一价浮动上浮1个ticks
OrderPriceType_AskPrice1PlusOneTicks = b'9'
#///卖一价浮动上浮2个ticks
OrderPriceType_AskPrice1PlusTwoTicks = b'A'
#///卖一价浮动上浮3个ticks
OrderPriceType_AskPrice1PlusThreeTicks = b'B'
#///买一价
OrderPriceType_BidPrice1 = b'C'
#///买一价浮动上浮1个ticks
OrderPriceType_BidPrice1PlusOneTicks = b'D'
#///买一价浮动上浮2个ticks
OrderPriceType_BidPrice1PlusTwoTicks = b'E'
#///买一价浮动上浮3个ticks
OrderPriceType_BidPrice1PlusThreeTicks = b'F'
#///五档价
OrderPriceType_FiveLevelPrice = b'G'
#///开仓
OffsetFlag_Open = b'0'
#///平仓
OffsetFlag_Close = b'1'
#///强平
OffsetFlag_ForceClose = b'2'
#///平今
OffsetFlag_CloseToday = b'3'
#///平昨
OffsetFlag_CloseYesterday = b'4'
#///强减
OffsetFlag_ForceOff = b'5'
#///本地强平
OffsetFlag_LocalForceClose = b'6'
#///非强平
ForceCloseReason_NotForceClose = b'0'
#///资金不足
ForceCloseReason_LackDeposit = b'1'
#///客户超仓
ForceCloseReason_ClientOverPositionLimit = b'2'
#///会员超仓
ForceCloseReason_MemberOverPositionLimit = b'3'
#///持仓非整数倍
ForceCloseReason_NotMultiple = b'4'
#///违规
ForceCloseReason_Violation = b'5'
#///其它
ForceCloseReason_Other = b'6'
#///自然人临近交割
ForceCloseReason_PersonDeliv = b'7'
#///正常
OrderType_Normal = b'0'
#///报价衍生
OrderType_DeriveFromQuote = b'1'
#///组合衍生
OrderType_DeriveFromCombination = b'2'
#///组合报单
OrderType_Combination = b'3'
#///条件单
OrderType_ConditionalOrder = b'4'
#///互换单
OrderType_Swap = b'5'
#///大宗交易成交衍生
OrderType_DeriveFromBlockTrade = b'6'
#///期转现成交衍生
OrderType_DeriveFromEFPTrade = b'7'
#///立即完成，否则撤销
TimeCondition_IOC = b'1'
#///本节有效
TimeCondition_GFS = b'2'
#///当日有效
TimeCondition_GFD = b'3'
#///指定日期前有效
TimeCondition_GTD = b'4'
#///撤销前有效
TimeCondition_GTC = b'5'
#///集合竞价有效
TimeCondition_GFA = b'6'
#///任何数量
VolumeCondition_AV = b'1'
#///最小数量
VolumeCondition_MV = b'2'
#///全部数量
VolumeCondition_CV = b'3'
#///立即
ContingentCondition_Immediately = b'1'
#///止损
ContingentCondition_Touch = b'2'
#///止赢
ContingentCondition_TouchProfit = b'3'
#///预埋单
ContingentCondition_ParkedOrder = b'4'
#///最新价大于条件价
ContingentCondition_LastPriceGreaterThanStopPrice = b'5'
#///最新价大于等于条件价
ContingentCondition_LastPriceGreaterEqualStopPrice = b'6'
#///最新价小于条件价
ContingentCondition_LastPriceLesserThanStopPrice = b'7'
#///最新价小于等于条件价
ContingentCondition_LastPriceLesserEqualStopPrice = b'8'
#///卖一价大于条件价
ContingentCondition_AskPriceGreaterThanStopPrice = b'9'
#///卖一价大于等于条件价
ContingentCondition_AskPriceGreaterEqualStopPrice = b'A'
#///卖一价小于条件价
ContingentCondition_AskPriceLesserThanStopPrice = b'B'
#///卖一价小于等于条件价
ContingentCondition_AskPriceLesserEqualStopPrice = b'C'
#///买一价大于条件价
ContingentCondition_BidPriceGreaterThanStopPrice = b'D'
#///买一价大于等于条件价
ContingentCondition_BidPriceGreaterEqualStopPrice = b'E'
#///买一价小于条件价
ContingentCondition_BidPriceLesserThanStopPrice = b'F'
#///买一价小于等于条件价
ContingentCondition_BidPriceLesserEqualStopPrice = b'H'
#///删除
ActionFlag_Delete = b'0'
#///修改
ActionFlag_Modify = b'3'
#///可以交易
TradingRight_Allow = b'0'
#///只能平仓
TradingRight_CloseOnly = b'1'
#///不能交易
TradingRight_Forbidden = b'2'
#///来自参与者
OrderSource_Participant = b'0'
#///来自管理员
OrderSource_Administrator = b'1'
#///组合持仓拆分为单一持仓,初始化不应包含该类型的持仓
TradeType_SplitCombination = b'#'
#///普通成交
TradeType_Common = b'0'
#///期权执行
TradeType_OptionsExecution = b'1'
#///OTC成交
TradeType_OTC = b'2'
#///期转现衍生成交
TradeType_EFPDerived = b'3'
#///组合衍生成交
TradeType_CombinationDerived = b'4'
#///大宗交易成交
TradeType_BlockTrade = b'5'
#///前成交价
PriceSource_LastPrice = b'0'
#///买委托价
PriceSource_Buy = b'1'
#///卖委托价
PriceSource_Sell = b'2'
#///场外成交价
PriceSource_OTC = b'3'
#///开盘前
InstrumentStatus_BeforeTrading = b'0'
#///非交易
InstrumentStatus_NoTrading = b'1'
#///连续交易
InstrumentStatus_Continous = b'2'
#///集合竞价报单
InstrumentStatus_AuctionOrdering = b'3'
#///集合竞价价格平衡
InstrumentStatus_AuctionBalance = b'4'
#///集合竞价撮合
InstrumentStatus_AuctionMatch = b'5'
#///收盘
InstrumentStatus_Closed = b'6'
#///自动切换
InstStatusEnterReason_Automatic = b'1'
#///手动切换
InstStatusEnterReason_Manual = b'2'
#///熔断
InstStatusEnterReason_Fuse = b'3'
#///未上传
BatchStatus_NoUpload = b'1'
#///已上传
BatchStatus_Uploaded = b'2'
#///审核失败
BatchStatus_Failed = b'3'
#///按所有品种
ReturnStyle_All = b'1'
#///按品种
ReturnStyle_ByProduct = b'2'
#///按成交手数
ReturnPattern_ByVolume = b'1'
#///按留存手续费
ReturnPattern_ByFeeOnHand = b'2'
#///级别1
ReturnLevel_Level1 = b'1'
#///级别2
ReturnLevel_Level2 = b'2'
#///级别3
ReturnLevel_Level3 = b'3'
#///级别4
ReturnLevel_Level4 = b'4'
#///级别5
ReturnLevel_Level5 = b'5'
#///级别6
ReturnLevel_Level6 = b'6'
#///级别7
ReturnLevel_Level7 = b'7'
#///级别8
ReturnLevel_Level8 = b'8'
#///级别9
ReturnLevel_Level9 = b'9'
#///分阶段返还
ReturnStandard_ByPeriod = b'1'
#///按某一标准
ReturnStandard_ByStandard = b'2'
#///质出
MortgageType_Out = b'0'
#///质入
MortgageType_In = b'1'
#///质押比例
InvestorSettlementParamID_MortgageRatio = b'4'
#///保证金算法
InvestorSettlementParamID_MarginWay = b'5'
#///结算单结存是否包含质押
InvestorSettlementParamID_BillDeposit = b'9'
#///质押比例
ExchangeSettlementParamID_MortgageRatio = b'1'
#///分项资金导入项
ExchangeSettlementParamID_OtherFundItem = b'2'
#///分项资金入交易所出入金
ExchangeSettlementParamID_OtherFundImport = b'3'
#///中金所开户最低可用金额
ExchangeSettlementParamID_CFFEXMinPrepa = b'6'
#///郑商所结算方式
ExchangeSettlementParamID_CZCESettlementType = b'7'
#///交易所交割手续费收取方式
ExchangeSettlementParamID_ExchDelivFeeMode = b'9'
#///投资者交割手续费收取方式
ExchangeSettlementParamID_DelivFeeMode = b'0'
#///郑商所组合持仓保证金收取方式
ExchangeSettlementParamID_CZCEComMarginType = b'A'
#///大商所套利保证金是否优惠
ExchangeSettlementParamID_DceComMarginType = b'B'
#///虚值期权保证金优惠比率
ExchangeSettlementParamID_OptOutDisCountRate = b'a'
#///最低保障系数
ExchangeSettlementParamID_OptMiniGuarantee = b'b'
#///投资者代码最小长度
SystemParamID_InvestorIDMinLength = b'1'
#///投资者帐号代码最小长度
SystemParamID_AccountIDMinLength = b'2'
#///投资者开户默认登录权限
SystemParamID_UserRightLogon = b'3'
#///投资者交易结算单成交汇总方式
SystemParamID_SettlementBillTrade = b'4'
#///统一开户更新交易编码方式
SystemParamID_TradingCode = b'5'
#///结算是否判断存在未复核的出入金和分项资金
SystemParamID_CheckFund = b'6'
#///是否启用手续费模板数据权限
SystemParamID_CommModelRight = b'7'
#///是否启用保证金率模板数据权限
SystemParamID_MarginModelRight = b'9'
#///是否规范用户才能激活
SystemParamID_IsStandardActive = b'8'
#///上传的交易所结算文件路径
SystemParamID_UploadSettlementFile = b'U'
#///上报保证金监控中心文件路径
SystemParamID_DownloadCSRCFile = b'D'
#///生成的结算单文件路径
SystemParamID_SettlementBillFile = b'S'
#///证监会文件标识
SystemParamID_CSRCOthersFile = b'C'
#///投资者照片路径
SystemParamID_InvestorPhoto = b'P'
#///全结经纪公司上传文件路径
SystemParamID_CSRCData = b'R'
#///开户密码录入方式
SystemParamID_InvestorPwdModel = b'I'
#///投资者中金所结算文件下载路径
SystemParamID_CFFEXInvestorSettleFile = b'F'
#///投资者代码编码方式
SystemParamID_InvestorIDType = b'a'
#///休眠户最高权益
SystemParamID_FreezeMaxReMain = b'r'
#///手续费相关操作实时上场开关
SystemParamID_IsSync = b'A'
#///解除开仓权限限制
SystemParamID_RelieveOpenLimit = b'O'
#///是否规范用户才能休眠
SystemParamID_IsStandardFreeze = b'X'
#///郑商所是否开放所有品种套保交易
SystemParamID_CZCENormalProductHedge = b'B'
#///系统加密算法
TradeParamID_EncryptionStandard = b'E'
#///系统风险算法
TradeParamID_RiskMode = b'R'
#///系统风险算法是否全局 0-否 1-是
TradeParamID_RiskModeGlobal = b'G'
#///密码加密算法
TradeParamID_modeEncode = b'P'
#///价格小数位数参数
TradeParamID_tickMode = b'T'
#///用户最大会话数
TradeParamID_SingleUserSessionMaxNum = b'S'
#///最大连续登录失败数
TradeParamID_LoginFailMaxNum = b'L'
#///是否强制认证
TradeParamID_IsAuthForce = b'A'
#///是否冻结证券持仓
TradeParamID_IsPosiFreeze = b'F'
#///是否限仓
TradeParamID_IsPosiLimit = b'M'
#///郑商所询价时间间隔
TradeParamID_ForQuoteTimeInterval = b'Q'
#///是否期货限仓
TradeParamID_IsFuturePosiLimit = b'B'
#///是否期货下单频率限制
TradeParamID_IsFutureOrderFreq = b'C'
#///行权冻结是否计算盈利
TradeParamID_IsExecOrderProfit = b'H'
#///银期开户是否验证开户银行卡号是否是预留银行账户
TradeParamID_IsCheckBankAcc = b'I'
#///弱密码最后修改日期
TradeParamID_PasswordDeadLine = b'J'
#///强密码校验
TradeParamID_IsStrongPassword = b'K'
#///自有资金质押比
TradeParamID_BalanceMorgage = b'a'
#///最小密码长度
TradeParamID_MinPwdLen = b'O'
#///IP当日最大登陆失败次数
TradeParamID_LoginFailMaxNumForIP = b'U'
#///密码有效期
TradeParamID_PasswordPeriod = b'V'
#///资金数据
FileID_SettlementFund = b'F'
#///成交数据
FileID_Trade = b'T'
#///投资者持仓数据
FileID_InvestorPosition = b'P'
#///投资者分项资金数据
FileID_SubEntryFund = b'O'
#///组合持仓数据
FileID_CZCECombinationPos = b'C'
#///上报保证金监控中心数据
FileID_CSRCData = b'R'
#///郑商所平仓了结数据
FileID_CZCEClose = b'L'
#///郑商所非平仓了结数据
FileID_CZCENoClose = b'N'
#///持仓明细数据
FileID_PositionDtl = b'D'
#///期权执行文件
FileID_OptionStrike = b'S'
#///结算价比对文件
FileID_SettlementPriceComparison = b'M'
#///上期所非持仓变动明细
FileID_NonTradePosChange = b'B'
#///结算
FileType_Settlement = b'0'
#///核对
FileType_Check = b'1'
#///文本文件(.txt)
FileFormat_Txt = b'0'
#///压缩文件(.zip)
FileFormat_Zip = b'1'
#///DBF文件(.dbf)
FileFormat_DBF = b'2'
#///上传成功
FileUploadStatus_SucceedUpload = b'1'
#///上传失败
FileUploadStatus_FailedUpload = b'2'
#///导入成功
FileUploadStatus_SucceedLoad = b'3'
#///导入部分成功
FileUploadStatus_PartSucceedLoad = b'4'
#///导入失败
FileUploadStatus_FailedLoad = b'5'
#///移出
TransferDirection_Out = b'0'
#///移入
TransferDirection_In = b'1'
#///没有特殊创建规则
SpecialCreateRule_NoSpecialRule = b'0'
#///不包含春节
SpecialCreateRule_NoSpringFestival = b'1'
#///上一合约结算价
BasisPriceType_LastSettlement = b'1'
#///上一合约收盘价
BasisPriceType_LaseClose = b'2'
#///活跃
ProductLifePhase_Active = b'1'
#///不活跃
ProductLifePhase_NonActive = b'2'
#///注销
ProductLifePhase_Canceled = b'3'
#///现金交割
DeliveryMode_CashDeliv = b'1'
#///实物交割
DeliveryMode_CommodityDeliv = b'2'
#///出入金
FundIOType_FundIO = b'1'
#///银期转帐
FundIOType_Transfer = b'2'
#///银期换汇
FundIOType_SwapCurrency = b'3'
#///银行存款
FundType_Deposite = b'1'
#///分项资金
FundType_ItemFund = b'2'
#///公司调整
FundType_Company = b'3'
#///资金内转
FundType_InnerTransfer = b'4'
#///入金
FundDirection_In = b'1'
#///出金
FundDirection_Out = b'2'
#///已录入
FundStatus_Record = b'1'
#///已复核
FundStatus_Check = b'2'
#///已冲销
FundStatus_Charge = b'3'
#///未发布
PublishStatus_None = b'1'
#///正在发布
PublishStatus_Publishing = b'2'
#///已发布
PublishStatus_Published = b'3'
#///不活跃
SystemStatus_NonActive = b'1'
#///启动
SystemStatus_Startup = b'2'
#///交易开始初始化
SystemStatus_Initialize = b'3'
#///交易完成初始化
SystemStatus_Initialized = b'4'
#///收市开始
SystemStatus_Close = b'5'
#///收市完成
SystemStatus_Closed = b'6'
#///结算
SystemStatus_Settlement = b'7'
#///初始
SettlementStatus_Initialize = b'0'
#///结算中
SettlementStatus_Settlementing = b'1'
#///已结算
SettlementStatus_Settlemented = b'2'
#///结算完成
SettlementStatus_Finished = b'3'
#///自然人
InvestorType_Person = b'0'
#///法人
InvestorType_Company = b'1'
#///投资基金
InvestorType_Fund = b'2'
#///特殊法人
InvestorType_SpecialOrgan = b'3'
#///资管户
InvestorType_Asset = b'4'
#///交易会员
BrokerType_Trade = b'0'
#///交易结算会员
BrokerType_TradeSettle = b'1'
#///低风险客户
RiskLevel_Low = b'1'
#///普通客户
RiskLevel_Normal = b'2'
#///关注客户
RiskLevel_Focus = b'3'
#///风险客户
RiskLevel_Risk = b'4'
#///按交易收取
FeeAcceptStyle_ByTrade = b'1'
#///按交割收取
FeeAcceptStyle_ByDeliv = b'2'
#///不收
FeeAcceptStyle_None = b'3'
#///按指定手续费收取
FeeAcceptStyle_FixFee = b'4'
#///交易密码
PasswordType_Trade = b'1'
#///资金密码
PasswordType_Account = b'2'
#///浮盈浮亏都计算
Algorithm_All = b'1'
#///浮盈不计，浮亏计
Algorithm_OnlyLost = b'2'
#///浮盈计，浮亏不计
Algorithm_OnlyGain = b'3'
#///浮盈浮亏都不计算
Algorithm_None = b'4'
#///包含平仓盈利
IncludeCloseProfit_Include = b'0'
#///不包含平仓盈利
IncludeCloseProfit_NotInclude = b'2'
#///无仓无成交不受可提比例限制
AllWithoutTrade_Enable = b'0'
#///受可提比例限制
AllWithoutTrade_Disable = b'2'
#///无仓不受可提比例限制
AllWithoutTrade_NoHoldEnable = b'3'
#///不核对
FuturePwdFlag_UnCheck = b'0'
#///核对
FuturePwdFlag_Check = b'1'
#///银行转期货
TransferType_BankToFuture = b'0'
#///期货转银行
TransferType_FutureToBank = b'1'
#///无效或失败
TransferValidFlag_Invalid = b'0'
#///有效
TransferValidFlag_Valid = b'1'
#///冲正
TransferValidFlag_Reverse = b'2'
#///错单
Reason_CD = b'0'
#///资金在途
Reason_ZT = b'1'
#///其它
Reason_QT = b'2'
#///未知
Sex_None = b'0'
#///男
Sex_Man = b'1'
#///女
Sex_Woman = b'2'
#///投资者
UserType_Investor = b'0'
#///操作员
UserType_Operator = b'1'
#///管理员
UserType_SuperUser = b'2'
#///保证金率
RateType_MarginRate = b'2'
#///交易结算单
NoteType_TradeSettleBill = b'1'
#///交易结算月报
NoteType_TradeSettleMonth = b'2'
#///追加保证金通知书
NoteType_CallMarginNotes = b'3'
#///强行平仓通知书
NoteType_ForceCloseNotes = b'4'
#///成交通知书
NoteType_TradeNotes = b'5'
#///交割通知书
NoteType_DelivNotes = b'6'
#///逐日盯市
SettlementStyle_Day = b'1'
#///逐笔对冲
SettlementStyle_Volume = b'2'
#///日报
SettlementBillType_Day = b'0'
#///月报
SettlementBillType_Month = b'1'
#///登录
UserRightType_Logon = b'1'
#///银期转帐
UserRightType_Transfer = b'2'
#///邮寄结算单
UserRightType_EMail = b'3'
#///传真结算单
UserRightType_Fax = b'4'
#///条件单
UserRightType_ConditionOrder = b'5'
#///昨结算价
MarginPriceType_PreSettlementPrice = b'1'
#///最新价
MarginPriceType_SettlementPrice = b'2'
#///成交均价
MarginPriceType_AveragePrice = b'3'
#///开仓价
MarginPriceType_OpenPrice = b'4'
#///未生成
BillGenStatus_None = b'0'
#///生成中
BillGenStatus_NoGenerated = b'1'
#///已生成
BillGenStatus_Generated = b'2'
#///持仓处理算法
AlgoType_HandlePositionAlgo = b'1'
#///寻找保证金率算法
AlgoType_FindMarginRateAlgo = b'2'
#///基本
HandlePositionAlgoID_Base = b'1'
#///大连商品交易所
HandlePositionAlgoID_DCE = b'2'
#///郑州商品交易所
HandlePositionAlgoID_CZCE = b'3'
#///基本
FindMarginRateAlgoID_Base = b'1'
#///大连商品交易所
FindMarginRateAlgoID_DCE = b'2'
#///郑州商品交易所
FindMarginRateAlgoID_CZCE = b'3'
#///基本
HandleTradingAccountAlgoID_Base = b'1'
#///大连商品交易所
HandleTradingAccountAlgoID_DCE = b'2'
#///郑州商品交易所
HandleTradingAccountAlgoID_CZCE = b'3'
#///指定下单人
PersonType_Order = b'1'
#///开户授权人
PersonType_Open = b'2'
#///资金调拨人
PersonType_Fund = b'3'
#///结算单确认人
PersonType_Settlement = b'4'
#///法人
PersonType_Company = b'5'
#///法人代表
PersonType_Corporation = b'6'
#///投资者联系人
PersonType_LinkMan = b'7'
#///分户管理资产负责人
PersonType_Ledger = b'8'
#///托（保）管人
PersonType_Trustee = b'9'
#///托（保）管机构法人代表
PersonType_TrusteeCorporation = b'A'
#///托（保）管机构开户授权人
PersonType_TrusteeOpen = b'B'
#///托（保）管机构联系人
PersonType_TrusteeContact = b'C'
#///境外自然人参考证件
PersonType_ForeignerRefer = b'D'
#///法人代表参考证件
PersonType_CorporationRefer = b'E'
#///所有
QueryInvestorRange_All = b'1'
#///查询分类
QueryInvestorRange_Group = b'2'
#///单一投资者
QueryInvestorRange_Single = b'3'
#///正常
InvestorRiskStatus_Normal = b'1'
#///警告
InvestorRiskStatus_Warn = b'2'
#///追保
InvestorRiskStatus_Call = b'3'
#///强平
InvestorRiskStatus_Force = b'4'
#///异常
InvestorRiskStatus_Exception = b'5'
#///登录
UserEventType_Login = b'1'
#///登出
UserEventType_Logout = b'2'
#///交易成功
UserEventType_Trading = b'3'
#///交易失败
UserEventType_TradingError = b'4'
#///修改密码
UserEventType_UpdatePassword = b'5'
#///客户端认证
UserEventType_Authenticate = b'6'
#///其他
UserEventType_Other = b'9'
#///先开先平
CloseStyle_Close = b'0'
#///先平今再平昨
CloseStyle_CloseToday = b'1'
#///----
StatMode_Non = b'0'
#///按合约统计
StatMode_Instrument = b'1'
#///按产品统计
StatMode_Product = b'2'
#///按投资者统计
StatMode_Investor = b'3'
#///未发送
ParkedOrderStatus_NotSend = b'1'
#///已发送
ParkedOrderStatus_Send = b'2'
#///已删除
ParkedOrderStatus_Deleted = b'3'
#///正在处理
VirDealStatus_Dealing = b'1'
#///处理成功
VirDealStatus_DeaclSucceed = b'2'
#///综合交易平台
OrgSystemID_Standard = b'0'
#///易盛系统
OrgSystemID_ESunny = b'1'
#///金仕达V6系统
OrgSystemID_KingStarV6 = b'2'
#///正常处理中
VirTradeStatus_NaturalDeal = b'0'
#///成功结束
VirTradeStatus_SucceedEnd = b'1'
#///失败结束
VirTradeStatus_FailedEND = b'2'
#///异常中
VirTradeStatus_Exception = b'3'
#///已人工异常处理
VirTradeStatus_ManualDeal = b'4'
#///通讯异常 ，请人工处理
VirTradeStatus_MesException = b'5'
#///系统出错，请人工处理
VirTradeStatus_SysException = b'6'
#///存折
VirBankAccType_BankBook = b'1'
#///储蓄卡
VirBankAccType_BankCard = b'2'
#///信用卡
VirBankAccType_CreditCard = b'3'
#///正常
VirementStatus_Natural = b'0'
#///销户
VirementStatus_Canceled = b'9'
#///未确认
VirementAvailAbility_NoAvailAbility = b'0'
#///有效
VirementAvailAbility_AvailAbility = b'1'
#///冲正
VirementAvailAbility_Repeal = b'2'
#///银行发起银行资金转期货
VirementTradeCode_BankBankToFuture = b'102001'
#///银行发起期货资金转银行
VirementTradeCode_BankFutureToBank = b'102002'
#///期货发起银行资金转期货
VirementTradeCode_FutureBankToFuture = b'202001'
#///期货发起期货资金转银行
VirementTradeCode_FutureFutureToBank = b'202002'
#///程序生成
AMLGenStatus_Program = b'0'
#///人工生成
AMLGenStatus_HandWork = b'1'
#///主动请求更新
CFMMCKeyKind_REQUEST = b'R'
#///CFMMC自动更新
CFMMCKeyKind_AUTO = b'A'
#///CFMMC手动更新
CFMMCKeyKind_MANUAL = b'M'
#///身份证
CertificationType_IDCard = b'0'
#///护照
CertificationType_Passport = b'1'
#///军官证
CertificationType_OfficerIDCard = b'2'
#///士兵证
CertificationType_SoldierIDCard = b'3'
#///回乡证
CertificationType_HomeComingCard = b'4'
#///户口簿
CertificationType_HouseholdRegister = b'5'
#///营业执照号
CertificationType_LicenseNo = b'6'
#///组织机构代码证
CertificationType_InstitutionCodeCard = b'7'
#///临时营业执照号
CertificationType_TempLicenseNo = b'8'
#///民办非企业登记证书
CertificationType_NoEnterpriseLicenseNo = b'9'
#///其他证件
CertificationType_OtherCard = b'x'
#///主管部门批文
CertificationType_SuperDepAgree = b'a'
#///其他
FileBusinessCode_Others = b'0'
#///转账交易明细对账
FileBusinessCode_TransferDetails = b'1'
#///客户账户状态对账
FileBusinessCode_CustAccStatus = b'2'
#///账户类交易明细对账
FileBusinessCode_AccountTradeDetails = b'3'
#///期货账户信息变更明细对账
FileBusinessCode_FutureAccountChangeInfoDetails = b'4'
#///客户资金台账余额明细对账
FileBusinessCode_CustMoneyDetail = b'5'
#///客户销户结息明细对账
FileBusinessCode_CustCancelAccountInfo = b'6'
#///客户资金余额对账结果
FileBusinessCode_CustMoneyResult = b'7'
#///其它对账异常结果文件
FileBusinessCode_OthersExceptionResult = b'8'
#///客户结息净额明细
FileBusinessCode_CustInterestNetMoneyDetails = b'9'
#///客户资金交收明细
FileBusinessCode_CustMoneySendAndReceiveDetails = b'a'
#///法人存管银行资金交收汇总
FileBusinessCode_CorporationMoneyTotal = b'b'
#///主体间资金交收汇总
FileBusinessCode_MainbodyMoneyTotal = b'c'
#///总分平衡监管数据
FileBusinessCode_MainPartMonitorData = b'd'
#///存管银行备付金余额
FileBusinessCode_PreparationMoney = b'e'
#///协办存管银行资金监管数据
FileBusinessCode_BankMoneyMonitorData = b'f'
#///汇
CashExchangeCode_Exchange = b'1'
#///钞
CashExchangeCode_Cash = b'2'
#///是
YesNoIndicator_Yes = b'0'
#///否
YesNoIndicator_No = b'1'
#///当前余额
BanlanceType_CurrentMoney = b'0'
#///可用余额
BanlanceType_UsableMoney = b'1'
#///可取余额
BanlanceType_FetchableMoney = b'2'
#///冻结余额
BanlanceType_FreezeMoney = b'3'
#///未知状态
Gender_Unknown = b'0'
#///男
Gender_Male = b'1'
#///女
Gender_Female = b'2'
#///由受益方支付费用
FeePayFlag_BEN = b'0'
#///由发送方支付费用
FeePayFlag_OUR = b'1'
#///由发送方支付发起的费用，受益方支付接受的费用
FeePayFlag_SHA = b'2'
#///交换密钥
PassWordKeyType_ExchangeKey = b'0'
#///密码密钥
PassWordKeyType_PassWordKey = b'1'
#///MAC密钥
PassWordKeyType_MACKey = b'2'
#///报文密钥
PassWordKeyType_MessageKey = b'3'
#///查询
FBTPassWordType_Query = b'0'
#///取款
FBTPassWordType_Fetch = b'1'
#///转帐
FBTPassWordType_Transfer = b'2'
#///交易
FBTPassWordType_Trade = b'3'
#///不加密
FBTEncryMode_NoEncry = b'0'
#///DES
FBTEncryMode_DES = b'1'
#///3DES
FBTEncryMode_3DES = b'2'
#///银行无需自动冲正
BankRepealFlag_BankNotNeedRepeal = b'0'
#///银行待自动冲正
BankRepealFlag_BankWaitingRepeal = b'1'
#///银行已自动冲正
BankRepealFlag_BankBeenRepealed = b'2'
#///期商无需自动冲正
BrokerRepealFlag_BrokerNotNeedRepeal = b'0'
#///期商待自动冲正
BrokerRepealFlag_BrokerWaitingRepeal = b'1'
#///期商已自动冲正
BrokerRepealFlag_BrokerBeenRepealed = b'2'
#///银行
InstitutionType_Bank = b'0'
#///期商
InstitutionType_Future = b'1'
#///券商
InstitutionType_Store = b'2'
#///是最后分片
LastFragment_Yes = b'0'
#///不是最后分片
LastFragment_No = b'1'
#///正常
BankAccStatus_Normal = b'0'
#///冻结
BankAccStatus_Freeze = b'1'
#///挂失
BankAccStatus_ReportLoss = b'2'
#///正常
MoneyAccountStatus_Normal = b'0'
#///销户
MoneyAccountStatus_Cancel = b'1'
#///指定存管
ManageStatus_Point = b'0'
#///预指定
ManageStatus_PrePoint = b'1'
#///撤销指定
ManageStatus_CancelPoint = b'2'
#///银期转帐
SystemType_FutureBankTransfer = b'0'
#///银证转帐
SystemType_StockBankTransfer = b'1'
#///第三方存管
SystemType_TheThirdPartStore = b'2'
#///正常处理中
TxnEndFlag_NormalProcessing = b'0'
#///成功结束
TxnEndFlag_Success = b'1'
#///失败结束
TxnEndFlag_Failed = b'2'
#///异常中
TxnEndFlag_Abnormal = b'3'
#///已人工异常处理
TxnEndFlag_ManualProcessedForException = b'4'
#///通讯异常 ，请人工处理
TxnEndFlag_CommuFailedNeedManualProcess = b'5'
#///系统出错，请人工处理
TxnEndFlag_SysErrorNeedManualProcess = b'6'
#///未处理
ProcessStatus_NotProcess = b'0'
#///开始处理
ProcessStatus_StartProcess = b'1'
#///处理完成
ProcessStatus_Finished = b'2'
#///自然人
CustType_Person = b'0'
#///机构户
CustType_Institution = b'1'
#///入金，银行转期货
FBTTransferDirection_FromBankToFuture = b'1'
#///出金，期货转银行
FBTTransferDirection_FromFutureToBank = b'2'
#///开户
OpenOrDestroy_Open = b'1'
#///销户
OpenOrDestroy_Destroy = b'0'
#///未确认
AvailabilityFlag_Invalid = b'0'
#///有效
AvailabilityFlag_Valid = b'1'
#///冲正
AvailabilityFlag_Repeal = b'2'
#///银行代理
OrganType_Bank = b'1'
#///交易前置
OrganType_Future = b'2'
#///银期转帐平台管理
OrganType_PlateForm = b'9'
#///银行总行或期商总部
OrganLevel_HeadQuarters = b'1'
#///银行分中心或期货公司营业部
OrganLevel_Branch = b'2'
#///期商协议
ProtocalID_FutureProtocal = b'0'
#///工行协议
ProtocalID_ICBCProtocal = b'1'
#///农行协议
ProtocalID_ABCProtocal = b'2'
#///中国银行协议
ProtocalID_CBCProtocal = b'3'
#///建行协议
ProtocalID_CCBProtocal = b'4'
#///交行协议
ProtocalID_BOCOMProtocal = b'5'
#///银期转帐平台协议
ProtocalID_FBTPlateFormProtocal = b'X'
#///短连接
ConnectMode_ShortConnect = b'0'
#///长连接
ConnectMode_LongConnect = b'1'
#///异步
SyncMode_ASync = b'0'
#///同步
SyncMode_Sync = b'1'
#///银行存折
BankAccType_BankBook = b'1'
#///储蓄卡
BankAccType_SavingCard = b'2'
#///信用卡
BankAccType_CreditCard = b'3'
#///银行存折
FutureAccType_BankBook = b'1'
#///储蓄卡
FutureAccType_SavingCard = b'2'
#///信用卡
FutureAccType_CreditCard = b'3'
#///启用
OrganStatus_Ready = b'0'
#///签到
OrganStatus_CheckIn = b'1'
#///签退
OrganStatus_CheckOut = b'2'
#///对帐文件到达
OrganStatus_CheckFileArrived = b'3'
#///对帐
OrganStatus_CheckDetail = b'4'
#///日终清理
OrganStatus_DayEndClean = b'5'
#///注销
OrganStatus_Invalid = b'9'
#///按金额扣收
CCBFeeMode_ByAmount = b'1'
#///按月扣收
CCBFeeMode_ByMonth = b'2'
#///客户端
CommApiType_Client = b'1'
#///服务端
CommApiType_Server = b'2'
#///交易系统的UserApi
CommApiType_UserApi = b'3'
#///已经连接
LinkStatus_Connected = b'1'
#///没有连接
LinkStatus_Disconnected = b'2'
#///不核对
PwdFlag_NoCheck = b'0'
#///明文核对
PwdFlag_BlankCheck = b'1'
#///密文核对
PwdFlag_EncryptCheck = b'2'
#///资金帐号
SecuAccType_AccountID = b'1'
#///资金卡号
SecuAccType_CardID = b'2'
#///上海股东帐号
SecuAccType_SHStockholderID = b'3'
#///深圳股东帐号
SecuAccType_SZStockholderID = b'4'
#///正常
TransferStatus_Normal = b'0'
#///被冲正
TransferStatus_Repealed = b'1'
#///期商
SponsorType_Broker = b'0'
#///银行
SponsorType_Bank = b'1'
#///请求
ReqRspType_Request = b'0'
#///响应
ReqRspType_Response = b'1'
#///签到
FBTUserEventType_SignIn = b'0'
#///银行转期货
FBTUserEventType_FromBankToFuture = b'1'
#///期货转银行
FBTUserEventType_FromFutureToBank = b'2'
#///开户
FBTUserEventType_OpenAccount = b'3'
#///销户
FBTUserEventType_CancelAccount = b'4'
#///变更银行账户
FBTUserEventType_ChangeAccount = b'5'
#///冲正银行转期货
FBTUserEventType_RepealFromBankToFuture = b'6'
#///冲正期货转银行
FBTUserEventType_RepealFromFutureToBank = b'7'
#///查询银行账户
FBTUserEventType_QueryBankAccount = b'8'
#///查询期货账户
FBTUserEventType_QueryFutureAccount = b'9'
#///签退
FBTUserEventType_SignOut = b'A'
#///密钥同步
FBTUserEventType_SyncKey = b'B'
#///预约开户
FBTUserEventType_ReserveOpenAccount = b'C'
#///撤销预约开户
FBTUserEventType_CancelReserveOpenAccount = b'D'
#///预约开户确认
FBTUserEventType_ReserveOpenAccountConfirm = b'E'
#///其他
FBTUserEventType_Other = b'Z'
#///插入
DBOperation_Insert = b'0'
#///更新
DBOperation_Update = b'1'
#///删除
DBOperation_Delete = b'2'
#///已同步
SyncFlag_Yes = b'0'
#///未同步
SyncFlag_No = b'1'
#///一次同步
SyncType_OneOffSync = b'0'
#///定时同步
SyncType_TimerSync = b'1'
#///定时完全同步
SyncType_TimerFullSync = b'2'
#///结汇
ExDirection_Settlement = b'0'
#///售汇
ExDirection_Sale = b'1'
#///成功
FBEResultFlag_Success = b'0'
#///账户余额不足
FBEResultFlag_InsufficientBalance = b'1'
#///交易结果未知
FBEResultFlag_UnknownTrading = b'8'
#///失败
FBEResultFlag_Fail = b'x'
#///正常
FBEExchStatus_Normal = b'0'
#///交易重发
FBEExchStatus_ReExchange = b'1'
#///数据包
FBEFileFlag_DataPackage = b'0'
#///文件
FBEFileFlag_File = b'1'
#///未交易
FBEAlreadyTrade_NotTrade = b'0'
#///已交易
FBEAlreadyTrade_Trade = b'1'
#///签到
FBEUserEventType_SignIn = b'0'
#///换汇
FBEUserEventType_Exchange = b'1'
#///换汇重发
FBEUserEventType_ReExchange = b'2'
#///银行账户查询
FBEUserEventType_QueryBankAccount = b'3'
#///换汇明细查询
FBEUserEventType_QueryExchDetial = b'4'
#///换汇汇总查询
FBEUserEventType_QueryExchSummary = b'5'
#///换汇汇率查询
FBEUserEventType_QueryExchRate = b'6'
#///对账文件通知
FBEUserEventType_CheckBankAccount = b'7'
#///签退
FBEUserEventType_SignOut = b'8'
#///其他
FBEUserEventType_Other = b'Z'
#///未处理
FBEReqFlag_UnProcessed = b'0'
#///等待发送
FBEReqFlag_WaitSend = b'1'
#///发送成功
FBEReqFlag_SendSuccess = b'2'
#///发送失败
FBEReqFlag_SendFailed = b'3'
#///等待重发
FBEReqFlag_WaitReSend = b'4'
#///正常
NotifyClass_NOERROR = b'0'
#///警示
NotifyClass_Warn = b'1'
#///追保
NotifyClass_Call = b'2'
#///强平
NotifyClass_Force = b'3'
#///穿仓
NotifyClass_CHUANCANG = b'4'
#///异常
NotifyClass_Exception = b'5'
#///手工强平
ForceCloseType_Manual = b'0'
#///单一投资者辅助强平
ForceCloseType_Single = b'1'
#///批量投资者辅助强平
ForceCloseType_Group = b'2'
#///系统通知
RiskNotifyMethod_System = b'0'
#///短信通知
RiskNotifyMethod_SMS = b'1'
#///邮件通知
RiskNotifyMethod_EMail = b'2'
#///人工通知
RiskNotifyMethod_Manual = b'3'
#///未生成
RiskNotifyStatus_NotGen = b'0'
#///已生成未发送
RiskNotifyStatus_Generated = b'1'
#///发送失败
RiskNotifyStatus_SendError = b'2'
#///已发送未接收
RiskNotifyStatus_SendOk = b'3'
#///已接收未确认
RiskNotifyStatus_Received = b'4'
#///已确认
RiskNotifyStatus_Confirmed = b'5'
#///导出数据
RiskUserEvent_ExportData = b'0'
#///使用最新价升序
ConditionalOrderSortType_LastPriceAsc = b'0'
#///使用最新价降序
ConditionalOrderSortType_LastPriceDesc = b'1'
#///使用卖价升序
ConditionalOrderSortType_AskPriceAsc = b'2'
#///使用卖价降序
ConditionalOrderSortType_AskPriceDesc = b'3'
#///使用买价升序
ConditionalOrderSortType_BidPriceAsc = b'4'
#///使用买价降序
ConditionalOrderSortType_BidPriceDesc = b'5'
#///未发送
SendType_NoSend = b'0'
#///已发送
SendType_Sended = b'1'
#///已生成
SendType_Generated = b'2'
#///报送失败
SendType_SendFail = b'3'
#///接收成功
SendType_Success = b'4'
#///接收失败
SendType_Fail = b'5'
#///取消报送
SendType_Cancel = b'6'
#///未申请
ClientIDStatus_NoApply = b'1'
#///已提交申请
ClientIDStatus_Submited = b'2'
#///已发送申请
ClientIDStatus_Sended = b'3'
#///完成
ClientIDStatus_Success = b'4'
#///拒绝
ClientIDStatus_Refuse = b'5'
#///已撤销编码
ClientIDStatus_Cancel = b'6'
#///单选
QuestionType_Radio = b'1'
#///多选
QuestionType_Option = b'2'
#///填空
QuestionType_Blank = b'3'
#///请求
BusinessType_Request = b'1'
#///应答
BusinessType_Response = b'2'
#///通知
BusinessType_Notice = b'3'
#///成功
CfmmcReturnCode_Success = b'0'
#///该客户已经有流程在处理中
CfmmcReturnCode_Working = b'1'
#///监控中客户资料检查失败
CfmmcReturnCode_InfoFail = b'2'
#///监控中实名制检查失败
CfmmcReturnCode_IDCardFail = b'3'
#///其他错误
CfmmcReturnCode_OtherFail = b'4'
#///所有
ClientType_All = b'0'
#///个人
ClientType_Person = b'1'
#///单位
ClientType_Company = b'2'
#///其他
ClientType_Other = b'3'
#///特殊法人
ClientType_SpecialOrgan = b'4'
#///资管户
ClientType_Asset = b'5'
#///上海期货交易所
ExchangeIDType_SHFE = b'S'
#///郑州商品交易所
ExchangeIDType_CZCE = b'Z'
#///大连商品交易所
ExchangeIDType_DCE = b'D'
#///中国金融期货交易所
ExchangeIDType_CFFEX = b'J'
#///上海国际能源交易中心股份有限公司
ExchangeIDType_INE = b'N'
#///套保
ExClientIDType_Hedge = b'1'
#///套利
ExClientIDType_Arbitrage = b'2'
#///投机
ExClientIDType_Speculation = b'3'
#///未更新
UpdateFlag_NoUpdate = b'0'
#///更新全部信息成功
UpdateFlag_Success = b'1'
#///更新全部信息失败
UpdateFlag_Fail = b'2'
#///更新交易编码成功
UpdateFlag_TCSuccess = b'3'
#///更新交易编码失败
UpdateFlag_TCFail = b'4'
#///已丢弃
UpdateFlag_Cancel = b'5'
#///开户
ApplyOperateID_OpenInvestor = b'1'
#///修改身份信息
ApplyOperateID_ModifyIDCard = b'2'
#///修改一般信息
ApplyOperateID_ModifyNoIDCard = b'3'
#///申请交易编码
ApplyOperateID_ApplyTradingCode = b'4'
#///撤销交易编码
ApplyOperateID_CancelTradingCode = b'5'
#///销户
ApplyOperateID_CancelInvestor = b'6'
#///账户休眠
ApplyOperateID_FreezeAccount = b'8'
#///激活休眠账户
ApplyOperateID_ActiveFreezeAccount = b'9'
#///未补全
ApplyStatusID_NoComplete = b'1'
#///已提交
ApplyStatusID_Submited = b'2'
#///已审核
ApplyStatusID_Checked = b'3'
#///已拒绝
ApplyStatusID_Refused = b'4'
#///已删除
ApplyStatusID_Deleted = b'5'
#///文件发送
SendMethod_ByAPI = b'1'
#///电子发送
SendMethod_ByFile = b'2'
#///增加
EventMode_ADD = b'1'
#///修改
EventMode_UPDATE = b'2'
#///删除
EventMode_DELETE = b'3'
#///复核
EventMode_CHECK = b'4'
#///复制
EventMode_COPY = b'5'
#///注销
EventMode_CANCEL = b'6'
#///冲销
EventMode_Reverse = b'7'
#///自动发送并接收
UOAAutoSend_ASR = b'1'
#///自动发送，不自动接收
UOAAutoSend_ASNR = b'2'
#///不自动发送，自动接收
UOAAutoSend_NSAR = b'3'
#///不自动发送，也不自动接收
UOAAutoSend_NSR = b'4'
#///投资者对应投资者组设置
FlowID_InvestorGroupFlow = b'1'
#///投资者手续费率设置
FlowID_InvestorRate = b'2'
#///投资者手续费率模板关系设置
FlowID_InvestorCommRateModel = b'3'
#///零级复核
CheckLevel_Zero = b'0'
#///一级复核
CheckLevel_One = b'1'
#///二级复核
CheckLevel_Two = b'2'
#///未复核
CheckStatus_Init = b'0'
#///复核中
CheckStatus_Checking = b'1'
#///已复核
CheckStatus_Checked = b'2'
#///拒绝
CheckStatus_Refuse = b'3'
#///作废
CheckStatus_Cancel = b'4'
#///未生效
UsedStatus_Unused = b'0'
#///已生效
UsedStatus_Used = b'1'
#///生效失败
UsedStatus_Fail = b'2'
#///手工录入
BankAcountOrigin_ByAccProperty = b'0'
#///银期转账
BankAcountOrigin_ByFBTransfer = b'1'
#///同日同合约
MonthBillTradeSum_ByInstrument = b'0'
#///同日同合约同价格
MonthBillTradeSum_ByDayInsPrc = b'1'
#///同合约
MonthBillTradeSum_ByDayIns = b'2'
#///银行发起银行转期货
FBTTradeCodeEnum_BankLaunchBankToBroker = b'102001'
#///期货发起银行转期货
FBTTradeCodeEnum_BrokerLaunchBankToBroker = b'202001'
#///银行发起期货转银行
FBTTradeCodeEnum_BankLaunchBrokerToBank = b'102002'
#///期货发起期货转银行
FBTTradeCodeEnum_BrokerLaunchBrokerToBank = b'202002'
#///无动态令牌
OTPType_NONE = b'0'
#///时间令牌
OTPType_TOTP = b'1'
#///未使用
OTPStatus_Unused = b'0'
#///已使用
OTPStatus_Used = b'1'
#///注销
OTPStatus_Disuse = b'2'
#///投资者
BrokerUserType_Investor = b'1'
#///操作员
BrokerUserType_BrokerUser = b'2'
#///商品期货
FutureType_Commodity = b'1'
#///金融期货
FutureType_Financial = b'2'
#///转账限额
FundEventType_Restriction = b'0'
#///当日转账限额
FundEventType_TodayRestriction = b'1'
#///期商流水
FundEventType_Transfer = b'2'
#///资金冻结
FundEventType_Credit = b'3'
#///投资者可提资金比例
FundEventType_InvestorWithdrawAlm = b'4'
#///单个银行帐户转账限额
FundEventType_BankRestriction = b'5'
#///银期签约账户
FundEventType_Accountregister = b'6'
#///交易所出入金
FundEventType_ExchangeFundIO = b'7'
#///投资者出入金
FundEventType_InvestorFundIO = b'8'
#///银期同步
AccountSourceType_FBTransfer = b'0'
#///手工录入
AccountSourceType_ManualEntry = b'1'
#///统一开户(已规范)
CodeSourceType_UnifyAccount = b'0'
#///手工录入(未规范)
CodeSourceType_ManualEntry = b'1'
#///所有
UserRange_All = b'0'
#///单一操作员
UserRange_Single = b'1'
#///按投资者统计
ByGroup_Investor = b'2'
#///按类统计
ByGroup_Group = b'1'
#///按合约统计
TradeSumStatMode_Instrument = b'1'
#///按产品统计
TradeSumStatMode_Product = b'2'
#///按交易所统计
TradeSumStatMode_Exchange = b'3'
#///相对已有规则设置
ExprSetMode_Relative = b'1'
#///典型设置
ExprSetMode_Typical = b'2'
#///公司标准
RateInvestorRange_All = b'1'
#///模板
RateInvestorRange_Model = b'2'
#///单一投资者
RateInvestorRange_Single = b'3'
#///未同步
SyncDataStatus_Initialize = b'0'
#///同步中
SyncDataStatus_Settlementing = b'1'
#///已同步
SyncDataStatus_Settlemented = b'2'
#///来自交易所普通回报
TradeSource_NORMAL = b'0'
#///来自查询
TradeSource_QUERY = b'1'
#///产品统计
FlexStatMode_Product = b'1'
#///交易所统计
FlexStatMode_Exchange = b'2'
#///统计所有
FlexStatMode_All = b'3'
#///属性统计
ByInvestorRange_Property = b'1'
#///统计所有
ByInvestorRange_All = b'2'
#///所有
PropertyInvestorRange_All = b'1'
#///投资者属性
PropertyInvestorRange_Property = b'2'
#///单一投资者
PropertyInvestorRange_Single = b'3'
#///未生成
FileStatus_NoCreate = b'0'
#///已生成
FileStatus_Created = b'1'
#///生成失败
FileStatus_Failed = b'2'
#///下发
FileGenStyle_FileTransmit = b'0'
#///生成
FileGenStyle_FileGen = b'1'
#///增加
SysOperMode_Add = b'1'
#///修改
SysOperMode_Update = b'2'
#///删除
SysOperMode_Delete = b'3'
#///复制
SysOperMode_Copy = b'4'
#///激活
SysOperMode_AcTive = b'5'
#///注销
SysOperMode_CanCel = b'6'
#///重置
SysOperMode_ReSet = b'7'
#///修改操作员密码
SysOperType_UpdatePassword = b'0'
#///操作员组织架构关系
SysOperType_UserDepartment = b'1'
#///角色管理
SysOperType_RoleManager = b'2'
#///角色功能设置
SysOperType_RoleFunction = b'3'
#///基础参数设置
SysOperType_BaseParam = b'4'
#///设置操作员
SysOperType_SetUserID = b'5'
#///用户角色设置
SysOperType_SetUserRole = b'6'
#///用户IP限制
SysOperType_UserIpRestriction = b'7'
#///组织架构管理
SysOperType_DepartmentManager = b'8'
#///组织架构向查询分类复制
SysOperType_DepartmentCopy = b'9'
#///交易编码管理
SysOperType_Tradingcode = b'A'
#///投资者状态维护
SysOperType_InvestorStatus = b'B'
#///投资者权限管理
SysOperType_InvestorAuthority = b'C'
#///属性设置
SysOperType_PropertySet = b'D'
#///重置投资者密码
SysOperType_ReSetInvestorPasswd = b'E'
#///投资者个性信息维护
SysOperType_InvestorPersonalityInfo = b'F'
#///查询当前交易日报送的数据
CSRCDataQueyType_Current = b'0'
#///查询历史报送的代理经纪公司的数据
CSRCDataQueyType_History = b'1'
#///活跃
FreezeStatus_Normal = b'1'
#///休眠
FreezeStatus_Freeze = b'0'
#///已规范
StandardStatus_Standard = b'0'
#///未规范
StandardStatus_NonStandard = b'1'
#///休眠户
RightParamType_Freeze = b'1'
#///激活休眠户
RightParamType_FreezeActive = b'2'
#///开仓权限限制
RightParamType_OpenLimit = b'3'
#///解除开仓权限限制
RightParamType_RelieveOpenLimit = b'4'
#///正常
DataStatus_Normal = b'0'
#///已删除
DataStatus_Deleted = b'1'
#///未复核
AMLCheckStatus_Init = b'0'
#///复核中
AMLCheckStatus_Checking = b'1'
#///已复核
AMLCheckStatus_Checked = b'2'
#///拒绝上报
AMLCheckStatus_RefuseReport = b'3'
#///检查日期
AmlDateType_DrawDay = b'0'
#///发生日期
AmlDateType_TouchDay = b'1'
#///零级审核
AmlCheckLevel_CheckLevel0 = b'0'
#///一级审核
AmlCheckLevel_CheckLevel1 = b'1'
#///二级审核
AmlCheckLevel_CheckLevel2 = b'2'
#///三级审核
AmlCheckLevel_CheckLevel3 = b'3'
#///CSV
ExportFileType_CSV = b'0'
#///Excel
ExportFileType_EXCEL = b'1'
#///DBF
ExportFileType_DBF = b'2'
#///结算前准备
SettleManagerType_Before = b'1'
#///结算
SettleManagerType_Settlement = b'2'
#///结算后核对
SettleManagerType_After = b'3'
#///结算后处理
SettleManagerType_Settlemented = b'4'
#///必要
SettleManagerLevel_Must = b'1'
#///警告
SettleManagerLevel_Alarm = b'2'
#///提示
SettleManagerLevel_Prompt = b'3'
#///不检查
SettleManagerLevel_Ignore = b'4'
#///交易所核对
SettleManagerGroup_Exhcange = b'1'
#///内部核对
SettleManagerGroup_ASP = b'2'
#///上报数据核对
SettleManagerGroup_CSRC = b'3'
#///可重复使用
LimitUseType_Repeatable = b'1'
#///不可重复使用
LimitUseType_Unrepeatable = b'2'
#///本系统
DataResource_Settle = b'1'
#///交易所
DataResource_Exchange = b'2'
#///报送数据
DataResource_CSRC = b'3'
#///交易所保证金率
MarginType_ExchMarginRate = b'0'
#///投资者保证金率
MarginType_InstrMarginRate = b'1'
#///投资者交易保证金率
MarginType_InstrMarginRateTrade = b'2'
#///仅当日生效
ActiveType_Intraday = b'1'
#///长期生效
ActiveType_Long = b'2'
#///交易所保证金率
MarginRateType_Exchange = b'1'
#///投资者保证金率
MarginRateType_Investor = b'2'
#///投资者交易保证金率
MarginRateType_InvestorTrade = b'3'
#///未生成备份数据
BackUpStatus_UnBak = b'0'
#///备份数据生成中
BackUpStatus_BakUp = b'1'
#///已生成备份数据
BackUpStatus_BakUped = b'2'
#///备份数据失败
BackUpStatus_BakFail = b'3'
#///结算初始化未开始
InitSettlement_UnInitialize = b'0'
#///结算初始化中
InitSettlement_Initialize = b'1'
#///结算初始化完成
InitSettlement_Initialized = b'2'
#///未生成报表数据
ReportStatus_NoCreate = b'0'
#///报表数据生成中
ReportStatus_Create = b'1'
#///已生成报表数据
ReportStatus_Created = b'2'
#///生成报表数据失败
ReportStatus_CreateFail = b'3'
#///归档未完成
SaveStatus_UnSaveData = b'0'
#///归档完成
SaveStatus_SaveDatad = b'1'
#///未归档数据
SettArchiveStatus_UnArchived = b'0'
#///数据归档中
SettArchiveStatus_Archiving = b'1'
#///已归档数据
SettArchiveStatus_Archived = b'2'
#///归档数据失败
SettArchiveStatus_ArchiveFail = b'3'
#///未知类型
CTPType_Unkown = b'0'
#///主中心
CTPType_MainCenter = b'1'
#///备中心
CTPType_BackUp = b'2'
#///正常
CloseDealType_Normal = b'0'
#///投机平仓优先
CloseDealType_SpecFirst = b'1'
#///不能使用
MortgageFundUseRange_None = b'0'
#///用于保证金
MortgageFundUseRange_Margin = b'1'
#///用于手续费、盈亏、保证金
MortgageFundUseRange_All = b'2'
#///人民币方案3
MortgageFundUseRange_CNY3 = b'3'
#///郑商所套保产品
SpecProductType_CzceHedge = b'1'
#///货币质押产品
SpecProductType_IneForeignCurrency = b'2'
#///大连短线开平仓产品
SpecProductType_DceOpenClose = b'3'
#///质押
FundMortgageType_Mortgage = b'1'
#///解质
FundMortgageType_Redemption = b'2'
#///基础保证金
AccountSettlementParamID_BaseMargin = b'1'
#///最低权益标准
AccountSettlementParamID_LowestInterest = b'2'
#///货币质入
FundMortDirection_In = b'1'
#///货币质出
FundMortDirection_Out = b'2'
#///盈利
BusinessClass_Profit = b'0'
#///亏损
BusinessClass_Loss = b'1'
#///其他
BusinessClass_Other = b'Z'
#///手工
SwapSourceType_Manual = b'0'
#///自动生成
SwapSourceType_Automatic = b'1'
#///结汇
CurrExDirection_Settlement = b'0'
#///售汇
CurrExDirection_Sale = b'1'
#///已录入
CurrencySwapStatus_Entry = b'1'
#///已审核
CurrencySwapStatus_Approve = b'2'
#///已拒绝
CurrencySwapStatus_Refuse = b'3'
#///已撤销
CurrencySwapStatus_Revoke = b'4'
#///已发送
CurrencySwapStatus_Send = b'5'
#///换汇成功
CurrencySwapStatus_Success = b'6'
#///换汇失败
CurrencySwapStatus_Failure = b'7'
#///未发送
ReqFlag_NoSend = b'0'
#///发送成功
ReqFlag_SendSuccess = b'1'
#///发送失败
ReqFlag_SendFailed = b'2'
#///等待重发
ReqFlag_WaitReSend = b'3'
#///成功
ResFlag_Success = b'0'
#///账户余额不足
ResFlag_InsuffiCient = b'1'
#///交易结果未知
ResFlag_UnKnown = b'8'
#///修改前
ExStatus_Before = b'0'
#///修改后
ExStatus_After = b'1'
#///国内客户
ClientRegion_Domestic = b'1'
#///港澳台客户
ClientRegion_GMT = b'2'
#///国外客户
ClientRegion_Foreign = b'3'
#///没有
HasBoard_No = b'0'
#///有
HasBoard_Yes = b'1'
#///正常
StartMode_Normal = b'1'
#///应急
StartMode_Emerge = b'2'
#///恢复
StartMode_Restore = b'3'
#///全量
TemplateType_Full = b'1'
#///增量
TemplateType_Increment = b'2'
#///备份
TemplateType_BackUp = b'3'
#///交易
LoginMode_Trade = b'0'
#///转账
LoginMode_Transfer = b'1'
#///合约上下市
PromptType_Instrument = b'1'
#///保证金分段生效
PromptType_Margin = b'2'
#///有
HasTrustee_Yes = b'1'
#///没有
HasTrustee_No = b'0'
#///银行
AmType_Bank = b'1'
#///证券公司
AmType_Securities = b'2'
#///基金公司
AmType_Fund = b'3'
#///保险公司
AmType_Insurance = b'4'
#///信托公司
AmType_Trust = b'5'
#///其他
AmType_Other = b'9'
#///出入金
CSRCFundIOType_FundIO = b'0'
#///银期换汇
CSRCFundIOType_SwapCurrency = b'1'
#///期货结算账户
CusAccountType_Futures = b'1'
#///纯期货资管业务下的资管结算账户
CusAccountType_AssetmgrFuture = b'2'
#///综合类资管业务下的期货资管托管账户
CusAccountType_AssetmgrTrustee = b'3'
#///综合类资管业务下的资金中转账户
CusAccountType_AssetmgrTransfer = b'4'
#///中文
LanguageType_Chinese = b'1'
#///英文
LanguageType_English = b'2'
#///个人资管客户
AssetmgrClientType_Person = b'1'
#///单位资管客户
AssetmgrClientType_Organ = b'2'
#///特殊单位资管客户
AssetmgrClientType_SpecialOrgan = b'4'
#///期货类
AssetmgrType_Futures = b'3'
#///综合类
AssetmgrType_SpecialOrgan = b'4'
#///合约交易所不存在
CheckInstrType_HasExch = b'0'
#///合约本系统不存在
CheckInstrType_HasATP = b'1'
#///合约比较不一致
CheckInstrType_HasDiff = b'2'
#///手工交割
DeliveryType_HandDeliv = b'1'
#///到期交割
DeliveryType_PersonDeliv = b'2'
#///不使用大额单边保证金算法
MaxMarginSideAlgorithm_NO = b'0'
#///使用大额单边保证金算法
MaxMarginSideAlgorithm_YES = b'1'
#///自然人
DAClientType_Person = b'0'
#///法人
DAClientType_Company = b'1'
#///其他
DAClientType_Other = b'2'
#///期货类
UOAAssetmgrType_Futures = b'1'
#///综合类
UOAAssetmgrType_SpecialOrgan = b'2'
#///Buy
DirectionEn_Buy = b'0'
#///Sell
DirectionEn_Sell = b'1'
#///Position Opening
OffsetFlagEn_Open = b'0'
#///Position Close
OffsetFlagEn_Close = b'1'
#///Forced Liquidation
OffsetFlagEn_ForceClose = b'2'
#///Close Today
OffsetFlagEn_CloseToday = b'3'
#///Close Prev.
OffsetFlagEn_CloseYesterday = b'4'
#///Forced Reduction
OffsetFlagEn_ForceOff = b'5'
#///Local Forced Liquidation
OffsetFlagEn_LocalForceClose = b'6'
#///Speculation
HedgeFlagEn_Speculation = b'1'
#///Arbitrage
HedgeFlagEn_Arbitrage = b'2'
#///Hedge
HedgeFlagEn_Hedge = b'3'
#///Deposit/Withdrawal
FundIOTypeEn_FundIO = b'1'
#///Bank-Futures Transfer
FundIOTypeEn_Transfer = b'2'
#///Bank-Futures FX Exchange
FundIOTypeEn_SwapCurrency = b'3'
#///Bank Deposit
FundTypeEn_Deposite = b'1'
#///Payment/Fee
FundTypeEn_ItemFund = b'2'
#///Brokerage Adj
FundTypeEn_Company = b'3'
#///Internal Transfer
FundTypeEn_InnerTransfer = b'4'
#///Deposit
FundDirectionEn_In = b'1'
#///Withdrawal
FundDirectionEn_Out = b'2'
#///Pledge
FundMortDirectionEn_In = b'1'
#///Redemption
FundMortDirectionEn_Out = b'2'
#///看涨
OptionsType_CallOptions = b'1'
#///看跌
OptionsType_PutOptions = b'2'
#///欧式
StrikeMode_Continental = b'0'
#///美式
StrikeMode_American = b'1'
#///百慕大
StrikeMode_Bermuda = b'2'
#///自身对冲
StrikeType_Hedge = b'0'
#///匹配执行
StrikeType_Match = b'1'
#///不执行数量
ApplyType_NotStrikeNum = b'4'
#///系统生成
GiveUpDataSource_Gen = b'0'
#///手工添加
GiveUpDataSource_Hand = b'1'
#///没有执行
ExecResult_NoExec = b'n'
#///已经取消
ExecResult_Canceled = b'c'
#///执行成功
ExecResult_OK = b'0'
#///期权持仓不够
ExecResult_NoPosition = b'1'
#///资金不够
ExecResult_NoDeposit = b'2'
#///会员不存在
ExecResult_NoParticipant = b'3'
#///客户不存在
ExecResult_NoClient = b'4'
#///合约不存在
ExecResult_NoInstrument = b'6'
#///没有执行权限
ExecResult_NoRight = b'7'
#///不合理的数量
ExecResult_InvalidVolume = b'8'
#///没有足够的历史成交
ExecResult_NoEnoughHistoryTrade = b'9'
#///未知
ExecResult_Unknown = b'a'
#///期货组合
CombinationType_Future = b'0'
#///垂直价差BUL
CombinationType_BUL = b'1'
#///垂直价差BER
CombinationType_BER = b'2'
#///跨式组合
CombinationType_STD = b'3'
#///宽跨式组合
CombinationType_STG = b'4'
#///备兑组合
CombinationType_PRT = b'5'
#///时间价差组合
CombinationType_CLD = b'6'
#///期货对锁组合
DceCombinationType_SPL = b'0'
#///期权对锁组合
DceCombinationType_OPL = b'1'
#///期货跨期组合
DceCombinationType_SP = b'2'
#///期货跨品种组合
DceCombinationType_SPC = b'3'
#///买入期权垂直价差组合
DceCombinationType_BLS = b'4'
#///卖出期权垂直价差组合
DceCombinationType_BES = b'5'
#///期权日历价差组合
DceCombinationType_CAS = b'6'
#///期权跨式组合
DceCombinationType_STD = b'7'
#///期权宽跨式组合
DceCombinationType_STG = b'8'
#///买入期货期权组合
DceCombinationType_BFO = b'9'
#///卖出期货期权组合
DceCombinationType_SFO = b'a'
#///昨结算价
OptionRoyaltyPriceType_PreSettlementPrice = b'1'
#///开仓价
OptionRoyaltyPriceType_OpenPrice = b'4'
#///最新价与昨结算价较大值
OptionRoyaltyPriceType_MaxPreSettlementPrice = b'5'
#///不计算期权市值盈亏
BalanceAlgorithm_Default = b'1'
#///计算期权市值亏损
BalanceAlgorithm_IncludeOptValLost = b'2'
#///执行
ActionType_Exec = b'1'
#///放弃
ActionType_Abandon = b'2'
#///已经提交
ForQuoteStatus_Submitted = b'a'
#///已经接受
ForQuoteStatus_Accepted = b'b'
#///已经被拒绝
ForQuoteStatus_Rejected = b'c'
#///按绝对值
ValueMethod_Absolute = b'0'
#///按比率
ValueMethod_Ratio = b'1'
#///保留
ExecOrderPositionFlag_Reserve = b'0'
#///不保留
ExecOrderPositionFlag_UnReserve = b'1'
#///自动平仓
ExecOrderCloseFlag_AutoClose = b'0'
#///免于自动平仓
ExecOrderCloseFlag_NotToClose = b'1'
#///期货
ProductType_Futures = b'1'
#///期权
ProductType_Options = b'2'
#///^\d{8}_zz_\d{4}
CZCEUploadFileName_CUFN_O = b'O'
#///^\d{8}成交表
CZCEUploadFileName_CUFN_T = b'T'
#///^\d{8}单腿持仓表new
CZCEUploadFileName_CUFN_P = b'P'
#///^\d{8}非平仓了结表
CZCEUploadFileName_CUFN_N = b'N'
#///^\d{8}平仓表
CZCEUploadFileName_CUFN_L = b'L'
#///^\d{8}资金表
CZCEUploadFileName_CUFN_F = b'F'
#///^\d{8}组合持仓表
CZCEUploadFileName_CUFN_C = b'C'
#///^\d{8}保证金参数表
CZCEUploadFileName_CUFN_M = b'M'
#///^\d{8}_dl_\d{3}
DCEUploadFileName_DUFN_O = b'O'
#///^\d{8}_成交表
DCEUploadFileName_DUFN_T = b'T'
#///^\d{8}_持仓表
DCEUploadFileName_DUFN_P = b'P'
#///^\d{8}_资金结算表
DCEUploadFileName_DUFN_F = b'F'
#///^\d{8}_优惠组合持仓明细表
DCEUploadFileName_DUFN_C = b'C'
#///^\d{8}_持仓明细表
DCEUploadFileName_DUFN_D = b'D'
#///^\d{8}_保证金参数表
DCEUploadFileName_DUFN_M = b'M'
#///^\d{8}_期权执行表
DCEUploadFileName_DUFN_S = b'S'
#///^\d{4}_\d{8}_\d{8}_DailyFundChg
SHFEUploadFileName_SUFN_O = b'O'
#///^\d{4}_\d{8}_\d{8}_Trade
SHFEUploadFileName_SUFN_T = b'T'
#///^\d{4}_\d{8}_\d{8}_SettlementDetail
SHFEUploadFileName_SUFN_P = b'P'
#///^\d{4}_\d{8}_\d{8}_Capital
SHFEUploadFileName_SUFN_F = b'F'
#///^\d{4}_SG\d{1}_\d{8}_\d{1}_Trade
CFFEXUploadFileName_SUFN_T = b'T'
#///^\d{4}_SG\d{1}_\d{8}_\d{1}_SettlementDetail
CFFEXUploadFileName_SUFN_P = b'P'
#///^\d{4}_SG\d{1}_\d{8}_\d{1}_Capital
CFFEXUploadFileName_SUFN_F = b'F'
#///^\d{4}_SG\d{1}_\d{8}_\d{1}_OptionExec
CFFEXUploadFileName_SUFN_S = b'S'
#///申请组合
CombDirection_Comb = b'0'
#///申请拆分
CombDirection_UnComb = b'1'
#///实值额
StrikeOffsetType_RealValue = b'1'
#///盈利额
StrikeOffsetType_ProfitValue = b'2'
#///实值比例
StrikeOffsetType_RealRatio = b'3'
#///盈利比例
StrikeOffsetType_ProfitRatio = b'4'
#///等待处理中
ReserveOpenAccStas_Processing = b'0'
#///已撤销
ReserveOpenAccStas_Cancelled = b'1'
#///已开户
ReserveOpenAccStas_Opened = b'2'
#///无效请求
ReserveOpenAccStas_Invalid = b'3'
#///弱密码库
WeakPasswordSource_Lib = b'1'
#///手工录入
WeakPasswordSource_Manual = b'2'
#///自对冲期权仓位
OptSelfCloseFlag_CloseSelfOptionPosition = b'1'
#///保留期权仓位
OptSelfCloseFlag_ReserveOptionPosition = b'2'
#///自对冲卖方履约后的期货仓位
OptSelfCloseFlag_SellCloseSelfFuturePosition = b'3'
#///保留卖方履约后的期货仓位
OptSelfCloseFlag_ReserveFuturePosition = b'4'
#///期货
BizType_Future = b'1'
#///证券
BizType_Stock = b'2'
#///直连的投资者
AppType_TYPE_Investor = b'1'
#///为每个投资者都创建连接的中继
AppType_TYPE_InvestorRelay = b'2'
#///所有投资者共享一个操作员连接的中继
AppType_TYPE_OperatorRelay = b'3'
#///未知
AppType_TYPE_UnKnown = b'4'
#///检查成功
ResponseValue_Right = b'0'
#///检查失败
ResponseValue_Refuse = b'1'
#///大宗交易
OTCTradeType_TRDT_Block = b'0'
#///期转现
OTCTradeType_TRDT_EFP = b'1'
#///基点价值
MatchType_MT_DV01 = b'1'
#///面值
MatchType_MT_ParValue = b'2'