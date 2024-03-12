import csv
from hash_table import HashTable

class Location:
    def __init__(self, address):
        self.address = address


    @classmethod
    def build_distance_and_location_hash(cls, location_file_path, distance_file_path):
        index = 0
        with open(distance_file_path) as distance_csv:
            distance_csv = list(csv.reader(distance_csv))
        location_hash = HashTable(capacity=27)
        with open(location_file_path) as location_csv:
            location_csv_reader = csv.reader(location_csv)
            next(location_csv_reader) #skip header
            for row in location_csv_reader:
                address = row[1]
                cls.distances_from_indexed_location(index, distance_csv)
                location = cls(address)
                location_hash [index] = location
                index += 1
        return location_hash
    
    @staticmethod
    def distances_from_indexed_location(index, distance_list):
        target_index = 0
        #for loop to iterate throuhg all indexes
        #create and write to list/touple/hash?
        distance = distance_list[index][target_index]
        if distance == ',':
            distance = distance_list[target_index][index]
        
        pass
