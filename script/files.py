#!/usr/bin/env python

# file = open("test.txt","w")
# file.write("testing!")
# file.close()


# file = open("test.txt","r")
# content = file.read()
# print content
# file.close()


# file=open("test.txt","a")
# file.write("\nThis goes to the next line!")
# file.close()


# with open("test.txt", 'w') as file:
#     file.write("The with method!")


# import os
#
# fullpath = "/Users/vai/fun/block-python/script/files.py"
# filename = os.path.basename(fullpath)
#
# print filename
# print os.path.splitext(filename)
# print os.path.exists(fullpath)
#
# if not os.path.exists(fullpath):
#     os.path.mkdir(fullpath)


import glob
import os

rawlist = glob.glob("*.txt")

print rawlist

for file in rawlist:
    filename = os.path.splitext(file)[0]
    newname = filename + ".zip"
    os.rename(file, newname)
