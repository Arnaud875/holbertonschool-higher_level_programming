#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv) - 1
    print("{:d} argument{:s}".format(args, "s:"
                                     if args > 1 else ":"
                                     if args > 0 else "s."))

    for i in range(args):
        print("{:d}: {}".format(i + 1, argv[i + 1]))