#!/usr/bin/env python

def main():

    life = []
    for i in range(2333):
        life.append('+1s')

    prophet = []
    prophet.extend(life)
    prophet.insert(0, '-1s')
    prophet.remove('-1s')

    print prophet


if __name__ == "__main__":
    main()
