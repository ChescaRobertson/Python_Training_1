table = ["Bath", "Derby", "Gloucester", "Lancaster", "Newcastle", "Plymouth", "Salford", "Wakefield"]

table.remove("Newcastle")
table.insert(2, "Newcastle")

table.remove("Derby")
table.insert(3, "Derby")

table.remove('Salford')

table.append("Canterbury")

table[5] = 'York'

to_play_in_europe = table[:2]

if 'Newcastle' in to_play_in_europe:
    print('Newcastle to play in europe')

for team in table:
    print(team)