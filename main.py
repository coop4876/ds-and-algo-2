from package import Package
from hash_table import HashTable
from csv_reader import package_hash_from_csv

package_hash = package_hash_from_csv('data\packages.csv')

print(package_hash[1].package_id)

print(package_hash[2].deadline)