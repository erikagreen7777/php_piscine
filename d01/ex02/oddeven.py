#!/usr/bin/python
# import sys

num = raw_input("Enter a number: ")

# def main():
#     while True:
try:
    number = int(num)
except ValueError:
    print "\'%s\' is not a number" % num
else:
    check = number%2
    if check == 0:
        print "The number %d is even" % int(number)
    elif check == 1:
        print "The number %d is odd" % int(number)
