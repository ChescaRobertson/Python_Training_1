from pax_list import pax_list

def search_pax(pax_list, ID):
    for person in pax_list:
        if person["id"] == ID:
            return person
    else:
        return None

def filter_pax(pax_list, filter_field, filter_value):
    matching_passengers = []

    if filter_field == "visited_countries":
        matching_passengers = [p for p in pax_list if filter_value in p[filter_field]]
    elif filter_field == "source" or filter_field == "dest":
        matching_passengers = [p for p in pax_list if p["flight"][filter_field] == filter_value]
    elif filter_field == "flight_time":
        matching_passengers = [p for p in pax_list if p[filter_field] <= (filter_value + 1) and p[filter_field] >= (filter_value - 1)]
    else:
        matching_passengers = [p for p in pax_list if p[filter_field] == filter_value]

    return matching_passengers
     
def format_pax(passengers):
    rows = []
    rows.append(f"{'ID':3}  {'Last Name':10}  {'First Name':10}  {'Source':15}  {'Dest':15}")

    for person in passengers:
        rows.append(f"{person['id']:3}  {person['lname']:10}  {person['fname']:10}  {person['flight']['source']:15}  {person['flight']['dest']:15}")
    return "\n".join(rows)
