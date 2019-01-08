#!/usr/bin/env python3

def smallest_multiple(num):
    n = 1
    smallest = 0
    for i in range(1, num + 1):
        if n % i == 0:
            print(n, i)
            smallest = n
        else:
            next
        n += 1

def main():
    smallest_multiple(10)

if __name__ == '__main__':
    main()
