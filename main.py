import csv
import json
from datetime import datetime

def process_crypto_data(input_file, output_file):
    hourly_volume = {}

    try:
        with open(input_file, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)

            headers = next(csv_reader, None)
            if headers is None:
                print("Ошибка: CSV-файл пуст.")
                return

            if 'timestamp' not in headers or 'volume' not in headers:
                print("Ошибка: CSV-файл должен содержать столбцы 'timestamp' и 'volume'.")
                return

            timestamp_index = headers.index('timestamp')
            volume_index = headers.index('volume')

            for row in csv_reader:
                try:
                    timestamp = row[timestamp_index]
                    volume = float(row[volume_index])

                    hour = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:00:00')

                    if hour in hourly_volume:
                        hourly_volume[hour] += volume
                    else:
                        hourly_volume[hour] = volume

                except ValueError as e:
                    print(f"Ошибка при обработке строки: {e}")
                except Exception as e:
                    print(f"Неизвестная ошибка: {e}")

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    result = [{'hour': hour, 'total_volume': volume} for hour, volume in hourly_volume.items()]

    try:
        with open(output_file, mode='w') as json_file:
            json.dump(result, json_file, indent=4)
        print(f"Данные успешно записаны в файл {output_file}.")
    except Exception as e:
        print(f"Ошибка при записи в JSON-файл: {e}")

input_file = 'data/crypto_intraday_5min_ETH_USD.csv'
output_file = 'data/hourly_volume.json'

process_crypto_data(input_file, output_file)