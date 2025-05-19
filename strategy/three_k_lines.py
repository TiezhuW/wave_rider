from market_data import get_stock_data


def has_3_neg_k_lines(code):
    stock_data = get_stock_data(code)
    last_3_changes = stock_data.tail(3)['涨跌幅']
    return (last_3_changes < 0).all()

# todo 底分型 顶分型
