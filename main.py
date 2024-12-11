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

