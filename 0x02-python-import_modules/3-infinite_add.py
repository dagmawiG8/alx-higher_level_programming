#!/usr/bin/python3
import sys

if __name__ = "__main__":
    i = 0;
    result = 0;

    for argument in sys.argv:
        if i != 0:
            result += int(argument)
        else:
            i++;

    print("{:d}".format(result))
else:
    exit();
