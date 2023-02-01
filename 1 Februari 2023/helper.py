import csv

header = []


def createList(database_name, to_dict=False):
    global header
    file = open(f'{database_name}.csv')
    reader = csv.reader(file)
    header = next(reader)

    rows = []
    for row in reader:
        if to_dict:
            rows.append(transform(row))
        else:
            rows.append(row)

    return rows


def transform(data):
    result = {}
    for i in range(len(header)):
        column = header[i]
        value = data[i]
        result[column] = value

    return result
