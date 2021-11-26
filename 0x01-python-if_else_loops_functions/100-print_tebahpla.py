#!/usr/bin/python3

for a in range(0, 26):
    if a % 2 == 0:
        print("{:c}".format(122 - a))
    else:
        print("{:c}".format(90 - a))
