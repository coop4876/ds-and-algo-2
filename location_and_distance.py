import csv
import sys


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
    
    def get_next_package(self, undelivered_packages, start_location):
        distance = 1000
        index = 0
        while index < (len(undelivered_packages) - 1):
            if undelivered_packages[index] == None:
                index += 1
            elif undelivered_packages[index].status == "In Warehouse":
                end_location = undelivered_packages[index].address
                test_distance = self.get_distance(start_location, end_location)
                if test_distance < distance:
                    next_package = undelivered_packages[index]
                    distance = test_distance
                index += 1
                next_package.distance_to_next_location = distance
            else:
                index += 1
        return next_package


    def time_distance_calculator(self, distance_traveled):
        time_passed = distance_traveled / 18 * 60
        return time_passed