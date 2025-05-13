import csv


def load_data_list(lst, csv_file, column_name):
    with open("insurance.csv", "r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            lst.append(row[column_name])
        return lst
