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

