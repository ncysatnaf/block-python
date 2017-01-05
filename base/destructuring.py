#!/usr/bin/env python

def yuyuko_feed(*foods):
    for food in foods:
        print "yuyuko are eating " + food

def main():
    yuyuko_feed("dumpling", "lamian", "sushi")

    yuyuko_feed(*["tempura", "takoyaki", "curry", "stateliness"])


if __name__ == "__main__":
    main()
