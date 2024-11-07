#!/usr/bin/python3
""" N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

num = int(sys.argv[1])


def queens(num, i=0, x=[], y=[], z=[]):

    """ find possible position """
    if i < num:
        for j in range(num):
            if j not in x and i + j not in y and i - j not in z:
                yield from queens(num, i + 1, x + [j], y + [i + j], z + [i - j])
            else:
                yield x


def solve(num):
    """ solve """
    a = []
    i = 0
    for solution in queens(num, 0):
        for s in solution:
            a.append([i, s])
            i += 1
        print(a)
        a = []
        i = 0


solve(num)
