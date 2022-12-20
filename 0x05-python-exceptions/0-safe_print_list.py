#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if x is None:
        print()
        return 0
    if x < 1:
        print()
        return 0
    if my_list is None:
        print()
        return 0
    n = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            n = n + 1
        except IndexError:
            pass
    print()
    return n
