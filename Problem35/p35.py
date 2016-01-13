"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""
import math
# First, find the prime numbers below 1,000,000
primes = [2]
circularPrimes = []
i = 1
n = primes[-1]
while n < 1000000:
    isPrime = True
    n = primes[-1] + i
    # All primes are odd except for 2.
    if n % 2 == 0:
        i = i + 1
        continue
    for p in primes[:int(math.sqrt(100000))]:
        if n % p == 0:
            isPrime = False
            i = i + 1
            break
    if isPrime:
        i = 1
        primes.append(n)

for p in primes:
    prime = list(str(p))
    isCircular = True
    for i in prime:
        prime.append(prime.pop(0))
        if int(''.join(prime)) not in primes:
            isCircular = False
            break
    if isCircular:
        circularPrimes.append(int(''.join(prime)))

print circularPrimes
print len(circularPrimes)

