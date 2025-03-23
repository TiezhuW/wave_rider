import random
import time

import akshare as ak
import pandas as pd
from MyTT import KDJ

from market_data import get_stock_data


def get_latest_j_and_price(code, period='daily'):
    stock_data = get_stock_data(code, period)
    stock_data['K'], stock_data['D'], stock_data['J'] = (
        KDJ(stock_data['收盘'], stock_data['最高'], stock_data['最低'], 9, 3, 3)
    )
    return stock_data['J'].iloc[-1], stock_data['收盘'].iloc[-1]


def get_low_j_stock_list_by_index(index_code, period='daily', j_threshold=0):
    print(f'start fetching j and price, index_code={index_code}, period={period}, j_threshold={j_threshold}')
    index_stock = ak.index_stock_cons_csindex(symbol=index_code)
    rows = len(index_stock)
    for index, row in index_stock.iterrows():
        code = row['成分券代码']
        name = row['成分券名称']
        print(f'fetching j and price started, code={code}, name={name}')
        time.sleep(random.uniform(0.5, 1))
        j, close_price = get_latest_j_and_price(code, period)
        print(f'fetching j and price finished ({index + 1}/{rows}), j={j}, close_price={close_price}')
        index_stock.at[index, 'J'] = j
        index_stock.at[index, '收盘价'] = close_price
    print(f'finish fetching j and price, index_code={index_code}, period={period}, j_threshold={j_threshold}')
    return index_stock['指数名称'].iloc[0], index_stock[['成分券代码', '成分券名称', '收盘价', 'J']][
        index_stock['J'] < j_threshold]


def get_low_j_stock_list_by_fund(fund_code, period='daily', j_threshold=0):
    print(f'start fetching j and price, fund_code={fund_code}, period={period}, j_threshold={j_threshold}')
    fund_info = ak.fund_individual_basic_info_xq(symbol=fund_code)
    fund_stock = ak.fund_portfolio_hold_em(symbol=fund_code, date="2024").drop_duplicates(subset=['股票代码'],
                                                                                          keep='last')
    rows = len(fund_stock)
    i = 1
    for index, row in fund_stock.iterrows():
        code = row['股票代码']
        name = row['股票名称']
        print(f'fetching j and price started, code={code}, name={name}')
        time.sleep(random.uniform(0.5, 1))
        j, close_price = get_latest_j_and_price(code, period)
        print(f'fetching j and price finished ({index + 1}/{rows}), j={j}, close_price={close_price}')
        fund_stock.at[index, 'J'] = j
        fund_stock.at[index, '收盘价'] = close_price
        i += 1
    print(f'finish fetching j and price, fund_code={fund_code}, period={period}, j_threshold={j_threshold}')
    return fund_info[fund_info['item'] == '基金名称']['value'].values[0], \
        fund_stock[['股票代码', '股票名称', '收盘价', 'J']][fund_stock['J'] < j_threshold]


def get_low_j_famous_foreign_stock_list(region, period='daily', j_threshold=0):
    stock_famous = pd.DataFrame()
    if region == 'us':
        all_symbols = ['科技类', '金融类', '医药食品类', '媒体类', '汽车能源类', '制造零售类']
        for symbol in all_symbols:
            temp_stock_df = ak.stock_us_famous_spot_em(symbol)
            stock_famous = pd.concat([stock_famous, temp_stock_df], ignore_index=True)
    elif region == 'hk':
        stock_famous = ak.stock_hk_famous_spot_em()
    else:
        print('invalid region!')
        return
    rows = len(stock_famous)
    for index, row in stock_famous.iterrows():
        code = row['代码']
        print(f'fetching j and price started, code={code}')
        time.sleep(random.uniform(0.1, 0.5))
        j, close_price = get_latest_j_and_price(code, period)
        print(f'fetching j and price finished ({index + 1}/{rows})')
        stock_famous.at[index, 'J'] = j
        stock_famous.at[index, '收盘价'] = close_price
    return stock_famous[['代码', '名称', '收盘价', 'J']][stock_famous['J'] < j_threshold]
