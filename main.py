from package import Package
from location import Location
from hash_table import HashTable

package_location = 'data\packages.csv'

l1 = Location("HUB")
l2 = Location("1060 Dalton Ave S (84104)")

print(l1.address)
print(l2.address)



# package_hash = Package.build_package_hash_from_csv(package_location)


# print(package_hash[0].address)

# print(package_hash[1].address)