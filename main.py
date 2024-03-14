from package import Package, Warehouse, Truck, DeliveredPackages
from location_and_distance import LocationAndDistanceLoader, DistanceCalculator


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


print(distance_calculator.get_next_package(warehouse.undelivered_package_hash, "HUB"))


# start_address = 'HUB'
# end_address = '195 W Oakland Ave (84115)'
# distance = distance_calculator.get_distance(start_address, end_address)



# index = 0
# while index < len(warehouse.undelivered_package_hash):
#     if warehouse.undelivered_package_hash[index] != None:
#         print(warehouse.undelivered_package_hash[index])
#     index += 1

# truck_1 = Truck()
# truck_1.current_deliveries = warehouse.load_truck()

# truck_2 = Truck()
# # truck_2.current_deliveries = warehouse.load_truck()

# print("**********packages on truck_1")
# index = 0
# while index < len(truck_1.current_deliveries):
#     print(truck_1.current_deliveries[index])
#     index += 1

# print("**********packages on truck_2")
# index = 0
# while index < len(truck_2.current_deliveries):
#     print(truck_2.current_deliveries[index])
#     index += 1

# print("**********packages in warehouse")
# index = 0
# while index < len(warehouse.undelivered_package_hash):
#     if warehouse.undelivered_package_hash[index] != None:
#         print(warehouse.undelivered_package_hash[index])
#     index += 1


# # print("**********packages on truck_1")
# # for package in truck_1.current_deliveries:
# #     print(truck_1.current_deliveries[package])