from concurrent.futures import ThreadPoolExecutor, as_completed

from strategy import *

INDEX_CODES = ['000300', '000905', '000688', '930930']
FUND_CODES = ['018044', '017641']
J_THRESHOLD = 5


def get_all_low_j_stock_list(period='daily'):
    results = []
    period_str = get_period_str(period)
    print(f"{get_formated_current_datetime()} 获取{period_str}线低J值列表开始")
    with ThreadPoolExecutor(max_workers=len(INDEX_CODES) + len(FUND_CODES)) as executor:
        index_futures = [executor.submit(get_low_j_stock_list_by_index, index_code, period, J_THRESHOLD) for index_code
                         in INDEX_CODES]
        fund_futures = [executor.submit(get_low_j_stock_list_by_fund, fund_code, period, J_THRESHOLD) for fund_code in
                        FUND_CODES]
        for future in as_completed(index_futures):
            try:
                index_name, result_list = future.result()
                results.append((index_name, result_list))
            except Exception as e:
                print(f"获取{index_name}成分股{period_str}线低J值列表失败: {e}")
        for future in as_completed(fund_futures):
            try:
                fund_name, result_list = future.result()
                results.append((fund_name, result_list))
            except Exception as e:
                print(f"获取{fund_name}成分股{period_str}线低J值列表失败: {e}")
    print(f"{get_formated_current_datetime()} 获取{period_str}线低J值列表结束")
    for name, result_list in results:
        print(name, '成分股', period_str, '线低J值列表：')
        print(result_list)


def main():
    get_all_low_j_stock_list('daily')
    if at_weekend():
        get_all_low_j_stock_list('weekly')
    if end_of_month():
        get_all_low_j_stock_list('monthly')


if __name__ == "__main__":
    main()
