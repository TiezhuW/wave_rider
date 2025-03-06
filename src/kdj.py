import akshare as ak
from MyTT import KDJ


def get_latest_j(code, period='daily'):
    stock_data = ak.stock_zh_a_hist(symbol=code, period=period, adjust='qfq')
    stock_data['K'], stock_data['D'], stock_data['J'] = (
        KDJ(stock_data['收盘'].values, stock_data['最高'].values, stock_data['最低'].values, 9, 3, 3)
    )
    return stock_data['J'].iloc[-1]


def get_low_j_stock_list(index_code, period='daily', j_threshold=0):
    index_stock = ak.index_stock_cons_csindex(symbol=index_code)
    index_stock['J'] = index_stock['成分券代码'].apply(get_latest_j, period=period)
    filter_index_stock = index_stock[index_stock['J'] < j_threshold]
    return filter_index_stock[['成分券代码', '成分券名称', 'J']]
