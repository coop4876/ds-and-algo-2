import csv
from hash_table import HashTable
from location_and_distance import DistanceCalculator

class Package:
    def __init__(self,package_id, address, city, state, zip_code, deadline, weight, notes=""):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        #todo special case for package not yet in warehouse
        self.status = "In Warehouse"
        self.delivery_time = "N/A"
        self.distance_to_next_location = 0

class Warehouse:
    def __init__(self):
        self.undelivered_package_hash = HashTable(capacity=40)
        self.out_for_delivery_packages = HashTable(capacity=16)
        self.delivered_packages = HashTable(capacity=40)

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
    
    def get_closest_next_package(self, current_location):
        pass

    def load_truck(self):
        #todo get closest package index for next package to load
        index = 0
        for package in self.undelivered_package_hash:
            if index <=15:
                self.out_for_delivery_packages[index] = package
                self.out_for_delivery_packages[index].status = "OutForDelivery"
                del self.undelivered_package_hash[index]
                index += 1
            else:
                break
        return self.out_for_delivery_packages

class Truck:
    def __init__(self, current_deliveries):
        #todo add current_time property
        self.total_milage = 0
        self.current_deliveries = current_deliveries

    def make_deliveries(self):
        #todo move to delivered hash table
        pass

    def print_pending_packages(self):
        pass

class DeliveredPackages:
    def __init__():
        pass

    def add_to_delivered():
        pass

    def print_delivered_packages():
        pass


