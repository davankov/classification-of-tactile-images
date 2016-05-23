#! /usr/bin/python3.4
import os


def fix_detector(line):
    values = line.split()
    values[16] = str((int(values[12])+int(values[13])+int(values[17]))//3)
    return ', '.join(values)

for file_name in os.listdir("raw_data"):
    with open("raw_data/" + file_name, "r") as f:
        data = [line for i, line in enumerate(f.readlines()) if i % 7 == 0]
    with open("data/" + file_name.replace("txt", "csv"), "w") as f:
        f.write(', '.join([str(number) for number in range(1, 20)]) + "\n")
        data = list(map(fix_detector, data))
        data = [line for line in data if sum(map(int, line.replace(",", "").split())) != 0]
        [f.write(line + "\n") for line in data]
    print("{} Success".format(file_name))
