import pandas as pd
csv_file = '/Users/ernestevtuhov/PycharmProjects/data_format/data/fx_weekly_EUR_USD.csv'
data = pd.read_csv(csv_file)

data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)

max_open = data.resample('YE')['open'].max()
max_close = data.resample('YE')['close'].max()

results = pd.DataFrame({
    'Max_Open': max_open,
    'Max_Close': max_close
})
