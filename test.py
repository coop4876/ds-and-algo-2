import datetime
from location_and_distance import DistanceCalculator, LocationAndDistanceLoader

#set paths to data files
location_file_path = 'data/location.csv'
distance_file_path = 'data/distance.csv'
package_file_path = 'data/packages.csv'

#initialize LocationAndDistanceLoader and load data from csv files
data_loader = LocationAndDistanceLoader(location_file_path, distance_file_path)
data_loader.load_location_and_distance()

#initialize DistanceCalculator
distance_calculator = DistanceCalculator(data_loader.location_data, data_loader.distance_data)


test_milage = 8

time_delta = distance_calculator.time_distance_calculator(test_milage)

print(time_delta)

time = datetime.datetime(year= 2024, month= 3, day= 15, hour=8, minute=0)

print(time)

time += datetime.timedelta(minutes=time_delta)

print(time)