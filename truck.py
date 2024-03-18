import datetime
from hash_table import HashTable

class Truck:
    def __init__(self, name):
        self.name = name
        self.current_time = datetime.datetime(year= 2024, month= 3, day= 15, hour=8, minute=0)
        self.total_milage = 0
        self.current_deliveries = HashTable(capacity=16)
        self.distance_after_last_package = 0
        
    def load_truck(self, distance_calculator, warehouse):
        #Initialize first delivery
        self.current_deliveries[0] = distance_calculator.get_next_package(warehouse.package_hash, "HUB")
        #return if no packages are available to load
        if self.current_deliveries[0] == None:
            return
        self.current_deliveries[0].status = "En Route - " + self.name
        #load subsequent deliveries until truck is full or all packages are loaded
        index = 1
        while index < 16:
            previous_address = self.current_deliveries[index - 1].address
            next_package = distance_calculator.get_next_package(warehouse.package_hash, previous_address)
            #all available packages are loaded, return to hub after
            if next_package is None:
                distance_to_hub = distance_calculator.distance_to_hub(self.current_deliveries[index - 1].address)
                self.distance_after_last_package = distance_to_hub
                # self.current_deliveries[index - 1].distance_from_last_location = distance_to_hub
                # self.current_deliveries[index - 1].status = "En Route - " + self.name
                break
            elif index == 15:
                #truck is full, return to hub after
                next_package.status = "En Route - " + self.name
                self.current_deliveries[index] = next_package
                distance_to_hub = distance_calculator.distance_to_hub(next_package.address)
                self.distance_after_last_package = distance_to_hub
                break
            else:
                #normal loading procedure
                next_package.status = "En Route - " + self.name
                self.current_deliveries[index] = next_package
                index += 1

    def make_deliveries(self, delivered_packages, distance_calculator):
        index = 0
        while index < 16:
            #last package on non-full truck
            if self.current_deliveries[index] is None:
                #update milage
                self.total_milage += self.distance_after_last_package
                print("distance after last: ", self.distance_after_last_package)
                #update current time
                travel_time = distance_calculator.time_distance_calculator(self.distance_after_last_package)
                self.current_time += datetime.timedelta(minutes=travel_time)
                return
            else:
                #get current delivery
                current_delivery = self.current_deliveries[index]
                #update travel time, total_milage, and current_time
                travel_time = distance_calculator.time_distance_calculator(current_delivery.distance_from_last_location)
                self.total_milage += current_delivery.distance_from_last_location
                self.current_time += datetime.timedelta(minutes=travel_time)
                #update package attributes
                current_delivery.delivery_time = self.current_time
                current_delivery.status = "Delivered"
                #get delivered package index and write to delivered packages hash table
                delivery_index = self.current_deliveries[index].package_id - 1
                delivered_packages[delivery_index] = current_delivery
                #remove from current deliveries
                del self.current_deliveries[index]
                #continue to next loop/package
                index += 1
        #update milage for trip back to hub
        self.total_milage += self.distance_after_last_package
        #update hub arrival time
        travel_time = distance_calculator.time_distance_calculator(self.distance_after_last_package)
        print("distance after last: ", self.distance_after_last_package)
        self.current_time += datetime.timedelta(minutes=travel_time)

    def print_pending_packages(self):
        index = 0
        while index < 16:
            if self.current_deliveries[index] == None:
                index += 1
            else:
                print(self.current_deliveries[index])
                index += 1
        print("Distance to HUB after last Package: ", self.distance_after_last_package)
        print("Time: ", self.current_time)