from MyTT import BBI


def add_bbi_col(stock_data):
    stock_data['BBI'] = (
        BBI(stock_data['收盘'], 3, 6, 12, 24)
    )


def latest_2_close_lt_bbi(stock_data):
    return stock_data['BBI'].iloc[-1] > stock_data['收盘'].iloc[-1] and stock_data['BBI'].iloc[-2] > \
        stock_data['收盘'].iloc[-2] and stock_data['BBI'].iloc[-3] <= stock_data['收盘'].iloc[-3]


def latest_2_close_gt_bbi(stock_data):
    return stock_data['BBI'].iloc[-1] < stock_data['收盘'].iloc[-1] and stock_data['BBI'].iloc[-2] < \
        stock_data['收盘'].iloc[-2] and stock_data['BBI'].iloc[-3] >= stock_data['收盘'].iloc[-3]
