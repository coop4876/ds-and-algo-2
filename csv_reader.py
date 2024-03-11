import csv
from package import Package
from hash_table import HashTable

def package_hash_from_csv(file_path):
    package_hash = HashTable(capacity=41)

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) #skip header row
        for row in csv_reader:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            delivery_deadline = row[5]
            weight = row[6]
            notes = row[7]

            working_package = Package(package_id, address, city, state, zip, delivery_deadline, weight, notes)
            package_hash[package_id] = working_package

    return package_hash