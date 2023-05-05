# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2023/5/15
@Remark: 
"""

import unittest
import sys
import os
file_exec_path = os.path.dirname(os.path.dirname(__file__))
restSpotPath = os.path.join(file_exec_path, "restSpot")
path = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, path)
sys.path.insert(0, file_exec_path)
sys.path.insert(0, restSpotPath)

from restFuture.HttpAPI import *  # NOQA


domain = "http://fapi-inc.xt-qa.com"

# publicAPI
publicAPI = PublicFutureHttpAPI(domain)

accesskey = "xxxxxxxxxxxxxxxxxxxx"
sercetkey = "yyyyyyyyyyyyyyyyyyyy"
signedHttpAPI = SignedFutureHttpAPI(accesskey, sercetkey, domain)
signedFutureHttpAPI = SignedFutureProfitHttpAPI(accesskey, sercetkey, domain)


class XT4HttpTest(unittest.TestCase):
    """ """

    @unittest.skip
    def test_get_coins_info(self):
        """ """
        res = publicAPI.get_coins_info()

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_symbol_detail(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }

        res = publicAPI.get_symbol_detail(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_marketconfig_list(self):
        """ """
        res = publicAPI.get_marketconfig_list()

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_leverage_bracket_detail(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_leverage_bracket_detail(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_leverage_bracket_detail(self):
        """ """
        res = publicAPI.get_leverage_bracket_list()

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_ticker(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_tickers(self):
        """ """
        res = publicAPI.get_tickers()

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_deal(self):
        """ """
        params = {
            "symbol": "btc_usdt",
            "num": "1",
        }
        res = publicAPI.get_deal(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_depth(self):
        """ """
        params = {
            "symbol": "btc_usdt",
            "level": "1",
        }
        res = publicAPI.get_depth(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_symbol_index_price(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_symbol_index_price(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_all_index_price(self):
        """ """
        res = publicAPI.get_all_index_price()

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_symbol_market_price(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_symbol_market_price(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_all_market_price(self):
        """ """
        res = publicAPI.get_all_market_price()

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_kline(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_kline(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_agg_ticker(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_agg_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_agg_tickers(self):
        """ """
        res = publicAPI.get_agg_tickers()

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_funding_rate(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_funding_rate(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_funding_rate_racord(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_funding_rate_racord(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_risk_balance(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_risk_balance(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_open_interest(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_open_interest(params)
        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_account_info(self):
        """ """
        res = signedHttpAPI.get_account_info()

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_listenkey(self):
        """ """
        res = signedHttpAPI.get_listenkey()

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_balance_detail(self):
        """ """
        params = {
            "coin": "usdt"
        }
        res = signedHttpAPI.get_balance_detail(params)

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_balance_list(self):
        """ """
        res = signedHttpAPI.get_balance_list()

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_balance_bills(self):
        """ """
        res = signedHttpAPI.get_balance_bills()

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_funding_rate_list(self):
        """ """
        res = signedHttpAPI.get_funding_rate_list()

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_get_position_list(self):
        """ """
        # params = {
        #     "symbol": "btc_usdt"
        # }
        res = signedHttpAPI.get_position_list()

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_position_adjust_leverage(self):
        """ """
        params = {
            "symbol": "btc_usdt",
            "positionSide": "SHORT",
            "leverage": "1",
        }
        res = signedHttpAPI.position_adjust_leverage(params)

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_position_margin(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = signedHttpAPI.position_margin(params)

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_position_auto_margin(self):
        """ """
        params = {
            "symbol": "btc_usdt",
            "positionSide": "SHORT",
            "autoMargin": True,
        }
        res = signedHttpAPI.position_auto_margin(params)

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_position_close_all(self):
        """ """
        res = signedHttpAPI.position_close_all()

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_position_adl(self):
        """ """
        res = signedHttpAPI.get_position_adl()

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_cancel_collection(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = signedHttpAPI.cancel_collection(params)

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_collection_list(self):
        """ """
        res = signedHttpAPI.get_collection_list()

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_position_change_type(self):
        """ """
        params = {
            "symbol": "btc_usdt",
            "positionSide": "SHORT",
            "positionType": "CROSSED",
        }
        res = signedHttpAPI.position_change_type(params)

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_order_create(self):
        """ """
        params = {
            "symbol": "btc_usdt",
            "orderSide": "BUY",
            "orderType": "MARKET",
            "origQty": "1",
            "price": "29180",
            "positionSide": "SHORT",
        }
        res = signedFutureHttpAPI.order_create(params)

        print(res)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_order_history_list(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = signedFutureHttpAPI.get_order_history_list(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_trade_list(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = signedFutureHttpAPI.get_trade_list(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_batch_order(self):
        """ """

        data = [
            {
                "symbol":       "btc_usdt",
                "price":        "29000",
                "orderSide":    "BUY",
                "orderType":    "MARKET",
                "origQty":      "1",
                "positionSide": "SHORT",
            },
        ]

        params = {
            "list": data,
        }
        res = signedFutureHttpAPI.batch_order(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_order_detail(self):
        """ """

        params = {
            "orderId": 224672020489736640,
        }
        res = signedFutureHttpAPI.get_order_detail(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_order_list(self):
        """ """
        res = signedFutureHttpAPI.get_order_list()

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_cancel_order(self):
        """ """
        params = {
            "orderId": 224672020489736640,
        }
        res = signedFutureHttpAPI.cancel_order(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_cancel_order_all(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = signedFutureHttpAPI.cancel_order_all(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_create_entrust_plan(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = signedFutureHttpAPI.create_entrust_plan(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_cancel_entrust_plan(self):
        """ """
        params = {
            "entrustId": "xxxxx",
        }
        res = signedFutureHttpAPI.cancel_entrust_plan(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_entrust_plan_list(self):
        """ """
        params = {
            "symbol": "xxxxx",
        }
        res = signedFutureHttpAPI.get_entrust_plan_list(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_entrust_plan_detail(self):
        """ """
        params = {
            "entrustId": "xxxxx",
        }
        res = signedFutureHttpAPI.get_entrust_plan_detail(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_entrust_history_list(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = signedFutureHttpAPI.get_entrust_history_list(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_create_entrust_profit(self):
        """ """
        params = {
            "symbol": "btc_usdt",
            "origQty": "",
            "triggerProfitPrice": "",
            "triggerStopPrice": "",
            "expireTime": "",
            "positionSide": "",
        }
        res = signedFutureHttpAPI.create_entrust_profit(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_cancel_entrust_profit_stop(self):
        """ """
        params = {
            "profitId": "xxxxx",
        }
        res = signedFutureHttpAPI.cancel_entrust_profit_stop(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_cancel_entrust_profit_stop_all(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = signedFutureHttpAPI.cancel_entrust_profit_stop_all(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_entrust_profit_stop_all(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = signedFutureHttpAPI.get_entrust_profit_stop_all(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_get_entrust_profit_detail(self):
        """ """
        params = {
            "profitId": "xxxxx",
        }
        res = signedFutureHttpAPI.get_entrust_profit_detail(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)

    @unittest.skip
    def test_update_entrust_profit_stop(self):
        """ """
        params = {
            "profitId": "xxxxx",
        }
        res = signedFutureHttpAPI.update_entrust_profit_stop(params)

        print(res.status, res.json)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)


if __name__ == "__main__":
    unittest.main()
    pass
