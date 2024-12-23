from hash_table import HashTable

class DeliveredPackages:
    def __init__(self):
        self.delivered_packages = HashTable(capacity=40)

    #add package to delivered hash table once delivery is complete
    def add_to_delivered(self, package):
        self.delivered_packages[package.package_id] = package

    #print all packages in delivered hash table
    def print_delivered_packages(self):
        print("-------------------------- Delivered Packages --------------------------")
        index = 0
        while index < 40:
            if self.delivered_packages[index] == None:
                index += 1
            else:
                print(self.delivered_packages[index])
                index += 1
        print("------------------------------------------------------------------------")