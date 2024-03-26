import datetime
from io import StringIO
import sys
import copy

#class to capture output of main() so it can be displayed as an interface option
class MainOutputCapture(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout

class UserInterface:
    def __init__(self, main_output, final_output, delivered_packages, trucks):
        self.main_output = main_output
        self.final_output = final_output
        self.delivered_packages = delivered_packages
        self.truck_list = trucks

    #prompt user for input
    def get_input(self):
        user_input = None
        while user_input != "quit":
            print("------------------------------------------------------------------------")
            print("Options:")
            print("----------")
            print("main | delivered | package | priority | trucks | final | help | quit")
            print("------------------------------------------------------------------------")
            user_input = input("Make selection:")
            #print main() output
            if user_input == "main": 
                print("\n".join(self.main_output))
            #print delivered packages hash table
            elif user_input == "delivered": 
                self.delivered_packages.print_delivered_packages()
            #lookup package status by ID and specified time
            elif user_input == "package": 
                self.package_time_lookup()
            #print EoD status of packages separated by deadline
            elif user_input =="priority": 
                self.print_priority_list()
            #print full package status for both trucks at 3 separate times, print final truck milage/times
            elif user_input =="trucks":
                self.trucks()
            elif user_input =="final":
                print("\n".join(self.final_output))
            #print details about each option to user
            elif user_input == "help": 
                self.get_help()
            #quit program
            elif user_input == "quit":
                pass
            else:#prompt for input again if invalid option entered
                print("Please make a valid selection")

    def print_priority_list(self):
        #initialize lists for each priority level
        p0 = []
        p1 = []
        p2 = []
        #loop through delivered packages and append to approproiate priority list based on deadline
        index = 0
        while index < len(self.delivered_packages.delivered_packages):
            if self.delivered_packages.delivered_packages[index].deadline == "9:00 AM":
                p0.append(self.delivered_packages.delivered_packages[index])
            elif self.delivered_packages.delivered_packages[index].deadline == "10:30 AM":
                p1.append(self.delivered_packages.delivered_packages[index])
            else:
                p2.append(self.delivered_packages.delivered_packages[index])
            index += 1
        #print headers for each list followed by the list of packages
        print("------------------------------------------------------------------------")
        print("P0 Packages:")
        print("------------------------------------------------------------------------")
        print(*p0, sep = "\n")
        print("------------------------------------------------------------------------")
        print("P1 Packages:")
        print("------------------------------------------------------------------------")
        print(*p1, sep = "\n")
        print("------------------------------------------------------------------------")
        print("P2 Packages:")
        print("------------------------------------------------------------------------")
        print(*p2, sep = "\n")
        print("------------------------------------------------------------------------")

    #recreates status of single package at user specified time
    def package_time_lookup(self):
        #prompt for package ID and convert to int
        package_id = input("Package ID: ")
        package_id = int(package_id)
        #verify package is in range and repeat input prompt if not
        while package_id > len(self.delivered_packages.delivered_packages) or package_id < 1:
            print("Enter a valid package ID ( 1 -", len(self.delivered_packages.delivered_packages), ")")
            package_id = input("Package ID: ")
            package_id = int(package_id)
        #prompt user for lookup time
        input_time = input("Lookup Time (24:00 format): ")
        #split to hours and minutes varialbel and convert to datetime object
        hours, minutes = map(int, input_time.split(":"))
        lookup_time = datetime.datetime(year= 2024, month= 3, day= 15, hour=hours, minute=minutes)
        #print header for package
        print("------------------------------------------------------------------------")
        print("Status of package ID", package_id, "at", lookup_time.strftime('%H:%M:%S'), ":")
        print("------------------------------------------------------------------------")
        #make shallow copy of package to modify
        display_package = copy.copy(self.delivered_packages.delivered_packages[package_id - 1])
        #package delivered, print EoD status (as is)
        if lookup_time > display_package.delivery_time:
            print(display_package)
        #package loaded, update status with En Route and carrying truck
        elif lookup_time > display_package.load_time:
            display_package.status = "En Route - " + display_package.loaded_on_truck
            print(display_package)
        #package not yet loaded, set status to beginning of day status (In Warehouse/In Warehouse - Notes)
        else:
            if display_package.notes != '':
                display_package.status = "In Warehouse - Notes"
            else:
                display_package.status = "In Warehouse"
            print(display_package)
        print("------------------------------------------------------------------------")

    #builds and prints truck status at 3 times specified by project requirements
    def trucks(self):
        #todo
        #8:35-9:25, 9:35-10:25, 12:03-1:12
        #go through all packages for each, if load_time < time above < delivery time, add to package list
        #linked list, add last package/nextpackage properties to package class?
        #allow user input for time
        hours = 9
        minutes = 31
        sample_time = datetime.datetime(year= 2024, month= 3, day= 15, hour=hours, minute=minutes)
        print()

        #todo clean up output, allow user to input time
        for truck in self.truck_list:
            print(truck.name)
            print(truck.first_package)
            for package in truck.first_package:
                print("new trip")
                current_package = self.delivered_packages.delivered_packages[package - 1]
                index = 0
                while index < 16:
                    if current_package.load_time <= sample_time and current_package.delivery_time <= sample_time:
                        print("Already delivered:")
                        print(current_package)
                    elif current_package.load_time <= sample_time and current_package.delivery_time > sample_time:
                        print("En Route")
                        print(current_package)
                    if current_package.next_package_pointer != None:
                        current_package = self.delivered_packages.delivered_packages[current_package.next_package_pointer - 1]
                    index += 1

    #prints additional details for each option to user
    def get_help(self):
        print("------------------------------------------------------------------------")
        print("main      | Print full main program output")
        print("delivered | Print a list of all delivered packages at EoD")
        print("package   | Select a package ID and print the status of that package at a specified time (24:00 format)")
        print("priority  | Print a list of packages at EoD grouped by delivery deadline")
        print("trucks    | Print full load details for trucks at 3 separate times and final truck milage/time stats")
        print("final     | Print final milage and time stats for each truck and total combined milage")
        print("help      | Display details on input options")
        print("quit      | Quit the program")
        print("------------------------------------------------------------------------")