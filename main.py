import csv

def open_file(csv_file, txt_file):
    profit = 0.0 

    try:
        with open(csv_file, 'r', encoding='utf-8') as f1, open(txt_file, 'w', encoding='utf-8') as f2:
            reader = csv.reader(f1, delimiter=';')

            for row in reader:
                try:
                    if '_' not in row[3]:
                        profit += float(row[3].replace(',', '.'))
                except (ValueError, IndexError):
                    continue

            f2.write(f'Профит - {profit:.2f}')

        print(f"Результат успешно записан в файл {txt_file}")

    except FileNotFoundError:
        print(f"Файл {csv_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

open_file(csv_file='data_format/data/sales2019.csv', txt_file='new_file.txt')
