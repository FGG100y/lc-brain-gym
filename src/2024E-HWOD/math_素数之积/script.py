#!/usr/bin/env python

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def factorize(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            j = num // i
            if is_prime(i) and is_prime(j):
                return sorted([i, j])
    return [-1, -1]

# Example usage:
# num = int(input())
num = 701
num = 99
factors = factorize(num)
if factors[0] == -1:
    print("1-1")
else:
    print(' '.join(map(str, factors)))
