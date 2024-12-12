import csv
import json
from pathlib import Path

def load_json(filepath):
    """Загружает JSON-файл и возвращает данные."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_data(json_data):
    """Извлекает даты, время восхода и заката солнца."""
    forecasts = json_data.get('forecasts', [])
    result = []
    for forecast in forecasts:
        result.append({"date": forecast["date"], "sunrise": forecast["sunrise"], "sunset": forecast["sunset"]})
    return result

def save_to_csv(data, output_filepath):
    """Сохраняет данные в CSV-файл."""
    file = open(output_filepath, 'w', encoding='utf-8', newline='')
    writer = csv.DictWriter(file, fieldnames=["date", "sunrise", "sunset"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)
    file.close()