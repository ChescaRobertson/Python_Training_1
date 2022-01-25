from pax_list import pax_list

def search_pax(pax_list, ID):
    for person in pax_list:
        if person["id"] == ID:
            return person
    else:
        return None

def filter_pax(pax_list, filter_field, filter_value):
    matching_passengers = []

    for person in pax_list:
        if filter_field == "visited_countries":
            if filter_value in person[filter_field]:
                matching_passengers.append(person)
        elif filter_field == "source" or filter_field == "dest":
            if person["flight"][filter_field] == filter_value:
                matching_passengers.append(person)
        elif filter_field == "flight_time":
            if person[filter_field] <= (filter_value + 1) and person[filter_field] >= (filter_value - 1):
                matching_passengers.append(person)
        else:
            if person[filter_field] == filter_value:
                matching_passengers.append(person)
    return matching_passengers
     
