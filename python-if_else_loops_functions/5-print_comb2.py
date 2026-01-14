#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        print("{:2}".format(i), end=", ")
    else:
        print("{:2}".format(i))
