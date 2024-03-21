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
        self.distance_from_last_location = 0
        self.delivery_time = "N/A"

    def __str__(self):
        if self.notes == '':
            print_string = 'package ID: ' + str(self.package_id) \
                + ' | package status: ' + str(self.status) \
                + ' | delivery address: ' + str(self.address) \
                + ' | distance from last location: ' + str(self.distance_from_last_location) \
                + ' | delivery time: ' +str(self.delivery_time) \
                + ' | deadline: ' +str(self.deadline)
        else:
            print_string = 'package ID: ' + str(self.package_id) \
                + ' | package status: ' + str(self.status) \
                + ' | Note: ' + str(self.notes) \
                + ' | delivery address: ' + str(self.address) \
                + ' | delivery time: ' +str(self.delivery_time) \
                + ' | deadline: ' +str(self.deadline)
        return print_string