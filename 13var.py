import csv
import os

folder_name = '/Users/maksimkrupkin/case/data_format/data'
file_name = 'weekly_IBM.csv'

import csv
import os


def count_csv_rows(folder_name, file_name):

    file_path = os.path.join(folder_name, file_name)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            

