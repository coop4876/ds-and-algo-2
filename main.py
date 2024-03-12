from package import Package
from location import Location

package_file = 'data\packages.csv'
location_file = 'data\location.csv'
distance_file = 'data\distance.csv'

location_hash = Location.build_distance_and_location_hash(location_file, distance_file)
package_hash = Package.build_package_hash_from_csv(package_file)

print(package_hash[0].address)
print(location_hash[0].address)

print(package_hash[1].address)
print(location_hash[1].address)