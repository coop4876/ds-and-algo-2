class Package:
    def __init__(self,package_id, address, city, state, zip_code, deadline, weight, status, notes="",):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        #todo special case for package not yet in warehouse
        self.status = status
        self.delivery_time = "N/A"
        self.distance_to_next_location = 0
        self.delivery_time = "N/A"

    def __str__(self):
        print_string = 'package ID: ' + str(self.package_id) \
            + ' | package status: ' + str(self.status) \
            + ' | delivery address: ' + str(self.address) \
            + ' | distance to next location: ' + str(self.distance_to_next_location) \
            + ' | delivery time: ' +str(self.delivery_time)
        return print_string

