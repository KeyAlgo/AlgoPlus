#include <vector>
#include <iostream>

#include "APApi.h"
#include "APUtilities.h"
#include "APCTPEventStruct.h"
#include "ThostFtdcUserApiStruct.h"

int g_n = 0;
TAPStandardIDType g_StansardID = { "ag2112" };
std::vector<std::string> vStandard = { g_StansardID };

CBaseTrader* g_pTrader;
CAPOrderField* pOrder = NULL;

void onMarketDataCallback(TAPEventIDType nEventID, CAPMarketDataField* pAPMarketDataField)
{
	TAPStructKeyValueMap mStructKeyValueMap = TAPStructKeyValueMap();
	CAPPrintHelper::toMap(mStructKeyValueMap, pAPMarketDataField);
	std::string strInstrumentID = mStructKeyValueMap["InstrumentID"];
	std::string strLastPrice = mStructKeyValueMap["LastPrice"];
	printf("%s:%f\n", strInstrumentID.c_str(), strLastPrice.c_str());
};
void onOrderCallback(TAPEventIDType nEventID, CAPOrderField* pAPOrderField, CAPPositionField* pAPPositionField, double dUsableCash)
{
	std::string strValueText = "";
	strValueText = CAPPrintHelper::toText(pAPOrderField, true, " || ");
	printf("EventID:%d,Order->%s\n", nEventID, strValueText.c_str());
	strValueText = CAPPrintHelper::toText(pAPPositionField, true, " || ");
	printf("EventID:%d,Position->%s\n", nEventID, strValueText.c_str());
	printf("EventID:%d,UsableCash->%f\n", nEventID, dUsableCash);
}
void onEventFunction(TAPEventIDType nEventID, void* pContentField, bool bIsLast, const char* szUserID, int nErrorID, const char* szMessage)
{
	std::string strValueText = "";
	if (nEventID == ENUM_CTPTaskID_Authenticate)
	{
		if (NULL != pContentField)
		{
			strValueText += CAPPrintHelper::toText((EVENTSTRUCT(ENUM_CTPTaskID_Authenticate)*)pContentField, true, " || ");
		}
	}
	else if (nEventID == ENUM_CTPTaskID_LoginTrader)
	{
		if (NULL != pContentField)
		{
			strValueText += CAPPrintHelper::toText((EVENTSTRUCT(ENUM_CTPTaskID_LoginTrader)*)pContentField, true, " || ");
		}
	}
	else if (nEventID == ENUM_CTPTaskID_ConfirmSettlementInfo)
	{
		if (NULL != pContentField)
		{
			strValueText += CAPPrintHelper::toText((EVENTSTRUCT(ENUM_CTPTaskID_ConfirmSettlementInfo)*)pContentField, true, " || ");
		}
	}
	else if (nEventID == ENUM_CTPTaskID_QryInstrument)
	{
		if (NULL != pContentField)
		{

		}
	}
	else if (nEventID == ENUM_CTPTaskID_QryOrder)
	{
		if (NULL != pContentField)
		{
			strValueText += CAPPrintHelper::toText((EVENTSTRUCT(ENUM_CTPTaskID_QryOrder)*)pContentField, true, " || ");
		}
	}
	else if (nEventID == ENUM_CTPTaskID_QryTrade)
	{
		if (NULL != pContentField)
		{
			strValueText += CAPPrintHelper::toText((EVENTSTRUCT(ENUM_CTPTaskID_QryTrade)*)pContentField, true, " || ");
		}
	}
	else if (nEventID == ENUM_CTPTaskID_QryPosition)
	{
		if (NULL != pContentField)
		{
			strValueText += CAPPrintHelper::toText((EVENTSTRUCT(ENUM_CTPTaskID_QryPosition)*)pContentField, true, " || ");
		}
	}
	else
		if (nEventID == ENUM_CTPTaskID_QryTradingAccount)
		{
			if (NULL != pContentField)
			{
				strValueText += CAPPrintHelper::toText((EVENTSTRUCT(ENUM_CTPTaskID_QryTradingAccount)*)pContentField, true, " || ");
			}
		}
		else if (nEventID == ENUM_CTPTaskID_LoginMd)
		{
			if (NULL != pContentField)
			{
				strValueText += CAPPrintHelper::toText((EVENTSTRUCT(ENUM_CTPTaskID_LoginMd)*)pContentField, true, " || ");
			}
		}

	printf("EventID:%d,ErrorID:%d,ErrorMsg:%s,%s.\n", nEventID, nErrorID, szMessage, strValueText.c_str());
}

void onMarketData(TAPEventIDType nEventID, CAPMarketDataField* pMarketData)
{

}

void onLoopFunction()
{
	int nStep = 100;
	double dAmount = 20000;

	++g_n;

	if (g_n % nStep == 0)
	{
		printf("onLoop:%d\n", g_n);
	}

	if (g_n == nStep * 1)
	{
		buyOpen(g_pTrader, g_StansardID, 8, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 2)
	{
		//sellClose(g_pTrader, g_StansardID, 2, ENUM_OrderType_FrontierLimitAndWait, 0, 0, NULL, ENUM_Direction_Sell, ENUM_OffsetFlag_CloseHistory);
	}
	else if (g_n == nStep * 3)
	{
		sellClose(g_pTrader, g_StansardID, 2, ENUM_OrderType_FrontierLimitAndWait, 0, 0, NULL, ENUM_Direction_Sell, ENUM_OffsetFlag_CloseToday);
	}
	else if (g_n == nStep * 4)
	{
		sellOpen(g_pTrader, g_StansardID, 8, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 5)
	{
		//buyClose(g_pTrader, g_StansardID, 2, ENUM_OrderType_FrontierLimitAndWait, 0, 0, NULL, ENUM_Direction_Sell, ENUM_OffsetFlag_CloseHistory);
	}
	else if (g_n == nStep * 6)
	{
		buyClose(g_pTrader, g_StansardID, 2, ENUM_OrderType_FrontierLimitAndWait, 0, 0, NULL, ENUM_Direction_Sell, ENUM_OffsetFlag_CloseToday);
	}
	else if (g_n == nStep * 7)
	{
		buy(g_pTrader, g_StansardID, 30, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 8)
	{
		buyAmount(g_pTrader, g_StansardID, dAmount, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 9)
	{
		sell(g_pTrader, g_StansardID, 24, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 10)
	{
		sellAmount(g_pTrader, g_StansardID, dAmount, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 11)
	{
		balanceToShortVolume(g_pTrader, g_StansardID, 10, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 12)
	{
		balanceToLongValue(g_pTrader, g_StansardID, dAmount, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 13)
	{
		balanceToLongVolume(g_pTrader, g_StansardID, 10, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 14)
	{
		closeLong(g_pTrader, g_StansardID, 1, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
	else if (g_n == nStep * 15)
	{
		closeLong(g_pTrader, g_StansardID, 9999, ENUM_OrderType_FrontierLimitAndWait, 0);
	}
}

int main()
{
	CAPLoginField* pLoginField = new CAPLoginField();

	///许可证
	///加QQ号2565657639(注明AlgoPlus授权)，或者公众号AlgoPlus后台留言，免费申请模拟交易授权。
	strcpy(pLoginField->License, "");
	///客户类型
	pLoginField->UserType = ENUM_UserType_SIMNOWFuture;
	///客户号
	strcpy(pLoginField->UserID, "");
	///密码
	strcpy(pLoginField->Password, "");
	///交易前置（tcp://127.0.0.1:22222）
	strcpy(pLoginField->TraderFront, "tcp://180.168.146.187:10201");
	///行情交易（tcp://127.0.0.1:22222）
	strcpy(pLoginField->MdFront, "tcp://180.168.146.187:10211");
	///BrokerID（期货专用）
	strcpy(pLoginField->BrokerID, "9999");
	///AppID（期货专用）
	strcpy(pLoginField->AppID, "simnow_client_test");
	///AuthCode（期货专用）
	strcpy(pLoginField->AuthCode, "0000000000000000");

	g_pTrader = init(1, pLoginField, NULL, NULL, onLoopFunction, NULL);
	if (NULL != g_pTrader)
	{
		if (vStandard.size() > 0)
		{
			char** ppStandard = new char*[vStandard.size()];
			for (int ikk = 0; ikk < vStandard.size(); ++ikk)
			{
				ppStandard[ikk] = (char*)(vStandard[ikk].c_str());
			}
			subscribe(g_pTrader, ppStandard, vStandard.size());
			delete[] ppStandard;
		}
		loop();
	}
	else
	{
		int n = getInitError();

		printf("%d\n", n);
	}
}