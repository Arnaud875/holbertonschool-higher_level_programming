#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            idx += 1
        except Exception as e:
            pass

    print("")
    return idx
