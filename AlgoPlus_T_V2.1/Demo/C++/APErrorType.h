#ifndef AP_ERRORS_H__
#define AP_ERRORS_H__

/////////////////////////////////////////////////////////////////////////
/// TAPErrorIDType是一个错误代码类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPErrorIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPMessageType是一个信息类型
/////////////////////////////////////////////////////////////////////////
typedef char TAPMessageType[256];

/// 无错误
#define ENUM_ErrorID_None 0
#define ENUM_ErrorMsg_None ""

/// 暂不支持
#define ENUM_ErrorID_Unsupported -1000100
#define ENUM_ErrorMsg_Unsupported "Error:Unsupported."

/// 非法的RunID
#define ENUM_ErrorID_InvalidRunID -1000200
#define ENUM_ErrorMsg_InvalidRunID "Error:RunID should belong to [0,99]."

/// 非法的登录信息
#define ENUM_ErrorID_InvalidLoginField -1000300
#define ENUM_ErrorMsg_InvalidLoginField "Error:Invalid LoginField."

/// 未授权
#define ENUM_ErrorID_Unauthorized -1000400
#define ENUM_ErrorMsg_Unauthorized "Error:Unauthorized."

/// 非法的客户号
#define ENUM_ErrorID_InvalidUserID -1000500
#define ENUM_ErrorMsg_InvalidUserID "Error:Invalid UserID."

/// 非法的密码
#define ENUM_ErrorID_InvalidPassword -1000600
#define ENUM_ErrorMsg_InvalidPassword "Error:Invalid Password."

/// 非法的用户类型
#define ENUM_ErrorID_InvalidUserType -1000700
#define ENUM_ErrorMsg_InvalidUserType "Error:Invalid UserType."

/// 非法的交易前置地址
#define ENUM_ErrorID_InvalidTraderFront -1000800
#define ENUM_ErrorMsg_InvalidTraderFront "Error:Invalid TraderFront."

/// 非法的行情前置地址
#define ENUM_ErrorID_InvalidMdFront -1000900
#define ENUM_ErrorMsg_InvalidMdFront "Error:Invalid MdFront."

/// 非法的文件路径
#define ENUM_ErrorID_InvalidFilePath -1001000
#define ENUM_ErrorMsg_InvalidFilePath "Error:Invalid FilePath."

/// 非法的BrokerID
#define ENUM_ErrorID_InvalidBrokerID -1001100
#define ENUM_ErrorMsg_InvalidBrokerID "Error:Invalid BrokerID."

/// 非法的AppID
#define ENUM_ErrorID_InvalidAppID -1001200
#define ENUM_ErrorMsg_InvalidAppID "Error:Invalid AppID."

/// 非法的AuthCode
#define ENUM_ErrorID_InvalidAuthCode -1001300
#define ENUM_ErrorMsg_InvalidAuthCode "Error:Invalid AuthCode."

/// 创建TraderApi实例失败
#define ENUM_ErrorID_FailToCreateTrader -1001400
#define ENUM_ErrorMsg_FailToCreateTrader "Error:Fail To Create Trader."

/// 与交易前置连接超时
#define ENUM_ErrorID_TraderConnectTimeout -1001500
#define ENUM_ErrorMsg_TraderConnectTimeout "Error:Trader Connect Timeout."

/// 与交易前置连接断开
#define ENUM_ErrorID_TraderDisconnected -1001600
#define ENUM_ErrorMsg_TraderDisconnected "Error:Trader Disconnected."

/// 创建MdApi实例失败
#define ENUM_ErrorID_FailToCreateMd -1001700
#define ENUM_ErrorMsg_FailToCreateMd "Error:Fail To Create Md."

/// 与行情前置连接超时
#define ENUM_ErrorID_MdConnectTimeout -1001800
#define ENUM_ErrorMsg_MdConnectTimeout "Error:Md Connect Timeout."

/// 与行情前置连接断开
#define ENUM_ErrorID_MdDisconnected -1001900
#define ENUM_ErrorMsg_MdDisconnected "Error:Md Disconnected."

/// 非法的TraderApi实例
#define ENUM_ErrorID_InvalidTraderInstance -1002000
#define ENUM_ErrorMsg_InvalidTraderInstance "Error:Invalid Trader Instance."

/// 非法的MdApi实例
#define ENUM_ErrorID_InvalidMdInstance -1002100
#define ENUM_ErrorMsg_InvalidMdInstance "Error:Invalid Md Instance."

/// 发送失败
#define ENUM_ErrorID_FailToSended -1002200
#define ENUM_ErrorMsg_FailToSended "Error:Fail To Sended."

/// 响应超时
#define ENUM_ErrorID_ResponseTimeout -1002300
#define ENUM_ErrorMsg_ResponseTimeout "Error:Response Timeout."

/// 非法价格
#define ENUM_ErrorID_InvalidPrice -1002400
#define ENUM_ErrorMsg_InvalidPrice "Error:Invalid Price."

/// 非法价格
#define ENUM_ErrorID_InvalidVolume -1002500
#define ENUM_ErrorMsg_InvalidVolume "Error:Invalid Volume."

/// 柜台拒绝
#define ENUM_ErrorID_BrokerReject -1002600
#define ENUM_ErrorMsg_BrokerReject "Error:Broker Reject."

/// 交易所拒绝
#define ENUM_ErrorID_ExchangeReject -1002700
#define ENUM_ErrorMsg_ExchangeReject "Error:Exchange Reject."

/// 非法的订单事件ID
#define ENUM_ErrorID_InvalidOrderEventID -10002800
#define ENUM_ErrorMsg_InvalidOrderEventID "Error:Invalid OrderEventID."

/// 非法的行情类型
#define ENUM_ErrorID_InvalidMarketDataType -1002900
#define ENUM_ErrorMsg_InvalidMarketDataType "Error:Invalid MarketDataType."

/// 非法的行情事件ID
#define ENUM_ErrorID_InvalidSnapDataEventID -10003000
#define ENUM_ErrorMsg_InvalidSnapDataEventID "Error:Invalid SnapDataEventID."

/// 非法的逐笔行情事件ID
#define ENUM_ErrorID_InvalidDetailDataEventID -10003100
#define ENUM_ErrorMsg_InvalidDetailDataEventID "Error:Invalid DetailDataEventID."

/// 非法的TaskID
#define ENUM_ErrorID_InvalidTaskID -1003200
#define ENUM_ErrorMsg_InvalidTaskID "Error:Invalid TaskID."

/// 非法的密码标识
#define ENUM_ErrorID_InvalidPasswordFlag -1003300
#define ENUM_ErrorMsg_InvalidPasswordFlag "Error:Failed To RepealTransferAsset."

#endif
