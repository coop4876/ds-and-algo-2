class Package:
    def __init__(self,package_id, address, city, state, zip, deadline, weight, notes=""):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes


p1 = Package(1, "195 W Oakland Ave" , "Salt Lake City" , "UT" , "84115" , "10:30 AM",21, "test note")

print(p1.notes)