import pandas as pd
import json

# Считываем данные из CSV-файла
url = r"C:\Users\user\envs\data_format\data\fx_daily_EUR_USD.csv"
data = pd.read_csv(url)

# Преобразуем колонку 'timestamp' в формат даты
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Устанавливаем 'timestamp' в качестве индекса
data.set_index('timestamp', inplace=True)

# Группируем данные по месяцам и рассчитываем среднюю цену закрытия
monthly_average = data.resample('ME').mean()['close']  # 'M' для конца месяца

# Преобразуем результаты в словарь с преобразованием ключей в строки
result = {str(key): value for key, value in monthly_average.items()}

# Сохраняем в JSON-файл
with open('monthly_average_close.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

# Выводим результат
print(result)


   
