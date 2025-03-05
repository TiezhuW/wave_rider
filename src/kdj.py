import akshare as ak
from MyTT import KDJ

def get_latest_j(code, period = 'daily'):
    stock_data = ak.stock_zh_a_hist(symbol=code, period=period, adjust='qfq') #todo other market
    stock_data['K'], stock_data['D'], stock_data['J'] =(
        KDJ(stock_data['收盘'].values, stock_data['最高'].values, stock_data['最低'].values, 9 , 3, 3))
    print(stock_data[['日期', '收盘', 'K', 'D', 'J']])
    return stock_data['J'].iloc[-1]
