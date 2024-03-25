
#todo add output to each package as it's delivered?
#todo add next location prop to package?
#todo add delivery route completion time list to trucks to rebuild delivery route for interface output?

import datetime
from io import StringIO
import sys
import copy


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
    def __init__(self, main_output, delivered_packages):
        self.main_output = main_output
        self.delivered_packages = delivered_packages

    #todo add truck option, print status at given time? might be too much extra
    def get_input(self):
        user_input = None
        while user_input != "quit":
            print("Options: main | delivered | package | priority | help | quit")
            user_input = input("Make selection:")
            if user_input == "main":
                print("\n".join(self.main_output))
            elif user_input == "delivered":
                #todo sort delivered list so they're in order of delivery time?
                self.delivered_packages.print_delivered_packages()
            elif user_input == "package":
                package_id = input("Package ID: ")
                package_id = int(package_id)
                while package_id > len(self.delivered_packages.delivered_packages):
                    print("Enter a valid package ID ( 1 -", len(self.delivered_packages.delivered_packages), ")")
                    package_id = input("Package ID: ")
                    package_id = int(package_id)
                input_time = input("Lookup Time (24:00 format): ")
                hours, minutes = map(int, input_time.split(":"))
                #todo try catch here for invalid input?
                lookup_time = datetime.datetime(year= 2024, month= 3, day= 15, hour=hours, minute=minutes)
                self.package_time_lookup(package_id, lookup_time)
            elif user_input =="priority":
                #todo time argument?
                self.print_priority_list()
            elif user_input == "help":
                #todo print more details on each option
                pass
            elif user_input == "quit":
                pass
            else:
                print("Please make a valid selection")

    def print_priority_list(self):
        p0 = []
        p1 = []
        p2 = []

        index = 0
        while index < len(self.delivered_packages.delivered_packages):
            if self.delivered_packages.delivered_packages[index].deadline == "9:00 AM":
                p0.append(self.delivered_packages.delivered_packages[index])
            elif self.delivered_packages.delivered_packages[index].deadline == "10:30 AM":
                p1.append(self.delivered_packages.delivered_packages[index])
            else:
                p2.append(self.delivered_packages.delivered_packages[index])
            index += 1

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

    def package_time_lookup(self, package_id, time):
        print("------------------------------------------------------------------------")
        print("Status of package ID", package_id, "at", time.strftime('%H:%M:%S'), ":")
        print("------------------------------------------------------------------------")
        display_package = copy.copy(self.delivered_packages.delivered_packages[package_id - 1])
        if time > display_package.delivery_time:
            print(display_package)
        elif time > display_package.load_time:
            display_package.status = "En Route - " + display_package.loaded_on_truck
            print(display_package)
        else:
            display_package.status = "In Warehouse"
            print(display_package)
        print("------------------------------------------------------------------------")