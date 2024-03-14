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

    def get_closest_next_package(self, current_location):
        pass

#modify build_package_hash_from_csv to function as an undelivered list?
#move from undelivered to truck to delivered?
    
class Warehouse:
    def __init__(self):
        self.undelivered_package_hash = HashTable(capacity=40)

    def build_undelivered_package_hash_table(self, package_file_path):
        with open(package_file_path, 'r') as package_file:
            csv_reader = csv.reader(package_file)
            next(csv_reader) #skip header row
            for row in csv_reader:
                package_id = int(row[0]) - 1
                address = row[1] + ' (' + row[4] + ')'
                city = row[2]
                state = row[3]
                zip = row[4]
                delivery_deadline = row[5]
                weight = row[6]
                notes = row[7]

                package = Package(package_id, address, city, state, zip, delivery_deadline, weight, notes)
                self.undelivered_package_hash[package_id] = package

        return self.undelivered_package_hash


class Truck:
    #load 16 packages onto turck
    #keep track of delivery times
    #move package to delivered, update status
    #print current status
    #list?
    def __init__():
        pass

    def load_truck():
        pass

    def make_deliveries():
        pass

class DeliveredPackages:
    #keep track of completed deliveries with times
    #print completed package details
    #list?
    def __init__():
        pass

    def add_to_delivered():
        pass


