#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list_rev = my_list[:]
    my_list_rev.reverse()
    for i in my_list_rev:
        print("{:d}".format(i))
