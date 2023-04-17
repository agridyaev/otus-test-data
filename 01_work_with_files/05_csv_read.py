import csv

from files import CSV_FILE_PATH

with open(CSV_FILE_PATH) as f:
    rd = csv.reader(f)

    headers = next(rd)
    for row in rd:
        print(dict(zip(headers, row)))

print('\n', 20 * "=", '\n')

with open(CSV_FILE_PATH) as f:
    rd = csv.DictReader(f)

    for row in rd:
        print(row)
