
//# AlgoPlus量化投资开源框架
//# 微信公众号：AlgoPlus
//# 官网：http://algo.plus

#ifndef MyTools_H
#define MyTools_H

class PyGILLock
{
public:
  PyGILLock()
  {
      m_gil_state = PyGILState_Ensure();
  }

  ~PyGILLock()
  {
      PyGILState_Release(m_gil_state);
  }

private:
  PyGILState_STATE m_gil_state;
};

#endif /* MyTools_H */
