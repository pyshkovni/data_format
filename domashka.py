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

output_file = 'max_prices.txt'
with open(output_file, 'w') as f:
    f.write('Year\tMax_Open\tMax_Close\n')
    for year, row in results.iterrows():
        f.write(f"{year.year}\t{row['Max_Open']:.5f}\t{row['Max_Close']:.5f}\n")
print(f"Данные записаны в файл {output_file}")
