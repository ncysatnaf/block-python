#!/usr/bin/env python
# encoding: utf-8

def plusLife():
    i = [0]
    def f():
        i[0] += 1
        return i
    return f


def main():

    ha = plusLife()
    print "续命成功，目前为+",ha()[0], '秒'
    print "续命成功，目前为+",ha()[0], '秒'
    print "续命成功，目前为+",ha()[0], '秒'

if __name__ == "__main__":
    main()
