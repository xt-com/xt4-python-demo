# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2022/9/15
@Remark:
"""
from XTHttpSDK.v4.restFuture.HttpCFG import *
from XTHttpSDK.v4.restFuture.HttpUtil import *

__all__ = ["PublicFutureHttpAPI",
           "SignedFutureHttpAPI", "SignedFutureProfitHttpAPI"]


class HttpAPI(object):
    """ """

    def __init__(self, domain=None) -> None:

        self._domain = domain or BASE_URI

    def url(self, uri):
        """ """
        return self._domain + uri

    def get_datas(self, param: dict = None):
        """ """
        data = {
            "accesskey": self._accesskey,
            "secretkey": self._secretkey
        }
        if param and isinstance(param, dict):
            data.update(**param)
        return data


class PublicFutureHttpAPI(HttpAPI):
    """ No signature required """

    def get_coins_info(self):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_COINS_URI))

    def get_symbol_detail(self,  params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_MARKETCONFIG_URI), params=params)

    def get_marketconfig_list(self):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_MARKETCONFIG_LIST_URI))

    def get_leverage_bracket_detail(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_LEVERAGE_BRACKET_DETAIL_URI), params=params)

    def get_leverage_bracket_list(self):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_LEVERAGE_BRACKET_LIST_URI))

    def get_ticker(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_TICKER_URI), params=params)

    def get_tickers(self):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_TICKERS_URI))

    def get_deal(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_DEAL_URI), params=params)

    def get_depth(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_DEPTH_URI), params=params)

    def get_symbol_index_price(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_INDEX_PRICE_URI), params=params)

    def get_all_index_price(self):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_ALL_INDEX_PRICE_URI))

    def get_symbol_market_price(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_MARKET_PRICE_URI), params=params)

    def get_all_market_price(self):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_ALL_MARKET_PRICE_URI))

    def get_kline(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_KLINE_URI), params=params)

    def get_agg_ticker(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_AGG_TICKER_URI), params=params)

    def get_agg_tickers(self):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_AGG_TICKERS_URI))

    def get_funding_rate(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_FUNDING_RATE_URI), params=params)

    def get_funding_rate_racord(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_FUNDING_RATE_RECORD_URI), params=params)

    def get_risk_balance(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_RISK_BALANCE_URI), params=params)

    def get_open_interest(self, params: dict):
        """ """
        return request("GET", self.url(XT4PlatFutureURI.GET_OPEN_INTEREST_URI), params=params)


class SignedFutureHttpAPI(PublicFutureHttpAPI):
    """ Signature required """

    def __init__(self, accesskey: str, secretkey: str, domain: str = None) -> None:
        """ """
        super().__init__(domain=domain)
        self._accesskey = accesskey
        self._secretkey = secretkey

    def get_account_info(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_ACCOUNT_INFO_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_listenkey(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_USER_LISTENKEY_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def open_account(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_ACCOUNT_OPEN_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_balance_detail(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_BALANCE_DETAIL_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_balance_list(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_BALANCE_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_balance_bills(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_BALANCE_BILLS_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_funding_rate_list(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_BALANCE_FUNDING_RATE_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_position_list(self, data: dict = None):
        """  """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_POSITION_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def position_adjust_leverage(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_POSITION_ADJUST_LEVERAGE_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def position_margin(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_POSITION_MARGIN_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def position_auto_margin(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_POSITION_AUTO_MARGIN_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def position_close_all(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_POSITION_CLOSE_ALL_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_position_adl(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_POSITION_ADL_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def add_collection(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_USER_COLLECTIONS_ADD_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def cancel_collection(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_USER_COLLECTIONS_CANCEL_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_collection_list(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_USER_COLLECTION_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_collection_list(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_USER_COLLECTION_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def position_change_type(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.POST_POSITION_CHANGE_TYPE_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)


class SignedFutureProfitHttpAPI(SignedFutureHttpAPI):
    """ Signature required """

    def order_create(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_ORDER_CREATE_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, json=data)

    def get_order_history_list(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_ORDER_HISTORY_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_trade_list(self,  data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_TRADE_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def batch_order(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_BATCH_ORDER_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, json=data)

    def get_order_detail(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_ORDER_DETAIL_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_order_list(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatFutureURI.GET_ORDER_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def cancel_order(self, data: dict = None):
        """  """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_ORDER_CANCEL_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def cancel_order_all(self, data: dict = None):
        """  """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_ALL_ORDER_CANCEL_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def create_entrust_plan(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_ENTRUST_CREATE_PLAN_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def cancel_entrust_plan(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_ENTRUST_CANCEL_PLAN_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def cancel_entrust_all_plan(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_ENTRUST_CANCEL_PLAN_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_entrust_plan_list(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(
            XT4PlatFutureURI.GET_ENTRUST_PLAN_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_entrust_plan_detail(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(
            XT4PlatFutureURI.GET_ENTRUST_PLAN_DETAIL_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_entrust_history_list(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(
            XT4PlatFutureURI.GET_ENTRUST_PLAN_HISTORY_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def create_entrust_profit(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_ENTRUST_CREATE_PROFIT_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def cancel_entrust_profit_stop(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatFutureURI.POST_ENTRUST_CANCEL_PROFIT_STOP_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def cancel_entrust_profit_stop_all(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(
            XT4PlatFutureURI.POST_ALL_ENTRUST_CANCEL_PROFIT_STOP_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_entrust_profit_stop_all(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(
            XT4PlatFutureURI.GET_ENTRUST_PLAN_HISTORY_LIST_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def get_entrust_profit_detail(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(
            XT4PlatFutureURI.GET_ENTRUST_PROFIT_DETAIL_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)

    def update_entrust_profit_stop(self, data: dict = None):
        """ """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(
            XT4PlatFutureURI.POST_ENTRUST_UPDATE_PROFIT_STOP_URI)

        headers, data = get_auth_payload(
            PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers, params=data)
