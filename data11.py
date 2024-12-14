import json
import csv


def json_to_csv(json_file: str, csv_file: str):
    # Открываем и читаем JSON файл
    with open(json_file, encoding="utf-8") as file:
        data = json.load(file)

    # Извлекаем данные по часам из "hours"
    hours_data = data['forecasts'][0]['hours']

    # Открываем CSV файл для записи
    with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        
        # Записываем заголовки
        writer.writerow(["Hour", "Feels_Like", "Condition"])
        
        # Записываем данные о погоде по часам
        for hour_data in hours_data:
            writer.writerow([hour_data["hour"], hour_data["feels_like"], hour_data["condition"]])

# Имя входного JSON-файла и выходного CSV-файла
#json_file = "Amsterdam24.09.06.json"
json_file = "data_format/data/Amsterdam24.09.06.json"
csv_file = "weather_data.csv"

# Запускаем функцию
json_to_csv(json_file, csv_file)
#print(f"Данные успешно записаны в {csv_file}")


