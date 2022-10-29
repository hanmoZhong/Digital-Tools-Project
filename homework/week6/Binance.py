# the root URL is https://api.binance.com/api/v3
# The endpoint is klines
# Specify a request string to retrieve 75 observations of klines data for BTCUSDT since 2022-09-01.
# https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=12h&startTime=1662036209&limit=75

import requests
from datetime import datetime
import json
import pandas as pd


ROOT_URL = "https://api.binance.com/api/v3"
# URL https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=12h&startTime=1662036209&limit=75

def req(currency_pair,startdate):
    date_time = datetime.strptime(startdate, '%d/%m/%Y %H:%M:%S')
    ts = date_time.timestamp()
    #construct request URL
    req = "{root_url}/{endpoint}?symbol={pair}&interval={interval}&startTime={startime}&limit={limit}" \
        .format(root_url="https://api.binance.com/api/v3",
                endpoint="klines",
                pair=currency_pair,
                interval="12h",
                startime=round(ts),
                limit="75")
    # kline
    data = requests.get(req).json()
    D = pd.DataFrame(data, index=[i for i in range(1,76)], columns=['open_time','open','high','low','close','volume','close_time','qav','num_trades','taker_base_vol','taker_quote_vol','is_best_match'])
    return D

print(req(currency_pair="BTCUSDT",startdate="01/09/2022 14:43:29"))

















