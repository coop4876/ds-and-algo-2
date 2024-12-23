import datetime
from hash_table import HashTable

class Truck:
    def __init__(self, name):
        self.name = name
        self.current_time = datetime.datetime(year= 2024, month= 3, day= 15, hour=8, minute=0)
        self.total_milage = 0
        self.current_deliveries = HashTable(capacity=16)
        self.distance_after_last_package = 0
        self.package_whitelist = []
        self.first_package = []
        self.truck_capacity = 16

    #load packages into truck based on whitelist, selecting the next closest highest priority package for next delivery
    def load_truck(self, distance_calculator, warehouse):
        print("Loading: ", self.name)
        print("Time:    ", self.current_time)
        #build whitelist for possible deliveries this trip
        self.build_package_whitelist(warehouse)
        #Initialize first delivery
        self.current_deliveries[0] = distance_calculator.get_next_package(warehouse.package_hash, "HUB", self)
        #return if no packages are available to load
        if self.current_deliveries[0] == None:
            return
        self.first_package.append(self.current_deliveries[0].package_id)
        self.current_deliveries[0].status = "En Route - " + self.name
        #load subsequent deliveries until truck is full or all packages are loaded
        index = 1
        while index < self.truck_capacity:
            previous_address = self.current_deliveries[index - 1].address
            next_package = distance_calculator.get_next_package(warehouse.package_hash, previous_address, self)
            #all available packages are loaded, return to hub after
            if next_package is None:
                distance_to_hub = distance_calculator.distance_to_hub(self.current_deliveries[index - 1].address)
                self.distance_after_last_package = distance_to_hub
                break
            #truck is full, return to hub after
            elif index == 15:
                next_package.status = "En Route - " + self.name
                self.current_deliveries[index] = next_package
                distance_to_hub = distance_calculator.distance_to_hub(next_package.address)
                self.distance_after_last_package = distance_to_hub
                self.current_deliveries[index - 1].next_package_pointer = self.current_deliveries[index].package_id
                break
            else:
                #normal loading procedure
                next_package.status = "En Route - " + self.name
                self.current_deliveries[index] = next_package
                self.current_deliveries[index - 1].next_package_pointer = self.current_deliveries[index].package_id
                index += 1

    #deliver packages in load order, update milage and time, remove packages from current_deliveries and add to delivered_packages
    def make_deliveries(self, delivered_packages, distance_calculator):
        print("Making Deliveries: ", self.name)
        print("------------------------------------------------------------------------")
        print("Departing HUB @ " + str(self.current_time.strftime('%H:%M:%S')))
        index = 0
        while index < self.truck_capacity:
            #after last package on non-full truck
            if self.current_deliveries[index] is None:
                #update milage
                self.total_milage += self.distance_after_last_package
                #update current time
                travel_time = distance_calculator.time_distance_calculator(self.distance_after_last_package)
                self.current_time += datetime.timedelta(minutes=travel_time)
                print("Returning to HUB")
                return
            else:
                #get current delivery
                current_delivery = self.current_deliveries[index]
                #update travel time, total_milage, and current_time
                travel_time = distance_calculator.time_distance_calculator(current_delivery.distance_from_last_location)
                self.total_milage += current_delivery.distance_from_last_location
                self.current_time += datetime.timedelta(minutes=travel_time)
                #print delivery message
                print("Delivering package ID {:02d}".format(current_delivery.package_id)  + " @ " + str(self.current_time.strftime('%H:%M:%S')) + " to " + str(current_delivery.address))
                #update package attributes
                current_delivery.delivery_time = self.current_time
                current_delivery.status = "Delivered - " + self.name
                #get delivered package index and write to delivered packages hash table
                delivery_index = self.current_deliveries[index].package_id - 1
                delivered_packages[delivery_index] = current_delivery
                #remove from current deliveries
                del self.current_deliveries[index]
                #continue to next loop/package
                index += 1
        #update milage for trip back to hub
        self.total_milage += self.distance_after_last_package
        print("Returning to HUB")
        #update hub arrival time
        travel_time = distance_calculator.time_distance_calculator(self.distance_after_last_package)
        self.current_time += datetime.timedelta(minutes=travel_time)

    #build package whitelist filled with sublists based on delivery deadlines load/deliver based on priority
    def build_package_whitelist(self, warehouse):
        #initialize priority lists
        p0 = []
        p1 = []
        p2 = []
        #add priority lists to whitelist
        self.package_whitelist = [p0, p1, p2]
        #set conditions to compare against for note cases
        loaded_or_delivered = ["En Route - Truck 1", "En Route - Truck 2", "Delivered - Truck 1", "Delivered - Truck 2"]
        group_delivery = ["Must be delivered with 15, 19", "Must be delivered with 13, 19", "Must be delivered with 13, 15"]
        #set package delay time
        delay_time = datetime.datetime(year= 2024, month= 3, day= 15, hour=9, minute=5)
        #set address correction time
        correct_address_time = datetime.datetime(year= 2024, month= 3, day= 15, hour=10, minute=20)
        index = 0
        while index < warehouse.package_hash.size:
            #set delivery priority
            if warehouse.package_hash[index].deadline == "9:00 AM":
                priority = 0
            elif warehouse.package_hash[index].deadline == "10:30 AM":
                priority = 1
            else:
                priority = 2
            #handle different notes cases
            #Case: already loaded or delivered
            if warehouse.package_hash[index].status in loaded_or_delivered:
                pass
            #Case: no notes
            elif warehouse.package_hash[index].status == "At Hub":
                self.package_whitelist[priority].append(index)
            #Case: can only be on truck 2
            elif(warehouse.package_hash[index].notes == "Can only be on truck 2" and \
                    self.name == "Truck 2"):
                self.package_whitelist[priority].append(index)
            #Case: package delayed until 9:05
            elif(warehouse.package_hash[index].notes == "Delayed on flight---will not arrive to depot until 9:05 am" and \
                    self.current_time >= delay_time):
                self.package_whitelist[priority].append(index)
            #Case: package with wrong address, corrected at 10:20
            elif(warehouse.package_hash[index].notes == "Wrong address listed" and \
                    self.current_time >= correct_address_time):
                warehouse.package_hash[index].address = "410 S State St (84111)"
                self.package_whitelist[priority].append(index)
            #Case: group of packages that have to be delivered together, 10:30 deadline so
            elif warehouse.package_hash[index].notes in group_delivery:
                self.package_whitelist[1].append(index)
            index += 1

    #pass time on truck, needed for packages that don't arrive At Hub until later in day
    def pass_time(self, minutes_to_pass):
        self.current_time += datetime.timedelta(minutes=minutes_to_pass)

    #print packages currently on delivery route
    def print_pending_packages(self):
        index = 0
        trip_milage = 0
        print("------------------------- Packages on ", self.name, "-------------------------")
        while index < self.truck_capacity:
            if self.current_deliveries[index] == None:
                index += 1
            else:
                trip_milage += self.current_deliveries[index].distance_from_last_location
                print(self.current_deliveries[index])
                index += 1
        trip_milage += self.distance_after_last_package
        print("------------------------------------------------------------------------")
        print("Start Time:     ", self.current_time.strftime('%H:%M:%S %p'))
        print("Current Milage: ", self.total_milage)
        print("Trip Milage:    ", trip_milage)
        print("------------------------------------------------------------------------")
