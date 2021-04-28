
//# AlgoPlus量化投资开源框架
//# 微信公众号：AlgoPlus
//# 官网：http://algo.plus

#ifndef CMdSpi_H
#define CMdSpi_H

#include "ThostFtdcMdApi.h"
#include "MyTools.h"

//声明静态函数，并没有实现，在Cython中实现，以实现回调 python 代码
//目的就是解决 C 回调 python 代码，才能实现在python中实现编写业务逻辑

static inline int MdSpi_OnFrontConnected(PyObject *);
static inline int MdSpi_OnFrontDisconnected(PyObject *, int);
static inline int MdSpi_OnHeartBeatWarning(PyObject *, int);
static inline int MdSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspUnSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspUnSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRtnDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *);
static inline int MdSpi_OnRtnForQuoteRsp(PyObject *, CThostFtdcForQuoteRspField *);


class CMdSpi : public CThostFtdcMdSpi{
public:

  CMdSpi(PyObject *obj):self(obj) {};
  virtual ~CMdSpi() {};

  ///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
  virtual void  OnFrontConnected() {
    PyGILLock gilLock;
    MdSpi_OnFrontConnected(self);
  };

  ///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
  ///@param nReason 错误原因
  ///0x1001 网络读失败
  ///0x1002 网络写失败
  ///0x2001 接收心跳超时
  ///0x2002 发送心跳失败
  ///0x2003 收到错误报文
  virtual void  OnFrontDisconnected(int nReason) {
    PyGILLock gilLock;
    MdSpi_OnFrontDisconnected(self, nReason);
  };

  ///心跳超时警告。当长时间未收到报文时，该方法被调用。
  ///@param nTimeLapse 距离上次接收报文的时间
  virtual void  OnHeartBeatWarning(int nTimeLapse) {
    PyGILLock gilLock;
    MdSpi_OnHeartBeatWarning(self, nTimeLapse);
  };

  ///登录请求响应
  virtual void  OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast);
  };

  ///登出请求响应
  virtual void  OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast);
  };

  ///错误应答
  virtual void  OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast);
  };

  ///订阅行情应答
  virtual void  OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
  };

  ///取消订阅行情应答
  virtual void  OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
  };

  ///订阅询价应答
  virtual void  OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
  };

  ///取消订阅询价应答
  virtual void  OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
  };

  ///深度行情通知
  virtual void  OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {
    PyGILLock gilLock;
    MdSpi_OnRtnDepthMarketData(self, pDepthMarketData);
  };

  ///询价通知
  virtual void  OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
    PyGILLock gilLock;
    MdSpi_OnRtnForQuoteRsp(self, pForQuoteRsp);
  };

private:
    PyObject *self;
};

#endif /* CMdSpi_H */
