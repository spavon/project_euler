def sum_of_squares(num):
    total = 0
    for x in range(num + 1):
        total += (x * x)
    return total


def square_of_sum(num):
    total = 0
    for x in range(num + 1):
        total += x
    return (total * total)

def main():
    x = 100
    print("{} - {} = {}".format(square_of_sum(x), sum_of_squares(x), square_of_sum(x) - sum_of_squares(x)))

if __name__ == '__main__':
    main()
