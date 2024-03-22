import csv

class LocationAndDistanceLoader:
    def __init__(self, location_file_path, distance_file_path):
        self.location_file_path = location_file_path
        self.distance_file_path = distance_file_path
        self.location_data = None
        self.distance_data = None
        

    def load_location_and_distance(self):
        with open(self.location_file_path, 'r') as location_file:
            self.location_data = list(csv.reader(location_file, delimiter=','))

        with open(self.distance_file_path, 'r') as distance_file:
            self.distance_data = list(csv.reader(distance_file, delimiter=','))

class DistanceCalculator:
    def __init__(self, location_data, distance_data):
        self.location_data = location_data
        self.distance_data = distance_data

    def get_distance(self, start_address, end_address):
        start_index = None
        end_index = None
        for current_index in range(len(self.location_data)):
            if self.location_data[current_index][1] == start_address:
                start_index = current_index
            if self.location_data[current_index][1] == end_address:
                end_index = current_index
        if self.distance_data[start_index][end_index] == '':
            distance = self.distance_data[end_index][start_index]
        else:
            distance = self.distance_data[start_index][end_index]
        return float(distance)
    
    def get_next_package(self, undelivered_packages, start_location, package_whitelist):
        distance = 1000

        next_package = None
        priority = 0
        #find highest priority non-empty package sub-whitelist
        print(package_whitelist)
        while priority < 3:
            if package_whitelist[priority] != []:
                break
            else:
                priority += 1

        if priority == 3: priority = 2
        print(priority)
        if package_whitelist[priority] == []:
            return
        index = 0
        while index < (len(undelivered_packages)):
            if undelivered_packages[index].package_id - 1 in package_whitelist[priority]:
                end_location = undelivered_packages[index].address
                test_distance = self.get_distance(start_location, end_location)
                if test_distance < distance:
                    next_package = undelivered_packages[index]
                    distance = test_distance
                index += 1
                next_package.distance_from_last_location = distance
            else:
                index += 1
        package_whitelist[priority].remove(next_package.package_id - 1)
        return next_package


    def distance_to_hub(self, previous_address):
        distance_to_hub = self.get_distance(previous_address, "HUB")
        return distance_to_hub

    def time_distance_calculator(self, distance_traveled):
        time_passed = distance_traveled / 18 * 60
        return float(time_passed)