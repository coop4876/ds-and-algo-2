from hash_table import HashTable

class DeliveredPackages:
    def __init__(self):
        self.delivered_packages = HashTable(capacity=40)

    def add_to_delivered(self, package):
        self.delivered_packages[package.package_id] = package

    def print_delivered_packages(self):
        index = 0
        while index < 40:
            if self.delivered_packages[index] == None:
                index += 1
            else:
                print(self.delivered_packages[index])
                index += 1


