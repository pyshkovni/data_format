
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


def main():

    input_filepath = Path("/Users/h1pyy/PycharmProjects/data_case3/Rome24.09.06.json")
    output_filepath = Path("Users/h1pyy/PycharmProjects/data_case3/output/sunrise_sunset.csv")

    output_filepath.parent.mkdir(parents=True, exist_ok=True)

    json_data = load_json(input_filepath)
    extracted_data = extract_data(json_data)
    save_to_csv(extracted_data, output_filepath)
    print(f"Данные успешно сохранены в {output_filepath}")