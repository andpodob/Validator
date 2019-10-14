import sys
import os
from subprocess import Popen, PIPE


solutions = ""
script = ""
expected = "0"


if len(sys.argv) < 3:
    print("Not eanugh args!")
    sys.exit()

if not os.path.isdir(sys.argv[1]):
    print("The solutions path is incorrect!")
    sys.exit()
else:
    solutions = sys.argv[1]

if not os.path.isfile(sys.argv[2]) or not sys.argv[2].endswith(".py"):
    print("The script path is incorrect or script is not a python script!")
    sys.exit()
else:
    script = sys.argv[2]


for filename in os.listdir(solutions):
    path = solutions+filename
    fp = open(path)
    first_line = fp.readline()
    #fp.close()
    if first_line[0] == 'c':
        expected = ''.join(filter(str.isdigit, first_line))
        output = Popen(["python",sys.argv[2], path],stdout=PIPE)
        response = int(output.communicate()[0])
        expected = int(expected)
        if response == expected:
            print("Accepted on: ", path)
        else:
            print("Failed on: ", path)
        

        