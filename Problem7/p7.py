# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
import timeit
import math

# I learned that you don't have to go over
# each of the primes, only up to the sqrt(index)
# which saves considerable time.
def solution(index):
    primes = [2]
    i = 1
    while len(primes) != index:
        isPrime = True
        _next = primes[-1] + i
        # OPTIMIZATION 2:
        # all primes except 2 are odd.
        if _next % 2 == 0:
            i = i + 1
            continue
        # OPTIMIZATION 1:
        # Only loop up until the sqrt(index)
        for p in primes[:int(math.sqrt(index))]:    
            if _next % p == 0:
                i = i + 1
                isPrime = False
                break
        if isPrime:
            i = 1
            primes.append(_next)
    return primes[-1]

start = timeit.default_timer()
print solution(10001)
stop = timeit.default_timer()
print "Completed in", stop - start, "seconds."

