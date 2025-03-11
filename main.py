from src import get_low_j_stock_list, at_weekend, end_of_month

INDEX_CODES = ['000300', '000905', '930930']
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
    for index_code in INDEX_CODES:
        index_name, result_list = get_low_j_stock_list(index_code, period, J_THRESHOLD)
        print(index_name, '指数成分股', period_str, '线低J值列表：')
        print(result_list)


def main():
    get_all_low_j_stock_list('daily')
    if at_weekend():
        get_all_low_j_stock_list('weekly')
    if end_of_month():
        get_all_low_j_stock_list('monthly')


if __name__ == "__main__":
    main()
