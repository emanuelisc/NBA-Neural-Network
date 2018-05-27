import csv
import re
data = ""
with open("resultsFromT1T2.txt", "r") as f:
    line = f.readline()
    counter = 0
    while len(line) > 0:
        digits =  [float(s) for s in re.findall(r'-?\d+\.?\d*', line)]
        if counter == 0:
            data += str(digits[0]) + "," + str(digits[1]) + ","
            counter += 1
        elif counter == 1:
            data += str(digits[0]) + "," + str(digits[1]) + ","
            counter += 1
        elif counter == 2:
            data += str(digits[0]) + "," + str(digits[1]) + "\n"
            counter = 0
        line = f.readline()

print(data)
with open("resultst1t2.txt", "w") as f:
    f.write(data)
