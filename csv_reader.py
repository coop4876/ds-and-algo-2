import csv

with open('data\packages.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]}')
            