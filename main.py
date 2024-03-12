from package import Package

package_file = 'data/packages.csv'
location_file = 'data/location.csv'
distance_file = 'data/distance.csv'

package_hash = Package.build_package_hash_from_csv(package_file)

# print(package_hash[0].address)
# print(location_hash[0].address)

# print(package_hash[1].address)
# print(location_hash[1].address)


for x in range(len(package_hash)):
    print(package_hash[x].address + ' ' + package_hash[x].zip)