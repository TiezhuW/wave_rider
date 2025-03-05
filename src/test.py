import akshare as ak
import pandas as pd

# 获取个股历史数据
stock_data = ak.stock_zh_a_hist(symbol="688981")

low_list = stock_data['最低'].rolling(9, min_periods=9).min()
low_list.fillna(value=stock_data['最低'].expanding().min(), inplace=True)
high_list = stock_data['最高'].rolling(9, min_periods=9).max()
high_list.fillna(value=stock_data['最高'].expanding().max(), inplace=True)
rsv = (stock_data['收盘'] - low_list) / (high_list - low_list) * 100
stock_data['K'] = pd.DataFrame(rsv).ewm(com=2).mean()
stock_data['D'] = stock_data['K'].ewm(com=2).mean()
stock_data['J'] = 3 * stock_data['K'] - 2 * stock_data['D']

# 打印包含KDJ指标的DataFrame
print(stock_data[['日期', '收盘', 'K', 'D', 'J']])
