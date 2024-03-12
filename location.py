import csv

location_file = open('data/location.csv', 'r')
location_data = list(csv.reader(location_file, delimiter=','))
location_file.close

distance_file = open('data/distance.csv', 'r')
distance_data = list(csv.reader(distance_file, delimiter=','))
distance_file.close


start_address = '1060 Dalton Ave S (84104)'
end_address = "195 W Oakland Ave (84115)"

for x in range(len(location_data)):
    if location_data[x][1] == start_address:
        start_index = x
    if location_data[x][1] == end_address:
        end_index = x

if distance_data[start_index][end_index] == '':
    distance = distance_data[end_index][start_index]
else:
    distance = distance_data[start_index][end_index]

print(distance)