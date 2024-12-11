import json
import csv

def read_json(file_path):
    """
    Читает JSON-файл и возвращает данные.
    :param file_path: Путь до JSON-файла
    :return: Данные из JSON-файла
    """
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def write_csv(data, output_path):
    """
    Записывает данные в CSV-файл в формате: link, company.
    :param data: Данные для записи
    :param output_path: Путь до выходного CSV-файла
    """
    with open(output_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')  # Явно указываем разделитель — запятая
        # Записываем заголовки таблицы
        writer.writerow(['link', 'company'])
        
        # Записываем данные из JSON в CSV
        for event in data:
            link = event.get('link')
            company = event.get('company')
            if link and company:
                writer.writerow([link, company])