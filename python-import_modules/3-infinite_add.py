#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv) - 1
    result = 0

    for i in range(args):
        result += int(argv[i + 1])

    print("{}".format(result))
