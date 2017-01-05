#!/usr/bin/env python

def main():
    for x in range(1, 6):
        if x % 2 == 0:
            continue
        print (x)
    for i in range(1, 10):
        if(i%5==0):
            break
        print(i)

    count = 7
    while True:
        print(count)
        count += 1
        if count >= 10:
            break

if __name__ == "__main__":
    main()
