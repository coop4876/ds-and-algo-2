import csv
import datetime
from hash_table import HashTable
from package import Package

class Warehouse:
    def __init__(self):
        self.package_hash = HashTable(capacity=40)
        self.current_time = datetime.datetime(year= 2024, month= 3, day= 15, hour=8, minute=0)

    #builds a hashtable of packages from provided csv
    def build_undelivered_package_hash_table(self, package_file_path):
        with open(package_file_path, 'r') as package_file:
            csv_reader = csv.reader(package_file)
            next(csv_reader) #skip header row
            for row in csv_reader:
                package_id = int(row[0]) 
                address = row[1] + ' (' + row[4] + ')'
                city = row[2]
                state = row[3]
                zip = row[4]
                deadline = row[5]
                weight = row[6]
                notes = row[7]
                if notes != '':
                    status = "In Warehouse - Notes"
                else:
                    status = "In Warehouse"
                package = Package(package_id, address, city, state, zip, deadline, weight, status, notes)
                self.package_hash[package_id - 1] = package
        return self.package_hash

    #method for looking up packages
    def package_lookup(self, package_id):
        if package_id < 0 or package_id > 40:
            return "Enter a valid package ID (1-40)"
        elif self.package_hash[package_id - 1] != None:
            return self.package_hash[package_id - 1]

    #prints packages currently in warehouse (not en route or delivered)
    def print_warehouse_packages(self):
        package_count = 0
        print("------------------------- Packages in Warehouse ------------------------")
        index = 0
        while index < 40:
            #if status is In Warehouse or In Warehouse - Notes, print package
            if self.package_hash[index].status == "In Warehouse" or self.package_hash[index].status == "In Warehouse - Notes":
                print(self.package_hash[index])
                index += 1
                package_count += 1
            else:
                index += 1
        #print when all packages have been loaded or delivered
        if package_count == 0:
            print("All Packages En Route or Delivered".center(68))
        print("------------------------------------------------------------------------")