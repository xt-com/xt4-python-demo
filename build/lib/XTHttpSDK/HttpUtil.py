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
import base64
import urllib.parse
from functools import wraps
from typing import Dict
from collections import OrderedDict, namedtuple
from urllib.parse import urlparse
from HttpConstant import *


__all__ = ["get_auth_payload", "request"]

# Logger
logger = logging.Logger(__file__)
# response
ResponseObj = namedtuple("ResponseObj", ["status", "response", "json"])


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
        header["xt-validate-timestamp"] = str(int(time.time() * 1000))
        return header

    def create_payload(self, payload: dict, uri) -> dict:
        """ """

        # Need sorted
        header = self.create_header()
        X = urllib.parse.urlencode(
            dict(sorted(header.items(), key=lambda kv: (kv[0], kv[1]))))
        path = urlparse(uri).path
        decode, tmp = XT_VALIDATE_CONTENTTYPE_JSON, None

        if payload.pop("urlencoded", False):
            tmp = urllib.parse.urlencode(
                dict(sorted(payload.items(), key=lambda kv: (kv[0], kv[1]))))
            decode = XT_VALIDATE_CONTENTTYPE_URLENCODE

        if not payload:
            param = None
            Y = "#{}".format(path)
        else:
            param = json.dumps(payload)
            Y = "#{}#{}".format(path, tmp or param)
            param = payload

        signature = create_signed(X + Y, self._secretKey)
        header["xt-validate-signature"] = signature
        header["Content-Type"] = decode

        print("[XY] ", X + Y)
        print("[headers] ", header)
        return header, param


def get_auth_payload(param: dict, uri) -> dict:
    """ return payload contains request params"""
    if not param.keys() & {"accesskey", "secretkey"}:
        return [None] * 2
    PUBLIC_KEY, SECRET_KEY = param.pop("accesskey"), param.pop("secretkey")
    auth = Auth(PUBLIC_KEY, SECRET_KEY)
    return auth.create_payload(param, uri)


def _request(method, url, **kwargs):
    """ """
    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        msg = 'Request timeout, content:{t}]........'.format(t=e.response.text)
        logger.info(msg)  # NOQA
        return ResponseObj(False, None, msg)

    if response.status_code == 200 and response:
        # self.timer_active = False
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
    if not auth:
        return _request(method, url, **kwargs)
    return _request(method, url, **kwargs)
