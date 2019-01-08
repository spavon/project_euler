def is_prime(num):
    prime = False
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                prime = False
                break
        else:
            prime = True
    return prime

def print_primes(num):
    if(is_prime(num)):
        print("Prime: ", num)
    else:
        print("Not: ", num)

def store_num_primes(num):
    primes = []
    count = 1
    while len(primes) < num:
        #print("count: ", count)
        if(is_prime(count)):
            primes.append(count)
        count += 1
    return(primes)

def store_primes_below_val(num):
    primes = []
    count = 1
    while count < num:
        #print("count: ", count)
        if(is_prime(count)):
            primes.append(count)
        count += 1
    return(primes)

def main():
    for i in range(1, 10):
        print_primes(i)

    print(store_num_primes(6))
    print(store_num_primes(10001))

if __name__ == '__main__':
    main()
