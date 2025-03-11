from src import at_weekend, end_of_month, get_low_j_stock_list_by_fund, get_low_j_stock_list_by_index

INDEX_CODES = ['000300', '000905', '000688', '930930']
FUND_CODES = ['018044', '017641']
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
        index_name, result_list = get_low_j_stock_list_by_index(index_code, period, J_THRESHOLD)
        print(index_name, '指数成分股', period_str, '线低J值列表：')
        print(result_list)
    for fund_code in FUND_CODES:
        fund_name, result_list = get_low_j_stock_list_by_fund(fund_code, period, J_THRESHOLD)
        print(fund_name, '基金成分股', period_str, '线低J值列表：')
        print(result_list)


def main():
    get_all_low_j_stock_list('daily')
    if at_weekend():
        get_all_low_j_stock_list('weekly')
    if end_of_month():
        get_all_low_j_stock_list('monthly')


if __name__ == "__main__":
    main()
