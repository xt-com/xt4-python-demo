# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2022/9/15
@Remark: 
"""


# Domain
BASE_URI = "http://sapi.xt-qa.com"


class XT4PlatConfig(object):
    """ """

    # Get currency information
    GET_COINS_INFO = "/v4/public/currencies"

    # Get timestamp from server
    GET_SERVER = '/v4/public/time'

    # Get trade account type
    GET_ACCOUNT = '/trade/api/v1/getAccounts'

    # Get trade config from market
    GET_MARKET_CONFIG = '/v4/public/symbol'

    # Get Kline
    GET_KLINE = '/v4/public/kline'

    # Get latest prices ticker
    GET_TICKER = "/v4/public/ticker/price"

    # Access to 24 hours of trading
    GET_FULL_TICKER = '/v4/public/ticker/full'

    # Obtain all trading quotations within 24 hours
    GET_TICKERS = '/v4/public/ticker/24h'

    # Get the best pending order ticker
    GET_BEST_TICKER = "/v4/public/ticker/book"

    # Get 24h statistics ticker
    GET_24H_TICKER = "/v4/public/ticker/24h"

    # Get the latest trading depth
    GET_DEPTH = '/v4/public/depth'

    # Get the latest transaction data
    GET_TRADES = '/v4/public/trade/recent'

    # Get balance of account
    GET_BALANCE = '/v4/balances'

    # Gets the specified account assets
    GET_FUNDS = '/v4/balances'

    # Place a order and Commissioned order
    SEND_ORDER = '/v4/order'

    # Batch order
    BATCH_ORDER = '/v4/batch-order'

    # Cancel order
    CANCEL_ORDER = '/v4/order'

    # Batch cancel
    BATCH_CANCEL = '/v4/batch-order'

    # OrderLine
    GET_ORDER = '/v4/order'

    # Obtain outstanding orders
    GET_OPEN_ORDERS = '/v4/open-order'

    # Cancell batch order
    DELETE_OPEN_ORDERS = "/v4/open-order"  # 1

    #
    GET_ACCOUNT_HISTORY_ORDER = "/v4/history-order"  # 1

    # Get multiple order information
    GET_BATCH_ORDERS = '/v4/batch-order'

    # Get myTrades
    GET_ACCOUNT_TRADES = "/v4/trade"

    # Get ListenKey
    GET_ACCOUNT_LISTENKEY = "/v4/ws-token"
