from pe_007_10001st_prime import *

def sum_list(_list):
    total = 0
    for i in range(len(_list)):
        total += _list[i]
    return(total)

def eratosthenes_sieve(num):
    primes = {i:True for i in range(2, num)}
    start = 0
    for i in range(2, int(num**0.5) + 1):
        if primes[i]:
            start = i * i
            while start < num:
                primes[start] = False
                start += i

    b_p = []
    for i in primes.keys():
        if primes[i]:
            b_p.append(i)
    return(b_p)
    #return(primes)

def main():
    #print(sum_list(store_primes_below_val(2000000)))
    #print(eratosthenes_sieve(30))
    #print(eratosthenes_sieve(2000000))
    print(sum_list(eratosthenes_sieve(2000000)))


if __name__ == '__main__':
    main()
