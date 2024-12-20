# Импорт
import json
from collections import Counter

# Функция
def count_wind_directions(json_file_path, output_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    wind_directions = []
    if 'fact' in data:
        wind_directions.append(data['fact']['wind_dir'])
    if 'forecasts' in data:
        for forecast in data['forecasts']:
            for part in forecast['parts'].values():
                wind_directions.append(part['wind_dir'])
            for hour in forecast['hours']:
                wind_directions.append(hour['wind_dir'])
    wind_count = Counter(wind_directions)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for direction, count in wind_count.most_common():
            output_file.write(f"{direction}: {count}\n")

# Запуск
json_file_path = 'data/Sochi24.09.06.json'
output_file_path = 'wind_directions_count.txt'
count_wind_directions(json_file_path, output_file_path)