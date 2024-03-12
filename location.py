import csv
import datetime

with open('data\distance_data.csv') as csv1:
    distance_csv = list(csv.reader(csv1, delimiter=','))

with open('data\location_data.csv') as csv2:
    location_csv = list(csv.reader(csv2, delimited=','))


class Location:
    def __init__(self, address):
        self.address = address
