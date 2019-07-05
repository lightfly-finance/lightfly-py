## Lightfly 金融数据平台 Python 客户端

 [![Build Status](https://travis-ci.com/lightfly-finance/lightfly-py.svg?branch=master)](https://travis-ci.com/lightfly-finance/lightfly-py)
 
 ## 安装
 
 ```
 pip install -U lightfly
 ```
 
 ## 使用
 
```python
from lightfly.stock import Stock
from lightfly.http import Client

http_client = Client(app_id='xxx', secret_key='xxx')
stock = Stock(http_client)
data = stock.hs300()
print(data)

```

## 文档

[文档](https://www.yuque.com/twn39/bb3s7k)
