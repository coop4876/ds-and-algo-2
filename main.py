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

truck_1 = Truck()
truck_2 = Truck()
deliveries = DeliveredPackages()

truck_1.load_truck(distance_calculator, warehouse)
truck_2.load_truck(distance_calculator, warehouse)

truck_1.make_deliveries(deliveries.delivered_packages)
truck_2.make_deliveries(deliveries.delivered_packages)

truck_1.load_truck(distance_calculator, warehouse)
truck_1.make_deliveries(deliveries.delivered_packages)

print("**********packages on truck_1")
truck_1.print_pending_packages()

print("**********packages on truck_2")
truck_2.print_pending_packages()

print("**********packages still in warehouse")
warehouse.print_warehouse_packages()

print("**********delivered packages")
deliveries.print_delivered_packages()

print("truck_1 milage: ", truck_1.total_milage)

print("truck_2 milage: ", truck_2.total_milage)