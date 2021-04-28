#ifndef AP_DATETYPE_H__
#define AP_DATETYPE_H__


/////////////////////////////////////////////////////////////////////////
/// ����
/////////////////////////////////////////////////////////////////////////
/// ��
const int ZERO_INT = 0;
/// int��Чֵ
const int MAX_INT = 999999999;
/// double��Чֵ
const double MAX_DOUBLE = 999999999999.99;
/// ���ַ���
const char NULL_CSTRING[2] = "";

/////////////////////////////////////////////////////////////////////////
/// TAPTimeAnchorType��һ��ʱ��������
/////////////////////////////////////////////////////////////////////////
#ifdef _WIN32
typedef __int64 TAPTimeAnchorType;
#else
typedef long long int TAPTimeAnchorType;
#endif
/// ����΢��Ļ��㵥λ
const TAPTimeAnchorType MICROSECONDS_IN_SECOND = 1000000;

/////////////////////////////////////////////////////////////////////////
/// TAPApiStatusType��һ���ӿ�״̬����
/////////////////////////////////////////////////////////////////////////
typedef char TAPApiStatusType;
/// �˳�
const TAPApiStatusType ENUM_ApiStatus_Exit = '0';
/// δ��ʼ��
const TAPApiStatusType ENUM_ApiStatus_Null = '1';
/// �Ͽ�����
const TAPApiStatusType ENUM_ApiStatus_Disconnected = '2';
/// ���ڳ�ʼ��
const TAPApiStatusType ENUM_ApiStatus_Initializing = '3';
/// ��������
const TAPApiStatusType ENUM_ApiStatus_Working = '4';

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPOrderStatusType��һ������״̬����
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPOrderStatusType;
/// δ����
const TAPOrderStatusType ENUM_OrderStatus_Null = '0';
/// ���ط�������ָ��
const TAPOrderStatusType ENUM_OrderStatus_Ordering = '1';
/// ���ط�������ָ��
const TAPOrderStatusType ENUM_OrderStatus_Canceling = '2';
/// �ɳ�����δ�ɽ������ֳɽ���
const TAPOrderStatusType ENUM_OrderStatus_Revocable = '3';
/// ���ɳ��������ɲ�����ȫ��������
const TAPOrderStatusType ENUM_OrderStatus_Irrevocable = '4';
/// ���󣨹�̨�ܾ����������ܾ���
const TAPOrderStatusType ENUM_OrderStatus_Error = '5';

/////////////////////////////////////////////////////////////////////////
/// TAPOrderEventIDType��һ�������¼�ID����
/////////////////////////////////////////////////////////////////////////
typedef int TAPOrderEventIDType;
/// ���ֳɽ���ֻ���³ɽ�������
const TAPOrderEventIDType ENUM_OrderEventID_PartTraded = 10001;
/// ���³ɽ������ݣ��Ҹ��³ɱ�����
const TAPOrderEventIDType ENUM_OrderEventID_TradedAndUpdateCost = 10002;
/// ȫ���ɽ���ֻ���³ɽ�������
const TAPOrderEventIDType ENUM_OrderEventID_AllTraded = 10003;
/// ʣ�೷�����Ҹ��³ɽ�������
const TAPOrderEventIDType ENUM_OrderEventID_TradedAndCanceled = 10004;
/// ʣ�೷��
const TAPOrderEventIDType ENUM_OrderEventID_Canceled = 10005;
/// ����ʧ��
const TAPOrderEventIDType ENUM_OrderEventID_Error = 10006;
/// ���³ɱ�����
const TAPOrderEventIDType ENUM_OrderEventID_UpdateCost = 10007;
/// �Ŷ�
const TAPOrderEventIDType ENUM_OrderEventID_Waiting = 10008;
/// Ԥ��
const TAPOrderEventIDType ENUM_OrderEventID_Cached = 10009;
/// ����ʧ��
const TAPOrderEventIDType ENUM_OrderEventID_FailToCancel = 10010;
/// ����ʧ��
const TAPOrderEventIDType ENUM_OrderEventID_IPO = 10011;

/////////////////////////////////////////////////////////////////////////
/// TAPEventIDType��һ���¼�ID����
/////////////////////////////////////////////////////////////////////////
typedef int TAPEventIDType;
/// ����TraderApi����ʧ��
const TAPEventIDType ENUM_EventID_FailToCreateTrader = 10001;
/// ��ʼ��ʧ��
const TAPEventIDType ENUM_EventID_FailToInitialize = 10002;
/// TraderApi���ӶϿ�
const TAPEventIDType ENUM_EventID_TraderDisconnected = 10003;
/// ����MdApi����ʧ��
const TAPEventIDType ENUM_EventID_FailToCreateMd = 10004;
/// MdApi���ӶϿ�
const TAPEventIDType ENUM_EventID_MdDisconnected = 10005;
/// ��������ʧ��
const TAPEventIDType ENUM_EventID_FailToSubscribeMarketData = 10006;
/// �˶�����ʧ��
const TAPEventIDType ENUM_EventID_FailToUnsubscribeMarketData = 10007;
/// �л�������
const TAPEventIDType ENUM_EventID_DayRolling = 10008;
/// ��ʼ�����
const TAPEventIDType ENUM_EventID_Ready = 10009;
/// ��ѯ����
const TAPEventIDType ENUM_EventID_QryOrder = 10010;
/// ��ѯ�ɽ�
const TAPEventIDType ENUM_EventID_QryTrade = 10011;
/// ��ѯ�ֲ�
const TAPEventIDType ENUM_EventID_QryPosition = 10012;
/// ��ѯ�ʽ�
const TAPEventIDType ENUM_EventID_QryBalance = 10013;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPOrderTypeType��һ��������������
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPOrderTypeType;
/// <summary>
/// ͨ��
/// </summary>
/// �޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_LimitAndWait = '0';
/// ���ŶԷ��޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_BestLimitAndWait = '1';
/// ���ű����޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_HomeBestLimitAndWait = '2';
/// ���޼۸��޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_FrontierLimitAndWait = '3';
/// ���³ɽ��޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_LastLimitAndWait = '4';
/// �����嵵�޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_FiveBestLimitAndWait = '5';
/// <summary>
/// ��Ʊ����
/// </summary>
/// �޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_SSE_LimitAndWait = 'a';
/// �����嵵���ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_SSE_FiveAndWait = 'b';
/// �����嵵��ʣ����������
const TAPOrderTypeType ENUM_OrderType_SSE_FiveAndKill = 'c';
/// ���ŶԷ����ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_SSEKC_BestAndWait = 'd';
/// ���ű������ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_SSEKC_HomeBestAndWait = 'e';
const TAPOrderTypeType ENUM_OrderType_SSEKC_Fix = 'f';
const TAPOrderTypeType ENUM_OrderType_SSEOPTION_LimitOrKill = 'g';
const TAPOrderTypeType ENUM_OrderType_SSEOPTION_AnyAndWait = 'h';
const TAPOrderTypeType ENUM_OrderType_SSEOPTION_AnyAndKill = 'i';
const TAPOrderTypeType ENUM_OrderType_SSEOPTION_AnyOrKill = 'j';
/// �޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_SZSE_LimitAndWait = 'k';
/// ���ŶԷ����ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_SZSE_BestAndWait = 'l';
/// ���ű������ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_SZSE_HomeBestAndWait = 'm';
/// �мۣ�ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_SZSE_AnyAndKill = 'n';
/// �мۣ�ȫ���ɽ�����ȫ������
const TAPOrderTypeType ENUM_OrderType_SZSE_AnyOrKill = 'o';
/// �����嵵��ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_SZSE_FiveAndKill = 'p';
const TAPOrderTypeType ENUM_OrderType_SZSESGT_AuctionLimit = 'q';
const TAPOrderTypeType ENUM_OrderType_SZSEOPTION_LimitOrKill = 'r';
/// <summary>
/// �ڻ�����
/// </summary>
/// �޼ۣ�������
const TAPOrderTypeType ENUM_OrderType_CZCE_LimitAndWait = 'A';
/// �޼ۣ�ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_CZCE_LimitAndKill = 'B';
/// �мۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_CZCE_AnyAndWait = 'C';
/// �мۣ�ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_CZCE_AnyAndKill = 'D';
/// �޼ۣ�ȫ���ɽ�����ȫ������
const TAPOrderTypeType ENUM_OrderType_CZCEOPTION_LimitOrKill = 'E';
/// �мۣ�ȫ���ɽ�����ȫ������
const TAPOrderTypeType ENUM_OrderType_CZCEOPTION_AnyOrKill = 'F';
/// �޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_DCE_LimitAndWait = 'G';
/// �޼ۣ�ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_DCE_LimitAndKill = 'H';
/// �޼ۣ�ȫ���ɽ�����ȫ������
const TAPOrderTypeType ENUM_OrderType_DCE_LimitOrKill = 'I';
/// �мۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_DCE_AnyAndWait = 'J';
/// �мۣ�ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_DCE_AnyAndKill = 'K';
/// �мۣ�ȫ���ɽ�����ȫ������
const TAPOrderTypeType ENUM_OrderType_DCE_AnyOrKill = 'L';
const TAPOrderTypeType ENUM_OrderType_DCE_AnyTouchAndWait = 'M';
const TAPOrderTypeType ENUM_OrderType_DCE_AnyTouchProfitAndWait = 'N';
/// �޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_SHFE_LimitAndWait = 'O';
/// �޼ۣ�ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_SHFE_LimitAndKill = 'P';
const TAPOrderTypeType ENUM_OrderType_SHFE_LimitAndKillAndLimit = 'Q';
/// �޼ۣ�ȫ���ɽ�����ȫ������
const TAPOrderTypeType ENUM_OrderType_SHFE_LimitOrKill = 'R';
/// �޼ۣ��ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_CFFEX_LimitAndWait = 'S';
/// �޼ۣ�ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_CFFEX_LimitAndKill = 'T';
const TAPOrderTypeType ENUM_OrderType_CFFEX_LimitAndKillAndLimit = 'U';
/// �޼ۣ�ȫ���ɽ�����ȫ������
const TAPOrderTypeType ENUM_OrderType_CFFEX_LimitOrKill = 'V';
/// �����嵵��ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_CFFEX_FiveAndKill = 'W';
/// �����嵵���ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_CFFEX_FiveAndWait = 'X';
/// ���ŶԷ���ʣ�೷��
const TAPOrderTypeType ENUM_OrderType_CFFEX_BestAndKill = 'Y';
/// ���ŶԷ����ȴ��ɽ�
const TAPOrderTypeType ENUM_OrderType_CFFEX_BestAndWait = 'Z';

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPCloseTypeType��һ��ƽ����������
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPCloseTypeType;
/// ��ֹƽ��
const TAPCloseTypeType ENUM_CloseType_HistoryOnly = '0';
/// �ȿ���ƽ
const TAPCloseTypeType ENUM_CloseType_FIFO = '1';
/// ƽ�����ƽ��
const TAPCloseTypeType ENUM_CloseType_Either = '2';

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPPositionDirectionType��һ���ֲֶ������
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPPositionDirectionType;
/// ��ͷ
const TAPPositionDirectionType ENUM_PositionDirection_Long = '0';
/// ��ͷ
const TAPPositionDirectionType ENUM_PositionDirection_Short = '1';

/////////////////////////////////////////////////////////////////////////
/// TAPOrderDirectionType��һ��Direction����
/////////////////////////////////////////////////////////////////////////
typedef char TAPOrderDirectionType[3];
/// ����
const TAPOrderDirectionType ENUM_OrderDirection_Buy = "00";
/// ����
const TAPOrderDirectionType ENUM_OrderDirection_Sell = "11";
/// ETF�깺
const TAPOrderDirectionType ENUM_OrderDirection_ETFPur = "2";
/// ETF���
const TAPOrderDirectionType ENUM_OrderDirection_ETFRed = "3";
/// �¹��깺
const TAPOrderDirectionType ENUM_OrderDirection_IPO = "4";
/// ���ع�
const TAPOrderDirectionType ENUM_OrderDirection_Repurchase = "5";
/// ��ع�
const TAPOrderDirectionType ENUM_OrderDirection_ReverseRepur = "60";
/// ����ʽ�����깺
const TAPOrderDirectionType ENUM_OrderDirection_OeFundPur = "8";
/// ����ʽ�������
const TAPOrderDirectionType ENUM_OrderDirection_OeFundRed = "9";
/// ����Ʒ����
const TAPOrderDirectionType ENUM_OrderDirection_CollateralIn = "a";
/// ����Ʒ����
const TAPOrderDirectionType ENUM_OrderDirection_CollateralOut = "b";
/// ��Ѻ���
const TAPOrderDirectionType ENUM_OrderDirection_PledgeIn = "d";
/// ��Ѻ����
const TAPOrderDirectionType ENUM_OrderDirection_PledgeOut = "e";
/// �����ծ
const TAPOrderDirectionType ENUM_OrderDirection_Rationed = "f";
/// ������
const TAPOrderDirectionType ENUM_OrderDirection_Split = "g";
/// ����ϲ�
const TAPOrderDirectionType ENUM_OrderDirection_Merge = "h";
/// ��������
const TAPOrderDirectionType ENUM_OrderDirection_CreditBuy = "i0";
/// ��ȯ����
const TAPOrderDirectionType ENUM_OrderDirection_CreditSell = "j0";
/// ��ȯ����
const TAPOrderDirectionType ENUM_OrderDirection_SellRepay = "k1";
/// ��ȯ��ȯ
const TAPOrderDirectionType ENUM_OrderDirection_BuyRepay = "l1";
/// ��ȯ��ת
const TAPOrderDirectionType ENUM_OrderDirection_RepayTransfer = "m";
/// ��ȯ��ת
const TAPOrderDirectionType ENUM_OrderDirection_SurplusTransfer = "n";
/// Դȯ��ת
const TAPOrderDirectionType ENUM_OrderDirection_SourceTransfer = "o";
/// ծȯת��
const TAPOrderDirectionType ENUM_OrderDirection_BondConvertStock = "t";
/// ծȯ����
const TAPOrderDirectionType ENUM_OrderDirection_BondPutback = "u";
/// ETFʵ���깺
const TAPOrderDirectionType ENUM_OrderDirection_ETFOtPur = "v";
/// ETFʵ�����
const TAPOrderDirectionType ENUM_OrderDirection_ETFOtRed = "w";
/// ���۳���
const TAPOrderDirectionType ENUM_OrderDirection_PutbackRelieve = "x";
/// ��������
const TAPOrderDirectionType ENUM_OrderDirection_IOIBuy = "A";
/// ��������
const TAPOrderDirectionType ENUM_OrderDirection_IOISell = "B";
/// �ɽ�ȷ������
const TAPOrderDirectionType ENUM_OrderDirection_TCRBuy = "C";
/// �ɽ�ȷ������
const TAPOrderDirectionType ENUM_OrderDirection_TCRSell = "D";
/// �򿪲�
const TAPOrderDirectionType ENUM_OrderDirection_BuyOpen = "00";
/// ��ƽ
const TAPOrderDirectionType ENUM_OrderDirection_SellClose = "11";
/// ��ƽ��
const TAPOrderDirectionType ENUM_OrderDirection_SellCloseToday = "13";
/// ��ƽ��
const TAPOrderDirectionType ENUM_OrderDirection_SellCloseHistory = "14";
/// ������
const TAPOrderDirectionType ENUM_OrderDirection_SellOpen = "10";
/// ��ƽ��
const TAPOrderDirectionType ENUM_OrderDirection_BuyClose = "01";
/// ��ƽ��
const TAPOrderDirectionType ENUM_OrderDirection_BuyCloseToday = "03";
/// ��ƽ��
const TAPOrderDirectionType ENUM_OrderDirection_BuyCloseHistory = "04";
/// ���ҿ���
const TAPOrderDirectionType ENUM_OrderDirection_CoveredOpen = "E";
/// ����ƽ��
const TAPOrderDirectionType ENUM_OrderDirection_CoveredClose = "F";
/// ��Ȩ
const TAPOrderDirectionType ENUM_OrderDirection_ExecOrder = "G";

/////////////////////////////////////////////////////////////////////////
/// TAPPriceTypeType��һ�������۸���������
/////////////////////////////////////////////////////////////////////////
typedef char TAPPriceTypeType;

/////////////////////////////////////////////////////////////////////////
/// TAPTimeConditionType��һ����Ч����������
/////////////////////////////////////////////////////////////////////////
typedef char TAPTimeConditionType;

/////////////////////////////////////////////////////////////////////////
/// TAPVolumeConditionType��һ���ɽ�����������
/////////////////////////////////////////////////////////////////////////
typedef char TAPVolumeConditionType;

/////////////////////////////////////////////////////////////////////////
/// TAPContingentConditionType��һ��������������
/////////////////////////////////////////////////////////////////////////
typedef char TAPContingentConditionType;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPExchangeIDType��һ������������
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPExchangeIDType[9];
/// δ֪
const TAPExchangeIDType ENUM_ExchangeID_Unknown = "U";
/// �Ϻ�������
const TAPExchangeIDType ENUM_ExchangeID_SSE = "1";
/// ���ڽ�����
const TAPExchangeIDType ENUM_ExchangeID_SZSE = "2";
/// ��۽�����
const TAPExchangeIDType ENUM_ExchangeID_HK = "3";
/// �й������ڻ�������
const TAPExchangeIDType ENUM_ExchangeID_CFFEX = "CFFEX";
/// �Ϻ��ڻ�������
const TAPExchangeIDType ENUM_ExchangeID_SHFE = "SHFE";
/// �Ϻ�������Դ�������Ĺɷ����޹�˾
const TAPExchangeIDType ENUM_ExchangeID_INE = "INE";
/// ������Ʒ������
const TAPExchangeIDType ENUM_ExchangeID_DCE = "DCE";
/// ֣����Ʒ������
const TAPExchangeIDType ENUM_ExchangeID_CZCE = "CZCE";

/////////////////////////////////////////////////////////////////////////
/// TAPStandardStatusType��һ������֤ȯ״̬����
/////////////////////////////////////////////////////////////////////////
typedef char TAPStandardStatusType;
/// ����ǰ
const TAPStandardStatusType ENUM_StandardStatus_PreOpen = '0';
/// ���Ͼ���
const TAPStandardStatusType ENUM_StandardStatus_CallAuction = '1';
/// ��������
const TAPStandardStatusType ENUM_StandardStatus_Continous = '2';
/// ����
const TAPStandardStatusType ENUM_StandardStatus_Pause = '3';
/// ͣ��
const TAPStandardStatusType ENUM_StandardStatus_Suspend = '4';
/// ����ͣ��
const TAPStandardStatusType ENUM_StandardStatus_LongSuspend = '5';
/// �������ж�
const TAPStandardStatusType ENUM_StandardStatus_UndulationInt = '6';
/// �۶Ͽɻָ�
const TAPStandardStatusType ENUM_StandardStatus_CircuitBreak = '7';
/// �۶ϲ��ɻָ�
const TAPStandardStatusType ENUM_StandardStatus_CircuitBreakU = '8';
/// ����
const TAPStandardStatusType ENUM_StandardStatus_Close = '9';
/// ����
const TAPStandardStatusType ENUM_StandardStatus_Other = 'a';
/// ���̼��Ͼ���
const TAPStandardStatusType ENUM_StandardStatus_CloseCallAuction = 'b';
/// ���д��(�̺󶨼�)
const TAPStandardStatusType ENUM_StandardStatus_CallMatch = 'c';
/// ��������(�̺󶨼�)
const TAPStandardStatusType ENUM_StandardStatus_PostContinous = 'd';
/// ����(�̺󶨼�)
const TAPStandardStatusType ENUM_StandardStatus_PostClose = 'e';
/// ����ǰ(�̺󶨼�)
const TAPStandardStatusType ENUM_StandardStatus_PrePostOpen = 'f';

/////////////////////////////////////////////////////////////////////////
/// TAPBoolType��һ������������
/////////////////////////////////////////////////////////////////////////
typedef bool TAPBoolType;

/////////////////////////////////////////////////////////////////////////
/// TAPCountType��һ����������
/////////////////////////////////////////////////////////////////////////
typedef int TAPCountType;

/////////////////////////////////////////////////////////////////////////
/// TAPDateType��һ����������
/////////////////////////////////////////////////////////////////////////
typedef char TAPDateType[9];

/////////////////////////////////////////////////////////////////////////
/// TAPTimeType��һ��ʱ������
/////////////////////////////////////////////////////////////////////////
typedef char TAPTimeType[9];

/////////////////////////////////////////////////////////////////////////
/// TAPDateTimeType��һ������ʱ������
/////////////////////////////////////////////////////////////////////////
typedef char TAPDateTimeType[18];

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPLicenseType��һ�����֤����
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPLicenseType[256];

/////////////////////////////////////////////////////////////////////////
/// TAPUserTypeType��һ���ͻ���������
/////////////////////////////////////////////////////////////////////////
typedef unsigned int TAPUserTypeType;
/// CTP�û�ʵ��
const TAPUserTypeType ENUM_UserType_CTP = 10001;
/// �����ͨ��Ʊ�û�ʵ��
const TAPUserTypeType ENUM_UserType_TORAStock = 10002;
/// ������ù�Ʊ�û�ʵ��
const TAPUserTypeType ENUM_UserType_TORACredit = 10003;
/// ����Ʊ��Ȩ�û�ʵ��
const TAPUserTypeType ENUM_UserType_TORAOption = 10004;

/// N�ӽ�ģ�⻷���ڻ��û�
const TAPUserTypeType ENUM_UserType_NSIGHTFuture = 20001;
/// N�ӽ�ģ�⻷����ͨ��Ʊ�û�
const TAPUserTypeType ENUM_UserType_NSIGHTStock = 20002;
/// N�ӽ�ģ�⻷�����ù�Ʊ�û�
const TAPUserTypeType ENUM_UserType_NSIGHTCredit = 20003;
/// N�ӽ�ģ�⻷����Ʊ��Ȩ�û�
const TAPUserTypeType ENUM_UserType_NSIGHTOption = 20004;
/// SimNowģ�⻷���û�
const TAPUserTypeType ENUM_UserType_SIMNOWFuture = 20005;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// TAPUserIDType��һ���ͻ�������
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef char TAPUserIDType[16];

/////////////////////////////////////////////////////////////////////////
/// TAPPasswordType��һ����������
/////////////////////////////////////////////////////////////////////////
typedef char TAPPasswordType[41];

/////////////////////////////////////////////////////////////////////////
/// TAPInvestorIDType��һ��Ͷ���ߴ�������
/////////////////////////////////////////////////////////////////////////
typedef char TAPInvestorIDType[16];

/////////////////////////////////////////////////////////////////////////
/// TAPShareholderIDType��һ���ɶ��˻���������
/////////////////////////////////////////////////////////////////////////
typedef char TAPShareholderIDType[11];

/////////////////////////////////////////////////////////////////////////
/// TAPFrontAddressType��һ��ǰ�õ�ַ����
/////////////////////////////////////////////////////////////////////////
typedef char TAPFrontAddressType[32];

/////////////////////////////////////////////////////////////////////////
/// TAPFilePathType��һ���ļ�·������
/////////////////////////////////////////////////////////////////////////
typedef char TAPFilePathType[128];

/////////////////////////////////////////////////////////////////////////
/// TAPBrokerIDType��һ�����͹�˾��������
/////////////////////////////////////////////////////////////////////////
typedef char TAPBrokerIDType[11];

/////////////////////////////////////////////////////////////////////////
/// TAPAppIDType��һ��AppID����
/////////////////////////////////////////////////////////////////////////
typedef char TAPAppIDType[33];

/////////////////////////////////////////////////////////////////////////
/// TAPAuthCodeType��һ���ͻ�����֤������
/////////////////////////////////////////////////////////////////////////
typedef char TAPAuthCodeType[17];

/////////////////////////////////////////////////////////////////////////
/// TAPHDSerialType��һ��Ӳ�����к�����
/////////////////////////////////////////////////////////////////////////
typedef char TAPHDSerialType[33];

/////////////////////////////////////////////////////////////////////////
/// TAPMacAddressType��һ��Mac��ַ����
/////////////////////////////////////////////////////////////////////////
typedef char TAPMacAddressType[21];

/////////////////////////////////////////////////////////////////////////
/// TAPIPAddressType��һ��IP��ַ����
/////////////////////////////////////////////////////////////////////////
typedef char TAPIPAddressType[16];

/////////////////////////////////////////////////////////////////////////
/// TAPPortType��һ���˿ں�����
/////////////////////////////////////////////////////////////////////////
typedef int TAPPortType;

/////////////////////////////////////////////////////////////////////////
/// TAPTerminalInfoType��һ���ն���Ϣ����
/////////////////////////////////////////////////////////////////////////
typedef char TAPTerminalInfoType[256];

/////////////////////////////////////////////////////////////////////////
/// TAPFrontIDType��һ��ǰ�ñ������
/////////////////////////////////////////////////////////////////////////
typedef int TAPFrontIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPSessionIDType��һ���Ự�������
/////////////////////////////////////////////////////////////////////////
typedef int TAPSessionIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPStandardIDType��һ����׼��Ĵ�������
/////////////////////////////////////////////////////////////////////////
typedef char TAPStandardIDType[31];

/////////////////////////////////////////////////////////////////////////
/// TAPStandardNameType��һ����׼�����������
/////////////////////////////////////////////////////////////////////////
typedef char TAPStandardNameType[81];

/////////////////////////////////////////////////////////////////////////
/// TAPOrderMarkType��һ�������������
/////////////////////////////////////////////////////////////////////////
typedef short TAPOrderMarkType;

/////////////////////////////////////////////////////////////////////////
/// TAPOrderIDType��һ������ID����
/////////////////////////////////////////////////////////////////////////
typedef int TAPOrderIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPOrderSysIDType��һ�������������
/////////////////////////////////////////////////////////////////////////
typedef char TAPOrderSysIDType[21];

/////////////////////////////////////////////////////////////////////////
/// TAPVolumeType��һ����������
/////////////////////////////////////////////////////////////////////////
typedef int TAPVolumeType;

/////////////////////////////////////////////////////////////////////////
/// TAPLongVolumeType��һ��LongVolume����
/////////////////////////////////////////////////////////////////////////
#ifdef _WIN32
typedef __int64 TAPLongVolumeType;
#else
typedef long long int TAPLongVolumeType;
#endif

/////////////////////////////////////////////////////////////////////////
/// TAPLargeVolumeType��һ��LargeVolume����
/////////////////////////////////////////////////////////////////////////
typedef double TAPLargeVolumeType;

/////////////////////////////////////////////////////////////////////////
/// TAPMoneyType��һ���ʽ�����
/////////////////////////////////////////////////////////////////////////
typedef double TAPMoneyType;

/////////////////////////////////////////////////////////////////////////
/// TAPPriceType��һ���۸�����
/////////////////////////////////////////////////////////////////////////
typedef double TAPPriceType;

/////////////////////////////////////////////////////////////////////////
/// TAPErrorIDType��һ�������������
/////////////////////////////////////////////////////////////////////////
typedef int TAPErrorIDType;

/////////////////////////////////////////////////////////////////////////
/// TAPMessageType��һ����Ϣ����
/////////////////////////////////////////////////////////////////////////
typedef char TAPMessageType[256];

/////////////////////////////////////////////////////////////////////////
/// TAPMarketIDType��һ���г���������
/////////////////////////////////////////////////////////////////////////
typedef char TAPMarketIDType;
/// �Ϻ�A��
const TAPMarketIDType ENUM_MarketID_SHA = '1';
/// ����A��
const TAPMarketIDType ENUM_MarketID_SZA = '2';
/// �Ϻ�B��
const TAPMarketIDType ENUM_MarketID_SHB = '3';
/// ����B��
const TAPMarketIDType ENUM_MarketID_SZB = '4';
/// ��������A��
const TAPMarketIDType ENUM_MarketID_SZThreeA = '5';
/// ��������B��
const TAPMarketIDType ENUM_MarketID_SZThreeB = '6';
/// �����г�
const TAPMarketIDType ENUM_MarketID_Foreign = '7';
/// ���ڸ۹�ͨ�г�
const TAPMarketIDType ENUM_MarketID_SZHK = '8';
/// �Ϻ��۹�ͨ�г�
const TAPMarketIDType ENUM_MarketID_SHHK = '9';

/////////////////////////////////////////////////////////////////////////
/// TAPProductIDType��һ��֤ȯƷ�ִ�������
/////////////////////////////////////////////////////////////////////////
typedef char TAPProductIDType;
/// ͨ��(�ڲ�ʹ��)
const TAPProductIDType ENUM_ProductID_COMMON = '0';
/// �Ϻ���Ʊ
const TAPProductIDType ENUM_ProductID_SHStock = '1';
/// �Ϻ�����
const TAPProductIDType ENUM_ProductID_SHFund = '3';
/// �Ϻ�ծȯ
const TAPProductIDType ENUM_ProductID_SHBond = '4';
/// �Ϻ���׼ȯ
const TAPProductIDType ENUM_ProductID_SHStandard = '5';
/// �Ϻ���Ѻʽ�ع�
const TAPProductIDType ENUM_ProductID_SHRepurchase = '6';
/// ���ڹ�Ʊ
const TAPProductIDType ENUM_ProductID_SZStock = '7';
/// ���ڻ���
const TAPProductIDType ENUM_ProductID_SZFund = '9';
/// ����ծȯ
const TAPProductIDType ENUM_ProductID_SZBond = 'a';
/// ���ڱ�׼ȯ
const TAPProductIDType ENUM_ProductID_SZStandard = 'b';
/// ������Ѻʽ�ع�
const TAPProductIDType ENUM_ProductID_SZRepurchase = 'c';
/// ���ͨ�۹�����
const TAPProductIDType ENUM_ProductID_SZSEHKMain = 'd';
/// ���ͨ�۹ɴ�ҵ��
const TAPProductIDType ENUM_ProductID_SZSEHKGEM = 'e';
/// ���ͨ�۹����佻��֤ȯ
const TAPProductIDType ENUM_ProductID_SZSEHKETS = 'f';
/// ���ͨ�۹�NasdaqAMX�г�
const TAPProductIDType ENUM_ProductID_SZSEHKNasdaqAMX = 'g';
/// �Ϻ��ƴ���
const TAPProductIDType ENUM_ProductID_SHKC = 'i';
/// �Ϻ�������Ȩ
const TAPProductIDType ENUM_ProductID_SHStockOption = 'u';
/// ���ڸ�����Ȩ
const TAPProductIDType ENUM_ProductID_SZStockOption = 'v';
/// �ڻ�
const TAPProductIDType ENUM_ProductID_Futures = 'B';
/// �ڻ���Ȩ
const TAPProductIDType ENUM_ProductID_Options = 'C';
/// ���
const TAPProductIDType ENUM_ProductID_Combination = 'D';
/// ����
const TAPProductIDType ENUM_ProductID_Spot = 'E';
/// ��ת��
const TAPProductIDType ENUM_ProductID_EFP = 'F';
/// �ֻ���Ȩ
const TAPProductIDType ENUM_ProductID_SpotOption = 'G';
/// TAS��Լ
const TAPProductIDType ENUM_ProductID_TAS = 'H';
/// ����ָ��
const TAPProductIDType ENUM_ProductID_MI = 'Z';

/////////////////////////////////////////////////////////////////////////
/// TAPStandardTypeType��һ������������
/////////////////////////////////////////////////////////////////////////
typedef char TAPStandardTypeType;
/// ͨ��(�ڲ�ʹ��)
const TAPStandardTypeType ENUM_StandardType_COMMON = '0';
/// �Ϻ�A��
const TAPStandardTypeType ENUM_StandardType_SHAShares = 'a';
/// �Ϻ����г���ƱETF
const TAPStandardTypeType ENUM_StandardType_SHSingleMarketStockETF = 'b';
/// �Ϻ����г�ʵ��ծȯETF
const TAPStandardTypeType ENUM_StandardType_SHSingleMarketBondETF = 'c';
/// �Ϻ��ƽ�ETF
const TAPStandardTypeType ENUM_StandardType_SHGoldETF = 'd';
/// �Ϻ�����ETF
const TAPStandardTypeType ENUM_StandardType_SHTradableMonetaryFund = 'e';
/// �Ϻ���ծ�ط�ծ
const TAPStandardTypeType ENUM_StandardType_SHBondNation = 'f';
/// �Ϻ���ҵծ
const TAPStandardTypeType ENUM_StandardType_SHBondCorporation = 'g';
/// �Ϻ���˾ծ
const TAPStandardTypeType ENUM_StandardType_SHBondCompany = 'h';
/// �Ϻ���תծ
const TAPStandardTypeType ENUM_StandardType_SHBondConversion = 'i';
/// �Ϻ�����ծ
const TAPStandardTypeType ENUM_StandardType_SHBondSeparation = 'j';
/// �Ϻ���׼ȯ
const TAPStandardTypeType ENUM_StandardType_SHStandard = 'o';
/// �Ϻ���Ѻʽ�ع�
const TAPStandardTypeType ENUM_StandardType_SHRepo = 'p';
/// �Ϻ����ʽ����
const TAPStandardTypeType ENUM_StandardType_SHCEFund = 'q';
/// �Ϻ�����ʽ����
const TAPStandardTypeType ENUM_StandardType_SHOEFund = 'r';
/// �Ϻ����г�ETF
const TAPStandardTypeType ENUM_StandardType_SHCrossMarketStockETF = 's';
/// �Ϻ��羳ETF
const TAPStandardTypeType ENUM_StandardType_SHCrossBorderETF = 't';
/// �Ϻ��ּ�ĸ����
const TAPStandardTypeType ENUM_StandardType_SHMontherStructFund = 'u';
/// �Ϻ��ּ��ӻ���
const TAPStandardTypeType ENUM_StandardType_SHSubStructFund = 'v';
/// �Ϻ�ʵʱ������һ���
const TAPStandardTypeType ENUM_StandardType_SHRealTimeMonetaryFund = 'w';
/// �Ϻ��ɽ���ծ
const TAPStandardTypeType ENUM_StandardType_SHExchangeableBond = 'x';
/// �Ϻ���׼LOF����
const TAPStandardTypeType ENUM_StandardType_SHLOF = 'A';
/// ��������A��
const TAPStandardTypeType ENUM_StandardType_SZMainAShares = 'B';
/// ������С��ҵ��
const TAPStandardTypeType ENUM_StandardType_SZSME = 'C';
/// ���ڹ�ծ���ط�ծ
const TAPStandardTypeType ENUM_StandardType_SZBondNation = 'D';
/// ������ҵծ
const TAPStandardTypeType ENUM_StandardType_SZBondCorporation = 'E';
/// ���ڹ�˾ծ
const TAPStandardTypeType ENUM_StandardType_SZBondCompany = 'F';
/// ���ڿ�תծ
const TAPStandardTypeType ENUM_StandardType_SZBondConversion = 'G';
/// ���ڷ���ծ
const TAPStandardTypeType ENUM_StandardType_SZBondSeparation = 'H';
/// ���ڴ�ҵ��(ע����)
const TAPStandardTypeType ENUM_StandardType_SZGEMReg = 'I';
/// ���ڴ�ҵ���תծ(ע����)
const TAPStandardTypeType ENUM_StandardType_SZGEMBondConversionReg = 'J';
/// ���ڿ羳ETF
const TAPStandardTypeType ENUM_StandardType_SZCrossBorderETF = 'K';
/// ���ڻƽ�ETF
const TAPStandardTypeType ENUM_StandardType_SZGoldETF = 'L';
/// �����ֽ�ծȯETF
const TAPStandardTypeType ENUM_StandardType_SZCashBondETF = 'M';
/// ���ڵ��г���ƱETF
const TAPStandardTypeType ENUM_StandardType_SZSingleMarketStockETF = 'N';
/// ���ڵ��г�ʵ��ծȯETF
const TAPStandardTypeType ENUM_StandardType_SZSingleMarketBondETF = 'O';
/// ���ڻ���ETF
const TAPStandardTypeType ENUM_StandardType_SZMonetaryFundETF = 'P';
/// ���ڴ�ҵ��
const TAPStandardTypeType ENUM_StandardType_SZGEM = 'Q';
/// ���ڴ�ҵ��ɽ���ծ
const TAPStandardTypeType ENUM_StandardType_SZGEMExchangeableBond = 'R';
/// ���ڴ�ҵ��ɽ���ծ(ע����)
const TAPStandardTypeType ENUM_StandardType_SZGEMExchangeableBondReg = 'S';
/// ���ڱ�׼ȯ
const TAPStandardTypeType ENUM_StandardType_SZStandard = 'T';
/// ������Ѻʽ�ع�
const TAPStandardTypeType ENUM_StandardType_SZRepo = 'U';
/// ���ڷ��ʽ����
const TAPStandardTypeType ENUM_StandardType_SZCEFund = 'V';
/// ���ڿ���ʽ����
const TAPStandardTypeType ENUM_StandardType_SZOEFund = 'W';
/// ���ڿ羳����ʽ����
const TAPStandardTypeType ENUM_StandardType_SZCrossBorderOEFund = 'X';
/// ���ڿ��г���ƱETF
const TAPStandardTypeType ENUM_StandardType_SZCrossMarketStockETF = 'Y';
/// ���ڱ�׼LOF����
const TAPStandardTypeType ENUM_StandardType_SZLOF = 'Z';
/// ���ڿ羳LOF����
const TAPStandardTypeType ENUM_StandardType_SZCrossBorderLOF = '1';
/// ���ڴ�ͳ�ּ�ĸ����
const TAPStandardTypeType ENUM_StandardType_SZMontherStructFund = '2';
/// ���ڴ�ͳ�ּ��ӻ���
const TAPStandardTypeType ENUM_StandardType_SZSubStructFund = '3';
/// ���ڿ羳�ּ�ĸ����
const TAPStandardTypeType ENUM_StandardType_SZMontherCrossBorderStructFund = '4';
/// ���ڿ羳�ּ��ӻ���
const TAPStandardTypeType ENUM_StandardType_SZSubCrossBorderStructFund = '5';
/// ���ڿɽ���ծ
const TAPStandardTypeType ENUM_StandardType_SZExchangeableBond = '6';
/// ���ڴ�ҵ���תծ
const TAPStandardTypeType ENUM_StandardType_SZGEMBondConversion = '7';
/// ���ͨ�۹�ծȯ
const TAPStandardTypeType ENUM_StandardType_SZSEHKBond = '8';
/// ���ͨ�۹�һ����Ȩ֤
const TAPStandardTypeType ENUM_StandardType_SZSEHKBasketWarrant = '9';
/// ���ͨ�۹ɹɱ�
const TAPStandardTypeType ENUM_StandardType_SZSEHKEquity = 'y';
/// ���ͨ�۹�����
const TAPStandardTypeType ENUM_StandardType_SZSEHKTrust = 'z';
/// ���ͨ�۹�Ȩ֤
const TAPStandardTypeType ENUM_StandardType_SZSEHKWarrant = '#';
/// �Ϻ�����ƾ֤
const TAPStandardTypeType ENUM_StandardType_SHCDR = '+';
/// �Ϻ��ƴ����Ʊ
const TAPStandardTypeType ENUM_StandardType_SHKC = '*';
/// �ƴ����Ʒ�����к�ǰ5�������գ�
const TAPStandardTypeType ENUM_StandardType_SHKC1 = '^';
/// �Ϻ��ƴ������ƾ֤
const TAPStandardTypeType ENUM_StandardType_SHKCCDR = '-';
/// �������塢��С�崴����ҵ��Ʊ�����ƾ֤
const TAPStandardTypeType ENUM_StandardType_SZCDR = 'k';
/// ���ڴ�ҵ�崴����ҵ��Ʊ�����ƾ֤
const TAPStandardTypeType ENUM_StandardType_SZGEMCDR = 'l';
/// ���ڴ�ҵ�崴����ҵ��Ʊ�����ƾ֤(ע����)
const TAPStandardTypeType ENUM_StandardType_SZGEMCDRReg = 'm';
/// ������Ʒ�ڻ�ETF
const TAPStandardTypeType ENUM_StandardType_SZCommFuturesETF = 'n';
/// ���ڻ�����ʩ����
const TAPStandardTypeType ENUM_StandardType_SZInfrastructureFund = '=';
/// �Ϻ��ƴ���ETF
const TAPStandardTypeType ENUM_StandardType_SHKCETF = '@';
/// �Ϻ��ƴ���LOF
const TAPStandardTypeType ENUM_StandardType_SHKCLOF = '%';
/// �Ϻ��ƴ����תծ
const TAPStandardTypeType ENUM_StandardType_SHKCBondConversion = '$';
/// �Ϻ������תծ
const TAPStandardTypeType ENUM_StandardType_SHOrientedConversionBond = '<';
/// ���ڶ����תծ
const TAPStandardTypeType ENUM_StandardType_SZOrientedConversionBond = '>';
/// �Ϻ���Ʊ�Ϳ�����Ȩ
const TAPStandardTypeType ENUM_StandardType_SHCallAStockOption = char(1);
/// �Ϻ���Ʊ�Ϳ�����Ȩ
const TAPStandardTypeType ENUM_StandardType_SHPullAStockOption = char(2);
/// �Ϻ������Ϳ�����Ȩ
const TAPStandardTypeType ENUM_StandardType_SHCallFundStockOption = char(3);
/// �Ϻ������Ϳ�����Ȩ
const TAPStandardTypeType ENUM_StandardType_SHPullFundStockOption = char(4);
/// ���ڹ�Ʊ�Ϳ�����Ȩ
const TAPStandardTypeType ENUM_StandardType_SZCallAStockOption = char(5);
/// ���ڹ�Ʊ�Ϳ�����Ȩ
const TAPStandardTypeType ENUM_StandardType_SZPullAStockOption = char(6);
/// ���ڻ����Ϳ�����Ȩ
const TAPStandardTypeType ENUM_StandardType_SZCallFundStockOption = char(7);
/// ���ڻ����Ϳ�����Ȩ
const TAPStandardTypeType ENUM_StandardType_SZPullFundStockOption = char(8);
/// �Ϻ������Ȩ
const TAPStandardTypeType ENUM_StandardType_SHCombOption = char(9);
/// ���������Ȩ
const TAPStandardTypeType ENUM_StandardType_SZCombOption = char(10);

/////////////////////////////////////////////////////////////////////////
/// TAPCombinationTypeType��һ�������������
/////////////////////////////////////////////////////////////////////////
typedef char TAPCombinationTypeType;
/// �ڻ����
const TAPCombinationTypeType ENUM_CombinationType_Future = '0';
/// ��ֱ�۲�BUL
const TAPCombinationTypeType ENUM_CombinationType_BUL = '1';
/// ��ֱ�۲�BER
const TAPCombinationTypeType ENUM_CombinationType_BER = '2';
/// ��ʽ���
const TAPCombinationTypeType ENUM_CombinationType_STD = '3';
/// ���ʽ���
const TAPCombinationTypeType ENUM_CombinationType_STG = '4';
/// �������
const TAPCombinationTypeType ENUM_CombinationType_PRT = '5';
/// ʱ��۲����
const TAPCombinationTypeType ENUM_CombinationType_CAS = '6';
/// ��Ȩ�������
const TAPCombinationTypeType ENUM_CombinationType_OPL = '7';
/// �򱸶����
const TAPCombinationTypeType ENUM_CombinationType_BFO = '8';
/// ������Ȩ��ֱ�۲����
const TAPCombinationTypeType ENUM_CombinationType_BLS = '9';
/// ������Ȩ��ֱ�۲����
const TAPCombinationTypeType ENUM_CombinationType_BES = 'a';

/////////////////////////////////////////////////////////////////////////
/// TAPVolumeMultipleType��һ��������Ʒ��������
/////////////////////////////////////////////////////////////////////////
typedef int TAPVolumeMultipleType;

/////////////////////////////////////////////////////////////////////////
/// TAPUnderlyingMultipleType��һ��������Ʒ��������
/////////////////////////////////////////////////////////////////////////
typedef double TAPUnderlyingMultipleType;

/////////////////////////////////////////////////////////////////////////
/// TAPOptionsTypeType��һ����Ȩ��������
/////////////////////////////////////////////////////////////////////////
typedef char TAPOptionsTypeType;
/// ����
const TAPOptionsTypeType ENUM_OptionsType_CallOptions = '1';
/// ����
const TAPOptionsTypeType ENUM_OptionsType_PutOptions = '2';

/////////////////////////////////////////////////////////////////////////
/// TAPMaxMarginSideAlgorithmType��һ�����߱�֤���㷨����
/////////////////////////////////////////////////////////////////////////
typedef char TAPMaxMarginSideAlgorithmType;
/// ��ʹ�ô��߱�֤���㷨
const TAPMaxMarginSideAlgorithmType ENUM_MaxMarginSideAlgorithm_NO = '0';
/// ʹ�ô��߱�֤���㷨
const TAPMaxMarginSideAlgorithmType ENUM_MaxMarginSideAlgorithm_YES = '1';

/////////////////////////////////////////////////////////////////////////
/// TAPRatioType��һ����������
/////////////////////////////////////////////////////////////////////////
typedef double TAPRatioType;

/////////////////////////////////////////////////////////////////////////
/// TAPPositionDateTypeType��һ���ֲ�������������
/////////////////////////////////////////////////////////////////////////
typedef char TAPPositionDateTypeType;
/// ʹ����ʷ�ֲ�
const TAPPositionDateTypeType ENUM_PositionDateType_UseHistory = '1';
/// ��ʹ����ʷ�ֲ�
const TAPPositionDateTypeType ENUM_PositionDateType_NoUseHistory = '2';

/////////////////////////////////////////////////////////////////////////
/// TAPPositionTypeType��һ���ֲ���������
/////////////////////////////////////////////////////////////////////////
typedef char TAPPositionTypeType;
/// ���ֲ�
const TAPPositionTypeType ENUM_PositionType_Net = '1';
/// �ۺϳֲ�
const TAPPositionTypeType ENUM_PositionType_Gross = '2';

/////////////////////////////////////////////////////////////////////////
/// TAPStrikeModeType��һ��ִ�з�ʽ����
/////////////////////////////////////////////////////////////////////////
typedef char TAPStrikeModeType;
/// ŷʽ
const TAPStrikeModeType ENUM_StrikeMode_Continental = '0';
/// ��ʽ
const TAPStrikeModeType ENUM_StrikeMode_American = '1';
/// ��Ľ��
const TAPStrikeModeType ENUM_StrikeMode_Bermuda = '2';

/////////////////////////////////////////////////////////////////////////
/// TAPInterestType��һ����Ϣ����
/////////////////////////////////////////////////////////////////////////
typedef double TAPInterestType;

/////////////////////////////////////////////////////////////////////////
/// TAPParValueType��һ����ֵ����
/////////////////////////////////////////////////////////////////////////
typedef double TAPParValueType;

/////////////////////////////////////////////////////////////////////////
/// TAPMillisecType��һ��ʱ�䣨���룩����
/////////////////////////////////////////////////////////////////////////
typedef int TAPMillisecType;

/////////////////////////////////////////////////////////////////////////
/// TAPQuotaIDType��һ����ȱ������
/////////////////////////////////////////////////////////////////////////
typedef char TAPQuotaIDType[17];

/////////////////////////////////////////////////////////////////////////
/// TAPCreditQuotaTypeType��һ������ͷ����������
/////////////////////////////////////////////////////////////////////////
typedef char TAPCreditQuotaTypeType;
/// ��ͨ
const TAPCreditQuotaTypeType ENUM_CreditQuotaType_Normal = '0';
/// ר��
const TAPCreditQuotaTypeType ENUM_CreditQuotaType_Special = '1';

/////////////////////////////////////////////////////////////////////////
/// TAPCreditDebtIDType��һ�����ø�ծ�������
/////////////////////////////////////////////////////////////////////////
typedef char TAPCreditDebtIDType[21];

/////////////////////////////////////////////////////////////////////////
/// TAPFloatInfoType��һ�������͸�����Ϣ����
/////////////////////////////////////////////////////////////////////////
typedef double TAPFloatInfoType;

/////////////////////////////////////////////////////////////////////////
/// TAPIntInfoType��һ�����θ�����Ϣ����
/////////////////////////////////////////////////////////////////////////
typedef int TAPIntInfoType;

/////////////////////////////////////////////////////////////////////////
/// TAPRequestIDType��һ������������
/////////////////////////////////////////////////////////////////////////
typedef int TAPRequestIDType;


#endif
