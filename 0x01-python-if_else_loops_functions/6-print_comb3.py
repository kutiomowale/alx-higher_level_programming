#!/usr/bin/python3
# This code prints numbers 01 to 89
# which are all possible different combinations of two digits
# The two digits must be different, so numbers like 11, 22, 33, etc are not
# printed
# numbers like 01 and 10 are considered the same combination of the two
# digits 0 and 1, so only the smallest 1.e 01 is printed
# the numbers are sepatated by a comma and a space
# the last number is followed by a new line

for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}".format(89))
        else:
            print("{}{}".format(i, j), end=", ")
