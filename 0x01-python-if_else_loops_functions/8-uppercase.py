#!/usr/bin/python3

# a function that prints a string in uppercase followed by a new line.
# Prototype: def uppercase(str):
# You can only use no more than 2 print functions with string format
# You can only use one loop in your code
# You are not allowed to import any module
# You are not allowed to use str.upper() and str.isupper()
# Tips: ord()


def uppercase(str):
    for i in range(len(str) - 1):
        print("{}".format((chr(ord(str[i]) - 32)) if (ord(str[i]) > 96 and
              ord(str[i]) < 123) else (str[i])), end='')
    print("{}".format((chr(ord(str[len(str) - 1]) - 32))
          if (ord(str[len(str) - 1]) > 96 and
          ord(str[len(str) - 1]) < 123) else (str[len(str) - 1])))
