#!/bin/env python3

def largest_palindrome_product(max_digits):
    max_num = 10 ** max_digits
    ans = 0
    i = 0
    while i < max_num:
        j = 0
        i += 1
        while j < max_num:
            str_num = str(i * j)
            num = i * j
            if str_num == str_num[::-1]:
                if num != 0:
                    if num > ans:
                        ans = num
            else:
                next
            j += 1
    print(ans)

def main():
    largest_palindrome_product(2)
    largest_palindrome_product(3)
    #largest_palindrome_product(4)


if __name__ == '__main__':
    main()
