from package import Package
from location_and_distance import DataLoader, DistanceCalculator

location_file_path = 'data/location.csv'
distance_file_path = 'data/distance.csv'

data_loader = DataLoader(location_file_path, distance_file_path)
data_loader.load_data()

distance_calculator = DistanceCalculator(data_loader.location_data, data_loader.distance_data)

start_address = '1060 Dalton Ave S (84104)'
end_address = '195 W Oakland Ave (84115)'

distance = distance_calculator.get_distance(start_address, end_address)

package_hash = Package.build_package_hash_from_csv()

print(distance)



for x in range(len(package_hash)):
    print(package_hash[x].address)