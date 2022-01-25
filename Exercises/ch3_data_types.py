id = 1234
first_name = "John"
last_name = "Doe"
checked_bags = False
visited_countries = ["Lativa", "Guyana", "Yemen", "Uzbekistan"]
flight = {
    "Outbound":"LGW",
    "Inbound": "CDG"
}
flight_time = 1.25

print(
    "ID:", id, type(id), 
    "\nFirst name:", first_name, type(first_name), 
    "\nLast name:", last_name, type(last_name), 
    "\nChecked bags:", checked_bags, type(checked_bags), 
    "\nVisited countries:", visited_countries, type(visited_countries), 
    "\nFlight:", flight, type(flight), 
    "\nFlight time:", flight_time, type(flight_time)
)
