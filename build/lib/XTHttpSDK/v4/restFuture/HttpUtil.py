# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2022/9/15
@Remark: 
"""
import time
import hmac
import requests
import logging
import hashlib
import json
import urllib.parse
from collections import OrderedDict, namedtuple
from urllib.parse import urlparse
from XTHttpSDK.v4.restSpot.HttpConstant import *


__all__ = ["get_auth_payload", "request", "PayloadObj"]

# Logger
logger = logging.Logger(__file__)
# response
ResponseObj = namedtuple("ResponseObj", ["status", "response", "json"])
# PayloadObj
PayloadObj = namedtuple("PayloadObj", ["data", "uri", "method"])


def create_signed(params: str, secretKey: str) -> str:
    """ """
    signature = hmac.new(secretKey.encode(
        'utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest().upper()
    return signature


class Auth:
    """Create auth signed  """

    def __init__(self, apiKey, secretKey):
        """ """
        self._apiKey: str = apiKey
        self._secretKey: str = secretKey

    def create_header(self):
        """ """
        header = OrderedDict()
        header["xt-validate-algorithms"] = XT_VALIDATE_ALGORITHMS
        header["xt-validate-appkey"] = self._apiKey
        header["xt-validate-recvwindow"] = XT_VALIDATE_RECVWINDOW
        header["xt-validate-timestamp"] = str(int(time.time() * 1000) + 1000)
        return header

    def create_payload(self, payload: PayloadObj) -> dict:
        """ """

        # Need sorted
        header = self.create_header()
        X = urllib.parse.urlencode(
            dict(sorted(header.items(), key=lambda kv: (kv[0], kv[1]))))
        path = urlparse(payload.uri).path
        decode, tmp = XT_VALIDATE_CONTENTTYPE_JSON, None

        if payload.data.pop("urlencoded", False):
            tmp = urllib.parse.urlencode(
                dict(sorted(payload.data.items(), key=lambda kv: (kv[0], kv[1]))), safe=",")
            decode = XT_VALIDATE_CONTENTTYPE_URLENCODE

        if not payload.data:
            param = None
            Y = "#{}".format(path)
        else:
            param = json.dumps(payload.data)
            Y = "#{}#{}".format(path, tmp or param)
            param = payload.data

        signature = create_signed(X + Y, self._secretKey)
        header["xt-validate-signature"] = signature
        header["Content-Type"] = decode

        return header, param


def get_auth_payload(payload) -> dict:
    """ return payload contains request params"""
    if not payload.data.keys() & {"accesskey", "secretkey"}:
        return [None] * 2
    PUBLIC_KEY, SECRET_KEY = payload.data.pop(
        "accesskey"), payload.data.pop("secretkey")
    auth = Auth(PUBLIC_KEY, SECRET_KEY)
    return auth.create_payload(payload)


def _request(method, url, **kwargs):
    """ """
    try:
        # proxy = {"http": "127.0.0.1:7890", "https": "127.0.0.1:7890"}
        # kwargs.setdefault("proxies", proxy)
        response = requests.request(method, url, **kwargs)
        # response = requests.request(method, url, verify=False, **kwargs)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        msg = 'Content:{t}........'.format(t=e)
        logger.info(msg)  # NOQA
        return ResponseObj(False, None, msg)

    if response.status_code == 200 and response:
        try:
            data = response.json()
        except Exception:
            msg = "Expecting value: line 1 column 1 (char 0)"
            return ResponseObj(False, None, msg)
        return ResponseObj(True, response, data)
    else:
        return ResponseObj(False, response, response.text)


# ResponseObj
def request(method, url, *, auth=False, **kwargs):
    """ """
    return _request(method, url, **kwargs)
