import json
from collections import Counter

def extract_wind_directions(data):
    wind_directions = []
    
    if isinstance(data, dict):
        if 'wind_dir' in data:
            wind_directions.append(data['wind_dir'])
        for value in data.values():
            wind_directions.extend(extract_wind_directions(value))
    
    elif isinstance(data, list):
        for item in data:
            wind_directions.extend(extract_wind_directions(item))
    
    return wind_directions

def process_wind_directions(json_file_path, output_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        wind_directions = extract_wind_directions(data)
        wind_counts = Counter(wind_directions)
        
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write("Статистика направлений ветра:\n")
            for direction, count in wind_counts.items():
                output_file.write(f"{direction}: {count}\n")

