import csv

class LocationAndDistanceLoader:
    def __init__(self, location_file_path, distance_file_path):
        self.location_file_path = location_file_path
        self.distance_file_path = distance_file_path
        self.location_data = None
        self.distance_data = None
        

    #load distance and location files
    def load_location_and_distance(self):
        with open(self.location_file_path, 'r') as location_file:
            self.location_data = list(csv.reader(location_file, delimiter=','))
        with open(self.distance_file_path, 'r') as distance_file:
            self.distance_data = list(csv.reader(distance_file, delimiter=','))

class DistanceCalculator:
    def __init__(self, location_data, distance_data):
        self.location_data = location_data
        self.distance_data = distance_data

    #get distance from start_address to end_address
    def get_distance(self, start_address, end_address):
        start_index = None
        end_index = None
        #find start and end address indices
        for current_index in range(len(self.location_data)):
            if self.location_data[current_index][1] == start_address:
                start_index = current_index
            if self.location_data[current_index][1] == end_address:
                end_index = current_index
        #distances are in a symmetric list so if [start_index][end_index] 
        #is empty value is in [end_index][start_index]
        if self.distance_data[start_index][end_index] == '':
            distance = self.distance_data[end_index][start_index]
        else:
            distance = self.distance_data[start_index][end_index]
        return float(distance)

    #find next closest package in highest priority whitelist
    def get_next_package(self, undelivered_packages, start_location, truck):
        #set max distance for initial comparison
        distance = float('inf')
        #find highest priority non-empty package sub-whitelist
        priority = 0
        while priority < 2:
            if truck.package_whitelist[priority] != []:
                break
            else:
                priority += 1
        if truck.package_whitelist[priority] == []:
            return
        #iterate through non-empty sublist to find next closest package
        index = 0
        sublist_length = len(truck.package_whitelist[priority])
        while index < sublist_length:
            #set the package to test distance
            test_package = truck.package_whitelist[priority][index]
            #get package address
            end_location =  undelivered_packages[test_package].address
            #find distance from last package to test_package
            test_distance = self.get_distance(start_location, end_location)
            #if distance is less then current lowest, set next_package to current_package and update distance
            if test_distance < distance:
                next_package = undelivered_packages[test_package]
                distance = test_distance
            #move to next package in sublist
            index += 1
        #set distance, load_time, and loaded_on_truck on closest package
        next_package.distance_from_last_location = distance
        next_package.load_time = truck.current_time
        next_package.loaded_on_truck = truck.name
        #remove package from whitelist and return
        truck.package_whitelist[priority].remove(next_package.package_id - 1)
        return next_package

    #get distance for trip back to HUB from last package
    def distance_to_hub(self, previous_address):
        distance_to_hub = self.get_distance(previous_address, "HUB")
        return distance_to_hub

    #convert distance traveled to time passed for time tracking
    #trucks move at constant 18mph
    def time_distance_calculator(self, distance_traveled):
        time_passed = distance_traveled / 18 * 60
        return float(time_passed)