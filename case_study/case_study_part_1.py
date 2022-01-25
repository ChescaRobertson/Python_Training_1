from pax_list import pax_list

while True:
    option = input("Enter 's' for search or 'f' for filter: ")

    if option == 's':
        Id = int(input("Please enter a user id: "))

        for person in pax_list:
            if Id == person["id"]:
                print(person["fname"], person["lname"])
                break
        print("Passenger not found")

    elif option == 'f':
        filter_field = input("Please enter the field you which to filter by: ")
        if filter_field == 'flight':
            flight_detail = input("Please enter if this source (source) or destination of the flight (dest): ")
        filter_value = input("Please enter the value you which to filter by: ")
        if filter_field == 'checked_bags':
            filter_value = bool(filter_value)
        if filter_field == 'flight_time':
            filter_value = float(filter_value)
    
        for person in pax_list:
            if filter_field == 'visited countries':
                if filter_value in person[filter_field] :
                    print(person["fname"], person["lname"])
            elif filter_field == 'flight': 
                if filter_value in person[filter_field][flight_detail]:
                    print(person["fname"], person["lname"])
            elif person[filter_field] == filter_value :
                print(person["fname"], person["lname"])
            else:
                print("Record not found")

    more = input("Enter 'y' to continue searching/filtering or 'n' to stop: " )
    if more == "n":
        print("Ending program, thank you")
        break