#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    Sum = 0
    if n > 1:
        for i in range(1, n):
            Sum = Sum + int(sys.argv[i])
    print("{}".format(Sum))
