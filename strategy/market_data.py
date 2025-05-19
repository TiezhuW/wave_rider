import re

import akshare as ak


def get_stock_data(code, period='daily'):
    if re.match(r'^\d{6}$', code) is not None:
        stock_data = ak.stock_zh_a_hist(symbol=code, period=period, adjust='qfq')
    elif re.match(r'^\d{5}$', code) is not None:
        stock_data = ak.stock_hk_hist(symbol=code, period=period, adjust='qfq')
    elif re.match(r'^\d{4}\.HK$', code) is not None:
        processed_code = '0' + code[:-3]
        stock_data = ak.stock_hk_hist(symbol=processed_code, period=period, adjust='qfq')
    elif re.match(r'^\d{3}\.[A-Z]{1,5}$', code) is not None:
        stock_data = ak.stock_us_hist(symbol=code, period=period, adjust='qfq')
    elif re.match(r'^[A-Z._]{1,5}$', code) is not None:
        if period != 'daily':
            print('period not supported!')
            return None
        processed_code = code.replace("_", ".")
        tmp_stock_data = ak.stock_us_daily(symbol=processed_code, adjust='qfq')
        stock_data = tmp_stock_data.rename(columns={'high': '最高', 'low': '最低', 'close': '收盘'})
        stock_data['涨跌幅'] = stock_data['close'] - stock_data['open']
    else:
        print('invalid code!')
        return None
    return stock_data
