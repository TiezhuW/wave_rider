from src.kdj import get_low_j_stock_list


def main():
    result = get_low_j_stock_list('000510', 'weekly', 0)
    print(result)


if __name__ == "__main__":
    main()
