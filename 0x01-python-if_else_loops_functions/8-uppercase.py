#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str) - 1):
        print("{}".format((chr(ord(str[i]) - 32)) if (ord(str[i]) > 96 and
              ord(str[i]) < 123) else (str[i])), end='')
    if len(str) > 0:
        print("{}".format((chr(ord(str[len(str) - 1]) - 32))
              if (ord(str[len(str) - 1]) > 96 and
              ord(str[len(str) - 1]) < 123) else (str[len(str) - 1])))
