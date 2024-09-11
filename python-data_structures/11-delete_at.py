#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list) - 1
    if idx < 0 or idx > length:
        return my_list

    for idx_, i in enumerate(my_list):
        if idx_ == idx:
            my_list.remove(i)
            break
    return my_list
