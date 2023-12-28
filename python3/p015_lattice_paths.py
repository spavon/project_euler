#!/bin/env python3
from math import factorial

def combinations(n,r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def main():
    r = int(input('Enter square grid length:'))

    n = 2*r

    result = combinations(n,r)
    print(result)

if __name__ == '__main__':
    main()
