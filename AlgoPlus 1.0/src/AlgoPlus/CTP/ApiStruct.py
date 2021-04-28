# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from ctypes import *
from AlgoPlus.utils.base_field import BaseField


class LocalInputOrderField(BaseField):
    _fields_ = [
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('OrderRef', c_char * 13),  # 报单引用
        ('Direction', c_char * 1),  # 买卖方向
        ('OffsetFlag', c_char * 5),  # 组合开平标志
        ('LimitPrice', c_double),  # 报单价格
        ('VolumeTotalOriginal', c_int),  # 数量
        ('VolumeTotal', c_int),  # 剩余数量
        ('OrderStatus', c_char * 1),  # 报单状态
        ('InputTime', c_float),  # 委托时间
    ]


class DisseminationField(BaseField):
    """信息分发"""
    _fields_ = [
        ('SequenceSeries', c_short),  # ///序列系列号
        ('SequenceNo', c_int)  # 序列号
    ]


class ReqUserLoginField(BaseField):
    """用户登录请求"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('Password', c_char * 41),  # 密码
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', c_char * 11),  # 协议信息
        ('MacAddress', c_char * 21),  # Mac地址
        ('OneTimePassword', c_char * 41),  # 动态密码
        ('ClientIPAddress', c_char * 16),  # 终端IP地址
        ('LoginRemark', c_char * 36),  # 登录备注
        ('ClientIPPort', c_int)  # 终端IP端口
    ]


class RspUserLoginField(BaseField):
    """用户登录应答"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('LoginTime', c_char * 9),  # 登录成功时间
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('SystemName', c_char * 41),  # 交易系统名称
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('MaxOrderRef', c_char * 13),  # 最大报单引用
        ('SHFETime', c_char * 9),  # 上期所时间
        ('DCETime', c_char * 9),  # 大商所时间
        ('CZCETime', c_char * 9),  # 郑商所时间
        ('FFEXTime', c_char * 9),  # 中金所时间
        ('INETime', c_char * 9)  # 能源中心时间
    ]


class UserLogoutField(BaseField):
    """用户登出请求"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class ForceUserLogoutField(BaseField):
    """强制交易员退出"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class ReqAuthenticateField(BaseField):
    """客户端认证请求"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('AuthCode', c_char * 17),  # 认证码
        ('AppID', c_char * 33)  # App代码
    ]


class RspAuthenticateField(BaseField):
    """客户端认证响应"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('AppID', c_char * 33),  # App代码
        ('AppType', c_char * 1)  # App类型
    ]


class AuthenticationInfoField(BaseField):
    """客户端认证信息"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('AuthInfo', c_char * 129),  # 认证信息
        ('IsResult', c_int),  # 是否为认证结果
        ('AppID', c_char * 33),  # App代码
        ('AppType', c_char * 1)  # App类型
    ]


class RspUserLogin2Field(BaseField):
    """用户登录应答2"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('LoginTime', c_char * 9),  # 登录成功时间
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('SystemName', c_char * 41),  # 交易系统名称
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('MaxOrderRef', c_char * 13),  # 最大报单引用
        ('SHFETime', c_char * 9),  # 上期所时间
        ('DCETime', c_char * 9),  # 大商所时间
        ('CZCETime', c_char * 9),  # 郑商所时间
        ('FFEXTime', c_char * 9),  # 中金所时间
        ('INETime', c_char * 9),  # 能源中心时间
        ('RandomString', c_char * 17)  # 随机串
    ]


class TransferHeaderField(BaseField):
    """银期转帐报文头"""
    _fields_ = [
        ('Version', c_char * 4),  # ///版本号，常量，1.0
        ('TradeCode', c_char * 7),  # 交易代码，必填
        ('TradeDate', c_char * 9),  # 交易日期，必填，格式：yyyymmdd
        ('TradeTime', c_char * 9),  # 交易时间，必填，格式：hhmmss
        ('TradeSerial', c_char * 9),  # 发起方流水号，N/A
        ('FutureID', c_char * 11),  # 期货公司代码，必填
        ('BankID', c_char * 4),  # 银行代码，根据查询银行得到，必填
        ('BankBrchID', c_char * 5),  # 银行分中心代码，根据查询银行得到，必填
        ('OperNo', c_char * 17),  # 操作员，N/A
        ('DeviceID', c_char * 3),  # 交易设备类型，N/A
        ('RecordNum', c_char * 7),  # 记录数，N/A
        ('SessionID', c_int),  # 会话编号，N/A
        ('RequestID', c_int)  # 请求编号，N/A
    ]


class TransferBankToFutureReqField(BaseField):
    """银行资金转期货请求，TradeCode=202001"""
    _fields_ = [
        ('FutureAccount', c_char * 13),  # ///期货资金账户
        ('FuturePwdFlag', c_char * 1),  # 密码标志
        ('FutureAccPwd', c_char * 17),  # 密码
        ('TradeAmt', c_double),  # 转账金额
        ('CustFee', c_double),  # 客户手续费
        ('CurrencyCode', c_char * 4)  # 币种：RMB-人民币 USD-美圆 HKD-港元
    ]


class TransferBankToFutureRspField(BaseField):
    """银行资金转期货请求响应"""
    _fields_ = [
        ('RetCode', c_char * 5),  # ///响应代码
        ('RetInfo', c_char * 129),  # 响应信息
        ('FutureAccount', c_char * 13),  # 资金账户
        ('TradeAmt', c_double),  # 转帐金额
        ('CustFee', c_double),  # 应收客户手续费
        ('CurrencyCode', c_char * 4)  # 币种
    ]


class TransferFutureToBankReqField(BaseField):
    """期货资金转银行请求，TradeCode=202002"""
    _fields_ = [
        ('FutureAccount', c_char * 13),  # ///期货资金账户
        ('FuturePwdFlag', c_char * 1),  # 密码标志
        ('FutureAccPwd', c_char * 17),  # 密码
        ('TradeAmt', c_double),  # 转账金额
        ('CustFee', c_double),  # 客户手续费
        ('CurrencyCode', c_char * 4)  # 币种：RMB-人民币 USD-美圆 HKD-港元
    ]


class TransferFutureToBankRspField(BaseField):
    """期货资金转银行请求响应"""
    _fields_ = [
        ('RetCode', c_char * 5),  # ///响应代码
        ('RetInfo', c_char * 129),  # 响应信息
        ('FutureAccount', c_char * 13),  # 资金账户
        ('TradeAmt', c_double),  # 转帐金额
        ('CustFee', c_double),  # 应收客户手续费
        ('CurrencyCode', c_char * 4)  # 币种
    ]


class TransferQryBankReqField(BaseField):
    """查询银行资金请求，TradeCode=204002"""
    _fields_ = [
        ('FutureAccount', c_char * 13),  # ///期货资金账户
        ('FuturePwdFlag', c_char * 1),  # 密码标志
        ('FutureAccPwd', c_char * 17),  # 密码
        ('CurrencyCode', c_char * 4)  # 币种：RMB-人民币 USD-美圆 HKD-港元
    ]


class TransferQryBankRspField(BaseField):
    """查询银行资金请求响应"""
    _fields_ = [
        ('RetCode', c_char * 5),  # ///响应代码
        ('RetInfo', c_char * 129),  # 响应信息
        ('FutureAccount', c_char * 13),  # 资金账户
        ('TradeAmt', c_double),  # 银行余额
        ('UseAmt', c_double),  # 银行可用余额
        ('FetchAmt', c_double),  # 银行可取余额
        ('CurrencyCode', c_char * 4)  # 币种
    ]


class TransferQryDetailReqField(BaseField):
    """查询银行交易明细请求，TradeCode=204999"""
    _fields_ = [
        ('FutureAccount', c_char * 13)  # ///期货资金账户
    ]


class TransferQryDetailRspField(BaseField):
    """查询银行交易明细请求响应"""
    _fields_ = [
        ('TradeDate', c_char * 9),  # ///交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('TradeCode', c_char * 7),  # 交易代码
        ('FutureSerial', c_int),  # 期货流水号
        ('FutureID', c_char * 11),  # 期货公司代码
        ('FutureAccount', c_char * 22),  # 资金帐号
        ('BankSerial', c_int),  # 银行流水号
        ('BankID', c_char * 4),  # 银行代码
        ('BankBrchID', c_char * 5),  # 银行分中心代码
        ('BankAccount', c_char * 41),  # 银行账号
        ('CertCode', c_char * 21),  # 证件号码
        ('CurrencyCode', c_char * 4),  # 货币代码
        ('TxAmount', c_double),  # 发生金额
        ('Flag', c_char * 1)  # 有效标志
    ]


class RspInfoField(BaseField):
    """响应信息"""
    _fields_ = [
        ('ErrorID', c_int),  # ///错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class ExchangeField(BaseField):
    """交易所"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('ExchangeName', c_char * 61),  # 交易所名称
        ('ExchangeProperty', c_char * 1)  # 交易所属性
    ]


class ProductField(BaseField):
    """产品"""
    _fields_ = [
        ('ProductID', c_char * 31),  # ///产品代码
        ('ProductName', c_char * 21),  # 产品名称
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ProductClass', c_char * 1),  # 产品类型
        ('VolumeMultiple', c_int),  # 合约数量乘数
        ('PriceTick', c_double),  # 最小变动价位
        ('MaxMarketOrderVolume', c_int),  # 市价单最大下单量
        ('MinMarketOrderVolume', c_int),  # 市价单最小下单量
        ('MaxLimitOrderVolume', c_int),  # 限价单最大下单量
        ('MinLimitOrderVolume', c_int),  # 限价单最小下单量
        ('PositionType', c_char * 1),  # 持仓类型
        ('PositionDateType', c_char * 1),  # 持仓日期类型
        ('CloseDealType', c_char * 1),  # 平仓处理类型
        ('TradeCurrencyID', c_char * 4),  # 交易币种类型
        ('MortgageFundUseRange', c_char * 1),  # 质押资金可用范围
        ('ExchangeProductID', c_char * 31),  # 交易所产品代码
        ('UnderlyingMultiple', c_double)  # 合约基础商品乘数
    ]


class InstrumentField(BaseField):
    """合约"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InstrumentName', c_char * 21),  # 合约名称
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('ProductID', c_char * 31),  # 产品代码
        ('ProductClass', c_char * 1),  # 产品类型
        ('DeliveryYear', c_int),  # 交割年份
        ('DeliveryMonth', c_int),  # 交割月
        ('MaxMarketOrderVolume', c_int),  # 市价单最大下单量
        ('MinMarketOrderVolume', c_int),  # 市价单最小下单量
        ('MaxLimitOrderVolume', c_int),  # 限价单最大下单量
        ('MinLimitOrderVolume', c_int),  # 限价单最小下单量
        ('VolumeMultiple', c_int),  # 合约数量乘数
        ('PriceTick', c_double),  # 最小变动价位
        ('CreateDate', c_char * 9),  # 创建日
        ('OpenDate', c_char * 9),  # 上市日
        ('ExpireDate', c_char * 9),  # 到期日
        ('StartDelivDate', c_char * 9),  # 开始交割日
        ('EndDelivDate', c_char * 9),  # 结束交割日
        ('InstLifePhase', c_char * 1),  # 合约生命周期状态
        ('IsTrading', c_int),  # 当前是否交易
        ('PositionType', c_char * 1),  # 持仓类型
        ('PositionDateType', c_char * 1),  # 持仓日期类型
        ('LongMarginRatio', c_double),  # 多头保证金率
        ('ShortMarginRatio', c_double),  # 空头保证金率
        ('MaxMarginSideAlgorithm', c_char * 1),  # 是否使用大额单边保证金算法
        ('UnderlyingInstrID', c_char * 31),  # 基础商品代码
        ('StrikePrice', c_double),  # 执行价
        ('OptionsType', c_char * 1),  # 期权类型
        ('UnderlyingMultiple', c_double),  # 合约基础商品乘数
        ('CombinationType', c_char * 1)  # 组合类型
    ]


class BrokerField(BaseField):
    """经纪公司"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('BrokerAbbr', c_char * 9),  # 经纪公司简称
        ('BrokerName', c_char * 81),  # 经纪公司名称
        ('IsActive', c_int)  # 是否活跃
    ]


class TraderField(BaseField):
    """交易所交易员"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('Password', c_char * 41),  # 密码
        ('InstallCount', c_int),  # 安装数量
        ('BrokerID', c_char * 11)  # 经纪公司代码
    ]


class InvestorField(BaseField):
    """投资者"""
    _fields_ = [
        ('InvestorID', c_char * 13),  # ///投资者代码
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorGroupID', c_char * 13),  # 投资者分组代码
        ('InvestorName', c_char * 81),  # 投资者名称
        ('IdentifiedCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('IsActive', c_int),  # 是否活跃
        ('Telephone', c_char * 41),  # 联系电话
        ('Address', c_char * 101),  # 通讯地址
        ('OpenDate', c_char * 9),  # 开户日期
        ('Mobile', c_char * 41),  # 手机
        ('CommModelID', c_char * 13),  # 手续费率模板代码
        ('MarginModelID', c_char * 13)  # 保证金率模板代码
    ]


class TradingCodeField(BaseField):
    """交易编码"""
    _fields_ = [
        ('InvestorID', c_char * 13),  # ///投资者代码
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ClientID', c_char * 11),  # 客户代码
        ('IsActive', c_int),  # 是否活跃
        ('ClientIDType', c_char * 1),  # 交易编码类型
        ('BranchID', c_char * 9),  # 营业部编号
        ('BizType', c_char * 1),  # 业务类型
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class PartBrokerField(BaseField):
    """会员编码和经纪公司编码对照表"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('IsActive', c_int)  # 是否活跃
    ]


class SuperUserField(BaseField):
    """管理用户"""
    _fields_ = [
        ('UserID', c_char * 16),  # ///用户代码
        ('UserName', c_char * 81),  # 用户名称
        ('Password', c_char * 41),  # 密码
        ('IsActive', c_int)  # 是否活跃
    ]


class SuperUserFunctionField(BaseField):
    """管理用户功能权限"""
    _fields_ = [
        ('UserID', c_char * 16),  # ///用户代码
        ('FunctionCode', c_char * 1)  # 功能代码
    ]


class InvestorGroupField(BaseField):
    """投资者组"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorGroupID', c_char * 13),  # 投资者分组代码
        ('InvestorGroupName', c_char * 41)  # 投资者分组名称
    ]


class TradingAccountField(BaseField):
    """资金账户"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('PreMortgage', c_double),  # 上次质押金额
        ('PreCredit', c_double),  # 上次信用额度
        ('PreDeposit', c_double),  # 上次存款额
        ('PreBalance', c_double),  # 上次结算准备金
        ('PreMargin', c_double),  # 上次占用的保证金
        ('InterestBase', c_double),  # 利息基数
        ('Interest', c_double),  # 利息收入
        ('Deposit', c_double),  # 入金金额
        ('Withdraw', c_double),  # 出金金额
        ('FrozenMargin', c_double),  # 冻结的保证金
        ('FrozenCash', c_double),  # 冻结的资金
        ('FrozenCommission', c_double),  # 冻结的手续费
        ('CurrMargin', c_double),  # 当前保证金总额
        ('CashIn', c_double),  # 资金差额
        ('Commission', c_double),  # 手续费
        ('CloseProfit', c_double),  # 平仓盈亏
        ('PositionProfit', c_double),  # 持仓盈亏
        ('Balance', c_double),  # 期货结算准备金
        ('Available', c_double),  # 可用资金
        ('WithdrawQuota', c_double),  # 可取资金
        ('Reserve', c_double),  # 基本准备金
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('Credit', c_double),  # 信用额度
        ('Mortgage', c_double),  # 质押金额
        ('ExchangeMargin', c_double),  # 交易所保证金
        ('DeliveryMargin', c_double),  # 投资者交割保证金
        ('ExchangeDeliveryMargin', c_double),  # 交易所交割保证金
        ('ReserveBalance', c_double),  # 保底期货结算准备金
        ('CurrencyID', c_char * 4),  # 币种代码
        ('PreFundMortgageIn', c_double),  # 上次货币质入金额
        ('PreFundMortgageOut', c_double),  # 上次货币质出金额
        ('FundMortgageIn', c_double),  # 货币质入金额
        ('FundMortgageOut', c_double),  # 货币质出金额
        ('FundMortgageAvailable', c_double),  # 货币质押余额
        ('MortgageableFund', c_double),  # 可质押货币金额
        ('SpecProductMargin', c_double),  # 特殊产品占用保证金
        ('SpecProductFrozenMargin', c_double),  # 特殊产品冻结保证金
        ('SpecProductCommission', c_double),  # 特殊产品手续费
        ('SpecProductFrozenCommission', c_double),  # 特殊产品冻结手续费
        ('SpecProductPositionProfit', c_double),  # 特殊产品持仓盈亏
        ('SpecProductCloseProfit', c_double),  # 特殊产品平仓盈亏
        ('SpecProductPositionProfitByAlg', c_double),  # 根据持仓盈亏算法计算的特殊产品持仓盈亏
        ('SpecProductExchangeMargin', c_double),  # 特殊产品交易所保证金
        ('BizType', c_char * 1),  # 业务类型
        ('FrozenSwap', c_double),  # 延时换汇冻结金额
        ('RemainSwap', c_double)  # 剩余换汇额度
    ]


class InvestorPositionField(BaseField):
    """投资者持仓"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('PosiDirection', c_char * 1),  # 持仓多空方向
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('PositionDate', c_char * 1),  # 持仓日期
        ('YdPosition', c_int),  # 上日持仓
        ('Position', c_int),  # 今日持仓
        ('LongFrozen', c_int),  # 多头冻结
        ('ShortFrozen', c_int),  # 空头冻结
        ('LongFrozenAmount', c_double),  # 开仓冻结金额
        ('ShortFrozenAmount', c_double),  # 开仓冻结金额
        ('OpenVolume', c_int),  # 开仓量
        ('CloseVolume', c_int),  # 平仓量
        ('OpenAmount', c_double),  # 开仓金额
        ('CloseAmount', c_double),  # 平仓金额
        ('PositionCost', c_double),  # 持仓成本
        ('PreMargin', c_double),  # 上次占用的保证金
        ('UseMargin', c_double),  # 占用的保证金
        ('FrozenMargin', c_double),  # 冻结的保证金
        ('FrozenCash', c_double),  # 冻结的资金
        ('FrozenCommission', c_double),  # 冻结的手续费
        ('CashIn', c_double),  # 资金差额
        ('Commission', c_double),  # 手续费
        ('CloseProfit', c_double),  # 平仓盈亏
        ('PositionProfit', c_double),  # 持仓盈亏
        ('PreSettlementPrice', c_double),  # 上次结算价
        ('SettlementPrice', c_double),  # 本次结算价
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('OpenCost', c_double),  # 开仓成本
        ('ExchangeMargin', c_double),  # 交易所保证金
        ('CombPosition', c_int),  # 组合成交形成的持仓
        ('CombLongFrozen', c_int),  # 组合多头冻结
        ('CombShortFrozen', c_int),  # 组合空头冻结
        ('CloseProfitByDate', c_double),  # 逐日盯市平仓盈亏
        ('CloseProfitByTrade', c_double),  # 逐笔对冲平仓盈亏
        ('TodayPosition', c_int),  # 今日持仓
        ('MarginRateByMoney', c_double),  # 保证金率
        ('MarginRateByVolume', c_double),  # 保证金率(按手数)
        ('StrikeFrozen', c_int),  # 执行冻结
        ('StrikeFrozenAmount', c_double),  # 执行冻结金额
        ('AbandonFrozen', c_int),  # 放弃执行冻结
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('YdStrikeFrozen', c_int),  # 执行冻结的昨仓
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('PositionCostOffset', c_double)  # 大商所持仓成本差值，只有大商所使用
    ]


class InstrumentMarginRateField(BaseField):
    """合约保证金率"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('LongMarginRatioByMoney', c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', c_double),  # 空头保证金费
        ('IsRelative', c_int),  # 是否相对交易所收取
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class InstrumentCommissionRateField(BaseField):
    """合约手续费率"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', c_double),  # 开仓手续费率
        ('OpenRatioByVolume', c_double),  # 开仓手续费
        ('CloseRatioByMoney', c_double),  # 平仓手续费率
        ('CloseRatioByVolume', c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', c_double),  # 平今手续费
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('BizType', c_char * 1),  # 业务类型
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class DepthMarketDataField(BaseField):
    """深度行情"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('LastPrice', c_double),  # 最新价
        ('PreSettlementPrice', c_double),  # 上次结算价
        ('PreClosePrice', c_double),  # 昨收盘
        ('PreOpenInterest', c_double),  # 昨持仓量
        ('OpenPrice', c_double),  # 今开盘
        ('HighestPrice', c_double),  # 最高价
        ('LowestPrice', c_double),  # 最低价
        ('Volume', c_int),  # 数量
        ('Turnover', c_double),  # 成交金额
        ('OpenInterest', c_double),  # 持仓量
        ('ClosePrice', c_double),  # 今收盘
        ('SettlementPrice', c_double),  # 本次结算价
        ('UpperLimitPrice', c_double),  # 涨停板价
        ('LowerLimitPrice', c_double),  # 跌停板价
        ('PreDelta', c_double),  # 昨虚实度
        ('CurrDelta', c_double),  # 今虚实度
        ('UpdateTime', c_char * 9),  # 最后修改时间
        ('UpdateMillisec', c_int),  # 最后修改毫秒
        ('BidPrice1', c_double),  # 申买价一
        ('BidVolume1', c_int),  # 申买量一
        ('AskPrice1', c_double),  # 申卖价一
        ('AskVolume1', c_int),  # 申卖量一
        ('BidPrice2', c_double),  # 申买价二
        ('BidVolume2', c_int),  # 申买量二
        ('AskPrice2', c_double),  # 申卖价二
        ('AskVolume2', c_int),  # 申卖量二
        ('BidPrice3', c_double),  # 申买价三
        ('BidVolume3', c_int),  # 申买量三
        ('AskPrice3', c_double),  # 申卖价三
        ('AskVolume3', c_int),  # 申卖量三
        ('BidPrice4', c_double),  # 申买价四
        ('BidVolume4', c_int),  # 申买量四
        ('AskPrice4', c_double),  # 申卖价四
        ('AskVolume4', c_int),  # 申卖量四
        ('BidPrice5', c_double),  # 申买价五
        ('BidVolume5', c_int),  # 申买量五
        ('AskPrice5', c_double),  # 申卖价五
        ('AskVolume5', c_int),  # 申卖量五
        ('AveragePrice', c_double),  # 当日均价
        ('ActionDay', c_char * 9)  # 业务日期
    ]


class InstrumentTradingRightField(BaseField):
    """投资者合约交易权限"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('TradingRight', c_char * 1)  # 交易权限
    ]


class BrokerUserField(BaseField):
    """经纪公司用户"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('UserName', c_char * 81),  # 用户名称
        ('UserType', c_char * 1),  # 用户类型
        ('IsActive', c_int),  # 是否活跃
        ('IsUsingOTP', c_int),  # 是否使用令牌
        ('IsAuthForce', c_int)  # 是否强制终端认证
    ]


class BrokerUserPasswordField(BaseField):
    """经纪公司用户口令"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('Password', c_char * 41),  # 密码
        ('LastUpdateTime', c_char * 17),  # 上次修改时间
        ('LastLoginTime', c_char * 17),  # 上次登陆时间
        ('ExpireDate', c_char * 9),  # 密码过期时间
        ('WeakExpireDate', c_char * 9)  # 弱密码过期时间
    ]


class BrokerUserFunctionField(BaseField):
    """经纪公司用户功能权限"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('BrokerFunctionCode', c_char * 1)  # 经纪公司功能代码
    ]


class TraderOfferField(BaseField):
    """交易所交易员报盘机"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('Password', c_char * 41),  # 密码
        ('InstallID', c_int),  # 安装编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('TraderConnectStatus', c_char * 1),  # 交易所交易员连接状态
        ('ConnectRequestDate', c_char * 9),  # 发出连接请求的日期
        ('ConnectRequestTime', c_char * 9),  # 发出连接请求的时间
        ('LastReportDate', c_char * 9),  # 上次报告日期
        ('LastReportTime', c_char * 9),  # 上次报告时间
        ('ConnectDate', c_char * 9),  # 完成连接日期
        ('ConnectTime', c_char * 9),  # 完成连接时间
        ('StartDate', c_char * 9),  # 启动日期
        ('StartTime', c_char * 9),  # 启动时间
        ('TradingDay', c_char * 9),  # 交易日
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('MaxTradeID', c_char * 21),  # 本席位最大成交编号
        ('MaxOrderMessageReference', c_char * 7)  # 本席位最大报单备拷
    ]


class SettlementInfoField(BaseField):
    """投资者结算结果"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('SettlementID', c_int),  # 结算编号
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('SequenceNo', c_int),  # 序号
        ('Content', c_char * 501),  # 消息正文
        ('AccountID', c_char * 13),  # 投资者帐号
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class InstrumentMarginRateAdjustField(BaseField):
    """合约保证金率调整"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('LongMarginRatioByMoney', c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', c_double),  # 空头保证金费
        ('IsRelative', c_int)  # 是否相对交易所收取
    ]


class ExchangeMarginRateField(BaseField):
    """交易所保证金率"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('LongMarginRatioByMoney', c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', c_double),  # 空头保证金费
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class ExchangeMarginRateAdjustField(BaseField):
    """交易所保证金率调整"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('LongMarginRatioByMoney', c_double),  # 跟随交易所投资者多头保证金率
        ('LongMarginRatioByVolume', c_double),  # 跟随交易所投资者多头保证金费
        ('ShortMarginRatioByMoney', c_double),  # 跟随交易所投资者空头保证金率
        ('ShortMarginRatioByVolume', c_double),  # 跟随交易所投资者空头保证金费
        ('ExchLongMarginRatioByMoney', c_double),  # 交易所多头保证金率
        ('ExchLongMarginRatioByVolume', c_double),  # 交易所多头保证金费
        ('ExchShortMarginRatioByMoney', c_double),  # 交易所空头保证金率
        ('ExchShortMarginRatioByVolume', c_double),  # 交易所空头保证金费
        ('NoLongMarginRatioByMoney', c_double),  # 不跟随交易所投资者多头保证金率
        ('NoLongMarginRatioByVolume', c_double),  # 不跟随交易所投资者多头保证金费
        ('NoShortMarginRatioByMoney', c_double),  # 不跟随交易所投资者空头保证金率
        ('NoShortMarginRatioByVolume', c_double)  # 不跟随交易所投资者空头保证金费
    ]


class ExchangeRateField(BaseField):
    """汇率"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('FromCurrencyID', c_char * 4),  # 源币种
        ('FromCurrencyUnit', c_double),  # 源币种单位数量
        ('ToCurrencyID', c_char * 4),  # 目标币种
        ('ExchangeRate', c_double)  # 汇率
    ]


class SettlementRefField(BaseField):
    """结算引用"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('SettlementID', c_int)  # 结算编号
    ]


class CurrentTimeField(BaseField):
    """当前时间"""
    _fields_ = [
        ('CurrDate', c_char * 9),  # ///当前日期
        ('CurrTime', c_char * 9),  # 当前时间
        ('CurrMillisec', c_int),  # 当前时间（毫秒）
        ('ActionDay', c_char * 9)  # 业务日期
    ]


class CommPhaseField(BaseField):
    """通讯阶段"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('CommPhaseNo', c_short),  # 通讯时段编号
        ('SystemID', c_char * 21)  # 系统编号
    ]


class LoginInfoField(BaseField):
    """登录信息"""
    _fields_ = [
        ('FrontID', c_int),  # ///前置编号
        ('SessionID', c_int),  # 会话编号
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('LoginDate', c_char * 9),  # 登录日期
        ('LoginTime', c_char * 9),  # 登录时间
        ('IPAddress', c_char * 16),  # IP地址
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', c_char * 11),  # 协议信息
        ('SystemName', c_char * 41),  # 系统名称
        ('PasswordDeprecated', c_char * 41),  # 密码,已弃用
        ('MaxOrderRef', c_char * 13),  # 最大报单引用
        ('SHFETime', c_char * 9),  # 上期所时间
        ('DCETime', c_char * 9),  # 大商所时间
        ('CZCETime', c_char * 9),  # 郑商所时间
        ('FFEXTime', c_char * 9),  # 中金所时间
        ('MacAddress', c_char * 21),  # Mac地址
        ('OneTimePassword', c_char * 41),  # 动态密码
        ('INETime', c_char * 9),  # 能源中心时间
        ('IsQryControl', c_int),  # 查询时是否需要流控
        ('LoginRemark', c_char * 36),  # 登录备注
        ('Password', c_char * 41)  # 密码
    ]


class LogoutAllField(BaseField):
    """登录信息"""
    _fields_ = [
        ('FrontID', c_int),  # ///前置编号
        ('SessionID', c_int),  # 会话编号
        ('SystemName', c_char * 41)  # 系统名称
    ]


class FrontStatusField(BaseField):
    """前置状态"""
    _fields_ = [
        ('FrontID', c_int),  # ///前置编号
        ('LastReportDate', c_char * 9),  # 上次报告日期
        ('LastReportTime', c_char * 9),  # 上次报告时间
        ('IsActive', c_int)  # 是否活跃
    ]


class UserPasswordUpdateField(BaseField):
    """用户口令变更"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('OldPassword', c_char * 41),  # 原来的口令
        ('NewPassword', c_char * 41)  # 新的口令
    ]


class InputOrderField(BaseField):
    """输入报单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('OrderRef', c_char * 13),  # 报单引用
        ('UserID', c_char * 16),  # 用户代码
        ('OrderPriceType', c_char * 1),  # 报单价格条件
        ('Direction', c_char * 1),  # 买卖方向
        ('CombOffsetFlag', c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', c_char * 5),  # 组合投机套保标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeTotalOriginal', c_int),  # 数量
        ('TimeCondition', c_char * 1),  # 有效期类型
        ('GTDDate', c_char * 9),  # GTD日期
        ('VolumeCondition', c_char * 1),  # 成交量类型
        ('MinVolume', c_int),  # 最小成交量
        ('ContingentCondition', c_char * 1),  # 触发条件
        ('StopPrice', c_double),  # 止损价
        ('ForceCloseReason', c_char * 1),  # 强平原因
        ('IsAutoSuspend', c_int),  # 自动挂起标志
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('RequestID', c_int),  # 请求编号
        ('UserForceClose', c_int),  # 用户强评标志
        ('IsSwapOrder', c_int),  # 互换单标志
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('ClientID', c_char * 11),  # 交易编码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class OrderField(BaseField):
    """报单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('OrderRef', c_char * 13),  # 报单引用
        ('UserID', c_char * 16),  # 用户代码
        ('OrderPriceType', c_char * 1),  # 报单价格条件
        ('Direction', c_char * 1),  # 买卖方向
        ('CombOffsetFlag', c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', c_char * 5),  # 组合投机套保标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeTotalOriginal', c_int),  # 数量
        ('TimeCondition', c_char * 1),  # 有效期类型
        ('GTDDate', c_char * 9),  # GTD日期
        ('VolumeCondition', c_char * 1),  # 成交量类型
        ('MinVolume', c_int),  # 最小成交量
        ('ContingentCondition', c_char * 1),  # 触发条件
        ('StopPrice', c_double),  # 止损价
        ('ForceCloseReason', c_char * 1),  # 强平原因
        ('IsAutoSuspend', c_int),  # 自动挂起标志
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('RequestID', c_int),  # 请求编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderSubmitStatus', c_char * 1),  # 报单提交状态
        ('NotifySequence', c_int),  # 报单提示序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('OrderSysID', c_char * 21),  # 报单编号
        ('OrderSource', c_char * 1),  # 报单来源
        ('OrderStatus', c_char * 1),  # 报单状态
        ('OrderType', c_char * 1),  # 报单类型
        ('VolumeTraded', c_int),  # 今成交数量
        ('VolumeTotal', c_int),  # 剩余数量
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 委托时间
        ('ActiveTime', c_char * 9),  # 激活时间
        ('SuspendTime', c_char * 9),  # 挂起时间
        ('UpdateTime', c_char * 9),  # 最后修改时间
        ('CancelTime', c_char * 9),  # 撤销时间
        ('ActiveTraderID', c_char * 21),  # 最后修改交易所交易员代码
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('SequenceNo', c_int),  # 序号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('StatusMsg', c_char * 81),  # 状态信息
        ('UserForceClose', c_int),  # 用户强评标志
        ('ActiveUserID', c_char * 16),  # 操作用户代码
        ('BrokerOrderSeq', c_int),  # 经纪公司报单编号
        ('RelativeOrderSysID', c_char * 21),  # 相关报单
        ('ZCETotalTradedVolume', c_int),  # 郑商所成交数量
        ('IsSwapOrder', c_int),  # 互换单标志
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ExchangeOrderField(BaseField):
    """交易所报单"""
    _fields_ = [
        ('OrderPriceType', c_char * 1),  # ///报单价格条件
        ('Direction', c_char * 1),  # 买卖方向
        ('CombOffsetFlag', c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', c_char * 5),  # 组合投机套保标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeTotalOriginal', c_int),  # 数量
        ('TimeCondition', c_char * 1),  # 有效期类型
        ('GTDDate', c_char * 9),  # GTD日期
        ('VolumeCondition', c_char * 1),  # 成交量类型
        ('MinVolume', c_int),  # 最小成交量
        ('ContingentCondition', c_char * 1),  # 触发条件
        ('StopPrice', c_double),  # 止损价
        ('ForceCloseReason', c_char * 1),  # 强平原因
        ('IsAutoSuspend', c_int),  # 自动挂起标志
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('RequestID', c_int),  # 请求编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderSubmitStatus', c_char * 1),  # 报单提交状态
        ('NotifySequence', c_int),  # 报单提示序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('OrderSysID', c_char * 21),  # 报单编号
        ('OrderSource', c_char * 1),  # 报单来源
        ('OrderStatus', c_char * 1),  # 报单状态
        ('OrderType', c_char * 1),  # 报单类型
        ('VolumeTraded', c_int),  # 今成交数量
        ('VolumeTotal', c_int),  # 剩余数量
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 委托时间
        ('ActiveTime', c_char * 9),  # 激活时间
        ('SuspendTime', c_char * 9),  # 挂起时间
        ('UpdateTime', c_char * 9),  # 最后修改时间
        ('CancelTime', c_char * 9),  # 撤销时间
        ('ActiveTraderID', c_char * 21),  # 最后修改交易所交易员代码
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('SequenceNo', c_int),  # 序号
        ('BranchID', c_char * 9),  # 营业部编号
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ExchangeOrderInsertErrorField(BaseField):
    """交易所报单插入失败"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class InputOrderActionField(BaseField):
    """输入报单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OrderActionRef', c_int),  # 报单操作引用
        ('OrderRef', c_char * 13),  # 报单引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('OrderSysID', c_char * 21),  # 报单编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeChange', c_int),  # 数量变化
        ('UserID', c_char * 16),  # 用户代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class OrderActionField(BaseField):
    """报单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OrderActionRef', c_int),  # 报单操作引用
        ('OrderRef', c_char * 13),  # 报单引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('OrderSysID', c_char * 21),  # 报单编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeChange', c_int),  # 数量变化
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('StatusMsg', c_char * 81),  # 状态信息
        ('InstrumentID', c_char * 31),  # 合约代码
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ExchangeOrderActionField(BaseField):
    """交易所报单操作"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('OrderSysID', c_char * 21),  # 报单编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeChange', c_int),  # 数量变化
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('BranchID', c_char * 9),  # 营业部编号
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ExchangeOrderActionErrorField(BaseField):
    """交易所报单操作失败"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('OrderSysID', c_char * 21),  # 报单编号
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class ExchangeTradeField(BaseField):
    """交易所成交"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('TradeID', c_char * 21),  # 成交编号
        ('Direction', c_char * 1),  # 买卖方向
        ('OrderSysID', c_char * 21),  # 报单编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('TradingRole', c_char * 1),  # 交易角色
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('OffsetFlag', c_char * 1),  # 开平标志
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('Price', c_double),  # 价格
        ('Volume', c_int),  # 数量
        ('TradeDate', c_char * 9),  # 成交时期
        ('TradeTime', c_char * 9),  # 成交时间
        ('TradeType', c_char * 1),  # 成交类型
        ('PriceSource', c_char * 1),  # 成交价来源
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('SequenceNo', c_int),  # 序号
        ('TradeSource', c_char * 1)  # 成交来源
    ]


class TradeField(BaseField):
    """成交"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('OrderRef', c_char * 13),  # 报单引用
        ('UserID', c_char * 16),  # 用户代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TradeID', c_char * 21),  # 成交编号
        ('Direction', c_char * 1),  # 买卖方向
        ('OrderSysID', c_char * 21),  # 报单编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('TradingRole', c_char * 1),  # 交易角色
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('OffsetFlag', c_char * 1),  # 开平标志
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('Price', c_double),  # 价格
        ('Volume', c_int),  # 数量
        ('TradeDate', c_char * 9),  # 成交时期
        ('TradeTime', c_char * 9),  # 成交时间
        ('TradeType', c_char * 1),  # 成交类型
        ('PriceSource', c_char * 1),  # 成交价来源
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('SequenceNo', c_int),  # 序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('BrokerOrderSeq', c_int),  # 经纪公司报单编号
        ('TradeSource', c_char * 1),  # 成交来源
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class UserSessionField(BaseField):
    """用户会话"""
    _fields_ = [
        ('FrontID', c_int),  # ///前置编号
        ('SessionID', c_int),  # 会话编号
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('LoginDate', c_char * 9),  # 登录日期
        ('LoginTime', c_char * 9),  # 登录时间
        ('IPAddress', c_char * 16),  # IP地址
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', c_char * 11),  # 协议信息
        ('MacAddress', c_char * 21),  # Mac地址
        ('LoginRemark', c_char * 36)  # 登录备注
    ]


class QueryMaxOrderVolumeField(BaseField):
    """查询最大报单数量"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('Direction', c_char * 1),  # 买卖方向
        ('OffsetFlag', c_char * 1),  # 开平标志
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('MaxVolume', c_int),  # 最大允许报单数量
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class SettlementInfoConfirmField(BaseField):
    """投资者结算结果确认信息"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ConfirmDate', c_char * 9),  # 确认日期
        ('ConfirmTime', c_char * 9),  # 确认时间
        ('SettlementID', c_int),  # 结算编号
        ('AccountID', c_char * 13),  # 投资者帐号
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class SyncDepositField(BaseField):
    """出入金同步"""
    _fields_ = [
        ('DepositSeqNo', c_char * 15),  # ///出入金流水号
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('Deposit', c_double),  # 入金金额
        ('IsForce', c_int),  # 是否强制进行
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class SyncFundMortgageField(BaseField):
    """货币质押同步"""
    _fields_ = [
        ('MortgageSeqNo', c_char * 15),  # ///货币质押流水号
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('FromCurrencyID', c_char * 4),  # 源币种
        ('MortgageAmount', c_double),  # 质押金额
        ('ToCurrencyID', c_char * 4)  # 目标币种
    ]


class BrokerSyncField(BaseField):
    """经纪公司同步"""
    _fields_ = [
        ('BrokerID', c_char * 11)  # ///经纪公司代码
    ]


class SyncingInvestorField(BaseField):
    """正在同步中的投资者"""
    _fields_ = [
        ('InvestorID', c_char * 13),  # ///投资者代码
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorGroupID', c_char * 13),  # 投资者分组代码
        ('InvestorName', c_char * 81),  # 投资者名称
        ('IdentifiedCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('IsActive', c_int),  # 是否活跃
        ('Telephone', c_char * 41),  # 联系电话
        ('Address', c_char * 101),  # 通讯地址
        ('OpenDate', c_char * 9),  # 开户日期
        ('Mobile', c_char * 41),  # 手机
        ('CommModelID', c_char * 13),  # 手续费率模板代码
        ('MarginModelID', c_char * 13)  # 保证金率模板代码
    ]


class SyncingTradingCodeField(BaseField):
    """正在同步中的交易代码"""
    _fields_ = [
        ('InvestorID', c_char * 13),  # ///投资者代码
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ClientID', c_char * 11),  # 客户代码
        ('IsActive', c_int),  # 是否活跃
        ('ClientIDType', c_char * 1)  # 交易编码类型
    ]


class SyncingInvestorGroupField(BaseField):
    """正在同步中的投资者分组"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorGroupID', c_char * 13),  # 投资者分组代码
        ('InvestorGroupName', c_char * 41)  # 投资者分组名称
    ]


class SyncingTradingAccountField(BaseField):
    """正在同步中的交易账号"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('PreMortgage', c_double),  # 上次质押金额
        ('PreCredit', c_double),  # 上次信用额度
        ('PreDeposit', c_double),  # 上次存款额
        ('PreBalance', c_double),  # 上次结算准备金
        ('PreMargin', c_double),  # 上次占用的保证金
        ('InterestBase', c_double),  # 利息基数
        ('Interest', c_double),  # 利息收入
        ('Deposit', c_double),  # 入金金额
        ('Withdraw', c_double),  # 出金金额
        ('FrozenMargin', c_double),  # 冻结的保证金
        ('FrozenCash', c_double),  # 冻结的资金
        ('FrozenCommission', c_double),  # 冻结的手续费
        ('CurrMargin', c_double),  # 当前保证金总额
        ('CashIn', c_double),  # 资金差额
        ('Commission', c_double),  # 手续费
        ('CloseProfit', c_double),  # 平仓盈亏
        ('PositionProfit', c_double),  # 持仓盈亏
        ('Balance', c_double),  # 期货结算准备金
        ('Available', c_double),  # 可用资金
        ('WithdrawQuota', c_double),  # 可取资金
        ('Reserve', c_double),  # 基本准备金
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('Credit', c_double),  # 信用额度
        ('Mortgage', c_double),  # 质押金额
        ('ExchangeMargin', c_double),  # 交易所保证金
        ('DeliveryMargin', c_double),  # 投资者交割保证金
        ('ExchangeDeliveryMargin', c_double),  # 交易所交割保证金
        ('ReserveBalance', c_double),  # 保底期货结算准备金
        ('CurrencyID', c_char * 4),  # 币种代码
        ('PreFundMortgageIn', c_double),  # 上次货币质入金额
        ('PreFundMortgageOut', c_double),  # 上次货币质出金额
        ('FundMortgageIn', c_double),  # 货币质入金额
        ('FundMortgageOut', c_double),  # 货币质出金额
        ('FundMortgageAvailable', c_double),  # 货币质押余额
        ('MortgageableFund', c_double),  # 可质押货币金额
        ('SpecProductMargin', c_double),  # 特殊产品占用保证金
        ('SpecProductFrozenMargin', c_double),  # 特殊产品冻结保证金
        ('SpecProductCommission', c_double),  # 特殊产品手续费
        ('SpecProductFrozenCommission', c_double),  # 特殊产品冻结手续费
        ('SpecProductPositionProfit', c_double),  # 特殊产品持仓盈亏
        ('SpecProductCloseProfit', c_double),  # 特殊产品平仓盈亏
        ('SpecProductPositionProfitByAlg', c_double),  # 根据持仓盈亏算法计算的特殊产品持仓盈亏
        ('SpecProductExchangeMargin', c_double),  # 特殊产品交易所保证金
        ('FrozenSwap', c_double),  # 延时换汇冻结金额
        ('RemainSwap', c_double)  # 剩余换汇额度
    ]


class SyncingInvestorPositionField(BaseField):
    """正在同步中的投资者持仓"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('PosiDirection', c_char * 1),  # 持仓多空方向
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('PositionDate', c_char * 1),  # 持仓日期
        ('YdPosition', c_int),  # 上日持仓
        ('Position', c_int),  # 今日持仓
        ('LongFrozen', c_int),  # 多头冻结
        ('ShortFrozen', c_int),  # 空头冻结
        ('LongFrozenAmount', c_double),  # 开仓冻结金额
        ('ShortFrozenAmount', c_double),  # 开仓冻结金额
        ('OpenVolume', c_int),  # 开仓量
        ('CloseVolume', c_int),  # 平仓量
        ('OpenAmount', c_double),  # 开仓金额
        ('CloseAmount', c_double),  # 平仓金额
        ('PositionCost', c_double),  # 持仓成本
        ('PreMargin', c_double),  # 上次占用的保证金
        ('UseMargin', c_double),  # 占用的保证金
        ('FrozenMargin', c_double),  # 冻结的保证金
        ('FrozenCash', c_double),  # 冻结的资金
        ('FrozenCommission', c_double),  # 冻结的手续费
        ('CashIn', c_double),  # 资金差额
        ('Commission', c_double),  # 手续费
        ('CloseProfit', c_double),  # 平仓盈亏
        ('PositionProfit', c_double),  # 持仓盈亏
        ('PreSettlementPrice', c_double),  # 上次结算价
        ('SettlementPrice', c_double),  # 本次结算价
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('OpenCost', c_double),  # 开仓成本
        ('ExchangeMargin', c_double),  # 交易所保证金
        ('CombPosition', c_int),  # 组合成交形成的持仓
        ('CombLongFrozen', c_int),  # 组合多头冻结
        ('CombShortFrozen', c_int),  # 组合空头冻结
        ('CloseProfitByDate', c_double),  # 逐日盯市平仓盈亏
        ('CloseProfitByTrade', c_double),  # 逐笔对冲平仓盈亏
        ('TodayPosition', c_int),  # 今日持仓
        ('MarginRateByMoney', c_double),  # 保证金率
        ('MarginRateByVolume', c_double),  # 保证金率(按手数)
        ('StrikeFrozen', c_int),  # 执行冻结
        ('StrikeFrozenAmount', c_double),  # 执行冻结金额
        ('AbandonFrozen', c_int),  # 放弃执行冻结
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('YdStrikeFrozen', c_int),  # 执行冻结的昨仓
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('PositionCostOffset', c_double)  # 大商所持仓成本差值，只有大商所使用
    ]


class SyncingInstrumentMarginRateField(BaseField):
    """正在同步中的合约保证金率"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('LongMarginRatioByMoney', c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', c_double),  # 空头保证金费
        ('IsRelative', c_int)  # 是否相对交易所收取
    ]


class SyncingInstrumentCommissionRateField(BaseField):
    """正在同步中的合约手续费率"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', c_double),  # 开仓手续费率
        ('OpenRatioByVolume', c_double),  # 开仓手续费
        ('CloseRatioByMoney', c_double),  # 平仓手续费率
        ('CloseRatioByVolume', c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', c_double)  # 平今手续费
    ]


class SyncingInstrumentTradingRightField(BaseField):
    """正在同步中的合约交易权限"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('TradingRight', c_char * 1)  # 交易权限
    ]


class QryOrderField(BaseField):
    """查询报单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('OrderSysID', c_char * 21),  # 报单编号
        ('InsertTimeStart', c_char * 9),  # 开始时间
        ('InsertTimeEnd', c_char * 9),  # 结束时间
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryTradeField(BaseField):
    """查询成交"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TradeID', c_char * 21),  # 成交编号
        ('TradeTimeStart', c_char * 9),  # 开始时间
        ('TradeTimeEnd', c_char * 9),  # 结束时间
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryInvestorPositionField(BaseField):
    """查询投资者持仓"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryTradingAccountField(BaseField):
    """查询资金账户"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('CurrencyID', c_char * 4),  # 币种代码
        ('BizType', c_char * 1),  # 业务类型
        ('AccountID', c_char * 13)  # 投资者帐号
    ]


class QryInvestorField(BaseField):
    """查询投资者"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13)  # 投资者代码
    ]


class QryTradingCodeField(BaseField):
    """查询交易编码"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ClientIDType', c_char * 1),  # 交易编码类型
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryInvestorGroupField(BaseField):
    """查询投资者组"""
    _fields_ = [
        ('BrokerID', c_char * 11)  # ///经纪公司代码
    ]


class QryInstrumentMarginRateField(BaseField):
    """查询合约保证金率"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryInstrumentCommissionRateField(BaseField):
    """查询手续费率"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryInstrumentTradingRightField(BaseField):
    """查询合约交易权限"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31)  # 合约代码
    ]


class QryBrokerField(BaseField):
    """查询经纪公司"""
    _fields_ = [
        ('BrokerID', c_char * 11)  # ///经纪公司代码
    ]


class QryTraderField(BaseField):
    """查询交易员"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class QrySuperUserFunctionField(BaseField):
    """查询管理用户功能权限"""
    _fields_ = [
        ('UserID', c_char * 16)  # ///用户代码
    ]


class QryUserSessionField(BaseField):
    """查询用户会话"""
    _fields_ = [
        ('FrontID', c_int),  # ///前置编号
        ('SessionID', c_int),  # 会话编号
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class QryPartBrokerField(BaseField):
    """查询经纪公司会员代码"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('ParticipantID', c_char * 11)  # 会员代码
    ]


class QryFrontStatusField(BaseField):
    """查询前置状态"""
    _fields_ = [
        ('FrontID', c_int)  # ///前置编号
    ]


class QryExchangeOrderField(BaseField):
    """查询交易所报单"""
    _fields_ = [
        ('ParticipantID', c_char * 11),  # ///会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class QryOrderActionField(BaseField):
    """查询报单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class QryExchangeOrderActionField(BaseField):
    """查询交易所报单操作"""
    _fields_ = [
        ('ParticipantID', c_char * 11),  # ///会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class QrySuperUserField(BaseField):
    """查询管理用户"""
    _fields_ = [
        ('UserID', c_char * 16)  # ///用户代码
    ]


class QryExchangeField(BaseField):
    """查询交易所"""
    _fields_ = [
        ('ExchangeID', c_char * 9)  # ///交易所代码
    ]


class QryProductField(BaseField):
    """查询产品"""
    _fields_ = [
        ('ProductID', c_char * 31),  # ///产品代码
        ('ProductClass', c_char * 1),  # 产品类型
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class QryInstrumentField(BaseField):
    """查询合约"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('ProductID', c_char * 31)  # 产品代码
    ]


class QryDepthMarketDataField(BaseField):
    """查询行情"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class QryBrokerUserField(BaseField):
    """查询经纪公司用户"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class QryBrokerUserFunctionField(BaseField):
    """查询经纪公司用户权限"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class QryTraderOfferField(BaseField):
    """查询交易员报盘机"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class QrySyncDepositField(BaseField):
    """查询出入金流水"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('DepositSeqNo', c_char * 15)  # 出入金流水号
    ]


class QrySettlementInfoField(BaseField):
    """查询投资者结算结果"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('TradingDay', c_char * 9),  # 交易日
        ('AccountID', c_char * 13),  # 投资者帐号
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class QryExchangeMarginRateField(BaseField):
    """查询交易所保证金率"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class QryExchangeMarginRateAdjustField(BaseField):
    """查询交易所调整保证金率"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('HedgeFlag', c_char * 1)  # 投机套保标志
    ]


class QryExchangeRateField(BaseField):
    """查询汇率"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('FromCurrencyID', c_char * 4),  # 源币种
        ('ToCurrencyID', c_char * 4)  # 目标币种
    ]


class QrySyncFundMortgageField(BaseField):
    """查询货币质押流水"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('MortgageSeqNo', c_char * 15)  # 货币质押流水号
    ]


class QryHisOrderField(BaseField):
    """查询报单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('OrderSysID', c_char * 21),  # 报单编号
        ('InsertTimeStart', c_char * 9),  # 开始时间
        ('InsertTimeEnd', c_char * 9),  # 结束时间
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int)  # 结算编号
    ]


class OptionInstrMiniMarginField(BaseField):
    """当前期权合约最小保证金"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('MinMargin', c_double),  # 单位（手）期权合约最小保证金
        ('ValueMethod', c_char * 1),  # 取值方式
        ('IsRelative', c_int)  # 是否跟随交易所收取
    ]


class OptionInstrMarginAdjustField(BaseField):
    """当前期权合约保证金调整系数"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('SShortMarginRatioByMoney', c_double),  # 投机空头保证金调整系数
        ('SShortMarginRatioByVolume', c_double),  # 投机空头保证金调整系数
        ('HShortMarginRatioByMoney', c_double),  # 保值空头保证金调整系数
        ('HShortMarginRatioByVolume', c_double),  # 保值空头保证金调整系数
        ('AShortMarginRatioByMoney', c_double),  # 套利空头保证金调整系数
        ('AShortMarginRatioByVolume', c_double),  # 套利空头保证金调整系数
        ('IsRelative', c_int),  # 是否跟随交易所收取
        ('MShortMarginRatioByMoney', c_double),  # 做市商空头保证金调整系数
        ('MShortMarginRatioByVolume', c_double)  # 做市商空头保证金调整系数
    ]


class OptionInstrCommRateField(BaseField):
    """当前期权合约手续费的详细内容"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', c_double),  # 开仓手续费率
        ('OpenRatioByVolume', c_double),  # 开仓手续费
        ('CloseRatioByMoney', c_double),  # 平仓手续费率
        ('CloseRatioByVolume', c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', c_double),  # 平今手续费
        ('StrikeRatioByMoney', c_double),  # 执行手续费率
        ('StrikeRatioByVolume', c_double),  # 执行手续费
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class OptionInstrTradeCostField(BaseField):
    """期权交易成本"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('FixedMargin', c_double),  # 期权合约保证金不变部分
        ('MiniMargin', c_double),  # 期权合约最小保证金
        ('Royalty', c_double),  # 期权合约权利金
        ('ExchFixedMargin', c_double),  # 交易所期权合约保证金不变部分
        ('ExchMiniMargin', c_double),  # 交易所期权合约最小保证金
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryOptionInstrTradeCostField(BaseField):
    """期权交易成本查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('InputPrice', c_double),  # 期权合约报价
        ('UnderlyingPrice', c_double),  # 标的价格,填0则用昨结算价
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryOptionInstrCommRateField(BaseField):
    """期权手续费率查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class IndexPriceField(BaseField):
    """股指现货指数"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ClosePrice', c_double)  # 指数现货收盘价
    ]


class InputExecOrderField(BaseField):
    """输入的执行宣告"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExecOrderRef', c_char * 13),  # 执行宣告引用
        ('UserID', c_char * 16),  # 用户代码
        ('Volume', c_int),  # 数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OffsetFlag', c_char * 1),  # 开平标志
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ActionType', c_char * 1),  # 执行类型
        ('PosiDirection', c_char * 1),  # 保留头寸申请的持仓方向
        ('ReservePositionFlag', c_char * 1),  # 期权行权后是否保留期货头寸的标记,该字段已废弃
        ('CloseFlag', c_char * 1),  # 期权行权后生成的头寸是否自动平仓
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('ClientID', c_char * 11),  # 交易编码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class InputExecOrderActionField(BaseField):
    """输入执行宣告操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExecOrderActionRef', c_int),  # 执行宣告操作引用
        ('ExecOrderRef', c_char * 13),  # 执行宣告引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ExecOrderSysID', c_char * 21),  # 执行宣告操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('UserID', c_char * 16),  # 用户代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ExecOrderField(BaseField):
    """执行宣告"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExecOrderRef', c_char * 13),  # 执行宣告引用
        ('UserID', c_char * 16),  # 用户代码
        ('Volume', c_int),  # 数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OffsetFlag', c_char * 1),  # 开平标志
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ActionType', c_char * 1),  # 执行类型
        ('PosiDirection', c_char * 1),  # 保留头寸申请的持仓方向
        ('ReservePositionFlag', c_char * 1),  # 期权行权后是否保留期货头寸的标记,该字段已废弃
        ('CloseFlag', c_char * 1),  # 期权行权后生成的头寸是否自动平仓
        ('ExecOrderLocalID', c_char * 13),  # 本地执行宣告编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderSubmitStatus', c_char * 1),  # 执行宣告提交状态
        ('NotifySequence', c_int),  # 报单提示序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('ExecOrderSysID', c_char * 21),  # 执行宣告编号
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 插入时间
        ('CancelTime', c_char * 9),  # 撤销时间
        ('ExecResult', c_char * 1),  # 执行结果
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('SequenceNo', c_int),  # 序号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('StatusMsg', c_char * 81),  # 状态信息
        ('ActiveUserID', c_char * 16),  # 操作用户代码
        ('BrokerExecOrderSeq', c_int),  # 经纪公司报单编号
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ExecOrderActionField(BaseField):
    """执行宣告操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExecOrderActionRef', c_int),  # 执行宣告操作引用
        ('ExecOrderRef', c_char * 13),  # 执行宣告引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ExecOrderSysID', c_char * 21),  # 执行宣告操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('ExecOrderLocalID', c_char * 13),  # 本地执行宣告编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('ActionType', c_char * 1),  # 执行类型
        ('StatusMsg', c_char * 81),  # 状态信息
        ('InstrumentID', c_char * 31),  # 合约代码
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryExecOrderField(BaseField):
    """执行宣告查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ExecOrderSysID', c_char * 21),  # 执行宣告编号
        ('InsertTimeStart', c_char * 9),  # 开始时间
        ('InsertTimeEnd', c_char * 9)  # 结束时间
    ]


class ExchangeExecOrderField(BaseField):
    """交易所执行宣告信息"""
    _fields_ = [
        ('Volume', c_int),  # ///数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OffsetFlag', c_char * 1),  # 开平标志
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ActionType', c_char * 1),  # 执行类型
        ('PosiDirection', c_char * 1),  # 保留头寸申请的持仓方向
        ('ReservePositionFlag', c_char * 1),  # 期权行权后是否保留期货头寸的标记,该字段已废弃
        ('CloseFlag', c_char * 1),  # 期权行权后生成的头寸是否自动平仓
        ('ExecOrderLocalID', c_char * 13),  # 本地执行宣告编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderSubmitStatus', c_char * 1),  # 执行宣告提交状态
        ('NotifySequence', c_int),  # 报单提示序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('ExecOrderSysID', c_char * 21),  # 执行宣告编号
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 插入时间
        ('CancelTime', c_char * 9),  # 撤销时间
        ('ExecResult', c_char * 1),  # 执行结果
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('SequenceNo', c_int),  # 序号
        ('BranchID', c_char * 9),  # 营业部编号
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryExchangeExecOrderField(BaseField):
    """交易所执行宣告查询"""
    _fields_ = [
        ('ParticipantID', c_char * 11),  # ///会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class QryExecOrderActionField(BaseField):
    """执行宣告操作查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class ExchangeExecOrderActionField(BaseField):
    """交易所执行宣告操作"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('ExecOrderSysID', c_char * 21),  # 执行宣告操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('ExecOrderLocalID', c_char * 13),  # 本地执行宣告编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('ActionType', c_char * 1),  # 执行类型
        ('BranchID', c_char * 9),  # 营业部编号
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21),  # Mac地址
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('Volume', c_int)  # 数量
    ]


class QryExchangeExecOrderActionField(BaseField):
    """交易所执行宣告操作查询"""
    _fields_ = [
        ('ParticipantID', c_char * 11),  # ///会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class ErrExecOrderField(BaseField):
    """错误执行宣告"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExecOrderRef', c_char * 13),  # 执行宣告引用
        ('UserID', c_char * 16),  # 用户代码
        ('Volume', c_int),  # 数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OffsetFlag', c_char * 1),  # 开平标志
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ActionType', c_char * 1),  # 执行类型
        ('PosiDirection', c_char * 1),  # 保留头寸申请的持仓方向
        ('ReservePositionFlag', c_char * 1),  # 期权行权后是否保留期货头寸的标记,该字段已废弃
        ('CloseFlag', c_char * 1),  # 期权行权后生成的头寸是否自动平仓
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('ClientID', c_char * 11),  # 交易编码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21),  # Mac地址
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class QryErrExecOrderField(BaseField):
    """查询错误执行宣告"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13)  # 投资者代码
    ]


class ErrExecOrderActionField(BaseField):
    """错误执行宣告操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExecOrderActionRef', c_int),  # 执行宣告操作引用
        ('ExecOrderRef', c_char * 13),  # 执行宣告引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ExecOrderSysID', c_char * 21),  # 执行宣告操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('UserID', c_char * 16),  # 用户代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21),  # Mac地址
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class QryErrExecOrderActionField(BaseField):
    """查询错误执行宣告操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13)  # 投资者代码
    ]


class OptionInstrTradingRightField(BaseField):
    """投资者期权合约交易权限"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('Direction', c_char * 1),  # 买卖方向
        ('TradingRight', c_char * 1)  # 交易权限
    ]


class QryOptionInstrTradingRightField(BaseField):
    """查询期权合约交易权限"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('Direction', c_char * 1)  # 买卖方向
    ]


class InputForQuoteField(BaseField):
    """输入的询价"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ForQuoteRef', c_char * 13),  # 询价引用
        ('UserID', c_char * 16),  # 用户代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ForQuoteField(BaseField):
    """询价"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ForQuoteRef', c_char * 13),  # 询价引用
        ('UserID', c_char * 16),  # 用户代码
        ('ForQuoteLocalID', c_char * 13),  # 本地询价编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 插入时间
        ('ForQuoteStatus', c_char * 1),  # 询价状态
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('StatusMsg', c_char * 81),  # 状态信息
        ('ActiveUserID', c_char * 16),  # 操作用户代码
        ('BrokerForQutoSeq', c_int),  # 经纪公司询价编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryForQuoteField(BaseField):
    """询价查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InsertTimeStart', c_char * 9),  # 开始时间
        ('InsertTimeEnd', c_char * 9),  # 结束时间
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class ExchangeForQuoteField(BaseField):
    """交易所询价信息"""
    _fields_ = [
        ('ForQuoteLocalID', c_char * 13),  # ///本地询价编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 插入时间
        ('ForQuoteStatus', c_char * 1),  # 询价状态
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryExchangeForQuoteField(BaseField):
    """交易所询价查询"""
    _fields_ = [
        ('ParticipantID', c_char * 11),  # ///会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class InputQuoteField(BaseField):
    """输入的报价"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('QuoteRef', c_char * 13),  # 报价引用
        ('UserID', c_char * 16),  # 用户代码
        ('AskPrice', c_double),  # 卖价格
        ('BidPrice', c_double),  # 买价格
        ('AskVolume', c_int),  # 卖数量
        ('BidVolume', c_int),  # 买数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('AskOffsetFlag', c_char * 1),  # 卖开平标志
        ('BidOffsetFlag', c_char * 1),  # 买开平标志
        ('AskHedgeFlag', c_char * 1),  # 卖投机套保标志
        ('BidHedgeFlag', c_char * 1),  # 买投机套保标志
        ('AskOrderRef', c_char * 13),  # 衍生卖报单引用
        ('BidOrderRef', c_char * 13),  # 衍生买报单引用
        ('ForQuoteSysID', c_char * 21),  # 应价编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('ClientID', c_char * 11),  # 交易编码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class InputQuoteActionField(BaseField):
    """输入报价操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('QuoteActionRef', c_int),  # 报价操作引用
        ('QuoteRef', c_char * 13),  # 报价引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('QuoteSysID', c_char * 21),  # 报价操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('UserID', c_char * 16),  # 用户代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('ClientID', c_char * 11),  # 交易编码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QuoteField(BaseField):
    """报价"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('QuoteRef', c_char * 13),  # 报价引用
        ('UserID', c_char * 16),  # 用户代码
        ('AskPrice', c_double),  # 卖价格
        ('BidPrice', c_double),  # 买价格
        ('AskVolume', c_int),  # 卖数量
        ('BidVolume', c_int),  # 买数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('AskOffsetFlag', c_char * 1),  # 卖开平标志
        ('BidOffsetFlag', c_char * 1),  # 买开平标志
        ('AskHedgeFlag', c_char * 1),  # 卖投机套保标志
        ('BidHedgeFlag', c_char * 1),  # 买投机套保标志
        ('QuoteLocalID', c_char * 13),  # 本地报价编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('NotifySequence', c_int),  # 报价提示序号
        ('OrderSubmitStatus', c_char * 1),  # 报价提交状态
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('QuoteSysID', c_char * 21),  # 报价编号
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 插入时间
        ('CancelTime', c_char * 9),  # 撤销时间
        ('QuoteStatus', c_char * 1),  # 报价状态
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('SequenceNo', c_int),  # 序号
        ('AskOrderSysID', c_char * 21),  # 卖方报单编号
        ('BidOrderSysID', c_char * 21),  # 买方报单编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('StatusMsg', c_char * 81),  # 状态信息
        ('ActiveUserID', c_char * 16),  # 操作用户代码
        ('BrokerQuoteSeq', c_int),  # 经纪公司报价编号
        ('AskOrderRef', c_char * 13),  # 衍生卖报单引用
        ('BidOrderRef', c_char * 13),  # 衍生买报单引用
        ('ForQuoteSysID', c_char * 21),  # 应价编号
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QuoteActionField(BaseField):
    """报价操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('QuoteActionRef', c_int),  # 报价操作引用
        ('QuoteRef', c_char * 13),  # 报价引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('QuoteSysID', c_char * 21),  # 报价操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('QuoteLocalID', c_char * 13),  # 本地报价编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('StatusMsg', c_char * 81),  # 状态信息
        ('InstrumentID', c_char * 31),  # 合约代码
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryQuoteField(BaseField):
    """报价查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('QuoteSysID', c_char * 21),  # 报价编号
        ('InsertTimeStart', c_char * 9),  # 开始时间
        ('InsertTimeEnd', c_char * 9),  # 结束时间
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class ExchangeQuoteField(BaseField):
    """交易所报价信息"""
    _fields_ = [
        ('AskPrice', c_double),  # ///卖价格
        ('BidPrice', c_double),  # 买价格
        ('AskVolume', c_int),  # 卖数量
        ('BidVolume', c_int),  # 买数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('AskOffsetFlag', c_char * 1),  # 卖开平标志
        ('BidOffsetFlag', c_char * 1),  # 买开平标志
        ('AskHedgeFlag', c_char * 1),  # 卖投机套保标志
        ('BidHedgeFlag', c_char * 1),  # 买投机套保标志
        ('QuoteLocalID', c_char * 13),  # 本地报价编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('NotifySequence', c_int),  # 报价提示序号
        ('OrderSubmitStatus', c_char * 1),  # 报价提交状态
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('QuoteSysID', c_char * 21),  # 报价编号
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 插入时间
        ('CancelTime', c_char * 9),  # 撤销时间
        ('QuoteStatus', c_char * 1),  # 报价状态
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('SequenceNo', c_int),  # 序号
        ('AskOrderSysID', c_char * 21),  # 卖方报单编号
        ('BidOrderSysID', c_char * 21),  # 买方报单编号
        ('ForQuoteSysID', c_char * 21),  # 应价编号
        ('BranchID', c_char * 9),  # 营业部编号
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryExchangeQuoteField(BaseField):
    """交易所报价查询"""
    _fields_ = [
        ('ParticipantID', c_char * 11),  # ///会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class QryQuoteActionField(BaseField):
    """报价操作查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class ExchangeQuoteActionField(BaseField):
    """交易所报价操作"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('QuoteSysID', c_char * 21),  # 报价操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('QuoteLocalID', c_char * 13),  # 本地报价编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryExchangeQuoteActionField(BaseField):
    """交易所报价操作查询"""
    _fields_ = [
        ('ParticipantID', c_char * 11),  # ///会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class OptionInstrDeltaField(BaseField):
    """期权合约delta值"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('Delta', c_double)  # Delta值
    ]


class ForQuoteRspField(BaseField):
    """发给做市商的询价请求"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ForQuoteSysID', c_char * 21),  # 询价编号
        ('ForQuoteTime', c_char * 9),  # 询价时间
        ('ActionDay', c_char * 9),  # 业务日期
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class StrikeOffsetField(BaseField):
    """当前期权合约执行偏移值的详细内容"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('Offset', c_double),  # 执行偏移值
        ('OffsetType', c_char * 1)  # 执行偏移类型
    ]


class QryStrikeOffsetField(BaseField):
    """期权执行偏移值查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31)  # 合约代码
    ]


class InputBatchOrderActionField(BaseField):
    """输入批量报单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OrderActionRef', c_int),  # 报单操作引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('UserID', c_char * 16),  # 用户代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class BatchOrderActionField(BaseField):
    """批量报单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OrderActionRef', c_int),  # 报单操作引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('StatusMsg', c_char * 81),  # 状态信息
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ExchangeBatchOrderActionField(BaseField):
    """交易所批量报单操作"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryBatchOrderActionField(BaseField):
    """查询批量报单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class CombInstrumentGuardField(BaseField):
    """组合合约安全系数"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('GuarantRatio', c_double)  # ,('ExchangeID',c_char*9)# 交易所代码
    ]


class QryCombInstrumentGuardField(BaseField):
    """组合合约安全系数查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class InputCombActionField(BaseField):
    """输入的申请组合"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('CombActionRef', c_char * 13),  # 组合引用
        ('UserID', c_char * 16),  # 用户代码
        ('Direction', c_char * 1),  # 买卖方向
        ('Volume', c_int),  # 数量
        ('CombDirection', c_char * 1),  # 组合指令方向
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21),  # Mac地址
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class CombActionField(BaseField):
    """申请组合"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('CombActionRef', c_char * 13),  # 组合引用
        ('UserID', c_char * 16),  # 用户代码
        ('Direction', c_char * 1),  # 买卖方向
        ('Volume', c_int),  # 数量
        ('CombDirection', c_char * 1),  # 组合指令方向
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ActionLocalID', c_char * 13),  # 本地申请组合编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('ActionStatus', c_char * 1),  # 组合状态
        ('NotifySequence', c_int),  # 报单提示序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('SequenceNo', c_int),  # 序号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('StatusMsg', c_char * 81),  # 状态信息
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21),  # Mac地址
        ('ComTradeID', c_char * 21),  # 组合编号
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryCombActionField(BaseField):
    """申请组合查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class ExchangeCombActionField(BaseField):
    """交易所申请组合信息"""
    _fields_ = [
        ('Direction', c_char * 1),  # ///买卖方向
        ('Volume', c_int),  # 数量
        ('CombDirection', c_char * 1),  # 组合指令方向
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ActionLocalID', c_char * 13),  # 本地申请组合编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('ActionStatus', c_char * 1),  # 组合状态
        ('NotifySequence', c_int),  # 报单提示序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('SequenceNo', c_int),  # 序号
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21),  # Mac地址
        ('ComTradeID', c_char * 21),  # 组合编号
        ('BranchID', c_char * 9)  # 营业部编号
    ]


class QryExchangeCombActionField(BaseField):
    """交易所申请组合查询"""
    _fields_ = [
        ('ParticipantID', c_char * 11),  # ///会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class ProductExchRateField(BaseField):
    """产品报价汇率"""
    _fields_ = [
        ('ProductID', c_char * 31),  # ///产品代码
        ('QuoteCurrencyID', c_char * 4),  # 报价币种类型
        ('ExchangeRate', c_double),  # 汇率
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class QryProductExchRateField(BaseField):
    """产品报价汇率查询"""
    _fields_ = [
        ('ProductID', c_char * 31),  # ///产品代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class QryForQuoteParamField(BaseField):
    """查询询价价差参数"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class ForQuoteParamField(BaseField):
    """询价价差参数"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('LastPrice', c_double),  # 最新价
        ('PriceInterval', c_double)  # 价差
    ]


class MMOptionInstrCommRateField(BaseField):
    """当前做市商期权合约手续费的详细内容"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', c_double),  # 开仓手续费率
        ('OpenRatioByVolume', c_double),  # 开仓手续费
        ('CloseRatioByMoney', c_double),  # 平仓手续费率
        ('CloseRatioByVolume', c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', c_double),  # 平今手续费
        ('StrikeRatioByMoney', c_double),  # 执行手续费率
        ('StrikeRatioByVolume', c_double)  # 执行手续费
    ]


class QryMMOptionInstrCommRateField(BaseField):
    """做市商期权手续费率查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31)  # 合约代码
    ]


class MMInstrumentCommissionRateField(BaseField):
    """做市商合约手续费率"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OpenRatioByMoney', c_double),  # 开仓手续费率
        ('OpenRatioByVolume', c_double),  # 开仓手续费
        ('CloseRatioByMoney', c_double),  # 平仓手续费率
        ('CloseRatioByVolume', c_double),  # 平仓手续费
        ('CloseTodayRatioByMoney', c_double),  # 平今手续费率
        ('CloseTodayRatioByVolume', c_double)  # 平今手续费
    ]


class QryMMInstrumentCommissionRateField(BaseField):
    """查询做市商合约手续费率"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31)  # 合约代码
    ]


class InstrumentOrderCommRateField(BaseField):
    """当前报单手续费的详细内容"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('OrderCommByVolume', c_double),  # 报单手续费
        ('OrderActionCommByVolume', c_double),  # 撤单手续费
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryInstrumentOrderCommRateField(BaseField):
    """报单手续费率查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31)  # 合约代码
    ]


class TradeParamField(BaseField):
    """交易参数"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('TradeParamID', c_char * 1),  # 参数代码
        ('TradeParamValue', c_char * 256),  # 参数代码值
        ('Memo', c_char * 161)  # 备注
    ]


class InstrumentMarginRateULField(BaseField):
    """合约保证金率调整"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('LongMarginRatioByMoney', c_double),  # 多头保证金率
        ('LongMarginRatioByVolume', c_double),  # 多头保证金费
        ('ShortMarginRatioByMoney', c_double),  # 空头保证金率
        ('ShortMarginRatioByVolume', c_double)  # 空头保证金费
    ]


class FutureLimitPosiParamField(BaseField):
    """期货持仓限制参数"""
    _fields_ = [
        ('InvestorRange', c_char * 1),  # ///投资者范围
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ProductID', c_char * 31),  # 产品代码
        ('SpecOpenVolume', c_int),  # 当日投机开仓数量限制
        ('ArbiOpenVolume', c_int),  # 当日套利开仓数量限制
        ('OpenVolume', c_int)  # 当日投机+套利开仓数量限制
    ]


class LoginForbiddenIPField(BaseField):
    """禁止登录IP"""
    _fields_ = [
        ('IPAddress', c_char * 16)  # ///IP地址
    ]


class IPListField(BaseField):
    """IP列表"""
    _fields_ = [
        ('IPAddress', c_char * 16),  # ///IP地址
        ('IsWhite', c_int)  # 是否白名单
    ]


class InputOptionSelfCloseField(BaseField):
    """输入的期权自对冲"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('OptionSelfCloseRef', c_char * 13),  # 期权自对冲引用
        ('UserID', c_char * 16),  # 用户代码
        ('Volume', c_int),  # 数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('OptSelfCloseFlag', c_char * 1),  # 期权行权的头寸是否自对冲
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('ClientID', c_char * 11),  # 交易编码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class InputOptionSelfCloseActionField(BaseField):
    """输入期权自对冲操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OptionSelfCloseActionRef', c_int),  # 期权自对冲操作引用
        ('OptionSelfCloseRef', c_char * 13),  # 期权自对冲引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('OptionSelfCloseSysID', c_char * 21),  # 期权自对冲操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('UserID', c_char * 16),  # 用户代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class OptionSelfCloseField(BaseField):
    """期权自对冲"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('OptionSelfCloseRef', c_char * 13),  # 期权自对冲引用
        ('UserID', c_char * 16),  # 用户代码
        ('Volume', c_int),  # 数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('OptSelfCloseFlag', c_char * 1),  # 期权行权的头寸是否自对冲
        ('OptionSelfCloseLocalID', c_char * 13),  # 本地期权自对冲编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderSubmitStatus', c_char * 1),  # 期权自对冲提交状态
        ('NotifySequence', c_int),  # 报单提示序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('OptionSelfCloseSysID', c_char * 21),  # 期权自对冲编号
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 插入时间
        ('CancelTime', c_char * 9),  # 撤销时间
        ('ExecResult', c_char * 1),  # 自对冲结果
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('SequenceNo', c_int),  # 序号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('StatusMsg', c_char * 81),  # 状态信息
        ('ActiveUserID', c_char * 16),  # 操作用户代码
        ('BrokerOptionSelfCloseSeq', c_int),  # 经纪公司报单编号
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class OptionSelfCloseActionField(BaseField):
    """期权自对冲操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OptionSelfCloseActionRef', c_int),  # 期权自对冲操作引用
        ('OptionSelfCloseRef', c_char * 13),  # 期权自对冲引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('OptionSelfCloseSysID', c_char * 21),  # 期权自对冲操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OptionSelfCloseLocalID', c_char * 13),  # 本地期权自对冲编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('StatusMsg', c_char * 81),  # 状态信息
        ('InstrumentID', c_char * 31),  # 合约代码
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryOptionSelfCloseField(BaseField):
    """期权自对冲查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('OptionSelfCloseSysID', c_char * 21),  # 期权自对冲编号
        ('InsertTimeStart', c_char * 9),  # 开始时间
        ('InsertTimeEnd', c_char * 9)  # 结束时间
    ]


class ExchangeOptionSelfCloseField(BaseField):
    """交易所期权自对冲信息"""
    _fields_ = [
        ('Volume', c_int),  # ///数量
        ('RequestID', c_int),  # 请求编号
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('OptSelfCloseFlag', c_char * 1),  # 期权行权的头寸是否自对冲
        ('OptionSelfCloseLocalID', c_char * 13),  # 本地期权自对冲编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderSubmitStatus', c_char * 1),  # 期权自对冲提交状态
        ('NotifySequence', c_int),  # 报单提示序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('OptionSelfCloseSysID', c_char * 21),  # 期权自对冲编号
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 插入时间
        ('CancelTime', c_char * 9),  # 撤销时间
        ('ExecResult', c_char * 1),  # 自对冲结果
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('SequenceNo', c_int),  # 序号
        ('BranchID', c_char * 9),  # 营业部编号
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryOptionSelfCloseActionField(BaseField):
    """期权自对冲操作查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class ExchangeOptionSelfCloseActionField(BaseField):
    """交易所期权自对冲操作"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('OptionSelfCloseSysID', c_char * 21),  # 期权自对冲操作编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OptionSelfCloseLocalID', c_char * 13),  # 本地期权自对冲编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('BranchID', c_char * 9),  # 营业部编号
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21),  # Mac地址
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('OptSelfCloseFlag', c_char * 1)  # 期权行权的头寸是否自对冲
    ]


class SyncDelaySwapField(BaseField):
    """延时换汇同步"""
    _fields_ = [
        ('DelaySwapSeqNo', c_char * 15),  # ///换汇流水号
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('FromCurrencyID', c_char * 4),  # 源币种
        ('FromAmount', c_double),  # 源金额
        ('FromFrozenSwap', c_double),  # 源换汇冻结金额(可用冻结)
        ('FromRemainSwap', c_double),  # 源剩余换汇额度(可提冻结)
        ('ToCurrencyID', c_char * 4),  # 目标币种
        ('ToAmount', c_double)  # 目标金额
    ]


class QrySyncDelaySwapField(BaseField):
    """查询延时换汇同步"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('DelaySwapSeqNo', c_char * 15)  # 延时换汇流水号
    ]


class InvestUnitField(BaseField):
    """投资单元"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('InvestorUnitName', c_char * 81),  # 投资者单元名称
        ('InvestorGroupID', c_char * 13),  # 投资者分组代码
        ('CommModelID', c_char * 13),  # 手续费率模板代码
        ('MarginModelID', c_char * 13),  # 保证金率模板代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class QryInvestUnitField(BaseField):
    """查询投资单元"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class SecAgentCheckModeField(BaseField):
    """二级代理商资金校验模式"""
    _fields_ = [
        ('InvestorID', c_char * 13),  # ///投资者代码
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('CurrencyID', c_char * 4),  # 币种
        ('BrokerSecAgentID', c_char * 13),  # 境外中介机构资金帐号
        ('CheckSelfAccount', c_int)  # 是否需要校验自己的资金账户
    ]


class SecAgentTradeInfoField(BaseField):
    """二级代理商信息"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('BrokerSecAgentID', c_char * 13),  # 境外中介机构资金帐号
        ('InvestorID', c_char * 13),  # 投资者代码
        ('LongCustomerName', c_char * 161)  # 二级代理商姓名
    ]


class MarketDataField(BaseField):
    """市场行情"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('LastPrice', c_double),  # 最新价
        ('PreSettlementPrice', c_double),  # 上次结算价
        ('PreClosePrice', c_double),  # 昨收盘
        ('PreOpenInterest', c_double),  # 昨持仓量
        ('OpenPrice', c_double),  # 今开盘
        ('HighestPrice', c_double),  # 最高价
        ('LowestPrice', c_double),  # 最低价
        ('Volume', c_int),  # 数量
        ('Turnover', c_double),  # 成交金额
        ('OpenInterest', c_double),  # 持仓量
        ('ClosePrice', c_double),  # 今收盘
        ('SettlementPrice', c_double),  # 本次结算价
        ('UpperLimitPrice', c_double),  # 涨停板价
        ('LowerLimitPrice', c_double),  # 跌停板价
        ('PreDelta', c_double),  # 昨虚实度
        ('CurrDelta', c_double),  # 今虚实度
        ('UpdateTime', c_char * 9),  # 最后修改时间
        ('UpdateMillisec', c_int),  # 最后修改毫秒
        ('ActionDay', c_char * 9)  # 业务日期
    ]


class MarketDataBaseField(BaseField):
    """行情基础属性"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('PreSettlementPrice', c_double),  # 上次结算价
        ('PreClosePrice', c_double),  # 昨收盘
        ('PreOpenInterest', c_double),  # 昨持仓量
        ('PreDelta', c_double)  # 昨虚实度
    ]


class MarketDataStaticField(BaseField):
    """行情静态属性"""
    _fields_ = [
        ('OpenPrice', c_double),  # ///今开盘
        ('HighestPrice', c_double),  # 最高价
        ('LowestPrice', c_double),  # 最低价
        ('ClosePrice', c_double),  # 今收盘
        ('UpperLimitPrice', c_double),  # 涨停板价
        ('LowerLimitPrice', c_double),  # 跌停板价
        ('SettlementPrice', c_double),  # 本次结算价
        ('CurrDelta', c_double)  # 今虚实度
    ]


class MarketDataLastMatchField(BaseField):
    """行情最新成交属性"""
    _fields_ = [
        ('LastPrice', c_double),  # ///最新价
        ('Volume', c_int),  # 数量
        ('Turnover', c_double),  # 成交金额
        ('OpenInterest', c_double)  # 持仓量
    ]


class MarketDataBestPriceField(BaseField):
    """行情最优价属性"""
    _fields_ = [
        ('BidPrice1', c_double),  # ///申买价一
        ('BidVolume1', c_int),  # 申买量一
        ('AskPrice1', c_double),  # 申卖价一
        ('AskVolume1', c_int)  # 申卖量一
    ]


class MarketDataBid23Field(BaseField):
    """行情申买二、三属性"""
    _fields_ = [
        ('BidPrice2', c_double),  # ///申买价二
        ('BidVolume2', c_int),  # 申买量二
        ('BidPrice3', c_double),  # 申买价三
        ('BidVolume3', c_int)  # 申买量三
    ]


class MarketDataAsk23Field(BaseField):
    """行情申卖二、三属性"""
    _fields_ = [
        ('AskPrice2', c_double),  # ///申卖价二
        ('AskVolume2', c_int),  # 申卖量二
        ('AskPrice3', c_double),  # 申卖价三
        ('AskVolume3', c_int)  # 申卖量三
    ]


class MarketDataBid45Field(BaseField):
    """行情申买四、五属性"""
    _fields_ = [
        ('BidPrice4', c_double),  # ///申买价四
        ('BidVolume4', c_int),  # 申买量四
        ('BidPrice5', c_double),  # 申买价五
        ('BidVolume5', c_int)  # 申买量五
    ]


class MarketDataAsk45Field(BaseField):
    """行情申卖四、五属性"""
    _fields_ = [
        ('AskPrice4', c_double),  # ///申卖价四
        ('AskVolume4', c_int),  # 申卖量四
        ('AskPrice5', c_double),  # 申卖价五
        ('AskVolume5', c_int)  # 申卖量五
    ]


class MarketDataUpdateTimeField(BaseField):
    """行情更新时间属性"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('UpdateTime', c_char * 9),  # 最后修改时间
        ('UpdateMillisec', c_int),  # 最后修改毫秒
        ('ActionDay', c_char * 9)  # 业务日期
    ]


class MarketDataExchangeField(BaseField):
    """行情交易所代码属性"""
    _fields_ = [
        ('ExchangeID', c_char * 9)  # ///交易所代码
    ]


class SpecificInstrumentField(BaseField):
    """指定的合约"""
    _fields_ = [
        ('InstrumentID', c_char * 31)  # ///合约代码
    ]


class InstrumentStatusField(BaseField):
    """合约状态"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('SettlementGroupID', c_char * 9),  # 结算组代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('InstrumentStatus', c_char * 1),  # 合约交易状态
        ('TradingSegmentSN', c_int),  # 交易阶段编号
        ('EnterTime', c_char * 9),  # 进入本状态时间
        ('EnterReason', c_char * 1)  # 进入本状态原因
    ]


class QryInstrumentStatusField(BaseField):
    """查询合约状态"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('ExchangeInstID', c_char * 31)  # 合约在交易所的代码
    ]


class InvestorAccountField(BaseField):
    """投资者账户"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class PositionProfitAlgorithmField(BaseField):
    """浮动盈亏算法"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Algorithm', c_char * 1),  # 盈亏算法
        ('Memo', c_char * 161),  # 备注
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class DiscountField(BaseField):
    """会员资金折扣"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('InvestorID', c_char * 13),  # 投资者代码
        ('Discount', c_double)  # 资金折扣比例
    ]


class QryTransferBankField(BaseField):
    """查询转帐银行"""
    _fields_ = [
        ('BankID', c_char * 4),  # ///银行代码
        ('BankBrchID', c_char * 5)  # 银行分中心代码
    ]


class TransferBankField(BaseField):
    """转帐银行"""
    _fields_ = [
        ('BankID', c_char * 4),  # ///银行代码
        ('BankBrchID', c_char * 5),  # 银行分中心代码
        ('BankName', c_char * 101),  # 银行名称
        ('IsActive', c_int)  # 是否活跃
    ]


class QryInvestorPositionDetailField(BaseField):
    """查询投资者持仓明细"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class InvestorPositionDetailField(BaseField):
    """投资者持仓明细"""
    _fields_ = [
        ('InstrumentID', c_char * 31),  # ///合约代码
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('Direction', c_char * 1),  # 买卖
        ('OpenDate', c_char * 9),  # 开仓日期
        ('TradeID', c_char * 21),  # 成交编号
        ('Volume', c_int),  # 数量
        ('OpenPrice', c_double),  # 开仓价
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('TradeType', c_char * 1),  # 成交类型
        ('CombInstrumentID', c_char * 31),  # 组合合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('CloseProfitByDate', c_double),  # 逐日盯市平仓盈亏
        ('CloseProfitByTrade', c_double),  # 逐笔对冲平仓盈亏
        ('PositionProfitByDate', c_double),  # 逐日盯市持仓盈亏
        ('PositionProfitByTrade', c_double),  # 逐笔对冲持仓盈亏
        ('Margin', c_double),  # 投资者保证金
        ('ExchMargin', c_double),  # 交易所保证金
        ('MarginRateByMoney', c_double),  # 保证金率
        ('MarginRateByVolume', c_double),  # 保证金率(按手数)
        ('LastSettlementPrice', c_double),  # 昨结算价
        ('SettlementPrice', c_double),  # 结算价
        ('CloseVolume', c_int),  # 平仓量
        ('CloseAmount', c_double),  # 平仓金额
        ('TimeFirstVolume', c_int),  # 按照时间顺序平仓的笔数,大商所专用
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class TradingAccountPasswordField(BaseField):
    """资金账户口令域"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 密码
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class MDTraderOfferField(BaseField):
    """交易所行情报盘机"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('Password', c_char * 41),  # 密码
        ('InstallID', c_int),  # 安装编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('TraderConnectStatus', c_char * 1),  # 交易所交易员连接状态
        ('ConnectRequestDate', c_char * 9),  # 发出连接请求的日期
        ('ConnectRequestTime', c_char * 9),  # 发出连接请求的时间
        ('LastReportDate', c_char * 9),  # 上次报告日期
        ('LastReportTime', c_char * 9),  # 上次报告时间
        ('ConnectDate', c_char * 9),  # 完成连接日期
        ('ConnectTime', c_char * 9),  # 完成连接时间
        ('StartDate', c_char * 9),  # 启动日期
        ('StartTime', c_char * 9),  # 启动时间
        ('TradingDay', c_char * 9),  # 交易日
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('MaxTradeID', c_char * 21),  # 本席位最大成交编号
        ('MaxOrderMessageReference', c_char * 7)  # 本席位最大报单备拷
    ]


class QryMDTraderOfferField(BaseField):
    """查询行情报盘机"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('TraderID', c_char * 21)  # 交易所交易员代码
    ]


class QryNoticeField(BaseField):
    """查询客户通知"""
    _fields_ = [
        ('BrokerID', c_char * 11)  # ///经纪公司代码
    ]


class NoticeField(BaseField):
    """客户通知"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('Content', c_char * 501),  # 消息正文
        ('SequenceLabel', c_char * 2)  # 经纪公司通知内容序列号
    ]


class UserRightField(BaseField):
    """用户权限"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('UserRightType', c_char * 1),  # 客户权限类型
        ('IsForbidden', c_int)  # 是否禁止
    ]


class QrySettlementInfoConfirmField(BaseField):
    """查询结算信息确认域"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class LoadSettlementInfoField(BaseField):
    """装载结算信息"""
    _fields_ = [
        ('BrokerID', c_char * 11)  # ///经纪公司代码
    ]


class BrokerWithdrawAlgorithmField(BaseField):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('WithdrawAlgorithm', c_char * 1),  # 可提资金算法
        ('UsingRatio', c_double),  # 资金使用率
        ('IncludeCloseProfit', c_char * 1),  # 可提是否包含平仓盈利
        ('AllWithoutTrade', c_char * 1),  # 本日无仓且无成交客户是否受可提比例限制
        ('AvailIncludeCloseProfit', c_char * 1),  # 可用是否包含平仓盈利
        ('IsBrokerUserEvent', c_int),  # 是否启用用户事件
        ('CurrencyID', c_char * 4),  # 币种代码
        ('FundMortgageRatio', c_double),  # 货币质押比率
        ('BalanceAlgorithm', c_char * 1)  # 权益算法
    ]


class TradingAccountPasswordUpdateV1Field(BaseField):
    """资金账户口令变更域"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OldPassword', c_char * 41),  # 原来的口令
        ('NewPassword', c_char * 41)  # 新的口令
    ]


class TradingAccountPasswordUpdateField(BaseField):
    """资金账户口令变更域"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('OldPassword', c_char * 41),  # 原来的口令
        ('NewPassword', c_char * 41),  # 新的口令
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class QryCombinationLegField(BaseField):
    """查询组合合约分腿"""
    _fields_ = [
        ('CombInstrumentID', c_char * 31),  # ///组合合约代码
        ('LegID', c_int),  # 单腿编号
        ('LegInstrumentID', c_char * 31)  # 单腿合约代码
    ]


class QrySyncStatusField(BaseField):
    """查询组合合约分腿"""
    _fields_ = [
        ('TradingDay', c_char * 9)  # ///交易日
    ]


class CombinationLegField(BaseField):
    """组合交易合约的单腿"""
    _fields_ = [
        ('CombInstrumentID', c_char * 31),  # ///组合合约代码
        ('LegID', c_int),  # 单腿编号
        ('LegInstrumentID', c_char * 31),  # 单腿合约代码
        ('Direction', c_char * 1),  # 买卖方向
        ('LegMultiple', c_int),  # 单腿乘数
        ('ImplyLevel', c_int)  # 派生层数
    ]


class SyncStatusField(BaseField):
    """数据同步状态"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('DataSyncStatus', c_char * 1)  # 数据同步状态
    ]


class QryLinkManField(BaseField):
    """查询联系人"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13)  # 投资者代码
    ]


class LinkManField(BaseField):
    """联系人"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('PersonType', c_char * 1),  # 联系人类型
        ('IdentifiedCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('PersonName', c_char * 81),  # 名称
        ('Telephone', c_char * 41),  # 联系电话
        ('Address', c_char * 101),  # 通讯地址
        ('ZipCode', c_char * 7),  # 邮政编码
        ('Priority', c_int),  # 优先级
        ('UOAZipCode', c_char * 11),  # 开户邮政编码
        ('PersonFullName', c_char * 101)  # 全称
    ]


class QryBrokerUserEventField(BaseField):
    """查询经纪公司用户事件"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('UserEventType', c_char * 1)  # 用户事件类型
    ]


class BrokerUserEventField(BaseField):
    """查询经纪公司用户事件"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('UserEventType', c_char * 1),  # 用户事件类型
        ('EventSequenceNo', c_int),  # 用户事件序号
        ('EventDate', c_char * 9),  # 事件发生日期
        ('EventTime', c_char * 9),  # 事件发生时间
        ('UserEventInfo', c_char * 1025),  # 用户事件信息
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31)  # 合约代码
    ]


class QryContractBankField(BaseField):
    """查询签约银行请求"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBrchID', c_char * 5)  # 银行分中心代码
    ]


class ContractBankField(BaseField):
    """查询签约银行响应"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBrchID', c_char * 5),  # 银行分中心代码
        ('BankName', c_char * 101)  # 银行名称
    ]


class InvestorPositionCombineDetailField(BaseField):
    """投资者组合持仓明细"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('OpenDate', c_char * 9),  # 开仓日期
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('SettlementID', c_int),  # 结算编号
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ComTradeID', c_char * 21),  # 组合编号
        ('TradeID', c_char * 21),  # 撮合编号
        ('InstrumentID', c_char * 31),  # 合约代码
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('Direction', c_char * 1),  # 买卖
        ('TotalAmt', c_int),  # 持仓量
        ('Margin', c_double),  # 投资者保证金
        ('ExchMargin', c_double),  # 交易所保证金
        ('MarginRateByMoney', c_double),  # 保证金率
        ('MarginRateByVolume', c_double),  # 保证金率(按手数)
        ('LegID', c_int),  # 单腿编号
        ('LegMultiple', c_int),  # 单腿乘数
        ('CombInstrumentID', c_char * 31),  # 组合持仓合约编码
        ('TradeGroupID', c_int),  # 成交组号
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class ParkedOrderField(BaseField):
    """预埋单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('OrderRef', c_char * 13),  # 报单引用
        ('UserID', c_char * 16),  # 用户代码
        ('OrderPriceType', c_char * 1),  # 报单价格条件
        ('Direction', c_char * 1),  # 买卖方向
        ('CombOffsetFlag', c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', c_char * 5),  # 组合投机套保标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeTotalOriginal', c_int),  # 数量
        ('TimeCondition', c_char * 1),  # 有效期类型
        ('GTDDate', c_char * 9),  # GTD日期
        ('VolumeCondition', c_char * 1),  # 成交量类型
        ('MinVolume', c_int),  # 最小成交量
        ('ContingentCondition', c_char * 1),  # 触发条件
        ('StopPrice', c_double),  # 止损价
        ('ForceCloseReason', c_char * 1),  # 强平原因
        ('IsAutoSuspend', c_int),  # 自动挂起标志
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('RequestID', c_int),  # 请求编号
        ('UserForceClose', c_int),  # 用户强评标志
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParkedOrderID', c_char * 13),  # 预埋报单编号
        ('UserType', c_char * 1),  # 用户类型
        ('Status', c_char * 1),  # 预埋单状态
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('IsSwapOrder', c_int),  # 互换单标志
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('ClientID', c_char * 11),  # 交易编码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ParkedOrderActionField(BaseField):
    """输入预埋单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OrderActionRef', c_int),  # 报单操作引用
        ('OrderRef', c_char * 13),  # 报单引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('OrderSysID', c_char * 21),  # 报单编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeChange', c_int),  # 数量变化
        ('UserID', c_char * 16),  # 用户代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ParkedOrderActionID', c_char * 13),  # 预埋撤单单编号
        ('UserType', c_char * 1),  # 用户类型
        ('Status', c_char * 1),  # 预埋撤单状态
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryParkedOrderField(BaseField):
    """查询预埋单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryParkedOrderActionField(BaseField):
    """查询预埋撤单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class RemoveParkedOrderField(BaseField):
    """删除预埋单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ParkedOrderID', c_char * 13),  # 预埋报单编号
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class RemoveParkedOrderActionField(BaseField):
    """删除预埋撤单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ParkedOrderActionID', c_char * 13),  # 预埋撤单编号
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class InvestorWithdrawAlgorithmField(BaseField):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('InvestorID', c_char * 13),  # 投资者代码
        ('UsingRatio', c_double),  # 可提资金比例
        ('CurrencyID', c_char * 4),  # 币种代码
        ('FundMortgageRatio', c_double)  # 货币质押比率
    ]


class QryInvestorPositionCombineDetailField(BaseField):
    """查询组合持仓明细"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('CombInstrumentID', c_char * 31),  # 组合持仓合约编码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class MarketDataAveragePriceField(BaseField):
    """成交均价"""
    _fields_ = [
        ('AveragePrice', c_double)  # ///当日均价
    ]


class VerifyInvestorPasswordField(BaseField):
    """校验投资者密码"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('Password', c_char * 41)  # 密码
    ]


class UserIPField(BaseField):
    """用户IP"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('IPAddress', c_char * 16),  # IP地址
        ('IPMask', c_char * 16),  # IP地址掩码
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class TradingNoticeInfoField(BaseField):
    """用户事件通知信息"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('SendTime', c_char * 9),  # 发送时间
        ('FieldContent', c_char * 501),  # 消息正文
        ('SequenceSeries', c_short),  # 序列系列号
        ('SequenceNo', c_int),  # 序列号
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class TradingNoticeField(BaseField):
    """用户事件通知"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('InvestorID', c_char * 13),  # 投资者代码
        ('SequenceSeries', c_short),  # 序列系列号
        ('UserID', c_char * 16),  # 用户代码
        ('SendTime', c_char * 9),  # 发送时间
        ('SequenceNo', c_int),  # 序列号
        ('FieldContent', c_char * 501),  # 消息正文
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryTradingNoticeField(BaseField):
    """查询交易事件通知"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryErrOrderField(BaseField):
    """查询错误报单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13)  # 投资者代码
    ]


class ErrOrderField(BaseField):
    """错误报单"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('OrderRef', c_char * 13),  # 报单引用
        ('UserID', c_char * 16),  # 用户代码
        ('OrderPriceType', c_char * 1),  # 报单价格条件
        ('Direction', c_char * 1),  # 买卖方向
        ('CombOffsetFlag', c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', c_char * 5),  # 组合投机套保标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeTotalOriginal', c_int),  # 数量
        ('TimeCondition', c_char * 1),  # 有效期类型
        ('GTDDate', c_char * 9),  # GTD日期
        ('VolumeCondition', c_char * 1),  # 成交量类型
        ('MinVolume', c_int),  # 最小成交量
        ('ContingentCondition', c_char * 1),  # 触发条件
        ('StopPrice', c_double),  # 止损价
        ('ForceCloseReason', c_char * 1),  # 强平原因
        ('IsAutoSuspend', c_int),  # 自动挂起标志
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('RequestID', c_int),  # 请求编号
        ('UserForceClose', c_int),  # 用户强评标志
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('IsSwapOrder', c_int),  # 互换单标志
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('ClientID', c_char * 11),  # 交易编码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class ErrorConditionalOrderField(BaseField):
    """查询错误报单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('OrderRef', c_char * 13),  # 报单引用
        ('UserID', c_char * 16),  # 用户代码
        ('OrderPriceType', c_char * 1),  # 报单价格条件
        ('Direction', c_char * 1),  # 买卖方向
        ('CombOffsetFlag', c_char * 5),  # 组合开平标志
        ('CombHedgeFlag', c_char * 5),  # 组合投机套保标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeTotalOriginal', c_int),  # 数量
        ('TimeCondition', c_char * 1),  # 有效期类型
        ('GTDDate', c_char * 9),  # GTD日期
        ('VolumeCondition', c_char * 1),  # 成交量类型
        ('MinVolume', c_int),  # 最小成交量
        ('ContingentCondition', c_char * 1),  # 触发条件
        ('StopPrice', c_double),  # 止损价
        ('ForceCloseReason', c_char * 1),  # 强平原因
        ('IsAutoSuspend', c_int),  # 自动挂起标志
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('RequestID', c_int),  # 请求编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('ExchangeInstID', c_char * 31),  # 合约在交易所的代码
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderSubmitStatus', c_char * 1),  # 报单提交状态
        ('NotifySequence', c_int),  # 报单提示序号
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('OrderSysID', c_char * 21),  # 报单编号
        ('OrderSource', c_char * 1),  # 报单来源
        ('OrderStatus', c_char * 1),  # 报单状态
        ('OrderType', c_char * 1),  # 报单类型
        ('VolumeTraded', c_int),  # 今成交数量
        ('VolumeTotal', c_int),  # 剩余数量
        ('InsertDate', c_char * 9),  # 报单日期
        ('InsertTime', c_char * 9),  # 委托时间
        ('ActiveTime', c_char * 9),  # 激活时间
        ('SuspendTime', c_char * 9),  # 挂起时间
        ('UpdateTime', c_char * 9),  # 最后修改时间
        ('CancelTime', c_char * 9),  # 撤销时间
        ('ActiveTraderID', c_char * 21),  # 最后修改交易所交易员代码
        ('ClearingPartID', c_char * 11),  # 结算会员编号
        ('SequenceNo', c_int),  # 序号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('StatusMsg', c_char * 81),  # 状态信息
        ('UserForceClose', c_int),  # 用户强评标志
        ('ActiveUserID', c_char * 16),  # 操作用户代码
        ('BrokerOrderSeq', c_int),  # 经纪公司报单编号
        ('RelativeOrderSysID', c_char * 21),  # 相关报单
        ('ZCETotalTradedVolume', c_int),  # 郑商所成交数量
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('IsSwapOrder', c_int),  # 互换单标志
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('AccountID', c_char * 13),  # 资金账号
        ('CurrencyID', c_char * 4),  # 币种代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21)  # Mac地址
    ]


class QryErrOrderActionField(BaseField):
    """查询错误报单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13)  # 投资者代码
    ]


class ErrOrderActionField(BaseField):
    """错误报单操作"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('OrderActionRef', c_int),  # 报单操作引用
        ('OrderRef', c_char * 13),  # 报单引用
        ('RequestID', c_int),  # 请求编号
        ('FrontID', c_int),  # 前置编号
        ('SessionID', c_int),  # 会话编号
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('OrderSysID', c_char * 21),  # 报单编号
        ('ActionFlag', c_char * 1),  # 操作标志
        ('LimitPrice', c_double),  # 价格
        ('VolumeChange', c_int),  # 数量变化
        ('ActionDate', c_char * 9),  # 操作日期
        ('ActionTime', c_char * 9),  # 操作时间
        ('TraderID', c_char * 21),  # 交易所交易员代码
        ('InstallID', c_int),  # 安装编号
        ('OrderLocalID', c_char * 13),  # 本地报单编号
        ('ActionLocalID', c_char * 13),  # 操作本地编号
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ClientID', c_char * 11),  # 客户代码
        ('BusinessUnit', c_char * 21),  # 业务单元
        ('OrderActionStatus', c_char * 1),  # 报单操作状态
        ('UserID', c_char * 16),  # 用户代码
        ('StatusMsg', c_char * 81),  # 状态信息
        ('InstrumentID', c_char * 31),  # 合约代码
        ('BranchID', c_char * 9),  # 营业部编号
        ('InvestUnitID', c_char * 17),  # 投资单元代码
        ('IPAddress', c_char * 16),  # IP地址
        ('MacAddress', c_char * 21),  # Mac地址
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class QryExchangeSequenceField(BaseField):
    """查询交易所状态"""
    _fields_ = [
        ('ExchangeID', c_char * 9)  # ///交易所代码
    ]


class ExchangeSequenceField(BaseField):
    """交易所状态"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('SequenceNo', c_int),  # 序号
        ('MarketStatus', c_char * 1)  # 合约交易状态
    ]


class QueryMaxOrderVolumeWithPriceField(BaseField):
    """根据价格查询最大报单数量"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('Direction', c_char * 1),  # 买卖方向
        ('OffsetFlag', c_char * 1),  # 开平标志
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('MaxVolume', c_int),  # 最大允许报单数量
        ('Price', c_double),  # 报单价格
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryBrokerTradingParamsField(BaseField):
    """查询经纪公司交易参数"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('CurrencyID', c_char * 4),  # 币种代码
        ('AccountID', c_char * 13)  # 投资者帐号
    ]


class BrokerTradingParamsField(BaseField):
    """经纪公司交易参数"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('MarginPriceType', c_char * 1),  # 保证金价格类型
        ('Algorithm', c_char * 1),  # 盈亏算法
        ('AvailIncludeCloseProfit', c_char * 1),  # 可用是否包含平仓盈利
        ('CurrencyID', c_char * 4),  # 币种代码
        ('OptionRoyaltyPriceType', c_char * 1),  # 期权权利金价格类型
        ('AccountID', c_char * 13)  # 投资者帐号
    ]


class QryBrokerTradingAlgosField(BaseField):
    """查询经纪公司交易算法"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InstrumentID', c_char * 31)  # 合约代码
    ]


class BrokerTradingAlgosField(BaseField):
    """经纪公司交易算法"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('HandlePositionAlgoID', c_char * 1),  # 持仓处理算法编号
        ('FindMarginRateAlgoID', c_char * 1),  # 寻找保证金率算法编号
        ('HandleTradingAccountAlgoID', c_char * 1)  # 资金处理算法编号
    ]


class QueryBrokerDepositField(BaseField):
    """查询经纪公司资金"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class BrokerDepositField(BaseField):
    """经纪公司资金"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日期
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('ParticipantID', c_char * 11),  # 会员代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('PreBalance', c_double),  # 上次结算准备金
        ('CurrMargin', c_double),  # 当前保证金总额
        ('CloseProfit', c_double),  # 平仓盈亏
        ('Balance', c_double),  # 期货结算准备金
        ('Deposit', c_double),  # 入金金额
        ('Withdraw', c_double),  # 出金金额
        ('Available', c_double),  # 可提资金
        ('Reserve', c_double),  # 基本准备金
        ('FrozenMargin', c_double)  # 冻结的保证金
    ]


class QryCFMMCBrokerKeyField(BaseField):
    """查询保证金监管系统经纪公司密钥"""
    _fields_ = [
        ('BrokerID', c_char * 11)  # ///经纪公司代码
    ]


class CFMMCBrokerKeyField(BaseField):
    """保证金监管系统经纪公司密钥"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('ParticipantID', c_char * 11),  # 经纪公司统一编码
        ('CreateDate', c_char * 9),  # 密钥生成日期
        ('CreateTime', c_char * 9),  # 密钥生成时间
        ('KeyID', c_int),  # 密钥编号
        ('CurrentKey', c_char * 21),  # 动态密钥
        ('KeyKind', c_char * 1)  # 动态密钥类型
    ]


class CFMMCTradingAccountKeyField(BaseField):
    """保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('ParticipantID', c_char * 11),  # 经纪公司统一编码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('KeyID', c_int),  # 密钥编号
        ('CurrentKey', c_char * 21)  # 动态密钥
    ]


class QryCFMMCTradingAccountKeyField(BaseField):
    """请求查询保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13)  # 投资者代码
    ]


class BrokerUserOTPParamField(BaseField):
    """用户动态令牌参数"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('OTPVendorsID', c_char * 2),  # 动态令牌提供商
        ('SerialNumber', c_char * 17),  # 动态令牌序列号
        ('AuthKey', c_char * 41),  # 令牌密钥
        ('LastDrift', c_int),  # 漂移值
        ('LastSuccess', c_int),  # 成功值
        ('OTPType', c_char * 1)  # 动态令牌类型
    ]


class ManualSyncBrokerUserOTPField(BaseField):
    """手工同步用户动态令牌"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('OTPType', c_char * 1),  # 动态令牌类型
        ('FirstOTP', c_char * 41),  # 第一个动态密码
        ('SecondOTP', c_char * 41)  # 第二个动态密码
    ]


class CommRateModelField(BaseField):
    """投资者手续费率模板"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('CommModelID', c_char * 13),  # 手续费率模板代码
        ('CommModelName', c_char * 161)  # 模板名称
    ]


class QryCommRateModelField(BaseField):
    """请求查询投资者手续费率模板"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('CommModelID', c_char * 13)  # 手续费率模板代码
    ]


class MarginModelField(BaseField):
    """投资者保证金率模板"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('MarginModelID', c_char * 13),  # 保证金率模板代码
        ('MarginModelName', c_char * 161)  # 模板名称
    ]


class QryMarginModelField(BaseField):
    """请求查询投资者保证金率模板"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('MarginModelID', c_char * 13)  # 保证金率模板代码
    ]


class EWarrantOffsetField(BaseField):
    """仓单折抵信息"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日期
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('Direction', c_char * 1),  # 买卖方向
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('Volume', c_int),  # 数量
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryEWarrantOffsetField(BaseField):
    """查询仓单折抵信息"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InstrumentID', c_char * 31),  # 合约代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QryInvestorProductGroupMarginField(BaseField):
    """查询投资者品种/跨品种保证金"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('ProductGroupID', c_char * 31),  # 品种/跨品种标示
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class InvestorProductGroupMarginField(BaseField):
    """投资者品种/跨品种保证金"""
    _fields_ = [
        ('ProductGroupID', c_char * 31),  # ///品种/跨品种标示
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('TradingDay', c_char * 9),  # 交易日
        ('SettlementID', c_int),  # 结算编号
        ('FrozenMargin', c_double),  # 冻结的保证金
        ('LongFrozenMargin', c_double),  # 多头冻结的保证金
        ('ShortFrozenMargin', c_double),  # 空头冻结的保证金
        ('UseMargin', c_double),  # 占用的保证金
        ('LongUseMargin', c_double),  # 多头保证金
        ('ShortUseMargin', c_double),  # 空头保证金
        ('ExchMargin', c_double),  # 交易所保证金
        ('LongExchMargin', c_double),  # 交易所多头保证金
        ('ShortExchMargin', c_double),  # 交易所空头保证金
        ('CloseProfit', c_double),  # 平仓盈亏
        ('FrozenCommission', c_double),  # 冻结的手续费
        ('Commission', c_double),  # 手续费
        ('FrozenCash', c_double),  # 冻结的资金
        ('CashIn', c_double),  # 资金差额
        ('PositionProfit', c_double),  # 持仓盈亏
        ('OffsetAmount', c_double),  # 折抵总金额
        ('LongOffsetAmount', c_double),  # 多头折抵总金额
        ('ShortOffsetAmount', c_double),  # 空头折抵总金额
        ('ExchOffsetAmount', c_double),  # 交易所折抵总金额
        ('LongExchOffsetAmount', c_double),  # 交易所多头折抵总金额
        ('ShortExchOffsetAmount', c_double),  # 交易所空头折抵总金额
        ('HedgeFlag', c_char * 1),  # 投机套保标志
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class QueryCFMMCTradingAccountTokenField(BaseField):
    """查询监控中心用户令牌"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('InvestUnitID', c_char * 17)  # 投资单元代码
    ]


class CFMMCTradingAccountTokenField(BaseField):
    """监控中心用户令牌"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('ParticipantID', c_char * 11),  # 经纪公司统一编码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('KeyID', c_int),  # 密钥编号
        ('Token', c_char * 21)  # 动态令牌
    ]


class QryProductGroupField(BaseField):
    """查询产品组"""
    _fields_ = [
        ('ProductID', c_char * 31),  # ///产品代码
        ('ExchangeID', c_char * 9)  # 交易所代码
    ]


class ProductGroupField(BaseField):
    """投资者品种/跨品种保证金产品组"""
    _fields_ = [
        ('ProductID', c_char * 31),  # ///产品代码
        ('ExchangeID', c_char * 9),  # 交易所代码
        ('ProductGroupID', c_char * 31)  # 产品组代码
    ]


class BulletinField(BaseField):
    """交易所公告"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('TradingDay', c_char * 9),  # 交易日
        ('BulletinID', c_int),  # 公告编号
        ('SequenceNo', c_int),  # 序列号
        ('NewsType', c_char * 3),  # 公告类型
        ('NewsUrgency', c_char * 1),  # 紧急程度
        ('SendTime', c_char * 9),  # 发送时间
        ('Abstract', c_char * 81),  # 消息摘要
        ('ComeFrom', c_char * 21),  # 消息来源
        ('Content', c_char * 501),  # 消息正文
        ('URLLink', c_char * 201),  # WEB地址
        ('MarketID', c_char * 31)  # 市场代码
    ]


class QryBulletinField(BaseField):
    """查询交易所公告"""
    _fields_ = [
        ('ExchangeID', c_char * 9),  # ///交易所代码
        ('BulletinID', c_int),  # 公告编号
        ('SequenceNo', c_int),  # 序列号
        ('NewsType', c_char * 3),  # 公告类型
        ('NewsUrgency', c_char * 1)  # 紧急程度
    ]


class ReqOpenAccountField(BaseField):
    """转帐开户请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('Gender', c_char * 1),  # 性别
        ('CountryCode', c_char * 21),  # 国家代码
        ('CustType', c_char * 1),  # 客户类型
        ('Address', c_char * 101),  # 地址
        ('ZipCode', c_char * 7),  # 邮编
        ('Telephone', c_char * 41),  # 电话号码
        ('MobilePhone', c_char * 21),  # 手机
        ('Fax', c_char * 41),  # 传真
        ('EMail', c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', c_char * 1),  # 资金账户状态
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('InstallID', c_int),  # 安装编号
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('CashExchangeCode', c_char * 1),  # 汇钞标志
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('TID', c_int),  # 交易ID
        ('UserID', c_char * 16),  # 用户标识
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class ReqCancelAccountField(BaseField):
    """转帐销户请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('Gender', c_char * 1),  # 性别
        ('CountryCode', c_char * 21),  # 国家代码
        ('CustType', c_char * 1),  # 客户类型
        ('Address', c_char * 101),  # 地址
        ('ZipCode', c_char * 7),  # 邮编
        ('Telephone', c_char * 41),  # 电话号码
        ('MobilePhone', c_char * 21),  # 手机
        ('Fax', c_char * 41),  # 传真
        ('EMail', c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', c_char * 1),  # 资金账户状态
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('InstallID', c_int),  # 安装编号
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('CashExchangeCode', c_char * 1),  # 汇钞标志
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('TID', c_int),  # 交易ID
        ('UserID', c_char * 16),  # 用户标识
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class ReqChangeAccountField(BaseField):
    """变更银行账户请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('Gender', c_char * 1),  # 性别
        ('CountryCode', c_char * 21),  # 国家代码
        ('CustType', c_char * 1),  # 客户类型
        ('Address', c_char * 101),  # 地址
        ('ZipCode', c_char * 7),  # 邮编
        ('Telephone', c_char * 41),  # 电话号码
        ('MobilePhone', c_char * 21),  # 手机
        ('Fax', c_char * 41),  # 传真
        ('EMail', c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', c_char * 1),  # 资金账户状态
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('NewBankAccount', c_char * 41),  # 新银行帐号
        ('NewBankPassWord', c_char * 41),  # 新银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('InstallID', c_int),  # 安装编号
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('TID', c_int),  # 交易ID
        ('Digest', c_char * 36),  # 摘要
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class ReqTransferField(BaseField):
    """转账请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('InstallID', c_int),  # 安装编号
        ('FutureSerial', c_int),  # 期货公司流水号
        ('UserID', c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('TradeAmount', c_double),  # 转帐金额
        ('FutureFetchAmount', c_double),  # 期货可取金额
        ('FeePayFlag', c_char * 1),  # 费用支付标志
        ('CustFee', c_double),  # 应收客户费用
        ('BrokerFee', c_double),  # 应收期货公司费用
        ('Message', c_char * 129),  # 发送方给接收方的消息
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('TransferStatus', c_char * 1),  # 转账交易状态
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class RspTransferField(BaseField):
    """银行发起银行资金转期货响应"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('InstallID', c_int),  # 安装编号
        ('FutureSerial', c_int),  # 期货公司流水号
        ('UserID', c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('TradeAmount', c_double),  # 转帐金额
        ('FutureFetchAmount', c_double),  # 期货可取金额
        ('FeePayFlag', c_char * 1),  # 费用支付标志
        ('CustFee', c_double),  # 应收客户费用
        ('BrokerFee', c_double),  # 应收期货公司费用
        ('Message', c_char * 129),  # 发送方给接收方的消息
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('TransferStatus', c_char * 1),  # 转账交易状态
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class ReqRepealField(BaseField):
    """冲正请求"""
    _fields_ = [
        ('RepealTimeInterval', c_int),  # ///冲正时间间隔
        ('RepealedTimes', c_int),  # 已经冲正次数
        ('BankRepealFlag', c_char * 1),  # 银行冲正标志
        ('BrokerRepealFlag', c_char * 1),  # 期商冲正标志
        ('PlateRepealSerial', c_int),  # 被冲正平台流水号
        ('BankRepealSerial', c_char * 13),  # 被冲正银行流水号
        ('FutureRepealSerial', c_int),  # 被冲正期货流水号
        ('TradeCode', c_char * 7),  # 业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('InstallID', c_int),  # 安装编号
        ('FutureSerial', c_int),  # 期货公司流水号
        ('UserID', c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('TradeAmount', c_double),  # 转帐金额
        ('FutureFetchAmount', c_double),  # 期货可取金额
        ('FeePayFlag', c_char * 1),  # 费用支付标志
        ('CustFee', c_double),  # 应收客户费用
        ('BrokerFee', c_double),  # 应收期货公司费用
        ('Message', c_char * 129),  # 发送方给接收方的消息
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('TransferStatus', c_char * 1),  # 转账交易状态
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class RspRepealField(BaseField):
    """冲正响应"""
    _fields_ = [
        ('RepealTimeInterval', c_int),  # ///冲正时间间隔
        ('RepealedTimes', c_int),  # 已经冲正次数
        ('BankRepealFlag', c_char * 1),  # 银行冲正标志
        ('BrokerRepealFlag', c_char * 1),  # 期商冲正标志
        ('PlateRepealSerial', c_int),  # 被冲正平台流水号
        ('BankRepealSerial', c_char * 13),  # 被冲正银行流水号
        ('FutureRepealSerial', c_int),  # 被冲正期货流水号
        ('TradeCode', c_char * 7),  # 业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('InstallID', c_int),  # 安装编号
        ('FutureSerial', c_int),  # 期货公司流水号
        ('UserID', c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('TradeAmount', c_double),  # 转帐金额
        ('FutureFetchAmount', c_double),  # 期货可取金额
        ('FeePayFlag', c_char * 1),  # 费用支付标志
        ('CustFee', c_double),  # 应收客户费用
        ('BrokerFee', c_double),  # 应收期货公司费用
        ('Message', c_char * 129),  # 发送方给接收方的消息
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('TransferStatus', c_char * 1),  # 转账交易状态
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class ReqQueryAccountField(BaseField):
    """查询账户信息请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('FutureSerial', c_int),  # 期货公司流水号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class RspQueryAccountField(BaseField):
    """查询账户信息响应"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('FutureSerial', c_int),  # 期货公司流水号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('BankUseAmount', c_double),  # 银行可用金额
        ('BankFetchAmount', c_double),  # 银行可取金额
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class FutureSignIOField(BaseField):
    """期商签到签退"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('Digest', c_char * 36),  # 摘要
        ('CurrencyID', c_char * 4),  # 币种代码
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int)  # 交易ID
    ]


class RspFutureSignInField(BaseField):
    """期商签到响应"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('Digest', c_char * 36),  # 摘要
        ('CurrencyID', c_char * 4),  # 币种代码
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('PinKey', c_char * 129),  # PIN密钥
        ('MacKey', c_char * 129)  # MAC密钥
    ]


class ReqFutureSignOutField(BaseField):
    """期商签退请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('Digest', c_char * 36),  # 摘要
        ('CurrencyID', c_char * 4),  # 币种代码
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int)  # 交易ID
    ]


class RspFutureSignOutField(BaseField):
    """期商签退响应"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('Digest', c_char * 36),  # 摘要
        ('CurrencyID', c_char * 4),  # 币种代码
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class ReqQueryTradeResultBySerialField(BaseField):
    """查询指定流水号的交易结果请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('Reference', c_int),  # 流水号
        ('RefrenceIssureType', c_char * 1),  # 本流水号发布者的机构类型
        ('RefrenceIssure', c_char * 36),  # 本流水号发布者机构编码
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('CurrencyID', c_char * 4),  # 币种代码
        ('TradeAmount', c_double),  # 转帐金额
        ('Digest', c_char * 36),  # 摘要
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class RspQueryTradeResultBySerialField(BaseField):
    """查询指定流水号的交易结果响应"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('Reference', c_int),  # 流水号
        ('RefrenceIssureType', c_char * 1),  # 本流水号发布者的机构类型
        ('RefrenceIssure', c_char * 36),  # 本流水号发布者机构编码
        ('OriginReturnCode', c_char * 7),  # 原始返回代码
        ('OriginDescrInfoForReturnCode', c_char * 129),  # 原始返回码描述
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('CurrencyID', c_char * 4),  # 币种代码
        ('TradeAmount', c_double),  # 转帐金额
        ('Digest', c_char * 36)  # 摘要
    ]


class ReqDayEndFileReadyField(BaseField):
    """日终文件就绪请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('FileBusinessCode', c_char * 1),  # 文件业务功能
        ('Digest', c_char * 36)  # 摘要
    ]


class ReturnResultField(BaseField):
    """返回结果"""
    _fields_ = [
        ('ReturnCode', c_char * 7),  # ///返回代码
        ('DescrInfoForReturnCode', c_char * 129)  # 返回码描述
    ]


class VerifyFuturePasswordField(BaseField):
    """验证期货资金密码"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('InstallID', c_int),  # 安装编号
        ('TID', c_int),  # 交易ID
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class VerifyCustInfoField(BaseField):
    """验证客户信息"""
    _fields_ = [
        ('CustomerName', c_char * 51),  # ///客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class VerifyFuturePasswordAndCustInfoField(BaseField):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ('CustomerName', c_char * 51),  # ///客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('CurrencyID', c_char * 4),  # 币种代码
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class DepositResultInformField(BaseField):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ('DepositSeqNo', c_char * 15),  # ///出入金流水号，该流水号为银期报盘返回的流水号
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('InvestorID', c_char * 13),  # 投资者代码
        ('Deposit', c_double),  # 入金金额
        ('RequestID', c_int),  # 请求编号
        ('ReturnCode', c_char * 7),  # 返回代码
        ('DescrInfoForReturnCode', c_char * 129)  # 返回码描述
    ]


class ReqSyncKeyField(BaseField):
    """交易核心向银期报盘发出密钥同步请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('Message', c_char * 129),  # 交易核心给银期报盘的消息
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int)  # 交易ID
    ]


class RspSyncKeyField(BaseField):
    """交易核心向银期报盘发出密钥同步响应"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('Message', c_char * 129),  # 交易核心给银期报盘的消息
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class NotifyQueryAccountField(BaseField):
    """查询账户信息通知"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustType', c_char * 1),  # 客户类型
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('FutureSerial', c_int),  # 期货公司流水号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('BankUseAmount', c_double),  # 银行可用金额
        ('BankFetchAmount', c_double),  # 银行可取金额
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class TransferSerialField(BaseField):
    """银期转账交易流水表"""
    _fields_ = [
        ('PlateSerial', c_int),  # ///平台流水号
        ('TradeDate', c_char * 9),  # 交易发起方日期
        ('TradingDay', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('TradeCode', c_char * 7),  # 交易代码
        ('SessionID', c_int),  # 会话编号
        ('BankID', c_char * 4),  # 银行编码
        ('BankBranchID', c_char * 5),  # 银行分支机构编码
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankSerial', c_char * 13),  # 银行流水号
        ('BrokerID', c_char * 11),  # 期货公司编码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('FutureAccType', c_char * 1),  # 期货公司帐号类型
        ('AccountID', c_char * 13),  # 投资者帐号
        ('InvestorID', c_char * 13),  # 投资者代码
        ('FutureSerial', c_int),  # 期货公司流水号
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CurrencyID', c_char * 4),  # 币种代码
        ('TradeAmount', c_double),  # 交易金额
        ('CustFee', c_double),  # 应收客户费用
        ('BrokerFee', c_double),  # 应收期货公司费用
        ('AvailabilityFlag', c_char * 1),  # 有效标志
        ('OperatorCode', c_char * 17),  # 操作员
        ('BankNewAccount', c_char * 41),  # 新银行帐号
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class QryTransferSerialField(BaseField):
    """请求查询转帐流水"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('BankID', c_char * 4),  # 银行编码
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class NotifyFutureSignInField(BaseField):
    """期商签到通知"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('Digest', c_char * 36),  # 摘要
        ('CurrencyID', c_char * 4),  # 币种代码
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('PinKey', c_char * 129),  # PIN密钥
        ('MacKey', c_char * 129)  # MAC密钥
    ]


class NotifyFutureSignOutField(BaseField):
    """期商签退通知"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('Digest', c_char * 36),  # 摘要
        ('CurrencyID', c_char * 4),  # 币种代码
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class NotifySyncKeyField(BaseField):
    """交易核心向银期报盘发出密钥同步处理结果的通知"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('InstallID', c_int),  # 安装编号
        ('UserID', c_char * 16),  # 用户标识
        ('Message', c_char * 129),  # 交易核心给银期报盘的消息
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('OperNo', c_char * 17),  # 交易柜员
        ('RequestID', c_int),  # 请求编号
        ('TID', c_int),  # 交易ID
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class QryAccountregisterField(BaseField):
    """请求查询银期签约关系"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('BankID', c_char * 4),  # 银行编码
        ('BankBranchID', c_char * 5),  # 银行分支机构编码
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class AccountregisterField(BaseField):
    """客户开销户信息表"""
    _fields_ = [
        ('TradeDay', c_char * 9),  # ///交易日期
        ('BankID', c_char * 4),  # 银行编码
        ('BankBranchID', c_char * 5),  # 银行分支机构编码
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BrokerID', c_char * 11),  # 期货公司编码
        ('BrokerBranchID', c_char * 31),  # 期货公司分支机构编码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('CustomerName', c_char * 51),  # 客户姓名
        ('CurrencyID', c_char * 4),  # 币种代码
        ('OpenOrDestroy', c_char * 1),  # 开销户类别
        ('RegDate', c_char * 9),  # 签约日期
        ('OutDate', c_char * 9),  # 解约日期
        ('TID', c_int),  # 交易ID
        ('CustType', c_char * 1),  # 客户类型
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class OpenAccountField(BaseField):
    """银期开户信息"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('Gender', c_char * 1),  # 性别
        ('CountryCode', c_char * 21),  # 国家代码
        ('CustType', c_char * 1),  # 客户类型
        ('Address', c_char * 101),  # 地址
        ('ZipCode', c_char * 7),  # 邮编
        ('Telephone', c_char * 41),  # 电话号码
        ('MobilePhone', c_char * 21),  # 手机
        ('Fax', c_char * 41),  # 传真
        ('EMail', c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', c_char * 1),  # 资金账户状态
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('InstallID', c_int),  # 安装编号
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('CashExchangeCode', c_char * 1),  # 汇钞标志
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('TID', c_int),  # 交易ID
        ('UserID', c_char * 16),  # 用户标识
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class CancelAccountField(BaseField):
    """银期销户信息"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('Gender', c_char * 1),  # 性别
        ('CountryCode', c_char * 21),  # 国家代码
        ('CustType', c_char * 1),  # 客户类型
        ('Address', c_char * 101),  # 地址
        ('ZipCode', c_char * 7),  # 邮编
        ('Telephone', c_char * 41),  # 电话号码
        ('MobilePhone', c_char * 21),  # 手机
        ('Fax', c_char * 41),  # 传真
        ('EMail', c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', c_char * 1),  # 资金账户状态
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('InstallID', c_int),  # 安装编号
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('CashExchangeCode', c_char * 1),  # 汇钞标志
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('DeviceID', c_char * 3),  # 渠道标志
        ('BankSecuAccType', c_char * 1),  # 期货单位帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankSecuAcc', c_char * 41),  # 期货单位帐号
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('OperNo', c_char * 17),  # 交易柜员
        ('TID', c_int),  # 交易ID
        ('UserID', c_char * 16),  # 用户标识
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class ChangeAccountField(BaseField):
    """银期变更银行账号信息"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 51),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('Gender', c_char * 1),  # 性别
        ('CountryCode', c_char * 21),  # 国家代码
        ('CustType', c_char * 1),  # 客户类型
        ('Address', c_char * 101),  # 地址
        ('ZipCode', c_char * 7),  # 邮编
        ('Telephone', c_char * 41),  # 电话号码
        ('MobilePhone', c_char * 21),  # 手机
        ('Fax', c_char * 41),  # 传真
        ('EMail', c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', c_char * 1),  # 资金账户状态
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('NewBankAccount', c_char * 41),  # 新银行帐号
        ('NewBankPassWord', c_char * 41),  # 新银行密码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('InstallID', c_int),  # 安装编号
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('BankPwdFlag', c_char * 1),  # 银行密码标志
        ('SecuPwdFlag', c_char * 1),  # 期货资金密码核对标志
        ('TID', c_int),  # 交易ID
        ('Digest', c_char * 36),  # 摘要
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81),  # 错误信息
        ('LongCustomerName', c_char * 161)  # 长客户姓名
    ]


class SecAgentACIDMapField(BaseField):
    """二级代理操作员银期权限"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('AccountID', c_char * 13),  # 资金账户
        ('CurrencyID', c_char * 4),  # 币种
        ('BrokerSecAgentID', c_char * 13)  # 境外中介机构资金帐号
    ]


class QrySecAgentACIDMapField(BaseField):
    """二级代理操作员银期权限查询"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('AccountID', c_char * 13),  # 资金账户
        ('CurrencyID', c_char * 4)  # 币种
    ]


class UserRightsAssignField(BaseField):
    """灾备中心交易权限"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///应用单元代码
        ('UserID', c_char * 16),  # 用户代码
        ('DRIdentityID', c_int)  # 交易中心代码
    ]


class BrokerUserRightAssignField(BaseField):
    """经济公司是否有在本标示的交易权限"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///应用单元代码
        ('DRIdentityID', c_int),  # 交易中心代码
        ('Tradeable', c_int)  # 能否交易
    ]


class DRTransferField(BaseField):
    """灾备交易转换报文"""
    _fields_ = [
        ('OrigDRIdentityID', c_int),  # ///原交易中心代码
        ('DestDRIdentityID', c_int),  # 目标交易中心代码
        ('OrigBrokerID', c_char * 11),  # 原应用单元代码
        ('DestBrokerID', c_char * 11)  # 目标易用单元代码
    ]


class FensUserInfoField(BaseField):
    """Fens用户信息"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('LoginMode', c_char * 1)  # 登录模式
    ]


class CurrTransferIdentityField(BaseField):
    """当前银期所属交易中心"""
    _fields_ = [
        ('IdentityID', c_int)  # ///交易中心代码
    ]


class LoginForbiddenUserField(BaseField):
    """禁止登录用户"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('IPAddress', c_char * 16)  # IP地址
    ]


class QryLoginForbiddenUserField(BaseField):
    """查询禁止登录用户"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class MulticastGroupInfoField(BaseField):
    """UDP组播组信息"""
    _fields_ = [
        ('GroupIP', c_char * 16),  # ///组播组IP地址
        ('GroupPort', c_int),  # 组播组IP端口
        ('SourceIP', c_char * 16)  # 源地址
    ]


class TradingAccountReserveField(BaseField):
    """资金账户基本准备金"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Reserve', c_double),  # 基本准备金
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class QryLoginForbiddenIPField(BaseField):
    """查询禁止登录IP"""
    _fields_ = [
        ('IPAddress', c_char * 16)  # ///IP地址
    ]


class QryIPListField(BaseField):
    """查询IP列表"""
    _fields_ = [
        ('IPAddress', c_char * 16)  # ///IP地址
    ]


class QryUserRightsAssignField(BaseField):
    """查询用户下单权限分配表"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///应用单元代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class ReserveOpenAccountConfirmField(BaseField):
    """银期预约开户确认请求"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 161),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('Gender', c_char * 1),  # 性别
        ('CountryCode', c_char * 21),  # 国家代码
        ('CustType', c_char * 1),  # 客户类型
        ('Address', c_char * 101),  # 地址
        ('ZipCode', c_char * 7),  # 邮编
        ('Telephone', c_char * 41),  # 电话号码
        ('MobilePhone', c_char * 21),  # 手机
        ('Fax', c_char * 41),  # 传真
        ('EMail', c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', c_char * 1),  # 资金账户状态
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('InstallID', c_int),  # 安装编号
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('TID', c_int),  # 交易ID
        ('AccountID', c_char * 13),  # 投资者帐号
        ('Password', c_char * 41),  # 期货密码
        ('BankReserveOpenSeq', c_char * 13),  # 预约开户银行流水号
        ('BookDate', c_char * 9),  # 预约开户日期
        ('BookPsw', c_char * 41),  # 预约开户验证密码
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class ReserveOpenAccountField(BaseField):
    """银期预约开户"""
    _fields_ = [
        ('TradeCode', c_char * 7),  # ///业务功能码
        ('BankID', c_char * 4),  # 银行代码
        ('BankBranchID', c_char * 5),  # 银行分支机构代码
        ('BrokerID', c_char * 11),  # 期商代码
        ('BrokerBranchID', c_char * 31),  # 期商分支机构代码
        ('TradeDate', c_char * 9),  # 交易日期
        ('TradeTime', c_char * 9),  # 交易时间
        ('BankSerial', c_char * 13),  # 银行流水号
        ('TradingDay', c_char * 9),  # 交易系统日期
        ('PlateSerial', c_int),  # 银期平台消息流水号
        ('LastFragment', c_char * 1),  # 最后分片标志
        ('SessionID', c_int),  # 会话号
        ('CustomerName', c_char * 161),  # 客户姓名
        ('IdCardType', c_char * 1),  # 证件类型
        ('IdentifiedCardNo', c_char * 51),  # 证件号码
        ('Gender', c_char * 1),  # 性别
        ('CountryCode', c_char * 21),  # 国家代码
        ('CustType', c_char * 1),  # 客户类型
        ('Address', c_char * 101),  # 地址
        ('ZipCode', c_char * 7),  # 邮编
        ('Telephone', c_char * 41),  # 电话号码
        ('MobilePhone', c_char * 21),  # 手机
        ('Fax', c_char * 41),  # 传真
        ('EMail', c_char * 41),  # 电子邮件
        ('MoneyAccountStatus', c_char * 1),  # 资金账户状态
        ('BankAccount', c_char * 41),  # 银行帐号
        ('BankPassWord', c_char * 41),  # 银行密码
        ('InstallID', c_int),  # 安装编号
        ('VerifyCertNoFlag', c_char * 1),  # 验证客户证件号码标志
        ('CurrencyID', c_char * 4),  # 币种代码
        ('Digest', c_char * 36),  # 摘要
        ('BankAccType', c_char * 1),  # 银行帐号类型
        ('BrokerIDByBank', c_char * 33),  # 期货公司银行编码
        ('TID', c_int),  # 交易ID
        ('ReserveOpenAccStas', c_char * 1),  # 预约开户状态
        ('ErrorID', c_int),  # 错误代码
        ('ErrorMsg', c_char * 81)  # 错误信息
    ]


class AccountPropertyField(BaseField):
    """银行账户属性"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('AccountID', c_char * 13),  # 投资者帐号
        ('BankID', c_char * 4),  # 银行统一标识类型
        ('BankAccount', c_char * 41),  # 银行账户
        ('OpenName', c_char * 101),  # 银行账户的开户人名称
        ('OpenBank', c_char * 101),  # 银行账户的开户行
        ('IsActive', c_int),  # 是否活跃
        ('AccountSourceType', c_char * 1),  # 账户来源
        ('OpenDate', c_char * 9),  # 开户日期
        ('CancelDate', c_char * 9),  # 注销日期
        ('OperatorID', c_char * 65),  # 录入员代码
        ('OperateDate', c_char * 9),  # 录入日期
        ('OperateTime', c_char * 9),  # 录入时间
        ('CurrencyID', c_char * 4)  # 币种代码
    ]


class QryCurrDRIdentityField(BaseField):
    """查询当前交易中心"""
    _fields_ = [
        ('DRIdentityID', c_int)  # ///交易中心代码
    ]


class CurrDRIdentityField(BaseField):
    """当前交易中心"""
    _fields_ = [
        ('DRIdentityID', c_int)  # ///交易中心代码
    ]


class QrySecAgentCheckModeField(BaseField):
    """查询二级代理商资金校验模式"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('InvestorID', c_char * 13)  # 投资者代码
    ]


class QrySecAgentTradeInfoField(BaseField):
    """查询二级代理商信息"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('BrokerSecAgentID', c_char * 13)  # 境外中介机构资金帐号
    ]


class UserSystemInfoField(BaseField):
    """用户系统信息"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('ClientSystemInfoLen', c_int),  # 用户端系统内部信息长度
        ('ClientSystemInfo', c_char * 273),  # 用户端系统内部信息
        ('ClientPublicIP', c_char * 16),  # 用户公网IP
        ('ClientIPPort', c_int),  # 终端IP端口
        ('ClientLoginTime', c_char * 9),  # 登录成功时间
        ('ClientAppID', c_char * 33)  # App代码
    ]


class ReqUserAuthMethodField(BaseField):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class RspUserAuthMethodField(BaseField):
    """用户发出获取安全安全登陆方法回复"""
    _fields_ = [
        ('UsableAuthMethod', c_int)  # ///当前可以用的认证模式
    ]


class ReqGenUserCaptchaField(BaseField):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class RspGenUserCaptchaField(BaseField):
    """生成的图片验证码信息"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('CaptchaInfoLen', c_int),  # 图片信息长度
        ('CaptchaInfo', c_char * 2561)  # 图片信息
    ]


class ReqGenUserTextField(BaseField):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16)  # 用户代码
    ]


class RspGenUserTextField(BaseField):
    """短信验证码生成的回复"""
    _fields_ = [
        ('UserTextSeq', c_int)  # ///短信验证码序号
    ]


class ReqUserLoginWithCaptchaField(BaseField):
    """用户发出带图形验证码的登录请求请求"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('Password', c_char * 41),  # 密码
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', c_char * 11),  # 协议信息
        ('MacAddress', c_char * 21),  # Mac地址
        ('ClientIPAddress', c_char * 16),  # 终端IP地址
        ('LoginRemark', c_char * 36),  # 登录备注
        ('Captcha', c_char * 41),  # 图形验证码的文字内容
        ('ClientIPPort', c_int)  # 终端IP端口
    ]


class ReqUserLoginWithTextField(BaseField):
    """用户发出带短信验证码的登录请求请求"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('Password', c_char * 41),  # 密码
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', c_char * 11),  # 协议信息
        ('MacAddress', c_char * 21),  # Mac地址
        ('ClientIPAddress', c_char * 16),  # 终端IP地址
        ('LoginRemark', c_char * 36),  # 登录备注
        ('Text', c_char * 41),  # 短信验证码文字内容
        ('ClientIPPort', c_int)  # 终端IP端口
    ]


class ReqUserLoginWithOTPField(BaseField):
    """用户发出带动态验证码的登录请求请求"""
    _fields_ = [
        ('TradingDay', c_char * 9),  # ///交易日
        ('BrokerID', c_char * 11),  # 经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('Password', c_char * 41),  # 密码
        ('UserProductInfo', c_char * 11),  # 用户端产品信息
        ('InterfaceProductInfo', c_char * 11),  # 接口端产品信息
        ('ProtocolInfo', c_char * 11),  # 协议信息
        ('MacAddress', c_char * 21),  # Mac地址
        ('ClientIPAddress', c_char * 16),  # 终端IP地址
        ('LoginRemark', c_char * 36),  # 登录备注
        ('OTPPassword', c_char * 41),  # OTP密码
        ('ClientIPPort', c_int)  # 终端IP端口
    ]


class ReqApiHandshakeField(BaseField):
    """api握手请求"""
    _fields_ = [
        ('CryptoKeyVersion', c_char * 31)  # ///api与front通信密钥版本号
    ]


class RspApiHandshakeField(BaseField):
    """front发给api的握手回复"""
    _fields_ = [
        ('FrontHandshakeDataLen', c_int),  # ///握手回复数据长度
        ('FrontHandshakeData', c_char * 301),  # 握手回复数据
        ('IsApiAuthEnabled', c_int)  # API认证是否开启
    ]


class ReqVerifyApiKeyField(BaseField):
    """api给front的验证key的请求"""
    _fields_ = [
        ('ApiHandshakeDataLen', c_int),  # ///握手回复数据长度
        ('ApiHandshakeData', c_char * 301)  # 握手回复数据
    ]


class DepartmentUserField(BaseField):
    """操作员组织架构关系"""
    _fields_ = [
        ('BrokerID', c_char * 11),  # ///经纪公司代码
        ('UserID', c_char * 16),  # 用户代码
        ('InvestorRange', c_char * 1),  # 投资者范围
        ('InvestorID', c_char * 13)  # 投资者代码
    ]


class QueryFreqField(BaseField):
    """查询频率，每秒查询比数"""
    _fields_ = [
        ('QueryFreq', c_int)  # ///查询频率
    ]

    def __init__(self, QueryFreq=0):
        super(QueryFreqField, self).__init__()
        self.QueryFreq = int(QueryFreq)

    def from_tuple(self, i_tuple):
        self.QueryFreq = int(i_tuple[1])
