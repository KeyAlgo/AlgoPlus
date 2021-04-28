# AlgoPlus 2.0

## 定位与规划

AlgoPlus 2.0是使用c++语言开发的用于全市场交易的SDK，旨在提高量化交易开发效率、促进量化交易技术交流。

项目将聚焦于以下几个方向：

* 在统一框架下提供实现二级市场业务的方法封装，包括但不限于期货、期货期权、普通股票、融资融券、股票期权……；
* 提供智能报单指令，例如特殊价格类型、金额报单、目标调仓、自动处理今仓和昨仓；[http://algo.plus/algoplus/0101006.html](http://algo.plus/algoplus/0101006.html)
* 连续运行自动初始化、断线重连恢复；
* 优化设计、降低延时、提高效率；
* 管理多账户；
* c++/python/java接口；
* 前端UI。

-------

## 范例

* [N视界股票仿真交易范例](/AlgoPlus%202.0%20Demo/Python%20Demo/future_demo.py)
* [N视界期货仿真交易范例](/AlgoPlus%202.0%20Demo/Python%20Demo/stock_demo.py)


-------

## 开发指南

1. 综述 [http://algo.plus/algoplus/0101001.html](http://algo.plus/algoplus/0101001.html)

2. 基础概念 [http://algo.plus/algoplus/0101002.html](http://algo.plus/algoplus/0101002.html)

3. 初始化 [http://algo.plus/algoplus/0101003.html](http://algo.plus/algoplus/0101003.html)

4. 行情 [http://algo.plus/algoplus/0101004.html](http://algo.plus/algoplus/0101004.html)

5. 订单要素 [http://algo.plus/algoplus/0101005.html](http://algo.plus/algoplus/0101005.html)

6. 报单 [http://algo.plus/algoplus/0101006.html](http://algo.plus/algoplus/0101006.html)

7. 撤销订单 [http://algo.plus/algoplus/0101007.html](http://algo.plus/algoplus/0101007.html)

8. 事件驱动 [http://algo.plus/algoplus/0101008.html](http://algo.plus/algoplus/0101008.html)

9. Loop驱动 [http://algo.plus/algoplus/0101009.html](http://algo.plus/algoplus/0101009.html)

10. 任务队列 [http://algo.plus/algoplus/0101010.html](http://algo.plus/algoplus/0101010.html)

11. 常用查询 [http://algo.plus/algoplus/0101011.html](http://algo.plus/algoplus/0101011.html)

12. 时间工具 [http://algo.plus/algoplus/0101012.html](http://algo.plus/algoplus/0101012.html)

**Python版特别说明** [http://algo.plus/algoplus/0102002.html](http://algo.plus/algoplus/0102002.html)

-------

## 模拟交易平台

N视界模拟系统官网：http://n-sight.com.cn/

注册之后，在个人中心可以找交易账户和密码。使用该账户和密码就可以使用N视界提供的股票、两融、期货、期权四套模拟交易环境。

#期货环境信息
BrokerID：10010
AppID：仿真环境暂时不需要。
AuthCode：仿真环境暂时不需要。

交易前置 tcp://210.14.72.12:4600
行情交易 tcp://210.14.72.12:4602

更多信息：[http://algo.plus/algoplus/0104001.html](http://algo.plus/algoplus/0104001.html)

-------

## 公测说明

AlgoPlus 2.0自2021年4月19日开放公测，至2021年7月31日结束。期间：

* 优先支持[N视界期货模拟](http://algo.plus/algoplus/0103001.html)业务，后续会增加对N视界股票、Simnow期货的支持；
* 参与公测的用户可获得三个月实盘授权奖励，可其他与奖励、赠送累加；
* 优先提供c++/python的windows版接口；
* 暂不支持管理多账户；
* 暂不提供ui。

-------

## 授权

任何基于AlgoPlus 2.0的开发都需要获得授权（模拟交易授权、实盘交易授权、商业开发授权）。

项目将对参与社区建设、分享经验的用户提供授权奖励。

项目将随机向加入社区的用户赠送授权。

奖励、赠送授权遵守《[奖励与赠送规则20210419](http://algo.plus/algoplus/0106001.html)》。

-------

## 下载

项目发布于以下托管平台：

码云（Gitee）： <https://gitee.com/algoplus/AlgoPlus>

GitHub： <https://github.com/keyalgo/algoplus>

-------

## 社区

* QQ群： **866469866**（加群注明AlgoPlus）
* 微信公众号： **AlgoPlus**
* 官网： <http://algo.plus> 、 <http://7jia.com>
* 邮箱： algo@algo.plus

-------

## 合作

合作可通过社区联系。
