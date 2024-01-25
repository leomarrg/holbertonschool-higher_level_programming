#!/usr/bin/python3
for i in range(100):
    if (i < 10):
        print("{:02}".format(i), end = ', ')
    else:
        print("{}".format(i) if i == 99 else "{}, ".format(i), end = '\n' if i == 99 else '')
