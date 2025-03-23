from market_data import get_stock_data


def has_three_neg_candlesticks(code):
    stock_data = get_stock_data(code)
    last_3_changes = stock_data.tail(3)['涨跌幅']
    return (last_3_changes < 0).all()
