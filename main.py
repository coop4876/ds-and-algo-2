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

    warehouse.print_warehouse_packages()

    truck_1.load_truck(distance_calculator, warehouse)
    truck_2.pass_time(65)
    truck_2.load_truck(distance_calculator, warehouse)

    truck_1.print_pending_packages()

    truck_2.print_pending_packages()

    truck_1.make_deliveries(deliveries.delivered_packages, distance_calculator)
    deliveries.print_delivered_packages()

    truck_2.make_deliveries(deliveries.delivered_packages, distance_calculator)
    deliveries.print_delivered_packages()

    warehouse.print_warehouse_packages()

    truck_2.load_truck(distance_calculator, warehouse)

    truck_2.print_pending_packages()

    truck_2.make_deliveries(deliveries.delivered_packages, distance_calculator)

    warehouse.print_warehouse_packages()

    deliveries.print_delivered_packages()

    print("------------------------------------------------------------------------")
    print("Final Milage and Times:")
    print("Truck 1 Milage: ", truck_1.total_milage)
    print("Truck 1 Time:   ", truck_1.current_time)

    print("Truck 2 Milage: ", truck_2.total_milage)
    print("Truck 2 Time:   ", truck_2.current_time)

    print("Total Milage:   ", truck_1.total_milage + truck_2.total_milage)
    print("------------------------------------------------------------------------")

    print(warehouse.package_lookup(15))

if __name__ == "__main__":
    main()