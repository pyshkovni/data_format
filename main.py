from functions_code import load_json, extract_data, save_to_csv

from pathlib import Path

def main():

    input_filepath = Path("/Users/h1pyy/PycharmProjects/data_case3/Rome24.09.06.json")
    output_filepath = Path("/Users/h1pyy/PycharmProjects/data_case3/output/sunrise_sunset.csv")

    output_filepath.parent.mkdir(parents=True, exist_ok=True)

    json_data = load_json(input_filepath)
    extracted_data = extract_data(json_data)
    save_to_csv(extracted_data, output_filepath)
    print(f"Данные успешно сохранены в {output_filepath}")

if __name__ == "__main__":
    main()
