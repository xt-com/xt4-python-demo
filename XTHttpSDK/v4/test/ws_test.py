# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2022/9/15
@Remark: 
"""
import time
import unittest
import sys
import os
file_exec_path = os.path.dirname(os.path.dirname(__file__))
restSpotPath = os.path.join(file_exec_path, "wsSpot")
sys.path.insert(0, file_exec_path)
sys.path.insert(0, restSpotPath)
from wsSpot.WSAPI import *  # NOQA


def callback(ws, message):
    print("[ws-callback]::: ", message)


publicWs = PublicWebSocket(callback=callback)

#
accesskey = "xxxxxxxxxxxxxxxxxx"
secretkey = "uuuuuuuuuuuuuuuuuu"
privateWs = PrivateWebsocket(
    accesskey=accesskey,
    secretkey=secretkey,
    callback=callback
)


class XT4WSTest(unittest.TestCase):
    """ """
    @unittest.skip
    def test_ping(self):
        """ """
        publicWs.start()
        while 1:
            time.sleep(1)
            publicWs.ping()

    @unittest.skip
    def test_on_trade(self):
        """ """
        cancel_count = 0

        topic = {
            "params": ["trade@btc_usdt"],
            "id": 1,
        }
        publicWs.start()
        publicWs.subscribe(topic)

        while 1:
            time.sleep(1)
            publicWs.ping()
            cancel_count += 1
            if cancel_count > 10:
                break
            print("[cancel_count] ", cancel_count)

        publicWs.unsubscribe(topic)

        # #########################################

        topic = {
            "params": ["trade@btc_usdt"],
        }
        publicWs.start()
        publicWs.subscribe(topic)

        while 1:
            time.sleep(1)
            publicWs.ping()

    @unittest.skip
    def test_on_kline(self):
        """ """
        topic = {
            "params": ["kline@btc_usdt,5m"],
            "id": 1,
        }
        publicWs.start()
        publicWs.subscribe(topic)

        while 1:
            time.sleep(1)
            publicWs.ping()

    @unittest.skip
    def test_on_depth(self):
        """ """
        topic = {
            "params": ["depth@btc_usdt,20"],
            "id": 1,
        }
        publicWs.start()
        publicWs.subscribe(topic)

        while 1:
            time.sleep(1)
            publicWs.ping()

    @unittest.skip
    def test_on_depth_update(self):
        """ """
        topic = {
            "params": ["depth_update@btc_usdt"],
            "id": 1,
        }
        publicWs.start()
        publicWs.subscribe(topic)

        while 1:
            time.sleep(1)
            publicWs.ping()

    @unittest.skip
    def test_on_ticker(self):
        """ """
        topic = {
            "params": ["ticker@btc_usdt"],
            "id": 1,
        }
        publicWs.start()
        publicWs.subscribe(topic)

        while 1:
            time.sleep(1)
            publicWs.ping()

    @unittest.skip
    def test_on_tickers(self):
        """ """
        topic = {
            "params": ["tickers"],
            "id": 1,
        }
        publicWs.start()
        publicWs.subscribe(topic)

        while 1:
            time.sleep(1)
            publicWs.ping()

# ################################################################################
# Ws-User
# ################################################################################
    @unittest.skip
    def test_on_user_balance(self):
        """ """
        topic = {
            "params": ["balance"],
            "id": 1,
        }
        privateWs.start()
        privateWs.subscribe(topic)

        while 1:
            time.sleep(1)
            privateWs.ping()

    @unittest.skip
    def test_on_user_order(self):
        """ """
        topic = {
            "params": ["order"],
            "id": 1,
        }
        privateWs.start()
        privateWs.subscribe(topic)

        while 1:
            time.sleep(1)
            privateWs.ping()

    @unittest.skip
    def test_on_user_trade(self):
        """ """
        topic = {
            "params": ["trade"],
            "id": 1,
        }
        privateWs.start()
        privateWs.subscribe(topic)

        while 1:
            time.sleep(1)
            privateWs.ping()


if __name__ == "__main__":
    unittest.main()
    pass
