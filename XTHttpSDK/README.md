# XTHttpAPISDK v0.0.2

## install
```
# Use SDK
python setup.py bdist_egg
python setup.py install 
from XTHttpSDK import PublicHttpAPI, SignedHttpAPI
```

## Rest

### test_get_server_time
```
publicAPI = PublicHttpAPI()
publicAPI.get_server_time()
```

### test_get_market_config
```
publicAPI = PublicHttpAPI()
params = {
    "symbol": "btc_usdt",
}
publicAPI.get_market_config(params)
```

### test_get_depth
```
publicAPI = PublicHttpAPI()
params = {
    "symbol": "btc_usdt",
}
publicAPI.get_depth(params)
```

### test_get_kline
```
publicAPI = PublicHttpAPI()
params = {
    "symbol": "btc_usdt",
    "interval": "1m",
}
publicAPI.get_kline(params)
```

### test_get_trades
```
publicAPI = PublicHttpAPI()
params = {
    "symbol": "btc_usdt",
}
publicAPI.get_trades(params)
```

### test_get_ticker
```
publicAPI = PublicHttpAPI()

params = {
    "symbol": "btc_usdt",
}
publicAPI.get_ticker(params)
```

### test_get_full_ticker
```
publicAPI = PublicHttpAPI()

params = {
    "symbol": "btc_usdt",
}
publicAPI.get_ticker(params)
```

### test_get_best_ticker
```
publicAPI = PublicHttpAPI()

params = {
    "symbol": "btc_usdt",
}
publicAPI.get_best_ticker(params)
```

### test_get_24h_ticker
```
publicAPI = PublicHttpAPI()
params = {
    "symbol": "btc_usdt",
}
publicAPI.get_24h_ticker(params)
```

### test_get_coins_info
```
publicAPI = PublicHttpAPI()
publicAPI.get_coins_info()
```

### test_get_order
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)
orderId = 140541112005403904
signedHttpAPI.get_order(orderId)
```

### test_get_order_list
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)
signedHttpAPI.get_order_list()
```

### test_send_order
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)
data = {
    "symbol": "btc_usdt",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "bizType": "SPOT",
    "price": "20009",
    "quantity": "0.1",
}
signedHttpAPI.send_order(data)
```

### test_cancel_order
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

orderId = 140541701988787456
signedHttpAPI.cancel_order(orderId)
```

### test_batch_order
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

data = {
    "orderIds": "139865641251887680"
}
signedHttpAPI.get_batch_order(data)
```

### test_send_batch_order
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

order = [
    {"symbol": "btc_usdt", "price": "19000", "quantity": "0.001",
        "side": "BUY", "type": "LIMIT", "timeInForce": "GTC", "bizType": "SPOT"},
    {"symbol": "btc_usdt", "price": "19001", "quantity": "0.001",
        "side": "BUY", "type": "LIMIT", "timeInForce": "GTC", "bizType": "SPOT"},
]

data = {
    "items": order
}
signedHttpAPI.send_batch_order(data)
```

### test_batch_cancel_order
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

data = {
    "items": ["140600606177600768"]
}
signedHttpAPI.batch_cancel_order(data)
```

### test_get_open_order
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

data = {
    "symbol": "btc_usdt"
}
signedHttpAPI.get_open_order(data)
```

### test_cancel_open_order
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

data = {
    "symbol": "btc_usdt"
}
signedHttpAPI.cancel_open_order(data)
```

### test_get_history_order
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

data = {
    "symbol": "btc_usdt"
}
signedHttpAPI.get_history_order(data)
```

### test_get_trade
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

data = {
    "symbol": "btc_usdt"
}
signedHttpAPI.get_trade(data)
```

### test_get_balance
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

data = {
    "currency": "usdt"
}
signedHttpAPI.get_balance(data)
```

### test_get_funds
```
accesskey = "xxxxxxxxxx"
sercetkey = "yyyyyyyyyy"
signedHttpAPI = SignedHttpAPI(accesskey, sercetkey)

data = {
    "currencies": "usdt"
}
signedHttpAPI.get_funds(data)
```

## WS

### test_ping
```
def callback(ws, message):
    print("[ws-callback]::: ", message)


publicWs = PublicWebSocket(callback=callback)
publicWs.start()
publicWs.ping()
```

### test_on_trade
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["trade@btc_usdt"],
    "id": 1,
}
publicWs = PublicWebSocket(callback=callback)
publicWs.start()
publicWs.subscribe(topic)
publicWs.ping()
```

### test_on_kline
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["kline@btc_usdt,5m"],
    "id": 1,
}
publicWs = PublicWebSocket(callback=callback)
publicWs.start()
publicWs.subscribe(topic)
publicWs.ping()
```

### test_on_depth
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["depth@btc_usdt,20"],
    "id": 1,
}
publicWs = PublicWebSocket(callback=callback)
publicWs.start()
publicWs.subscribe(topic)
publicWs.ping()
```

### test_on_depth_update
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["depth_update@btc_usdt"],
    "id": 1,
}
publicWs = PublicWebSocket(callback=callback)
publicWs.start()
publicWs.subscribe(topic)
publicWs.ping()
```

### test_on_ticker
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["ticker@btc_usdt"],
    "id": 1,
}
publicWs = PublicWebSocket(callback=callback)
publicWs.start()
publicWs.subscribe(topic)
publicWs.ping()
```

### test_on_tickers
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["tickers"],
    "id": 1,
}
publicWs = PublicWebSocket(callback=callback)
publicWs.start()
publicWs.subscribe(topic)
publicWs.ping()
```

### test_on_user_balance
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["balance"],
    "id": 1,
}

accesskey = "xxxxxxxxxx"
secretkey = "yyyyyyyyyy"
privateWs = PrivateWebsocket(
    accesskey=accesskey,
    secretkey=secretkey,
    callback=callback
)
privateWs.start()
privateWs.subscribe(topic)
privateWs.ping()
```

### test_on_user_trigger
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["trigger"],
    "id": 1,
}

accesskey = "xxxxxxxxxx"
secretkey = "yyyyyyyyyy"
privateWs = PrivateWebsocket(
    accesskey=accesskey,
    secretkey=secretkey,
    callback=callback
)
privateWs.start()
privateWs.subscribe(topic)
privateWs.ping()
```

### test_on_user_order
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["order"],
    "id": 1,
}

accesskey = "xxxxxxxxxx"
secretkey = "yyyyyyyyyy"
privateWs = PrivateWebsocket(
    accesskey=accesskey,
    secretkey=secretkey,
    callback=callback
)
privateWs.start()
privateWs.subscribe(topic)
privateWs.ping()
```

### test_on_user_trade
```
def callback(ws, message):
    print("[ws-callback]::: ", message)

topic = {
    "params": ["trade"],
    "id": 1,
}

accesskey = "xxxxxxxxxx"
secretkey = "yyyyyyyyyy"
privateWs = PrivateWebsocket(
    accesskey=accesskey,
    secretkey=secretkey,
    callback=callback
)
privateWs.start()
privateWs.subscribe(topic)
privateWs.ping()
```

## realease

### v0.0.1
- RestAPI demo

### v0.0.2
- WSAPI demo

