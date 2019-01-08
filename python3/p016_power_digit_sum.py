def pow_digit_sum(base, exp):
    num = base ** exp
    total = sum((int(i) for i in str(num)))
    return(total)

def main():
    base = 2
    exp = 1000
    print(pow_digit_sum(base, exp))

if __name__ == '__main__':
    main()
