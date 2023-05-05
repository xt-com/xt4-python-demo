# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2022/9/15
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
from restSpot.HttpAPI import *  # NOQA


# publicAPI
publicAPI = PublicHttpAPI()

accesskey = "xxxxxxxxxxxxxxxxxxxx"
sercetkey = "yyyyyyyyyyyyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)


class XT4HttpTest(unittest.TestCase):
    """ """

    @unittest.skip
    def test_get_server_time(self):
        """ """
        res = publicAPI.get_server_time()

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_market_config(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_market_config(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

        # ##############################################

        params = {
            "symbols": ["BTC_USDT", "ETH_USDT"],
        }
        res = publicAPI.get_market_config(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_depth(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_depth(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

        # ##############################################

        params = {
            "symbol": "btc_usdt",
            "limit": 10,
        }
        res = publicAPI.get_depth(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json)

    @unittest.skip
    def test_get_kline(self):
        """ """
        params = {
            "symbol": "btc_usdt",
            "interval": "1m",
        }
        res = publicAPI.get_kline(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json, "\n")

        # ##############################################

        params = {
            "symbol": "btc_usdt",
            "interval": "1m",
            "limit": 10,
        }
        res = publicAPI.get_kline(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json, "\n")

    @unittest.skip
    def test_get_trades(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_trades(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json, "\n")

        # ##############################################

        params = {
            "symbol": "btc_usdt",
            "limit": 10,
        }
        res = publicAPI.get_trades(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json, "\n")

    @unittest.skip
    def test_get_ticker(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json, "\n")

        # ##############################################

        params = {
            # "symbol": "btc_usdt",
            "symbols": ["BTC_USDT", "ETH_USDT"],
        }
        res = publicAPI.get_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print(res.status, res.json, "\n")

    @unittest.skip
    def test_get_full_ticker(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_full_ticker]-1", res.status, res.json, "\n")

        # ##############################################

        params = {
            "symbol": "btc_usdt",
            "symbols": ["BTC_USDT", "ETH_USDT"],
        }
        res = publicAPI.get_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_full_ticker]-2", res.status, res.json, "\n")

    @unittest.skip
    def test_get_best_ticker(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_best_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_best_ticker]-1", res.status, res.json, "\n")

        # ##############################################

        params = {
            "symbol": "btc_usdt",
            "symbols": ["BTC_USDT", "ETH_USDT"],
        }
        res = publicAPI.get_best_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_best_ticker]-2", res.status, res.json, "\n")

    @unittest.skip
    def test_get_24h_ticker(self):
        """ """
        params = {
            "symbol": "btc_usdt",
        }
        res = publicAPI.get_24h_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_24h_ticker]-1", res.status, res.json, "\n")

        # ##############################################

        params = {
            "symbol": "btc_usdt",
            "symbols": ["BTC_USDT", "ETH_USDT"],
        }
        res = publicAPI.get_24h_ticker(params)

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_24h_ticker]-2", res.status, res.json, "\n")

    @unittest.skip
    def test_get_coins_info(self):
        """ """
        res = publicAPI.get_coins_info()

        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_24h_ticker]-1", res.status, res.json, "\n")

# ####################################################################################################
#                   SignedHttpAPI-TEST
# ####################################################################################################

    @unittest.skip
    def test_get_order(self):
        """ """
        # 140541834558153984

        orderId = {
            "orderId": 140541112005403904
        }

        res = signedHttpAPI.get_order(orderId)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_order]-1", res.status, res.json, "\n")

    @unittest.skip
    def test_get_order_list(self):
        """ """
        # 140537740057617664
        orderId = {
            "orderId": 140541112005403904
        }
        res = signedHttpAPI.get_order_list(orderId)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_order_list]-1", res.status, res.json, "\n")
        pass

        # ##############################################

    # @unittest.skip
    def test_send_order(self):
        """ """
        data = {
            "symbol": "btc_usdt",
            "side": "BUY",
            "type": "LIMIT",
            "timeInForce": "GTC",
            "bizType": "SPOT",
            "price": "29011",
            "quantity": "0.1",
        }
        res = signedHttpAPI.send_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_send_order]-1", res.status, res.json, "\n")

        # ##############################################

        data = {
            "symbol": "btc_usdt",
            "side": "BUY",
            "type": "MARKET",
            "timeInForce": "IOC",
            "bizType": "SPOT",
            "quoteQty": "1",
        }
        res = signedHttpAPI.send_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_send_order]-1", res.status, res.json, "\n")

    @unittest.skip
    def test_cancel_order(self):
        """ """
        orderId = 142328296097341376
        # orderId = {
        #     "orderId": 140541112005403904
        # }

        res = signedHttpAPI.cancel_order(orderId)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_order]-1", res.status, res.json, "\n")

    @unittest.skip
    def test_batch_order(self):
        """ """
        data = {
            "orderIds": "139865641251887680"
        }

        res = signedHttpAPI.get_batch_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_batch_order]-1", res.status, res.json, "\n")
        pass

    @unittest.skip
    def test_send_batch_order(self):
        """ """
        order = [
            {"symbol": "btc_usdt", "price": "19000", "quantity": "0.001",
                "side": "BUY", "type": "LIMIT", "timeInForce": "GTC", "bizType": "SPOT"},
            {"symbol": "btc_usdt", "price": "19001", "quantity": "0.001",
                "side": "BUY", "type": "LIMIT", "timeInForce": "GTC", "bizType": "SPOT"},
        ]

        data = {
            "items": order
        }

        res = signedHttpAPI.send_batch_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_send_batch_order]-1", res.status, res.json, "\n")

        # ##############################################

        order = [
            {"symbol": "btc_usdt",  "quoteQty": "1", "side": "BUY",
                "type": "MARKET", "timeInForce": "IOC", "bizType": "SPOT"},
            {"symbol": "btc_usdt",  "quoteQty": "1", "side": "BUY",
                "type": "MARKET", "timeInForce": "IOC", "bizType": "SPOT"},
        ]

        data = {
            "items": order
        }

        res = signedHttpAPI.send_batch_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_send_batch_order]-2", res.status, res.json, "\n")

# 140600606177600768
# 140600606173406464

    @unittest.skip
    def test_batch_cancel_order(self):
        """ """
        data = {
            "orderIds": ["140600606177600768"]
        }

        res = signedHttpAPI.batch_cancel_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_batch_cancel_order]-1", res.status, res.json, "\n")

    @unittest.skip
    def test_get_open_order(self):
        """ """
        data = {
            "symbol": "btc_usdt"
        }

        res = signedHttpAPI.get_open_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_open_order]-1", res.status, res.json, "\n")

        # ##############################################

        data = {
            "symbol": "btc_usdt",
            "bizType": "SPOT",
            "side": "BUY",
        }

        res = signedHttpAPI.get_open_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_open_order]-2", res.status, res.json, "\n")

    @unittest.skip
    def test_cancel_open_order(self):
        """ """
        data = {
            "symbol": "btc_usdt"
        }

        res = signedHttpAPI.cancel_open_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_cancel_open_order]-1", res.status, res.json, "\n")

        # ##############################################

        data = {
            "symbol": "btc_usdt",
            "bizType": "SPOT",
            "side": "BUY",
        }

        res = signedHttpAPI.cancel_open_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_cancel_open_order]-2", res.status, res.json, "\n")

    @unittest.skip
    def test_get_history_order(self):
        """ """
        data = {
            "symbol": "btc_usdt"
        }

        res = signedHttpAPI.get_history_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_history_order]-1", res.status, res.json, "\n")

        # ##############################################

        data = {
            "symbol": "btc_usdt",
            "bizType": "SPOT",
            "side": "BUY",
        }

        res = signedHttpAPI.get_history_order(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_history_order]-2", res.status, res.json, "\n")

    @unittest.skip
    def test_get_trade(self):
        """ """
        data = {
            "symbol": "btc_usdt"
        }

        res = signedHttpAPI.get_trade(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_trade]-1", res.status, res.json, "\n")

        # ##############################################

        data = {
            "symbol": "btc_usdt",
            "bizType": "SPOT",
            "side": "BUY",
        }

        res = signedHttpAPI.get_trade(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_trade]-2", res.status, res.json, "\n")

    @unittest.skip
    def test_get_balance(self):
        """ """
        data = {
            # "currency": "usdt"
        }

        res = signedHttpAPI.get_balance(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_balance]-1", res.status,
              res.json, res.response.url, "\n")

    @unittest.skip
    def test_get_funds(self):
        """ """
        data = {
            "currencies": "btc"
        }

        res = signedHttpAPI.get_funds(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_funds]-1", res.status, res.json, "\n")

        # ##############################################
        # TODO 不支持EG的传参类型
        data = {
            "currencies": "btc,usdt"
        }

        res = signedHttpAPI.get_funds(data)
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_funds]-2", res.status, res.json, "\n")

    @unittest.skip
    def test_get_listenkey(self):
        """ """
        # TODO
        res = signedHttpAPI.get_listenKey()
        self.assertEqual(res.status, True)
        self.assertIsInstance(res.json, dict)
        print("[test_get_funds]-1", res.status, res.json, "\n")


if __name__ == "__main__":
    unittest.main()
    pass

# `{"data":[{"exchange":"XT","accesskey":"67783be7-b4ab-4ffc-ae3f-3268acc04c93","secretkey":"0e16ad37592d894b75ad83aa01496a709a36475a","data":{"symbol":"btc_usdt","side":"BUY","type":"LIMIT","timeInForce":"GTC","bizType":"SPOT","price":"18570","quantity":"0.1"}},{"exchange":"Binance"}]}`
# {
#     "code": 0,
#     "msg": "OK",
#     "data": {
#         "BINANCE": {
#             "data": null,
#             "msg": "Chain request for entitlement not found",
#             "name": "BINANCE",
#             "origin": null,
#             "path": "",
#             "service": "",
#             "status": false
#         },
#         "XT": {
#             "data": {
#                 "orderId": "145355615524282048"
#             },
#             "msg": "Success",
#             "name": "XT",
#             "origin": {
#                 "ma": [],
#                 "mc": "SUCCESS",
#                 "rc": 0,
#                 "result": {
#                     "orderId": "145355615524282048"
#                 }
#             },
#             "path": "http://sapi.xt-uat.com/v4/order",
#             "service": "Gateway.XTSPOT",
#             "status": true
#         }
#     }
# }
