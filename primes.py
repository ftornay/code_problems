#!/usr/bin/env python3
""" Implemenation of Eratosthenes' sieve """

def is_prime(n, ar):
    """ Checks whether a number is prime """
    if n > len(ar):
        raise ValueError("Too high a number!")
    else:
        return ar[n-1]

def primes(n):
    """ Returns an array with each i = true iff
    i+1 is prime """
    # Initialize the array
    ar = [True] * n
    ar[0] = False # 1 is not prime
    # Even numbers are not prime
    for number in range(1, n, 2):
        ar[number] = False
    ar[1] = True # 2 is prime
    # It's enough to check up to sqrt(no)
    i = 2
    while i*i < n:
        if ar[i]:
            j = (i+1)*(i+1)
            while j < n:
                ar[j-1] = False
                j += i + 1
        i += 1
    return ar

if __name__ == '__main__':
    p_ar = primes(1000)
    test_primes = [2, 3, 5, 7, 11, 13, 571, 577]
    print("These should be prime:")
    for i in test_primes:
        print(f"Is {i} prime? {is_prime(i, p_ar)}")
    test_composites = [1, 4, 49, 7*12, 15**2, 13*20, 574, 921]
    print()
    print("These should NOT be prime:")
    for i in test_composites:
        print(f"Is {i} prime? {is_prime(i, p_ar)}")
