birth_year = int(input("Please enter your birth year: "))

if birth_year >= 1946 and birth_year <= 1965:
    print("Baby Boomer")
elif birth_year >= 1966 and birth_year <= 1976:
    print("Generation X")
elif birth_year >= 1977 and birth_year <= 1994:
    print("Millenial")
elif birth_year >= 1995:
    print("Generation Z")
else: 
    print("Birth year out of range of program")