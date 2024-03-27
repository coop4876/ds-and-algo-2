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
        self.status = status
        self.load_time = "N/A"
        self.loaded_on_truck = "N/A"
        self.delivery_time = "N/A"
        self.distance_from_last_location = 0
        self.next_package_pointer = None

    #define print method for packages
    def __str__(self):
        status_check = ["At Hub - Notes", "At Hub", "En Route - Truck 1", "En Route - Truck 2"]
        #if package is delivered, add delivery time to status
        if self.status not in status_check:
            status_string = str(self.status) + " @ " + str(self.delivery_time.strftime('%H:%M:%S'))
        else:
            status_string = str(self.status)
        #print value headers and values specifc to package formatted to fill a consistent table
        print_string = 'Package ID: {:02d}'.format(self.package_id) \
            + ' | Package Weight: {:02}'.format(self.weight) \
            + ' | Package Status: {:<30s}'.format(status_string) \
            + ' | Deadline: {:<8s}'.format(str(self.deadline)) \
            + ' | Delivery Address: {:<46s}'.format(str(self.address)) \
            + ' | Notes: ' + str(self.notes)
        return print_string