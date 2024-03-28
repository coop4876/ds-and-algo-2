#Ian Cooper - Studnet ID: 011018309
from location_and_distance import LocationAndDistanceLoader, DistanceCalculator
from truck import Truck
from warehouse import Warehouse
from delivered_packages import DeliveredPackages
from interface import UserInterface, MainOutputCapture

def main():
    #capture main() output so it can be displayed from user_interface
    with MainOutputCapture() as main_output:
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

        #initialize truck_1, truck_2, and delivered_packages
        truck_1 = Truck("Truck 1")
        truck_2 = Truck("Truck 2")
        delivered_packages = DeliveredPackages()

        #print initial state - no packages loaded yet
        warehouse.print_warehouse_packages()

        #load truck 1 and print result
        truck_1.load_truck(distance_calculator, warehouse)
        truck_1.print_pending_packages()

        #truck 2 waits until 9:05 so delayed packages are available for loading
        truck_2.pass_time(65)
        #load truck 2 and print results
        truck_2.load_truck(distance_calculator, warehouse)
        truck_2.print_pending_packages()

        #send truck 1 for deliveries, print delivered package list after
        truck_1.make_deliveries(delivered_packages.delivered_packages, distance_calculator)
        delivered_packages.print_delivered_packages()

        #send truck 2 for deliveries, print delivered package list after
        truck_2.make_deliveries(delivered_packages.delivered_packages, distance_calculator)
        delivered_packages.print_delivered_packages()

        #print remaining packages At Hub
        warehouse.print_warehouse_packages()

        #second load on truck 2, print results
        truck_2.load_truck(distance_calculator, warehouse)
        truck_2.print_pending_packages()

        #print packages still At Hub to show they're all delivered on en route
        warehouse.print_warehouse_packages()

        #send truck 2 for deliveries
        truck_2.make_deliveries(delivered_packages.delivered_packages, distance_calculator)

        #print delivered package hash table after all packages have been delivered
        delivered_packages.print_delivered_packages()

        #print final milage and time stats for both trucks and combined milage
        with MainOutputCapture() as final_output:
            print("------------------------------------------------------------------------")
            print("Final Milage and Times".center(68))
            print("Truck 1 Milage: ", truck_1.total_milage)
            print("Truck 1 Time:   ", truck_1.current_time.strftime('%H:%M:%S'))
            print("Truck 2 Milage: ", truck_2.total_milage)
            print("Truck 2 Time:   ", truck_2.current_time.strftime('%H:%M:%S'))
            print("Total Milage:   ", truck_1.total_milage + truck_2.total_milage)
            print("------------------------------------------------------------------------")

    print("\n".join(final_output))

    #create list of trucks to pass to user_interface
    trucks = [truck_1, truck_2]
    #initialize user_interface
    user_interface = UserInterface(main_output, final_output, delivered_packages, trucks)
    #allow user interaction
    user_interface.get_input()

#run main()
if __name__ == "__main__":
        main()
