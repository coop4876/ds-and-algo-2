from location_and_distance import LocationAndDistanceLoader, DistanceCalculator
from truck import Truck
from warehouse import Warehouse
from delivered_packages import DeliveredPackages

def main():
    #set paths to data files
    location_file_path = 'data/location.csv'
    distance_file_path = 'data/distance.csv'
    package_file_path = 'data/packages.csv'

    #initialize LocationAndDistanceLoader and load data from csv files
    data_loader = LocationAndDistanceLoader(location_file_path, distance_file_path)
    data_loader.load_location_and_distance()

    #initialize DistanceCalculator
    distance_calculator = DistanceCalculator(data_loader.location_data, data_loader.distance_data)

    #initialize Warehouse and build hash table of all undelivered packages
    warehouse = Warehouse()
    warehouse.build_undelivered_package_hash_table(package_file_path)

    truck_1 = Truck("Truck1")

    truck_1.build_package_whitelist(warehouse)

    print(truck_1.package_whitelist)


main()