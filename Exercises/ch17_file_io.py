studentsfile = "students.dat"
file_read_ref = open(studentsfile, "r")

results = []

for name in file_read_ref:
    name = name.rstrip('\n')
    grade = input(f"Please enter a grade for {name}: ")
    entry = f"{name}, {grade}"
    results.append(entry)
    #  results.append((name, grade))
 
file_read_ref.close()
print(results)

studentsgrades = "studentsgrades.txt"
file_write_ref = open(studentsgrades, "w")

for entry in results:
    file_write_ref.write(entry + '\n')
    # file_write_ref.write(f"{name}, {grade} \n")

file_write_ref.close()