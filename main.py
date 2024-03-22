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

    truck_1 = Truck("Truck 1")
    truck_2 = Truck("Truck 2")
    deliveries = DeliveredPackages()

    truck_1.load_truck(distance_calculator, warehouse)
    truck_2.pass_time(65)
    truck_2.load_truck(distance_calculator, warehouse)

    print("**********packages on Truck 1")
    truck_1.print_pending_packages()

    print("**********packages on Truck 2")
    truck_2.print_pending_packages()

    truck_1.make_deliveries(deliveries.delivered_packages, distance_calculator)
    truck_2.make_deliveries(deliveries.delivered_packages, distance_calculator)

    truck_2.load_truck(distance_calculator, warehouse)
    truck_2.make_deliveries(deliveries.delivered_packages, distance_calculator)

    # truck_1.load_truck(distance_calculator, warehouse)
    # # truck_1.make_deliveries(deliveries.delivered_packages, distance_calculator)
    # truck_2.load_truck(distance_calculator, warehouse)
    # # truck_2.make_deliveries(deliveries.delivered_packages, distance_calculator)

    print("**********packages still in warehouse")
    warehouse.print_warehouse_packages()

    print("**********delivered packages")
    deliveries.print_delivered_packages()

    print("truck_1 milage: ", truck_1.total_milage)
    print("truck_1 time: ", truck_1.current_time)

    print("truck_2 milage: ", truck_2.total_milage)
    print("truck_2 time: ", truck_2.current_time)


if __name__ == "__main__":
    main()