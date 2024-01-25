#!/usr/bin/python3
charCode = 61
for charCode in range(ord('a'), ord('z')):
    if (charCode == ord('q') or charCode == ord('e')):
        continue
    print(chr(charCode), end = '')