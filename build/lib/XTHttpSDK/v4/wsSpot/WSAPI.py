# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2022/9/16
@Remark: 
"""

# pip install websocket-client
import json
import websocket
import logging
from functools import partial
from typing import Any, Callable
from threading import Thread, Event
from XTHttpSDK.v4.wsSpot.WSCFG import *
from XTHttpSDK.v4.restSpot.HttpAPI import SignedHttpAPI

# Logger
logger = logging.Logger(__file__)
# Trace
websocket.enableTrace(False)


class _WebsocketHelper:
    """ """

    def __init__(self, conn=None, callback=None) -> None:
        """ """
        self.conn = conn(
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self._event = Event()
        self._t = Thread(target=self._run, daemon=True, name="WebsocketHelper")
        self._handle = callback

    def on_event(self, topic):
        """ """
        self._event.wait()
        self.conn.send(json.dumps(topic))

    def on_open(self, ws):
        """ """
        logger.debug("Opened connection")
        self._event.set()

    def on_close(self, close_status_code, close_msg, close_status):
        """ """
        print(close_status_code, close_msg, close_status)
        logger.debug("### closed ###")

    def on_error(self, ws, error):
        """ """
        logger.error(error)

    def on_message(self, ws, message):
        if self._handle:
            self._handle(ws, message)

    def ping(self):
        """ """
        self.conn.send("ping")

    def _run(self):
        """ """
        self.conn.run_forever()

    def start(self):
        """ """
        self._t.start()


class PublicWebSocket(_WebsocketHelper):
    """ """

    def __init__(self, *,
                 uri=None,
                 callback: Callable[[websocket.WebSocketApp, str], Any] = None) -> None:

        uri = uri or XT4PlatWSConfig.BASE_URI
        self.ws = partial(websocket.WebSocketApp, uri)
        super().__init__(self.ws, callback=callback)

    def subscribe(self, topic: dict):
        """ """
        topic["method"] = "subscribe"
        self.on_event(topic)

    def unsubscribe(self, topic: dict):
        """ """
        topic["method"] = "unsubscribe"
        self.on_event(topic)


class PrivateWebsocket(_WebsocketHelper):
    """ """

    def __init__(self, *,
                 accesskey,
                 secretkey,
                 uri=None,
                 callback: Callable[[websocket.WebSocketApp, str], Any] = None) -> None:

        self._accesskey = accesskey
        self._secretkey = secretkey
        uri = uri or XT4PlatWSUserConfig.BASE_URI
        self.ws = partial(websocket.WebSocketApp, uri)
        super().__init__(self.ws, callback=callback)
        self._active = False

    def renew_listenKey(self):
        """ """
        # TODO
        signedHttpAPI = SignedHttpAPI(self._accesskey, self._secretkey)
        resp = signedHttpAPI.get_listenKey()
        try:
            listenkey = resp.json["result"]["accessToken"]
        except KeyError:
            logger.error("Get listenkey failed")
            return None
        return listenkey

    def _resub(self, topic):
        """ """
        for _ in iter(lambda: self._active, False):
            topic["listenKey"] = self.renew_listenKey()
            self.on_event(topic)

    def subscribe(self, topic: dict):
        """ """
        topic["method"] = "subscribe"
        topic["listenKey"] = self.renew_listenKey()
        self._timer = Thread(target=self._resub, args=(topic,), daemon=True)
        self.on_event(topic)

    def unsubscribe(self, topic: dict):
        """ """
        topic["method"] = "unsubscribe"
        topic["listenKey"] = self.renew_listenKey()
        self.on_event(topic)
        self._active = False
        self._timer.join()

    def start(self):
        """ """
        self._active = True
        super().start()
