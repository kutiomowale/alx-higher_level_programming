#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    # Write a function that prints x elements of a list.
    # Prototype: def safe_print_list(my_list=[], x=0):
    # my_list can contain any type (integer, string, etc.)
    # All elements must be printed on the same line followed by a new line.
    # x represents the number of elements to print
    # x can be bigger than the length of my_list
    # Returns the real number of elements printed
    # You have to use try: / except:
    # You are not allowed to import any module
    # You are not allowed to use len()

    if x < 1:
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
