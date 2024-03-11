from package import Package
from hash_table import HashTable

package_hash = HashTable(capacity=40)

p1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", "84115", "10:30 AM", "21")

p2 = Package(2,"2530 S 500 E","Salt Lake City","UT","84106","EOD","44")

package_hash[1] = p1
package_hash[2] = p2

print(package_hash[1].package_id)

print(package_hash[2].deadline)