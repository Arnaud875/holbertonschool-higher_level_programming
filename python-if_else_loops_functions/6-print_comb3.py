#!/usr/bin/python3
print(", ".join("{:d}{:d}".format(i, j)
                for i in range(0, 9)
                for j in range(i + 1, 10) if (i + j) < 17) + ", 89")
