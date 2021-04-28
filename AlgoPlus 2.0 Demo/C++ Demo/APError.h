#ifndef AP_ERRORS_H__
#define AP_ERRORS_H__


#include "APDataType.h"


/// 无错误
const TAPErrorIDType ENUM_ErrorID_None = 0;
const TAPMessageType ENUM_ErrorMsg_None = "";

/// 暂不支持
const TAPErrorIDType ENUM_ErrorID_Unsupported = -1000100;
const TAPMessageType ENUM_ErrorMsg_Unsupported = "Errors:Unsupported.";

/// 非法的RunID
const TAPErrorIDType ENUM_ErrorID_InvalidRunID = -1000200;
const TAPMessageType ENUM_ErrorMsg_InvalidRunID = "UserID:%s,Errors:RunID should belong to [0,99].";

/// 非法的行情回调函数
const TAPErrorIDType ENUM_ErrorID_InvalidMarketDataCallback = -1000300;
const TAPMessageType ENUM_ErrorMsg_InvalidMarketDataCallback = "UserID:%s,Errors:MarketData callback should not be null.";

/// 非法的报单回调函数
const TAPErrorIDType ENUM_ErrorID_InvalidOrderCallback = -1000400;
const TAPMessageType ENUM_ErrorMsg_InvalidOrderCallback = "UserID:%s,Errors:Order callback should not be null.";

/// 非法的事件回调函数
const TAPErrorIDType ENUM_ErrorID_InvalidEventCallback = -1000500;
const TAPMessageType ENUM_ErrorMsg_InvalidEventCallback = "UserID:%s,Errors:Event callback should not be null.";

/// 非法的登录信息
const TAPErrorIDType ENUM_ErrorID_InvalidLoginField = -1000600;
const TAPMessageType ENUM_ErrorMsg_InvalidLoginField = "UserID:%s,Errors:Invalid LoginField.";

/// 未授权
const TAPErrorIDType ENUM_ErrorID_Unauthorized = -1000700;
const TAPMessageType ENUM_ErrorMsg_Unauthorized = "UserID:%s,Errors:Unauthorized.";

/// 非法的UserID
const TAPErrorIDType ENUM_ErrorID_InvalidUserID = -1000800;
const TAPMessageType ENUM_ErrorMsg_InvalidUserID = "UserID:%s,Errors:Invalid UserID.";

/// 非法的用户类型
const TAPErrorIDType ENUM_ErrorID_InvalidPassword = -1000900;
const TAPMessageType ENUM_ErrorMsg_InvalidPassword = "UserID:%s,Errors:Invalid UserType.";

/// 非法的用户类型
const TAPErrorIDType ENUM_ErrorID_InvalidUserType = -1001000;
const TAPMessageType ENUM_ErrorMsg_InvalidUserType = "UserID:%s,Errors:Invalid UserType.";

/// 非法的交易前置地址
const TAPErrorIDType ENUM_ErrorID_InvalidTraderFront = -1001100;
const TAPMessageType ENUM_ErrorMsg_InvalidTraderFront = "UserID:%s,Errors:Invalid TraderFront.";

/// 非法的行情前置地址
const TAPErrorIDType ENUM_ErrorID_InvalidMdFront = -1001200;
const TAPMessageType ENUM_ErrorMsg_InvalidMdFront = "UserID:%s,Errors:Invalid MdFront.";

/// 非法的文件路径
const TAPErrorIDType ENUM_ErrorID_InvalidFilePath = -1001300;
const TAPMessageType ENUM_ErrorMsg_InvalidFilePath = "UserID:%s,Errors:Invalid FilePath.";

/// 非法的BrokerID
const TAPErrorIDType ENUM_ErrorID_InvalidBrokerID = -1001400;
const TAPMessageType ENUM_ErrorMsg_InvalidBrokerID = "UserID:%s,Errors:Invalid BrokerID.";

/// 非法的AppID
const TAPErrorIDType ENUM_ErrorID_InvalidAppID = -1001500;
const TAPMessageType ENUM_ErrorMsg_InvalidAppID = "UserID:%s,Errors:Invalid AppID.";

/// 非法的AuthCode
const TAPErrorIDType ENUM_ErrorID_InvalidAuthCode = -1001600;
const TAPMessageType ENUM_ErrorMsg_InvalidAuthCode = "UserID:%s,Errors:Invalid AuthCode.";

/// 创建TraderApi连接失败
const TAPErrorIDType ENUM_ErrorID_FailToCreateTrader = -1001700;
const TAPMessageType ENUM_ErrorMsg_FailToCreateTrader = "Errors:Fail To Create Trader.";

/// 连接超时
const TAPErrorIDType ENUM_ErrorID_TraderConnectTimeout = -1001800;
const TAPMessageType ENUM_ErrorMsg_TraderConnectTimeout = "UserID:%s,Errors:Trader Connect Timeout.";

/// TraderApi连接断开
const TAPErrorIDType ENUM_ErrorID_TraderDisconnected = -1001900;
const TAPMessageType ENUM_ErrorMsg_TraderDisconnected = "Errors:Trader Disconnected.";

/// 创建MdApi连接失败
const TAPErrorIDType ENUM_ErrorID_FailToCreateMd = -1002000;
const TAPMessageType ENUM_ErrorMsg_FailToCreateMd = "Errors:Fail To CreateMd.";

/// 连接超时
const TAPErrorIDType ENUM_ErrorID_MdConnectTimeout = -1002100;
const TAPMessageType ENUM_ErrorMsg_MdConnectTimeout = "UserID:%s,Errors:Md Connect Timeout.";

/// MdApi连接断开
const TAPErrorIDType ENUM_ErrorID_MdDisconnected = -1002200;
const TAPMessageType ENUM_ErrorMsg_MdDisconnected = "Errors:Md Disconnected.";

/// 初始化失败
const TAPErrorIDType ENUM_ErrorID_FailToInitalize = -1002300;
const TAPMessageType ENUM_ErrorMsg_FailToInitalize = "%s UserID:%s,Errors:Fail To Initalize.";

/// 交易所拒绝
const TAPErrorIDType ENUM_ErrorID_InvalidTraderInstance = -1002400;
const TAPMessageType ENUM_ErrorMsg_InvalidTraderInstance = "Errors:Invalid Trader Instance.";

/// 交易所拒绝
const TAPErrorIDType ENUM_ErrorID_InvalidMdInstance = -1002500;
const TAPMessageType ENUM_ErrorMsg_InvalidMdInstance = "Errors:Invalid Md Instance.";

/// 发送失败
const TAPErrorIDType ENUM_ErrorID_FailToSended = -1002600;
const TAPMessageType ENUM_ErrorMsg_FailToSended = "Errors:Fail To Sended.";

/// 响应超时
const TAPErrorIDType ENUM_ErrorID_ResponseTimeout = -1002700;
const TAPMessageType ENUM_ErrorMsg_ResponseTimeout = "Errors:Response Timeout.";

/// 非法价格
const TAPErrorIDType ENUM_ErrorID_InvalidPrice = -1002800;
const TAPMessageType ENUM_ErrorMsg_InvalidPrice = "Errors:Invalid Price.";

/// 非法价格
const TAPErrorIDType ENUM_ErrorID_InvalidVolume = -1002900;
const TAPMessageType ENUM_ErrorMsg_InvalidVolume = "Errors:Invalid Volume.";

/// 柜台拒绝
const TAPErrorIDType ENUM_ErrorID_BrokerReject = -1003000;
const TAPMessageType ENUM_ErrorMsg_BrokerReject = "Errors:Broker Reject.";

/// 交易所拒绝
const TAPErrorIDType ENUM_ErrorID_ExchangeReject = -1003100;
const TAPMessageType ENUM_ErrorMsg_ExchangeReject = "Errors:Exchange Reject.";


#endif