import random
import time

import akshare as ak
from MyTT import KDJ


def get_latest_j_and_price(code, period='daily'):
    length = len(code)
    if length == 6:
        stock_data = ak.stock_zh_a_hist(symbol=code, period=period, adjust='qfq')
    elif length == 5:
        stock_data = ak.stock_hk_hist(symbol=code, period=period, adjust='qfq')
    else:
        print('invalid code!')
        return
    stock_data['K'], stock_data['D'], stock_data['J'] = (
        KDJ(stock_data['收盘'], stock_data['最高'], stock_data['最低'], 9, 3, 3)
    )
    return stock_data['J'].iloc[-1], stock_data['收盘'].iloc[-1]


def get_low_j_stock_list(index_code, period='daily', j_threshold=0):
    index_stock = ak.index_stock_cons_csindex(symbol=index_code)
    rows = len(index_stock)
    for index, row in index_stock.iterrows():
        code = row['成分券代码']
        print('fetching j and price started, code = ', code)
        time.sleep(random.uniform(0.1, 0.5))
        j, close_price = get_latest_j_and_price(code, period)
        print('fetching j and price finished (', index + 1, '/', rows, ')')
        index_stock.at[index, 'J'] = j
        index_stock.at[index, '收盘价'] = close_price
    return index_stock[['成分券代码', '成分券名称', '收盘价', 'J']][index_stock['J'] < j_threshold]


def get_low_j_stock_list_hk(period='daily', j_threshold=0):
    stock_hk_famous = ak.stock_hk_famous_spot_em()
    rows = len(stock_hk_famous)
    for index, row in stock_hk_famous.iterrows():
        code = row['代码']
        print('fetching j and price started, code = ', code)
        time.sleep(random.uniform(0.1, 0.5))
        j, close_price = get_latest_j_and_price(code, period)
        print('fetching j and price finished (', index + 1, '/', rows, ')')
        stock_hk_famous.at[index, 'J'] = j
        stock_hk_famous.at[index, '收盘价'] = close_price
    return stock_hk_famous[['代码', '名称', '收盘价', 'J']][stock_hk_famous['J'] < j_threshold]
