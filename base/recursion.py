#!/usr/bin/env python

def rec():
    print("+1s")
    if True:
        rec()

def main():
    rec()

if __name__ == "__main__":
    main()
