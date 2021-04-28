# encoding:utf-8
# distutils: language=c++

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from cpython cimport PyObject
from libc.string cimport const_char
from libcpp cimport bool as cbool
# from libcpp.memory cimport shared_ptr,make_shared
from .ThostFtdcUserApiStruct cimport *


cdef extern from 'ThostFtdcMdApi.h':

    cdef cppclass CMdApi "CThostFtdcMdApi":
        #获取API的版本信息
        #@retrun 获取到的版本号
        @staticmethod
        const_char *GetApiVersion ()nogil

        #删除接口对象本身
        #@remark 不再使用本接口对象时,调用该函数删除接口对象
        void Release ()nogil

        #初始化
        #@remark 初始化运行环境,只有调用后,接口才开始工作
        void Init ()nogil

        #等待接口线程结束运行
        #@return 线程退出代码
        int Join ()nogil

        #获取当前交易日
        #@retrun 获取到的交易日
        #@remark 只有登录成功后,才能得到正确的交易日
        const_char *GetTradingDay ()nogil except +

        #注册前置机网络地址
        #@param pszFrontAddress：前置机网络地址。
        #@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
        #@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        void RegisterFront (char *pszFrontAddress)nogil except +

        #注册名字服务器网络地址
        #@param pszNsAddress：名字服务器网络地址。
        #@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。
        #@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        #@remark RegisterNameServer优先于RegisterFront
        void RegisterNameServer (char *pszNsAddress)nogil except +

        #注册名字服务器用户信息
        #@param pFensUserInfo：用户信息。
        void RegisterFensUserInfo (CThostFtdcFensUserInfoField * pFensUserInfo)nogil except +

        #注册回调接口
        #@param pSpi 派生自回调接口类的实例
        void RegisterSpi (CMdSpi *pSpi)nogil except +

        #订阅行情。
        #@param ppInstrumentID 合约ID
        #@param nCount 要订阅/退订行情的合约个数
        #@remark
        int SubscribeMarketData (char *ppInstrumentID[], int nCount)nogil except +

        #退订行情。
        #@param ppInstrumentID 合约ID
        #@param nCount 要订阅/退订行情的合约个数
        #@remark
        int UnSubscribeMarketData (char *ppInstrumentID[], int nCount)nogil except +

        #订阅询价。
        #@param ppInstrumentID 合约ID
        #@param nCount 要订阅/退订行情的合约个数
        #@remark
        int SubscribeForQuoteRsp (char *ppInstrumentID[], int nCount)nogil except +

        #退订询价。
        #@param ppInstrumentID 合约ID
        #@param nCount 要订阅/退订行情的合约个数
        #@remark
        int UnSubscribeForQuoteRsp (char *ppInstrumentID[], int nCount)nogil except +

        #用户登录请求
        int ReqUserLogin (CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID)nogil except +

        #登出请求
        int ReqUserLogout (CThostFtdcUserLogoutField *pUserLogout, int nRequestID)nogil except +


cdef extern from 'ThostFtdcMdApi.h' namespace "CThostFtdcMdApi":
    CMdApi  *CreateFtdcMdApi(const_char *pszFlowPath, cbool bIsUsingUdp, cbool bIsMulticast) nogil except +


cdef extern from 'CMdAPI.h':
    cdef cppclass CMdSpi:
        CMdSpi(PyObject *obj)