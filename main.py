from package import Package
from location_and_distance import LocationAndDistanceLoader, DistanceCalculator

#set paths to data files
location_file_path = 'data/location.csv'
distance_file_path = 'data/distance.csv'

#initialize DataLoader and load data
data_loader = LocationAndDistanceLoader(location_file_path, distance_file_path)
data_loader.load_location_and_distance()

#initialize DistanceCalculator
distance_calculator = DistanceCalculator(data_loader.location_data, data_loader.distance_data)

package_hash = Package.build_package_hash_from_csv()




start_address = '1060 Dalton Ave S (84104)'
end_address = '195 W Oakland Ave (84115)'

distance = distance_calculator.get_distance(start_address, end_address)


print(distance)

#print all package addresses
for x in range(len(package_hash)):
    print(package_hash[x].address)