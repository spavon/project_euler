#!/bin/env python3
def get_collatz_list(num):
    nums = [num]
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1
        nums.append(num)
    return(nums)

def main():
    collatz_lengths = []

    for num in range(1000001):
        collatz_lengths.append(len(get_collatz_list(num)))

    print(collatz_lengths.index(max(collatz_lengths)))


if __name__ == '__main__':
    main()
