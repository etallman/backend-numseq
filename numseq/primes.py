# Primes
'''Creates a module named prime within the numseq package. Defines the following functions: 1) primes(n) returns a list of all primes less than n and 2)
is_prime(m) returns a boolean indicating whether m is a prime number.'''


def is_prime(m):
    if m > 1:
        for i in range(2, m):
            if (m % i) == 0:
                return False
            else:
                return True


def primes(n):
    prime_list = []
    for i in range(1, n):
        if is_prime(i) == True:
            prime_list.append(i)
    return prime_list
