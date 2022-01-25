from case_study_part8_functions import search_pax, filter_pax, format_pax, read_pax_json, write_pax_to_db

pax_list = read_pax_json("pax_list.json")

while True:
    option = input("Enter 's' for search or 'f' for filter: ")

    if option == 's':
        try:
            Id = int(input("Please enter a user ID "))  
        except:
            print("Invalid input: user ID must be an integer")
        else:
            pax = search_pax(pax_list, Id)
            if pax:
                print(pax["fname"], pax["lname"])
            else:
                print("Passenger not found")

    if option == 'f':
        filter_field = input("Please enter the field you which to filter by: ")
        filter_value = input("Please enter the value you which to filter by: ")

        if filter_field == "checked_bags":
            if filter_value == "True":
                filter_value = True
            else:
                filter_value = False
            print(f"filter_value: {filter_value}")
        elif filter_field == "flight_time":
            try:
                filter_value = float(filter_value)
            except:
                print("Invalid input: flight time must be a number")
                continue

        matching_passengers = filter_pax(pax_list, filter_field, filter_value)

        if matching_passengers:
            matching_passengers.sort(key=lambda p: p["lname"])
            print(format_pax(matching_passengers))
            to_db = input("Would you like to write the passengers to the database? y/n: ")
            if to_db == 'y':
                write_pax_to_db(matching_passengers)
        else:
            print("No matching passengers found")

    more = input("Enter 'y' to continue searching/filtering or 'n' to stop: " )
    if more == "n":
        print("Ending program, thank you")
        break