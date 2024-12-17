# код для решения 14 задачи

#14. Запишите в файл формата JSON следующую информацию из YAML-файла `mkdocs.yml`: 
# Найдите информацию о ссылках на социальные сети в блоке `social`.

import os
import json
import yaml

# Кастомный конструктор для обработки тега !ENV
def env_constructor(loader, node):
    value = loader.construct_scalar(node)
    return os.getenv(value)


yaml.add_constructor('!ENV', env_constructor)

def extract_social_links(yaml_file_path, json_file_path):
    # Проверяем, существует ли файл
    if not os.path.exists(yaml_file_path):
        print(f"Файл {yaml_file_path} не найден.")
        return
    
    # Читаем YAML файл
    with open(yaml_file_path, 'r') as yaml_file:
        try:
            data = yaml.load(yaml_file, Loader=yaml.Loader)
        except yaml.YAMLError as e:
            print(f"Ошибка при чтении YAML файла: {e}")
            return


    # Извлекаем социальные ссылки
    social_links = data.get('extra', {}).get('social', [])
    
    # Формируем данные для JSON
    social_data = [{"icon": link.get('icon'), "link": link.get('link')} for link in social_links]

    # Записываем данные в JSON файл
    with open(json_file_path, 'w') as json_file:
        json.dump(social_data, json_file, indent=4)

    print(f"Социальные ссылки успешно записаны в {json_file_path}")

 
yaml_file_path = 'data/mkdocs.yml'   
json_file_path = 'data/social_links.json'  # Путь для сохранения JSON файла

extract_social_links(yaml_file_path, json_file_path)