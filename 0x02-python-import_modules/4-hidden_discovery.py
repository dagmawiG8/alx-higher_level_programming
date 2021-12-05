#!/usr/bin/python3
import hidden_4 as hiddenfile
import sys

if __name__ != "__main__":
    exit()

for hiddennames in dir(hiddenfile):
    if hiddennames[0:2] != "__":
        print("{}".format(hiddennames))
