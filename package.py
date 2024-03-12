import csv
from hash_table import HashTable

class Package:
    def __init__(self,package_id, address, city, state, zip, deadline, weight, notes=""):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

    @classmethod
    def build_package_hash_from_csv(cls):
        package_hash = HashTable(capacity=40)

        with open('data/packages.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) #skip header row
            for row in csv_reader:
                package_id = int(row[0]) - 1
                address = row[1]
                city = row[2]
                state = row[3]
                zip = row[4]
                delivery_deadline = row[5]
                weight = row[6]
                notes = row[7]

                package = cls(package_id, address, city, state, zip, delivery_deadline, weight, notes)
                package_hash[package_id] = package

        return package_hash