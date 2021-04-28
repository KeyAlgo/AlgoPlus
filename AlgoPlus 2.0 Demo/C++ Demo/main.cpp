#include "APApi.h"
#include <string.h>
#include <vector>

CAPOrderField* pOrder = NULL;
CBaseTrader* g_pTrader;
int g_n = 0;
std::vector<std::string> vStandard = { "bc2106", "bu2106", "cu2105", "fu2105", "i2109", "j2105", "jm2105" };
void onMarketDataFunction(CAPMarketDataField* pAPMarketDataField)
{
	char szText[1024] = { 0 };
	sprintf(szText, "%s,%s,%s,%.4f,%.4f,%s,%d,%s,%d,%lld,%lld,%.4f,%.4f,%.4f,%.4f,%.4f,%.4f,%d,%.4f,%d,%.4f,%.4f,%.4f,%d,%.4f,%d,%.4f,%d,%.4f,%d,%.4f,%d,%.4f,%d,%.4f,%d,%.4f,%d.",
		pAPMarketDataField->TradingDay,
		pAPMarketDataField->StandardID,
		pAPMarketDataField->ExchangeID,
		pAPMarketDataField->PreClosePrice,
		pAPMarketDataField->OpenPrice,
		std::string(1, pAPMarketDataField->StandardStatus).c_str(),
		pAPMarketDataField->TradingCount,
		pAPMarketDataField->UpdateTime,
		pAPMarketDataField->UpdateMillisec,
		pAPMarketDataField->OpenInterest,
		pAPMarketDataField->Volume,
		pAPMarketDataField->Turnover,
		pAPMarketDataField->AveragePrice,
		pAPMarketDataField->LastPrice,
		pAPMarketDataField->HighestPrice,
		pAPMarketDataField->LowestPrice,
		pAPMarketDataField->BidPrice1,
		pAPMarketDataField->BidVolume1,
		pAPMarketDataField->AskPrice1,
		pAPMarketDataField->AskVolume1,
		pAPMarketDataField->UpperLimitPrice,
		pAPMarketDataField->LowerLimitPrice,
		pAPMarketDataField->BidPrice2,
		pAPMarketDataField->BidVolume2,
		pAPMarketDataField->AskPrice2,
		pAPMarketDataField->AskVolume2,
		pAPMarketDataField->BidPrice3,
		pAPMarketDataField->BidVolume3,
		pAPMarketDataField->AskPrice3,
		pAPMarketDataField->AskVolume3,
		pAPMarketDataField->BidPrice4,
		pAPMarketDataField->BidVolume4,
		pAPMarketDataField->AskPrice4,
		pAPMarketDataField->AskVolume4,
		pAPMarketDataField->BidPrice5,
		pAPMarketDataField->BidVolume5,
		pAPMarketDataField->AskPrice5,
		pAPMarketDataField->AskVolume5);
	printf("%s\n", szText);
};
void onOrderFunction(TAPEventIDType nEventID, const CAPOrderField* pAPOrderField, const CAPPositionField* pAPPositionField, double dUsableCash)
{
	char szText[4096] = { 0 };
	sprintf(szText, "%s,%s,%s,%d,%d,%d,%d,%d,%d,%s,%s,%d,%s,%s,%d,%s,%s,%s,%s,%d,%f,%lld,%s,%s,%s,%s,%d,%d,%d,%f,%d,%d,%f,%f,%f,%s,%s,%s,%d,%s.",
		pAPOrderField->TradingDay,
		pAPOrderField->UserID,
		pAPOrderField->ShareholderID,
		pAPOrderField->SessionID,
		pAPOrderField->FrontID,
		pAPOrderField->RequestID,
		pAPOrderField->OrderID,
		pAPOrderField->NextOrderID,
		pAPOrderField->OrderMark,
		pAPOrderField->ExchangeID,
		pAPOrderField->StandardID,
		int(pAPOrderField->IsBuyFromMarket),
		pAPOrderField->Direction,
		std::string(1, pAPOrderField->OrderType).c_str(),
		int(pAPOrderField->IsLimitOrder),
		std::string(1, pAPOrderField->PriceType).c_str(),
		std::string(1, pAPOrderField->TimeCondition).c_str(),
		std::string(1, pAPOrderField->VolumeCondition).c_str(),
		std::string(1, pAPOrderField->ContingentCondition).c_str(),
		pAPOrderField->OriginalVolume,
		pAPOrderField->OriginalPrice,
		pAPOrderField->OrderLocalTime,
		pAPOrderField->OrderSysID,
		pAPOrderField->InsertTime,
		pAPOrderField->UpdateTime,
		std::string(1, pAPOrderField->OrderStatus).c_str(),
		pAPOrderField->TradedVolumeChange,
		pAPOrderField->TradedVolume,
		pAPOrderField->CancelVolume,
		pAPOrderField->LastTradedPrice,
		pAPOrderField->TradedVolumeChangeOfTurnover,
		pAPOrderField->TradedVolumeOfTurnover,
		pAPOrderField->TurnoverChange,
		pAPOrderField->Turnover,
		pAPOrderField->AverageCost,
		pAPOrderField->CreditQuotaID,
		std::string(1, pAPOrderField->CreditQuotaType).c_str(),
		pAPOrderField->CreditDebtID,
		pAPOrderField->ErrorID,
		pAPOrderField->Message);
	printf("%s\n", szText);
}
void onEventFunction(TAPEventIDType nEventID, const void* pContentField, bool bIsLast, int nErrorID, const char* szMessage)
{
	printf("OnEventFunction:%d,ErrorID:%d,ErrorMsg:%s\n", nEventID, nErrorID, szMessage);
}
void onLoopFunction()
{
	++g_n;
	printf("onLoop:%d\n", g_n);
	if (g_n == 1)
	{
		cancelOrderAll(g_pTrader);
	}
	else if (g_n == 100)
	{
		for (auto iter : vStandard)
		{
			buyOpen(g_pTrader, iter.c_str(), 10, ENUM_OrderType_FrontierLimitAndWait, 0);
		}
	}
}

int main()
{
	CAPLoginField* pLoginField = new CAPLoginField;
	memset(pLoginField, 0, sizeof(CAPLoginField));

	///许可证
	// 关于授权的说明：http://algo.plus/algoplus/0106001.html
	// 加QQ号2565657639(注明AlgoPlus授权)，或者公众号AlgoPlus后台留言，申请模拟交易授权。
	strcpy(pLoginField->License, "");
	///客户类型
	pLoginField->UserType = ENUM_UserType_NSIGHTFuture;
	///客户号
	strcpy(pLoginField->UserID, "");
	///投资者代码
	strcpy(pLoginField->InvestorID, "");
	///密码
	strcpy(pLoginField->Password, "");
	///交易前置（tcp://127.0.0.1:22222）
	strcpy(pLoginField->TraderFront, "tcp://210.14.72.12:4600");
	///行情交易（tcp://127.0.0.1:22222）
	strcpy(pLoginField->MdFront, "tcp://210.14.72.12:4602");
	///登录超时设置
	pLoginField->ConnectTimeout = 0;
	///账户任务执行间隔
	pLoginField->TaskExecuteGap = MICROSECONDS_IN_SECOND * 2;
	///循环线程间隔
	//pLoginField->LoopGap = 
	///文件路径
	strcpy(pLoginField->BasePath, "./");
	///BrokerID（期货专用）
	strcpy(pLoginField->BrokerID, "10010");
	///AppID（期货专用）
	strcpy(pLoginField->AppID, "0");
	///AuthCode（期货专用）
	strcpy(pLoginField->AuthCode, "0");
	//pLoginField->TaskExecuteGap = 100000;

	g_pTrader = init(1, pLoginField, onMarketDataFunction, onOrderFunction, onEventFunction, onLoopFunction);
	if (NULL != g_pTrader)
	{
		char** ppStandard = new char*[vStandard.size()];
		for (int ikk = 0; ikk < vStandard.size(); ++ikk)
		{
			ppStandard[ikk] = (char*)(vStandard[ikk].c_str());
		}
		subscribe(g_pTrader, ppStandard, vStandard.size());
		delete[] ppStandard;
		loop();
	}
	else
	{
		int n = getInitError();

		printf("%d\n", n);
	}
}