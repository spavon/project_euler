def triangle_number(num):
    return int((num * (num + 1))/2)

def num_divisors(num):
    divs = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divs.append(i)
            divs.append(i)
    return divs

def main():
    target = 500
    count = 1
    loop = True
    while loop:
        n = triangle_number(count)
        d = num_divisors(n)
        x = len(d)
        print(count, x)
        if x > target:
            print("Tri Num: ", n)
            loop = False
        else:
            count += 1





if __name__ == '__main__':
    main()
