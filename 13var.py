import csv
import os


def count_csv_rows(folder_name, file_name):
    folder_name = '/Users/maksimkrupkin/case/data_format/data'
    file_name = 'weekly_IBM.csv'

    file_path = os.path.join(folder_name, file_name)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            # Подсчёт количества строк в файле
            row_count = sum(1 for row in csv_reader)
            
            with open('number.txt', 'w') as file:
                # Записываем число в файл
                file.write(str(row_count))
                print("Число сохранено в файл 'number.txt'")

folder_name = '/Users/maksimkrupkin/case/data_format/data'
file_name = 'weekly_IBM.csv'
row_count = count_csv_rows(folder_name, file_name)


