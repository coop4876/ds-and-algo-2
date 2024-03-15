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

    def __str__(self):
        print_string = 'package ID: ' + str(self.package_id) \
            + ' | package status: ' + str(self.status) \
            + ' | delivery address: ' + str(self.address) \
            + ' | distance to next location: ' + str(self.distance_to_next_location)
        return print_string

class Warehouse:
    def __init__(self):
        self.package_hash = HashTable(capacity=40)

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
                delivery_deadline = row[5]
                weight = row[6]
                notes = row[7]

                package = Package(package_id, address, city, state, zip, delivery_deadline, weight, notes)
                self.package_hash[package_id - 1] = package

        return self.package_hash
    
    def print_warehouse_packages(self):
        index = 0
        while index < 40:
            if self.package_hash[index].status == "In Warehouse":
                print(self.package_hash[index])
                index += 1
            else:
                index += 1

class Truck:
    def __init__(self):
        #todo add current_time property
        self.total_milage = 0
        self.current_deliveries = HashTable(capacity=16)
        self.current_time = 8
        

    def load_truck(self, distance_calculator, warehouse):
        index = 1
        self.current_deliveries[0] = distance_calculator.get_next_package(warehouse.package_hash, "HUB")
        self.current_deliveries[0].status = "En Route"
        while index < 16:
            previous_address = self.current_deliveries[index -1].address
            self.current_deliveries[index] = distance_calculator.get_next_package(warehouse.package_hash, previous_address)
            self.current_deliveries[index].status = "En Route"
            index += 1

    def make_deliveries(self, delivered_packages):
        index = 0
        while index < 16:
            if self.current_deliveries[index] == None:
                break
            else:
                delivery_index = self.current_deliveries[index].package_id
                self.total_milage += self.current_deliveries[index].distance_to_next_location
                delivered_packages[delivery_index] = self.current_deliveries[index]
                delivered_packages[delivery_index].status = "Delivered"
                del self.current_deliveries[index]
                index += 1
        return



    def print_pending_packages(self):
        index = 0
        while index < 16:
            if self.current_deliveries[index] == None:
                index += 1
            else:
                print(self.current_deliveries[index])
                index += 1
        return

class DeliveredPackages:
    def __init__(self):
        self.delivered_packages = HashTable(capacity=40)

    def add_to_delivered(self, package):
        self.delivered_packages[package.package_id] = package
        return

    def print_delivered_packages(self):
        index = 0
        while index < 40:
            if self.delivered_packages[index] == None:
                index += 1
            else:
                print(self.delivered_packages[index])
                index += 1


