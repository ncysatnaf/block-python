#!/usr/bin/env python

def baka():
    return 9

def biggest32():
    return 2147483647, -2147483647

def main():
    cirno = baka()
    print cirno

    max, min = biggest32()
    print max, min

    all = biggest32()
    print all

if __name__ == "__main__":
    main()
