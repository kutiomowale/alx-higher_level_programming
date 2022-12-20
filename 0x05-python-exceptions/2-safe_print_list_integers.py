#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    n = 0
    if x < 1:
        print()
        return 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            n = n + 1
        except (ValueError, TypeError):
            pass
    print()
    return n
