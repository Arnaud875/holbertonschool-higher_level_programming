#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv) - 1
    print("{} argument{}.".format(args, "s" if args > 0 else ""))

    for i in range(args):
        print("{}: {}".format(i + 1, argv[i + 1]))
