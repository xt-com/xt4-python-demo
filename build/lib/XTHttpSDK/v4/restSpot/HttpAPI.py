# -*- coding:utf8 -*-
"""
@author: Laowang
@contact: QQ:1125564921
@Created on: 2022/9/15
@Remark:
"""
from XTHttpSDK.v4.restSpot.HttpCFG import *
from XTHttpSDK.v4.restSpot.HttpUtil import *

__all__ = ["PublicHttpAPI", "SignedHttpAPI"]


class PublicHttpAPI:
    """ """

    def __init__(self, domain=None) -> None:

        self._domain = domain or BASE_URI

    def url(self, uri):
        """ """
        return self._domain + uri

    def get_server_time(self):
        """
        @Param: None
        @Return
        {
            "rc": 0,
            "mc": "SUCCESS",
            "ma": [],
            "result": {
                "serverTime": 1662435658062  //服务器时间
            }
        }
        """

        return request("GET", self.url(XT4PlatConfig.GET_SERVER))

    def get_coins_info(self):
        """
        @Param: None
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": [
                    {
                    "id": 11,  //currency id
                    "currency": "usdt", //currency name
                    "fullName": "usdt",  //currency full name
                    "logo": null,   //currency logo
                    "cmcLink": null,  //cmc link
                    "weight": 100,
                    "maxPrecision": 6,
                    "depositStatus": 1,  //Recharge status(0 close 1 open)
                    "withdrawStatus": 1,  //Withdrawal status(0 close 1 open)
                    "convertEnabled": 1,  //Small asset exchange switch[0=close;1=open]
                    "transferEnabled": 1  //swipe switch[0=close;1=open]
                    }
                ]
            }
        """
        return request("GET", self.url(XT4PlatConfig.GET_COINS_INFO))

    def get_market_config(self, params: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : symbol	    string	    false		          	    trading pair eg:btc_usdt
            ::param : symbols	    string	    false		          	    Collection of trading pairs. Priority is higher than symbol. eg: btc_usdt,eth_usdt
            ::param : version	    string	    false		                Version number, when the request version number is consistent with the response content version, the list will not be returned, reducing IO eg: 2e14d2cd5czcb2c2af2c1db65078d075
        @Return
            See: https://xt-com.github.io/xt4-api/#market_cn2symbol
        """

        return request("GET", self.url(XT4PlatConfig.GET_MARKET_CONFIG), params = params)

    def get_depth(self, params: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description        Ranges
            ::param : symbol	    string	    true		          	    trading pair
            ::param : limit	        number	    false		 200                               1,1000
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": [
                    {
                    "i": 0,   //ID
                    "t": 0,   //transaction time
                    "p": "string", //transaction price
                    "q": "string",  //transaction quantity
                    "v": "string",  //transaction volume
                    "b": true   //buyerMaker
                    }
                ]
            }
        """
        return request("GET", self.url(XT4PlatConfig.GET_DEPTH), params = params)

    def get_kline(self, params: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : symbol	    string	    true		          	    trading pair eg:btc_usdt
            ::param : interval	    string	    true		                K line type ,1m;3m;5m;15m;30m;1h;2h;4h;6h;8h;12h;1d;3d;1w;1M eg:1m
            ::param : startTime     number      false                       start timestamp
            ::param : endTime       number      false                       start timestamp
            ::param : limit         number      false        100
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": [
                    {
                    "i": 0,   //ID
                    "t": 0,   //transaction time
                    "p": "string", //transaction price
                    "q": "string",  //transaction quantity
                    "v": "string",  //transaction volume
                    "b": true   //buyerMaker
                    }
                ]
            }
        """
        return request("GET", self.url(XT4PlatConfig.GET_KLINE), params = params)

    def get_trades(self, params: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : symbol	    string	    true		          	    trading pair eg:btc_usdt
            ::param : limit         number      false        200	        1,1000
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": [
                    {
                    "i": 0,   //ID
                    "t": 0,   //transaction time
                    "p": "string", //transaction price
                    "q": "string",  //transaction quantity
                    "v": "string",  //transaction volume
                    "b": true   //buyerMaker
                    }
                ]
            }
        """
        return request("GET", self.url(XT4PlatConfig.GET_TRADES), params = params)

    def get_ticker(self,  params: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description                 Ranges
            ::param : symbol	    string	    false		          	    trading pair eg:btc_usdt
            ::param : symbols	    array	    false		          	    Collection of trading pairs. Priority is higher than symbol. eg: btc_usdt,eth_usdt
        @Return
            {
            "rc": 0,
            "mc": "SUCCESS",
            "ma": [],
            "result": [
                    {
                    "s": "btc_usdt",   //symbol
                    "p": "9000.0000",   //price
                    "t": 1661856036925   //time
                    }
                ]
            }
        """
        return request("GET", self.url(XT4PlatConfig.GET_TICKER), params = params)

    def get_full_ticker(self, params: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description                 Ranges
            ::param : symbol	    string	    false		          	    trading pair eg:btc_usdt
            ::param : symbols	    array	    false		          	    Collection of trading pairs. Priority is higher than symbol. eg: btc_usdt,eth_usdt
        @Return
            {
            "rc": 0,
            "mc": "SUCCESS",
            "ma": [],
            "result": [
                    {
                    "s": "btc_usdt",     //symbol
                    "t": 1661856036925,  //time
                    "cv": "0.0000",      //change value
                    "cr": "0.00",        //change rate
                    "o": "9000.0000",    //open price
                    "l": "9000.0000",    //low
                    "h": "9000.0000",    //high
                    "c": "9000.0000",    //close price
                    "q": "0.0136",       //quantity
                    "v": "122.9940",     //volume
                    "ap": null,          //asks price(sell one price)
                    "aq": null,          //asks qty(sell one quantity)
                    "bp": null,           //bids price(buy one price)
                    "bq": null           //bids qty(buy one quantity)
                    }
                ]
            }
        """
        return request("GET", self.url(XT4PlatConfig.GET_FULL_TICKER), params = params)

    def get_best_ticker(self, params: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description                 Ranges
            ::param : symbol	    string	    false		          	    trading pair eg:btc_usdt
            ::param : symbols	    array	    false		          	    Collection of trading pairs. Priority is higher than symbol. eg: btc_usdt,eth_usdt
        @Return
            {
            "rc": 0,
            "mc": "SUCCESS",
            "ma": [],
            "result": [
                    {
                    "s": "btc_usdt",  //symbol
                    "ap": null,  //asks price(sell one price)
                    "aq": null,  //asks qty(sell one quantity)
                    "bp": null,   //bids price(buy one price)
                    "bq": null    //bids qty(buy one quantity)
                    }
                ]
            }
        """
        return request("GET", self.url(XT4PlatConfig.GET_BEST_TICKER), params = params)

    def get_24h_ticker(self, params: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description                 Ranges
            ::param : symbol	    string	    false		          	    trading pair eg:btc_usdt
            ::param : symbols	    array	    false		          	    Collection of trading pairs. Priority is higher than symbol. eg: btc_usdt,eth_usdt
        @Return
            {
            "rc": 0,
            "mc": "SUCCESS",
            "ma": [],
            "result": [
                    {
                    "s": "btc_usdt",   //symbol
                    "cv": "0.0000",   //price change value
                    "cr": "0.00",     //price change rate
                    "o": "9000.0000",   //open price
                    "l": "9000.0000",   //lowest price
                    "h": "9000.0000",   //highest price
                    "c": "9000.0000",   //close price
                    "q": "0.0136",      //transaction quantity
                    "v": "122.9940"    //transaction volume
                    }
                ]
            }
        """
        return request("GET", self.url(XT4PlatConfig.GET_24H_TICKER), params = params)


class SignedHttpAPI(PublicHttpAPI):
    """
    ::param accesskey       appkey
    ::param sercetkey       secret
    ---
    Usage:
        See: https://xt-com.github.io/xt4-api/#market_cn2symbol

    Since XT needs to provide some open interfaces for third-party platforms,
    it requires data security issues of the interface,
    such as whether the data has been tampered with,
    whether the data is outdated,
    whether the data can be submitted repeatedly,
    and the frequency of access to the interface within a certain period of time.
    Among them, whether the data has been tampered with is the most important.
    """

    def __init__(self, accesskey: str, secretkey: str, domain: str = None) -> None:
        """ """
        super().__init__(domain = domain)
        self._accesskey=accesskey
        self._secretkey=secretkey

    def get_datas(self, param: dict = None):
        """ """
        data={
            "accesskey": self._accesskey,
            "secretkey": self._secretkey
        }
        if param and isinstance(param, dict):
            data.update(**param)
        return data

    def get_order(self, data):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : orderId	    number	    true
        @Return
            See: https://xt-com.github.io/xt4-api/#market_cn2symbol
        """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatConfig.GET_ORDER)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))
        return request(method, uri, params=data, headers=headers)

    def get_order_list(self, data: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : orderId	    number	    true
            ::param : clientOrderId	string	    false
        @Return
            See: https://xt-com.github.io/xt4-api/#market_cn2symbol
        """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatConfig.GET_ORDER)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))
        return request(method, uri, params=data, headers=headers)

    def cancel_order(self, orderId: int=None):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : orderId	    number	    true
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": {
                    "cancelId": "6216559590087220004"
                }
            }
        """
        _data = self.get_datas()
        method = "DELETE"
        uri = self.url(XT4PlatConfig.GET_ORDER)
        # _data["urlencoded"] = True

        uri = "{}/{}".format(uri, orderId)
        headers, _ = get_auth_payload(PayloadObj(_data, uri, method))
        return request(method, uri, headers=headers)

    def send_order(self, data: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : symbol	    string	    true
            ::param : clientOrderId	string	    false	                    The longest number is 32 characters
            ::param : side      	string	    true	                    BUY,SELL
            ::param : type      	string	    true	                    order type:LIMIT,MARKET
            ::param : timeInForce   string	    true	                    effective way:GTC, FOK, IOC, GTX
            ::param : bizType       string	    true	                    SPOT, LEVER
            ::param : price         number	    false	                    price. Required if it is the LIMIT price; blank if it is the MARKET price
            ::param : quantity      number	    false	                    quantity. Required if it is the LIMIT price or the order is placed at the market price by quantity
            ::param : quoteQty      number	    false	                    amount. Required if it is the LIMIT price or the order is the market price when placing an order by amount
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": {
                    "orderId": "6216559590087220004"
                }
            }
        """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatConfig.GET_ORDER)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))
        return request("POST", uri, json=data, headers=headers)

    def get_batch_order(self, data: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : orderId	    string	    true		                order Ids eg: 6216559590087220004,6216559590087220004
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": {
                    "cancelId": "6216559590087220004"
                }
            }
        """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatConfig.GET_BATCH_ORDERS)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))
        return request(method, uri, params=data, headers=headers)

    def send_batch_order(self, data: dict):
        """
        @Param:
            @Desc     Parameter	        Type	    mandatory    Default	    Description
            ::param : clientBatchId	    string	    false		                Client batch number
            ::param : items	            array	    true		                array
            ::param : item.symbol	    string	    true
            ::param : item.clientOrderIdstring	    false		                The longest number is 32 characters
            ::param : item.side         string	    true		                BUY,SELL
            ::param : item.type         string	    true		                order type:LIMIT,MARKET
            ::param : item.timeInForce  string	    true		                effective way:GTC, FOK, IOC, GTX
            ::param : item.bizType      string	    true		                SPOT, LEVER
            ::param : item.price        number	    false		                price. Required if it is the LIMIT price; blank if it is the MARKET price
            ::param : item.quantity     number	    false		                quantity. Required if it is the LIMIT price or the order is placed at the market price by quantity
            ::param : item.quoteQty     number	    false		                amount. Required if it is the LIMIT price or the order is the market price when placing an order by amount
        @Return
            {
            "clientBatchId": "51232",
            "items": [
                    {
                    "symbol": "BTC_USDT",
                    "clientOrderId": "16559590087220001",
                    "side": "BUY",
                    "type": "LIMIT",
                    "timeInForce": "GTC",
                    "bizType": "SPOT",
                    "price": 40000,
                    "quantity": 2,
                    "quoteQty": 80000
                    }
                ]
            }
        """
        _data = self.get_datas(data)
        method = "POST"
        uri = self.url(XT4PlatConfig.BATCH_ORDER)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))
        return request(method, uri, json=data, headers=headers)

    def batch_cancel_order(self, data: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : clientBatchId	string	    false		                client batch id
            ::param : orderIds	    array	    true		                [6216559590087220004,6216559590087220005]
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": {}
            }
        """
        _data = self.get_datas(data)
        method = "DELETE"
        uri = self.url(XT4PlatConfig.DELETE_OPEN_ORDERS)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))
        return request(method, uri, json=data, headers=headers)

    def get_open_order(self, data: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : symbol    	string	    false		                Trading pair, if not filled in, represents all
            ::param : bizType	    string	    false		                SPOT, LEVER
            ::param : side  	    string	    false		                BUY,SELL
        @Return
            See: https://xt-com.github.io/xt4-api/#market_cn2symbol
        """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatConfig.GET_OPEN_ORDERS)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))

        return request(method, uri, params=data, headers=headers)

    def cancel_open_order(self, data: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : symbol    	string	    false		                Trading pair, if not filled in, represents all
            ::param : bizType	    string	    false		                SPOT, LEVER
            ::param : side  	    string	    false		                BUY,SELL
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": {}
            }
        """
        _data = self.get_datas(data)
        method = "DELETE"
        uri = self.url(XT4PlatConfig.DELETE_OPEN_ORDERS)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))

        return request(method, uri, json=data, headers=headers)

    def get_history_order(self, data: dict):
        """
        @Param:
            @Desc     Parameter	        Type	    mandatory    Default	    Description
            ::param : symbol    	    string	    false		                Trading pair, if not filled in, represents all
            ::param : bizType	        string	    false		                SPOT, LEVER
            ::param : side      	    string	    false		                BUY,SELL
            ::param : type              string	    false		                LIMIT, MARKET
            ::param : state             string	    false		                PARTIALLY_FILLED,FILLED,CANCELED,REJECTED,EXPIRED
            ::param : fromId            number	    false		                start id
            ::param : direction         string	    false		                query direction:PREV, NEXT
            ::param : limit             number	    false		 20             Limit number, max 100
            ::param : startTime         number	    false		                eg:1657682804112
            ::param : endTime           number	    false
            ::param : hiddenCanceled    number	    bool
        @Return
            See: https://xt-com.github.io/xt4-api/#market_cn2symbol
        """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatConfig.GET_ACCOUNT_HISTORY_ORDER)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))

        return request(method, uri, params=data, headers=headers)

    def get_trade(self, data: dict):
        """
        @Param:
            @Desc     Parameter	        Type	    mandatory    Default	    Description
            ::param : symbol    	    string	    false		                Trading pair, if not filled in, represents all
            ::param : bizType	        string	    false		                SPOT, LEVER
            ::param : orderSide      	string	    false		                BUY,SELL
            ::param : orderType         string	    false		                LIMIT, MARKET
            ::param : orderId           number	    false
            ::param : fromId            number	    false		                start id
            ::param : direction         string	    false		                query direction:PREV, NEXT
            ::param : limit             number	    false		 20             Limit number, max 100
            ::param : startTime         number	    false		                eg:1657682804112
            ::param : endTime           number	    false
            ::param : hiddenCanceled    number	    bool
        @Return
            See: https://xt-com.github.io/xt4-api/#market_cn2symbol
        """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatConfig.GET_ACCOUNT_TRADES)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))

        return request(method, uri, params=data, headers=headers)

    def get_balance(self, data: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : currency    	string	    true		                eg:usdt
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": {
                    "currency": "usdt",
                    "currencyId": 0,
                    "frozenAmount": 0,
                    "availableAmount": 0,
                    "totalAmount": 0,
                    "convertBtcAmount": 0  //Converted BTC amount
                }
            }
        """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatConfig.GET_BALANCE)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))

        return request(method, uri, params=data, headers=headers)

    def get_funds(self, data: dict):
        """
        @Param:
            @Desc     Parameter	    Type	    mandatory    Default	    Description
            ::param : currencies    string	    false		                List of currencies, comma separated,eg: usdt,btc
        @Return
            {
            "rc": 0,
            "mc": "string",
            "ma": [
                {}
            ],
            "result": {
                "totalBtcAmount": 0,
                "assets": [
                        {
                            "currency": "string",
                            "currencyId": 0,
                            "frozenAmount": 0,
                            "availableAmount": 0,
                            "totalAmount": 0,
                            "convertBtcAmount": 0
                        }
                    ]
                }
            }
        """
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "GET"
        uri = self.url(XT4PlatConfig.GET_FUNDS)

        headers, data = get_auth_payload(PayloadObj(
            _data, uri, method))
        return request(method, uri, params=data, headers=headers)

    def get_listenKey(self, data: dict=None):
        """ """
        # TODO
        _data = self.get_datas(data)
        _data["urlencoded"] = True
        method = "POST"
        uri = self.url(XT4PlatConfig.GET_ACCOUNT_LISTENKEY)

        headers, data = get_auth_payload(
        PayloadObj(_data, uri, method))
        return request(method, uri, headers = headers)
