#  Open NINO file for reading
#  Define a refular expression pattern for NINOs
#  Loop through the NINO file to validate all NINOs, dislpaying the console all valid NINOs
#  Write any invalid NINOs to a file called bad_NINOs.dat

from os import close
import re

ninos_file = "natinsnrs.txt"
bad_ninos = "badninos.txt"

file_read_ref = open(ninos_file, "r")
file_write_ref = open(bad_ninos, "w")

nino_pattern = "^[A-Z]{2}[0-9]{6}[A-Z]$"

for nino in file_read_ref:
    match_object = re.match(nino_pattern, nino)
    if match_object:
        nino = nino.rstrip()
        print(f"{nino}")
    else:
        file_write_ref.write(f"{nino}")

file_read_ref.close()
file_write_ref.close()