from pax_list import pax_list
from case_study_part3_functions import search_pax, filter_pax

while True:
    option = input("Enter 's' for search or 'f' for filter: ")

    if option == 's':
        Id = int(input("Please enter a user id: "))
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
            filter_value = float(filter_value)

        matching_passengers = filter_pax(pax_list, filter_field, filter_value)

        if matching_passengers:
            for person in matching_passengers:
                print(person["fname"], person["lname"])
        else:
            print("No matching passengers found")

    more = input("Enter 'y' to continue searching/filtering or 'n' to stop: " )
    if more == "n":
        print("Ending program, thank you")
        break