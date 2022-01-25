name = "Francesca" # Creating a string object in memory
age = 25 # References an integer object
job = input("What is your job?: ") # Input function always returns a string

print(name, age, job)
print("Name:", name, "\nAge:", age, "\nJob:", job, sep="\t") # The sep changes the default arg separator in the print statement
print(f"Hello {name}, you are {age} years old and you are a {job}")
# Print function automatically adds a new lineto the end of the printed string