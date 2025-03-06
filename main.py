from src import get_low_j_stock_list, get_low_j_stock_list_hk

INDEX_CODE = '000510'
PERIOD = 'daily'
J_THRESHOLD = 0


def main():
    result = get_low_j_stock_list(INDEX_CODE, PERIOD, J_THRESHOLD)
    result_hk = get_low_j_stock_list_hk(PERIOD, J_THRESHOLD)
    print('A股列表：')
    print(result)
    print('港股列表:')
    print(result_hk)


if __name__ == "__main__":
    main()
