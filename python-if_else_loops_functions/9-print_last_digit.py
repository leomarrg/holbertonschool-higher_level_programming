#!/usr/bin/env python3
def print_last_digit(number):
        lastDig = abs(number) % 10

        if number < 0:
            return -lastDig
        else:
            return lastDig