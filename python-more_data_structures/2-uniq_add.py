#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = []
    result = 0

    for i in my_list:
        if i not in unique_int:
            unique_int.append(i)
            result += i
    return result
