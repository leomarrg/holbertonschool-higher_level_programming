#!/usr/bin/python3
def pow(a, b):
    if b > 0:
        result = 1
        for i in range(abs(b)):
            result *= a
        return result
    elif b < 0:
        result = 1
        for i in range(abs(b)):
            result /= a
        return result
    else:
        return 1