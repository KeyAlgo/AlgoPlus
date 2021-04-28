
//# AlgoPlus����Ͷ�ʿ�Դ���
//# ΢�Ź��ںţ�AlgoPlus
//# ������http://algo.plus

#ifndef CMdSpi_H
#define CMdSpi_H

#include "ThostFtdcMdApi.h"
#include "MyTools.h"

//������̬��������û��ʵ�֣���Cython��ʵ�֣���ʵ�ֻص� python ����
//Ŀ�ľ��ǽ�� C �ص� python ���룬����ʵ����python��ʵ�ֱ�дҵ���߼�

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

  ///���ͻ����뽻�׺�̨������ͨ������ʱ����δ��¼ǰ�����÷��������á�
  virtual void  OnFrontConnected() {
    PyGILLock gilLock;
    MdSpi_OnFrontConnected(self);
  };

  ///���ͻ����뽻�׺�̨ͨ�����ӶϿ�ʱ���÷��������á���������������API���Զ��������ӣ��ͻ��˿ɲ�������
  ///@param nReason ����ԭ��
  ///0x1001 �����ʧ��
  ///0x1002 ����дʧ��
  ///0x2001 ����������ʱ
  ///0x2002 ��������ʧ��
  ///0x2003 �յ�������
  virtual void  OnFrontDisconnected(int nReason) {
    PyGILLock gilLock;
    MdSpi_OnFrontDisconnected(self, nReason);
  };

  ///������ʱ���档����ʱ��δ�յ�����ʱ���÷��������á�
  ///@param nTimeLapse �����ϴν��ձ��ĵ�ʱ��
  virtual void  OnHeartBeatWarning(int nTimeLapse) {
    PyGILLock gilLock;
    MdSpi_OnHeartBeatWarning(self, nTimeLapse);
  };

  ///��¼������Ӧ
  virtual void  OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast);
  };

  ///�ǳ�������Ӧ
  virtual void  OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast);
  };

  ///����Ӧ��
  virtual void  OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast);
  };

  ///��������Ӧ��
  virtual void  OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
  };

  ///ȡ����������Ӧ��
  virtual void  OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
  };

  ///����ѯ��Ӧ��
  virtual void  OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
  };

  ///ȡ������ѯ��Ӧ��
  virtual void  OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    PyGILLock gilLock;
    MdSpi_OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
  };

  ///�������֪ͨ
  virtual void  OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {
    PyGILLock gilLock;
    MdSpi_OnRtnDepthMarketData(self, pDepthMarketData);
  };

  ///ѯ��֪ͨ
  virtual void  OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
    PyGILLock gilLock;
    MdSpi_OnRtnForQuoteRsp(self, pForQuoteRsp);
  };

private:
    PyObject *self;
};

#endif /* CMdSpi_H */
