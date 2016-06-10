#! /usr/bin/python3.4
import os

types = {"stick": 1, "point": 2, "ring": 3, "uniform": 4}


def read_file(train, tpe):
    for file_name in os.listdir("data (train)_new/{}".format(tpe)):
        with open("data (train)_new/{}/".format(tpe) + file_name, "r") as f:
            for line in f.readlines()[1:]:
                if max(line) >= 50:
                    train.write(line.rstrip() + ", {}\n".format(types[tpe]))


with open("data (train)_/train_sec.csv", "w") as f:
    for tpe in types.keys():
        read_file(f, tpe)





