#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    n = len(argv)
    if n == 0:
        print("0 arguments.")
    else:
        if n == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(n))
        for i in range(n):
            print("{}: {}".format(i + 1, argv[i]))
