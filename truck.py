import datetime
from hash_table import HashTable

class Truck:
    def __init__(self, name):
        self.name = name
        self.current_time = datetime.datetime(year= 2024, month= 3, day= 15, hour=8, minute=0)
        self.total_milage = 0
        self.current_deliveries = HashTable(capacity=16)
        
    def load_truck(self, distance_calculator, warehouse):
        #Initialize first delivery
        self.current_deliveries[0] = distance_calculator.get_next_package(warehouse.package_hash, "HUB")
        #return if no packages are available to load
        if self.current_deliveries[0] == None:
            return
        self.current_deliveries[0].status = "En Route - " + self.name
        #load subsequent deliveries until truck is full or all pakcgaes are loaded
        index = 1
        while index < 16:
            previous_address = self.current_deliveries[index - 1].address
            next_package = distance_calculator.get_next_package(warehouse.package_hash, previous_address)
            if next_package is None:
                #all available packages are loaded, return to hub after
                distance_to_hub = distance_calculator.distance_to_hub(self.current_deliveries[index - 1].address)
                self.current_deliveries[index - 1].distance_from_last_location = distance_to_hub
                self.current_deliveries[index - 1].status = "En Route - " + self.name
                break
            elif index == 15:
                #truck is full, return to hub after
                distance_to_hub = distance_calculator.distance_to_hub(next_package.address)
                next_package.distance_from_last_location = distance_to_hub
                next_package.status = "En Route - " + self.name
                self.current_deliveries[index] = next_package
                break
            else:
                #normal loading procedure
                next_package.status = "En Route - " + self.name
                self.current_deliveries[index] = next_package
                index += 1

    def make_deliveries_(self, delivered_packages):
        index = 0
        while index < 16:
            if self.current_deliveries[index] is None:
                break
            else:
                delivery_index = self.current_deliveries[index].package_id - 1
                self.total_milage += self.current_deliveries[index].distance_from_last_location
                delivered_packages[delivery_index] = self.current_deliveries[index]
                delivered_packages[delivery_index].status = "Delivered"
                del self.current_deliveries[index]
                index += 1

    def make_deliveries(self, delivered_packages, distance_calculator):
        index = 0
        while index < 16:
            if self.current_deliveries[index] is None:
                break
            else:
                current_delivery = self.current_deliveries[index]
                travel_time = distance_calculator.time_distance_calculator(current_delivery.distance_from_last_location)
                self.total_milage += current_delivery.distance_from_last_location
                self.current_time += datetime.timedelta(minutes=travel_time)
                current_delivery.delivery_time = self.current_time
                current_delivery.status = "Delivered"
                delivery_index = self.current_deliveries[index].package_id - 1

                delivered_packages[delivery_index] = current_delivery
                del self.current_deliveries[index]

                index += 1

    def print_pending_packages(self):
        index = 0
        while index < 16:
            if self.current_deliveries[index] == None:
                index += 1
            else:
                print(self.current_deliveries[index])
                index += 1