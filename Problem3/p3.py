"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
def getFactors(n, i=2, factors=[]):
    if (n % i) == 0:
        factors.append(i)
        if reduce(lambda x,y: x*y, factors) >= n:
            return factors
    if n == i:
        return factors
    return getFactors(n, i+1, factors)

def getFactors2(n):
    factors = []
    i = 2
    while i < n:
        if (n % i) == 0:
            factors.append(i)
            if reduce(lambda x,y: x*y, factors) >= n:
                return factors
        i = i + 1
    return factors

print getFactors2(n=13195)
print getFactors2(n=600851475143)[-1]

