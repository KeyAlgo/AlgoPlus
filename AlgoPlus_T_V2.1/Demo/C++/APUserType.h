#ifndef AP_USERTYPE_H__
#define AP_USERTYPE_H__

/////////////////////////////////////////////////////////////////////////
/// TAPUserTypeType是一个客户类型类型
/////////////////////////////////////////////////////////////////////////
typedef int TAPUserTypeType;

/// CTP用户实盘
#define ENUM_UserType_CTP 10001
/// 奇点普通股票用户实盘
#define ENUM_UserType_TORAStock 10002
/// 奇点信用股票用户实盘
#define ENUM_UserType_TORACredit 10003
/// 奇点股票期权用户实盘
#define ENUM_UserType_TORAOption 10004
/// 奇点普通股票L2行情用户实盘
#define ENUM_UserType_TORAStockL2 10005
/// 奇点信用股票L2行情用户实盘
#define ENUM_UserType_TORACreditL2 10006
/// N视界模拟环境期货用户
#define ENUM_UserType_NSIGHTFuture 20001
/// N视界模拟环境普通股票用户
#define ENUM_UserType_NSIGHTStock 20002
/// N视界模拟环境信用股票用户
#define ENUM_UserType_NSIGHTCredit 20003
/// N视界模拟环境股票期权用户
#define ENUM_UserType_NSIGHTOption 20004
/// SimNow模拟环境用户
#define ENUM_UserType_SIMNOWFuture 20005

#endif
