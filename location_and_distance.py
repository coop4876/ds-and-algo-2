import csv


class DataLoader:
    def __init__(self, location_file_path, distance_file_path):
        self.location_file_path = location_file_path
        self.distance_file_path = distance_file_path
        self.location_data = None
        self.distance_data = None
        

    def load_data(self):
        # with open(self.location_file_path, 'r') as location_file:
        #     self.location_data = list(csv.reader(location_file, delimiter=','))

        # with open(self.distance_file_path, 'r') as distance_file:
        #     self.distance_data = list(csv.reader(distance_file, delimiter=','))
        location_file = open(self.location_file_path, 'r')
        self.location_data = list(csv.reader(location_file, delimiter=','))
        location_file.close

        distance_file = open(self.distance_file_path, 'r')
        self.distance_data = list(csv.reader(distance_file, delimiter=','))
        distance_file.close


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
            distance = self.distance_data[start_index[end_index]]

        return distance