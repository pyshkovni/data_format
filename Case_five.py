import yaml
import csv
from collections import Counter

def process_yaml_stages(input_file: str, output_file: str):
    # Считываем YAML-файл
    with open("C:\\Users\\Lenovo\\Downloads\\data\\gitlab-ci.yml", 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # Предполагается, что data - словарь с заданиями, где каждое задание - ключ верхнего уровня.
    # Пример:
    # build_job:
    #   stage: build
    #   script: ...
    # test_job:
    #   stage: test
    #   script: ...
    # и т.д.

    # Извлекаем все значения stage
    stages = []
    for job_name, job_content in data.items():
        if isinstance(job_content, dict) and 'stage' in job_content:
            stages.append(job_content['stage'])

    # Считаем количество каждого stage
    counter = Counter(stages)

    # Записываем результат в CSV
    # Формат: stage, count
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["stage", "count"])  # заголовок CSV
        for stage, count in counter.items():
            writer.writerow([stage, count])


if __name__ == "__main__":
    # Вызов функции
    process_yaml_stages("data/gitlab-ci.yml", "data/output_stages_count.csv")