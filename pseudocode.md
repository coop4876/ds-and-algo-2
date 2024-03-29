function get_next_package(undelivered_packages, start_location, truck):

    #set highest value possible for comparison so any package will be closer
    ASSIGN float('inf') to comparison_distance
    #iterate through each sub-list in whitelist to find first non-empty list and then exit for each
    FOR EACH sublist in truck.whitelist
        if sublist is not empty
            ASSIGN to current_sublist
            END Foreach 

    #iterate through each package in the selected whitelist
    FOR EACH package in current_sublist
        #if the distance is less than the comparison distance, set it to next_package
        if distance_from_start_location is less than comparison_distance
            ASSIGN package to next_package
            ASSIGN distance_from_start_location to comparison_distance

    #once closest package has been found
    #update package properties
    UPDATE package.distance_from_last_location to comparison_distance
    UPDATE package.load_time to truck.current_time
    UPDATE package.loaded_on_truck to truck.name
    #remove it from the whitelist so it is not selected again
    REMOVE package from current_sublist
    #return the package to truck for loading
    RETURN package
    