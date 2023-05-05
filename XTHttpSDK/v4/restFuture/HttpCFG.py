# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2022/9/15
@Remark: 
"""


# Domain
# Default: USDT-M
BASE_URI = "https://fapi.xt.com"

# https://fapi.xt.com/future/market/v1/public/time

# uri


class XT4PlatFutureURI:
    """ """

    GET_COINS_URI = "/future/market/v1/public/symbol/coins"
    GET_MARKETCONFIG_URI = "/future/market/v1/public/symbol/detail"
    GET_MARKETCONFIG_LIST_URI = "/future/market/v1/public/symbol/list"
    GET_LEVERAGE_BRACKET_DETAIL_URI = "/future/market/v1/public/leverage/bracket/detail"
    GET_LEVERAGE_BRACKET_LIST_URI = "/future/market/v1/public/leverage/bracket/list"
    GET_TICKER_URI = "/future/market/v1/public/q/ticker"
    GET_TICKERS_URI = "/future/market/v1/public/q/tickers"
    GET_DEAL_URI = "/future/market/v1/public/q/deal"
    GET_DEPTH_URI = "/future/market/v1/public/q/depth"
    GET_INDEX_PRICE_URI = "/future/market/v1/public/q/symbol-index-price"
    GET_ALL_INDEX_PRICE_URI = "/future/market/v1/public/q/index-price"
    GET_MARKET_PRICE_URI = "/future/market/v1/public/q/symbol-mark-price"
    GET_ALL_MARKET_PRICE_URI = "/future/market/v1/public/q/mark-price"
    GET_KLINE_URI = "/future/market/v1/public/q/kline"
    GET_AGG_TICKER_URI = "/future/market/v1/public/q/agg-ticker"
    GET_AGG_TICKERS_URI = "/future/market/v1/public/q/agg-tickers"
    GET_FUNDING_RATE_URI = "/future/market/v1/public/q/funding-rate"
    GET_FUNDING_RATE_RECORD_URI = "/future/market/v1/public/q/funding-rate-record"
    GET_RISK_BALANCE_URI = "/future/market/v1/public/contract/risk-balance"
    GET_OPEN_INTEREST_URI = "/future/market/v1/public/contract/open-interest"

    POST_ORDER_CREATE_URI = "/future/trade/v1/order/create"
    GET_ORDER_HISTORY_LIST_URI = "/future/trade/v1/order/list-history"
    GET_TRADE_LIST_URI = "/future/trade/v1/order/trade-list"
    POST_BATCH_ORDER_URI = "/future/trade/v1/order/create-batch"
    GET_ORDER_DETAIL_URI = "/future/trade/v1/order/detail"
    GET_ORDER_LIST_URI = "/future/trade/v1/order/list"
    POST_ORDER_CANCEL_URI = "/future/trade/v1/order/cancel"
    POST_ALL_ORDER_CANCEL_URI = "/future/trade/v1/order/cancel-all"

    POST_ENTRUST_CREATE_PLAN_URI = "/future/trade/v1/entrust/create-plan"
    POST_ENTRUST_CANCEL_PLAN_URI = "/future/trade/v1/entrust/cancel-plan"
    POST_ALL_ENTRUST_CANCEL_PLAN_URI = "/future/trade/v1/entrust/cancel-all-plan"
    GET_ENTRUST_PLAN_LIST_URI = "/future/trade/v1/entrust/plan-list"
    GET_ENTRUST_PLAN_DETAIL_URI = "/future/trade/v1/entrust/plan-detail"
    GET_ENTRUST_PLAN_HISTORY_LIST_URI = "/future/trade/v1/entrust/plan-list-history"
    POST_ENTRUST_CREATE_PROFIT_URI = "/future/trade/v1/entrust/create-profit"
    POST_ENTRUST_CANCEL_PROFIT_STOP_URI = "/future/trade/v1/entrust/cancel-profit-stop"
    POST_ALL_ENTRUST_CANCEL_PROFIT_STOP_URI = "/future/trade/v1/entrust/cancel-all-profit-stop"
    GET_ENTRUST_PROFIT_LIST_URI = "/future/trade/v1/entrust/profit-list"
    GET_ENTRUST_PROFIT_DETAIL_URI = "/future/trade/v1/entrust/profit-detail"
    POST_ENTRUST_UPDATE_PROFIT_STOP_URI = "/future/trade/v1/entrust/update-profit-stop"

    GET_ACCOUNT_INFO_URI = "/future/user/v1/account/info"
    GET_USER_LISTENKEY_URI = "/future/user/v1/user/listen-key"
    POST_ACCOUNT_OPEN_URI = "/future/user/v1/account/open"
    GET_BALANCE_DETAIL_URI = "/future/user/v1/balance/detail"
    GET_BALANCE_LIST_URI = "/future/user/v1/balance/list"
    GET_BALANCE_BILLS_URI = "/future/user/v1/balance/bills"
    GET_BALANCE_FUNDING_RATE_LIST_URI = "/future/user/v1/balance/funding-rate-list"
    GET_POSITION_LIST_URI = "/future/user/v1/position/list"
    POST_POSITION_ADJUST_LEVERAGE_URI = "/future/user/v1/position/adjust-leverage"
    POST_POSITION_MARGIN_URI = "/future/user/v1/position/margin"
    POST_POSITION_AUTO_MARGIN_URI = "/future/user/v1/position/auto-margin"
    POST_POSITION_CLOSE_ALL_URI = "/future/user/v1/position/close-all"
    GET_POSITION_ADL_URI = "/future/user/v1/position/adl"
    POST_USER_COLLECTIONS_ADD_URI = "/future/user/v1/user/collection/add"
    POST_USER_COLLECTIONS_CANCEL_URI = "/future/user/v1/user/collection/cancel"
    GET_USER_COLLECTION_LIST_URI = "/future/user/v1/user/collection/list"
    POST_POSITION_CHANGE_TYPE_URI = "/future/user/v1/position/change-type"
