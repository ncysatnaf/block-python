#!/usr/bin/env python

import platform

def main():
    print "python " + platform.python_version()

    print "1+1 =", 1+1
    print "7.0/3.0 =", 7.0/3.0

    print True and False
    print True or False
    print not True

if __name__ == "__main__":
    main()
