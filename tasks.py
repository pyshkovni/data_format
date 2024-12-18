import csv
import os

def process_csv_file(csv_filename, output_filename):
    csv_file_path = os.path.join('data', csv_filename)
    if not os.path.exists(csv_file_path):
        print(f"Ошибка: Файл {csv_file_path} не найден.")
        return
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader, None)
        row_count = sum(1 for row in csv_reader)
    output_file_path = os.path.join('data', output_filename)
    with open(output_file_path, mode='w', encoding='utf-8') as output_file:
        output_file.write(f"Количество строк в таблице (исключая заголовок): {row_count}\n")

    print(f"Результат успешно записан в файл: {output_file_path}")
    csv_filename = 'weekly_IBM.csv' 
output_filename = 'output.txt'  
process_csv_file(csv_filename, output_filename)
