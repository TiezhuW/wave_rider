from src import get_low_j_stock_list, get_low_j_stock_list_hk, at_weekend, end_of_month

INDEX_CODE = '000510'
J_THRESHOLD = 0


def get_all_low_j_stock_list(period='daily'):
    if period == 'daily':
        period_str = '日'
    elif period == 'weekly':
        period_str = '周'
    elif period == 'monthly':
        period_str = '月'
    else:
        return
    print('--------------开始获取A股', period_str, '线 低J值列表--------------')
    result_daily = get_low_j_stock_list(INDEX_CODE, 'daily', J_THRESHOLD)
    print('--------------获取港股', period_str, '线低J值列表结束--------------')
    print('A股', period_str, '线低J值列表：')
    print(result_daily)
    print('--------------开始获取港股', period_str, '线低J值列表--------------')
    result_daily_hk = get_low_j_stock_list_hk('daily', J_THRESHOLD)
    print('--------------获取港股', period_str, '线低J值列表结束--------------')
    print('港股', period_str, '线低J值列表：')
    print(result_daily_hk)


def main():
    get_all_low_j_stock_list('daily')
    if at_weekend():
        get_all_low_j_stock_list('weekly')
    if end_of_month():
        get_all_low_j_stock_list('monthly')


if __name__ == "__main__":
    main()
