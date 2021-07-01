#ifndef AP_ERRORS_H__
#define AP_ERRORS_H__

/////////////////////////////////////////////////////////////////////////
/// TAPErrorIDType��һ�������������
/////////////////////////////////////////////////////////////////////////
typedef int TAPErrorIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPMessageType��һ����Ϣ����
/////////////////////////////////////////////////////////////////////////
typedef char TAPMessageType[256];

/// �޴���
#define ENUM_ErrorID_None 0
#define ENUM_ErrorMsg_None ""

/// �ݲ�֧��
#define ENUM_ErrorID_Unsupported -1000100
#define ENUM_ErrorMsg_Unsupported "Error:Unsupported."

/// �Ƿ���RunID
#define ENUM_ErrorID_InvalidRunID -1000200
#define ENUM_ErrorMsg_InvalidRunID "Error:RunID should belong to [0,99]."

/// �Ƿ��ĵ�¼��Ϣ
#define ENUM_ErrorID_InvalidLoginField -1000300
#define ENUM_ErrorMsg_InvalidLoginField "Error:Invalid LoginField."

/// δ��Ȩ
#define ENUM_ErrorID_Unauthorized -1000400
#define ENUM_ErrorMsg_Unauthorized "Error:Unauthorized."

/// �Ƿ��Ŀͻ���
#define ENUM_ErrorID_InvalidUserID -1000500
#define ENUM_ErrorMsg_InvalidUserID "Error:Invalid UserID."

/// �Ƿ�������
#define ENUM_ErrorID_InvalidPassword -1000600
#define ENUM_ErrorMsg_InvalidPassword "Error:Invalid Password."

/// �Ƿ����û�����
#define ENUM_ErrorID_InvalidUserType -1000700
#define ENUM_ErrorMsg_InvalidUserType "Error:Invalid UserType."

/// �Ƿ��Ľ���ǰ�õ�ַ
#define ENUM_ErrorID_InvalidTraderFront -1000800
#define ENUM_ErrorMsg_InvalidTraderFront "Error:Invalid TraderFront."

/// �Ƿ�������ǰ�õ�ַ
#define ENUM_ErrorID_InvalidMdFront -1000900
#define ENUM_ErrorMsg_InvalidMdFront "Error:Invalid MdFront."

/// �Ƿ����ļ�·��
#define ENUM_ErrorID_InvalidFilePath -1001000
#define ENUM_ErrorMsg_InvalidFilePath "Error:Invalid FilePath."

/// �Ƿ���BrokerID
#define ENUM_ErrorID_InvalidBrokerID -1001100
#define ENUM_ErrorMsg_InvalidBrokerID "Error:Invalid BrokerID."

/// �Ƿ���AppID
#define ENUM_ErrorID_InvalidAppID -1001200
#define ENUM_ErrorMsg_InvalidAppID "Error:Invalid AppID."

/// �Ƿ���AuthCode
#define ENUM_ErrorID_InvalidAuthCode -1001300
#define ENUM_ErrorMsg_InvalidAuthCode "Error:Invalid AuthCode."

/// ����TraderApiʵ��ʧ��
#define ENUM_ErrorID_FailToCreateTrader -1001400
#define ENUM_ErrorMsg_FailToCreateTrader "Error:Fail To Create Trader."

/// �뽻��ǰ�����ӳ�ʱ
#define ENUM_ErrorID_TraderConnectTimeout -1001500
#define ENUM_ErrorMsg_TraderConnectTimeout "Error:Trader Connect Timeout."

/// �뽻��ǰ�����ӶϿ�
#define ENUM_ErrorID_TraderDisconnected -1001600
#define ENUM_ErrorMsg_TraderDisconnected "Error:Trader Disconnected."

/// ����MdApiʵ��ʧ��
#define ENUM_ErrorID_FailToCreateMd -1001700
#define ENUM_ErrorMsg_FailToCreateMd "Error:Fail To Create Md."

/// ������ǰ�����ӳ�ʱ
#define ENUM_ErrorID_MdConnectTimeout -1001800
#define ENUM_ErrorMsg_MdConnectTimeout "Error:Md Connect Timeout."

/// ������ǰ�����ӶϿ�
#define ENUM_ErrorID_MdDisconnected -1001900
#define ENUM_ErrorMsg_MdDisconnected "Error:Md Disconnected."

/// �Ƿ���TraderApiʵ��
#define ENUM_ErrorID_InvalidTraderInstance -1002000
#define ENUM_ErrorMsg_InvalidTraderInstance "Error:Invalid Trader Instance."

/// �Ƿ���MdApiʵ��
#define ENUM_ErrorID_InvalidMdInstance -1002100
#define ENUM_ErrorMsg_InvalidMdInstance "Error:Invalid Md Instance."

/// ����ʧ��
#define ENUM_ErrorID_FailToSended -1002200
#define ENUM_ErrorMsg_FailToSended "Error:Fail To Sended."

/// ��Ӧ��ʱ
#define ENUM_ErrorID_ResponseTimeout -1002300
#define ENUM_ErrorMsg_ResponseTimeout "Error:Response Timeout."

/// �Ƿ��۸�
#define ENUM_ErrorID_InvalidPrice -1002400
#define ENUM_ErrorMsg_InvalidPrice "Error:Invalid Price."

/// �Ƿ��۸�
#define ENUM_ErrorID_InvalidVolume -1002500
#define ENUM_ErrorMsg_InvalidVolume "Error:Invalid Volume."

/// ��̨�ܾ�
#define ENUM_ErrorID_BrokerReject -1002600
#define ENUM_ErrorMsg_BrokerReject "Error:Broker Reject."

/// �������ܾ�
#define ENUM_ErrorID_ExchangeReject -1002700
#define ENUM_ErrorMsg_ExchangeReject "Error:Exchange Reject."

/// �Ƿ��Ķ����¼�ID
#define ENUM_ErrorID_InvalidOrderEventID -10002800
#define ENUM_ErrorMsg_InvalidOrderEventID "Error:Invalid OrderEventID."

/// �Ƿ�����������
#define ENUM_ErrorID_InvalidMarketDataType -1002900
#define ENUM_ErrorMsg_InvalidMarketDataType "Error:Invalid MarketDataType."

/// �Ƿ��������¼�ID
#define ENUM_ErrorID_InvalidSnapDataEventID -10003000
#define ENUM_ErrorMsg_InvalidSnapDataEventID "Error:Invalid SnapDataEventID."

/// �Ƿ�����������¼�ID
#define ENUM_ErrorID_InvalidDetailDataEventID -10003100
#define ENUM_ErrorMsg_InvalidDetailDataEventID "Error:Invalid DetailDataEventID."

/// �Ƿ���TaskID
#define ENUM_ErrorID_InvalidTaskID -1003200
#define ENUM_ErrorMsg_InvalidTaskID "Error:Invalid TaskID."

/// �Ƿ��������ʶ
#define ENUM_ErrorID_InvalidPasswordFlag -1003300
#define ENUM_ErrorMsg_InvalidPasswordFlag "Error:Failed To RepealTransferAsset."

#endif
