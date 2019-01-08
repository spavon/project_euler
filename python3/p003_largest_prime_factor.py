#!/bin/env python3

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(num):
    x = 2
    while x * x < num:
        while num % x == 0:
            num = num / x
        x = x + 1

    return num
    
def main():
    #x = 13195
    x = 600851475143
    print(largest_prime_factor(x))


if __name__ == '__main__':
    main()
