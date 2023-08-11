#!/usr/bin/python3
def uppercase(str):
    for C in str:
        if ord(C) >= 97 and ord(C) <= 122:
            C = chr(ord(C) - 32)
        print("{}".format(C), end="")
    print("")
