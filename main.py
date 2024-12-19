import json

folder = "data"
input_file = "Berlin24.09.06.json"
output_file = "Berlin_temperatures.txt"

def extract_temperature_data():
    with open(f"{folder}\{input_file}", 'r', encoding='utf-8') as file:
        weather_data = json.load(file)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Температурная статистика для Берлина:\n\n")

        for day in weather_data.get("forecasts", [{}]):
            file.write(f"Прогноз на {day.get('date', 'неизвестную дату')}:\n")
            parts = day.get("parts", {})

            for period, stats in parts.items():
                temp_avg = stats.get('temp_avg', 'нет данных')
                temp_max = stats.get('temp_max', 'нет данных')
                temp_min = stats.get('temp_min', 'нет данных')

                file.write(f"{period.capitalize()}:\n")
                file.write(f"  Средняя температура: {temp_avg}\n")
                file.write(f"  Максимальная температура: {temp_max}\n")
                file.write(f"  Минимальная температура: {temp_min}\n\n")

    print(f"Результаты сохранены в файл {output_file}.")

if __name__ == "__main__":
    extract_temperature_data()