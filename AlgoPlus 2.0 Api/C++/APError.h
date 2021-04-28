#ifndef AP_ERRORS_H__
#define AP_ERRORS_H__


#include "APDataType.h"


/// �޴���
const TAPErrorIDType ENUM_ErrorID_None = 0;
const TAPMessageType ENUM_ErrorMsg_None = "";

/// �ݲ�֧��
const TAPErrorIDType ENUM_ErrorID_Unsupported = -1000100;
const TAPMessageType ENUM_ErrorMsg_Unsupported = "Errors:Unsupported.";

/// �Ƿ���RunID
const TAPErrorIDType ENUM_ErrorID_InvalidRunID = -1000200;
const TAPMessageType ENUM_ErrorMsg_InvalidRunID = "UserID:%s,Errors:RunID should belong to [0,99].";

/// �Ƿ�������ص�����
const TAPErrorIDType ENUM_ErrorID_InvalidMarketDataCallback = -1000300;
const TAPMessageType ENUM_ErrorMsg_InvalidMarketDataCallback = "UserID:%s,Errors:MarketData callback should not be null.";

/// �Ƿ��ı����ص�����
const TAPErrorIDType ENUM_ErrorID_InvalidOrderCallback = -1000400;
const TAPMessageType ENUM_ErrorMsg_InvalidOrderCallback = "UserID:%s,Errors:Order callback should not be null.";

/// �Ƿ����¼��ص�����
const TAPErrorIDType ENUM_ErrorID_InvalidEventCallback = -1000500;
const TAPMessageType ENUM_ErrorMsg_InvalidEventCallback = "UserID:%s,Errors:Event callback should not be null.";

/// �Ƿ��ĵ�¼��Ϣ
const TAPErrorIDType ENUM_ErrorID_InvalidLoginField = -1000600;
const TAPMessageType ENUM_ErrorMsg_InvalidLoginField = "UserID:%s,Errors:Invalid LoginField.";

/// δ��Ȩ
const TAPErrorIDType ENUM_ErrorID_Unauthorized = -1000700;
const TAPMessageType ENUM_ErrorMsg_Unauthorized = "UserID:%s,Errors:Unauthorized.";

/// �Ƿ���UserID
const TAPErrorIDType ENUM_ErrorID_InvalidUserID = -1000800;
const TAPMessageType ENUM_ErrorMsg_InvalidUserID = "UserID:%s,Errors:Invalid UserID.";

/// �Ƿ����û�����
const TAPErrorIDType ENUM_ErrorID_InvalidPassword = -1000900;
const TAPMessageType ENUM_ErrorMsg_InvalidPassword = "UserID:%s,Errors:Invalid UserType.";

/// �Ƿ����û�����
const TAPErrorIDType ENUM_ErrorID_InvalidUserType = -1001000;
const TAPMessageType ENUM_ErrorMsg_InvalidUserType = "UserID:%s,Errors:Invalid UserType.";

/// �Ƿ��Ľ���ǰ�õ�ַ
const TAPErrorIDType ENUM_ErrorID_InvalidTraderFront = -1001100;
const TAPMessageType ENUM_ErrorMsg_InvalidTraderFront = "UserID:%s,Errors:Invalid TraderFront.";

/// �Ƿ�������ǰ�õ�ַ
const TAPErrorIDType ENUM_ErrorID_InvalidMdFront = -1001200;
const TAPMessageType ENUM_ErrorMsg_InvalidMdFront = "UserID:%s,Errors:Invalid MdFront.";

/// �Ƿ����ļ�·��
const TAPErrorIDType ENUM_ErrorID_InvalidFilePath = -1001300;
const TAPMessageType ENUM_ErrorMsg_InvalidFilePath = "UserID:%s,Errors:Invalid FilePath.";

/// �Ƿ���BrokerID
const TAPErrorIDType ENUM_ErrorID_InvalidBrokerID = -1001400;
const TAPMessageType ENUM_ErrorMsg_InvalidBrokerID = "UserID:%s,Errors:Invalid BrokerID.";

/// �Ƿ���AppID
const TAPErrorIDType ENUM_ErrorID_InvalidAppID = -1001500;
const TAPMessageType ENUM_ErrorMsg_InvalidAppID = "UserID:%s,Errors:Invalid AppID.";

/// �Ƿ���AuthCode
const TAPErrorIDType ENUM_ErrorID_InvalidAuthCode = -1001600;
const TAPMessageType ENUM_ErrorMsg_InvalidAuthCode = "UserID:%s,Errors:Invalid AuthCode.";

/// ����TraderApi����ʧ��
const TAPErrorIDType ENUM_ErrorID_FailToCreateTrader = -1001700;
const TAPMessageType ENUM_ErrorMsg_FailToCreateTrader = "Errors:Fail To Create Trader.";

/// ���ӳ�ʱ
const TAPErrorIDType ENUM_ErrorID_TraderConnectTimeout = -1001800;
const TAPMessageType ENUM_ErrorMsg_TraderConnectTimeout = "UserID:%s,Errors:Trader Connect Timeout.";

/// TraderApi���ӶϿ�
const TAPErrorIDType ENUM_ErrorID_TraderDisconnected = -1001900;
const TAPMessageType ENUM_ErrorMsg_TraderDisconnected = "Errors:Trader Disconnected.";

/// ����MdApi����ʧ��
const TAPErrorIDType ENUM_ErrorID_FailToCreateMd = -1002000;
const TAPMessageType ENUM_ErrorMsg_FailToCreateMd = "Errors:Fail To CreateMd.";

/// ���ӳ�ʱ
const TAPErrorIDType ENUM_ErrorID_MdConnectTimeout = -1002100;
const TAPMessageType ENUM_ErrorMsg_MdConnectTimeout = "UserID:%s,Errors:Md Connect Timeout.";

/// MdApi���ӶϿ�
const TAPErrorIDType ENUM_ErrorID_MdDisconnected = -1002200;
const TAPMessageType ENUM_ErrorMsg_MdDisconnected = "Errors:Md Disconnected.";

/// ��ʼ��ʧ��
const TAPErrorIDType ENUM_ErrorID_FailToInitalize = -1002300;
const TAPMessageType ENUM_ErrorMsg_FailToInitalize = "%s UserID:%s,Errors:Fail To Initalize.";

/// �������ܾ�
const TAPErrorIDType ENUM_ErrorID_InvalidTraderInstance = -1002400;
const TAPMessageType ENUM_ErrorMsg_InvalidTraderInstance = "Errors:Invalid Trader Instance.";

/// �������ܾ�
const TAPErrorIDType ENUM_ErrorID_InvalidMdInstance = -1002500;
const TAPMessageType ENUM_ErrorMsg_InvalidMdInstance = "Errors:Invalid Md Instance.";

/// ����ʧ��
const TAPErrorIDType ENUM_ErrorID_FailToSended = -1002600;
const TAPMessageType ENUM_ErrorMsg_FailToSended = "Errors:Fail To Sended.";

/// ��Ӧ��ʱ
const TAPErrorIDType ENUM_ErrorID_ResponseTimeout = -1002700;
const TAPMessageType ENUM_ErrorMsg_ResponseTimeout = "Errors:Response Timeout.";

/// �Ƿ��۸�
const TAPErrorIDType ENUM_ErrorID_InvalidPrice = -1002800;
const TAPMessageType ENUM_ErrorMsg_InvalidPrice = "Errors:Invalid Price.";

/// �Ƿ��۸�
const TAPErrorIDType ENUM_ErrorID_InvalidVolume = -1002900;
const TAPMessageType ENUM_ErrorMsg_InvalidVolume = "Errors:Invalid Volume.";

/// ��̨�ܾ�
const TAPErrorIDType ENUM_ErrorID_BrokerReject = -1003000;
const TAPMessageType ENUM_ErrorMsg_BrokerReject = "Errors:Broker Reject.";

/// �������ܾ�
const TAPErrorIDType ENUM_ErrorID_ExchangeReject = -1003100;
const TAPMessageType ENUM_ErrorMsg_ExchangeReject = "Errors:Exchange Reject.";


#endif