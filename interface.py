
#todo add output to each package as it's delivered?

from datetime import datetime
from io import StringIO
import sys


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
                lookup_time = input("Lookup Time: ")
                #todo switch all times to 24:00, validate user input, convert to datetime object
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
        print(*p0, sep = "\n")
        print("------------------------------------------------------------------------")
        print("P1 Packages:")
        print(*p1, sep = "\n")
        print("------------------------------------------------------------------------")
        print("P2 Packages:")
        print(*p2, sep = "\n")
        print("------------------------------------------------------------------------")

    def package_time_lookup(self, package_id, time):
        #todo if time > delivery time, print package
        #todo if delivery time > time > load time print loaded on truck
        #todo if time < load time, print in warehouse
        #todo create new package object or modify print string?
        pass