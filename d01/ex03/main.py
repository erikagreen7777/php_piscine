#!/usr/bin/python
from ft_split import ft_split

def main():
    array = ft_split(("Hello               World AAA"))
    i = 0
    print("Array\n(")
    while i < len(array):
        print("\t[%d] => %s" % (i, array[i]))
        i += 1
    print(")")

if __name__ == "__main__":
    main()