#!/usr/bin/env python2.7

import sys

def lower_file(filename):
    with open(filename, "r") as f:
        for line in f:
            print line.lower(),

def main():
    if len(sys.argv) < 2:
        print "usage: lower <filename>"
        exit()

    filename = sys.argv[1]

    lower_file(filename)

if __name__ == "__main__":
    main()
