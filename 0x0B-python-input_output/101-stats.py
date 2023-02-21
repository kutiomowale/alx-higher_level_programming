#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
Total file size: File size: <total size>
where file size is the sum of all previous file sizes
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, it doesn’t print anything for that status code
format: <status code>: <number>
status codes are printed in ascending order

"""
import sys


def print_stats(total, possible, appeared):
    """Prints the required stats

    Args:
        total (int): The total file size
        possible (list): List os possible status codes
        appeared: (dict): Status codes that have appeared with their numbers
    """
    print("File size: {}".format(total))
    for code in possible:
        if code in appeared:
            print("{}: {}".format(code, appeared[code]))


try:
    total_file_size = 0
    """int: The sum of all previous file sizes"""
    possible_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    """list: Possible status codes"""
    appeared_codes = {}
    """dict: dictionary of code and number pairs that have appaired"""
    for i, line in enumerate(sys.stdin):
        i += 1
        """int: Line number starting from 1"""
        line = line.split()
        """list: line text split by whitespace. i is line index from 0"""
        if len(line) != 6: # line should originally be a text of 6 strings
            # including the "-" character
            break
        new_code = int(line[-2])
        """int: Status code for a line"""
        if new_code in appeared_codes:
            appeared_codes[new_code] += 1
        else:
            appeared_codes[new_code] = 1
        file_size = int((line[-1]).rstrip("\n"))
        """int: File size for a line (sys.stin includes \n,
        so it is removed)"""
        total_file_size += file_size
        if i % 10 == 0:
            print_stats(total_file_size, possible_codes, appeared_codes)
    print_stats(total_file_size, possible_codes, appeared_codes)
except KeyboardInterrupt:
    print_stats(total_file_size, possible_codes, appeared_codes)
