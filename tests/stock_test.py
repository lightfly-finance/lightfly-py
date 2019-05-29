from lightfly.http import Client
from lightfly.stock import Stock
from pandas.core.frame import DataFrame
import os


app_id = os.environ['LIGHTFLY_APP_ID']
secret_key = os.environ['LIGHTFLY_SECRET_KEY']

http = Client(app_id, secret_key)
stock = Stock(http)


def test_hs300():
    data = stock.hs300()
    assert DataFrame == type(data)


def test_daily_history():
    data = stock.daily_history('sz002142', '2019-05-01', '2019-06-01')
    assert DataFrame == type(data)


def test_stock_realtime():
    data = stock.stock_realtime('sz002142')
    assert DataFrame == type(data)


def test_hgs_trade_realtime():
    data = stock.hgs_trade_realtime()
    assert DataFrame == type(data)


def test_hgtong_top10():
    data = stock.hgtong_top10()
    assert DataFrame == type(data)
