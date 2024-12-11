
import json
import csv
from pathlib import Path

def load_json(filepath):

    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_data(json_data):

    forecasts = json_data.get('forecasts', [])
    return [{"date": forecast["date"], "sunrise": forecast["sunrise"], "sunset": forecast["sunset"]} for forecast in forecasts]

def save_to_csv(data, output_filepath):

    with open(output_filepath, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["date", "sunrise", "sunset"])
        writer.writeheader()
        writer.writerows(data)


