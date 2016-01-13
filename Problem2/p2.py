"""
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
go = True
total = 0
i = 2
while go:
    number = fib(i)
    if number > 4000000:
        go = False
    else:
        if (number % 2) == 0:
            total = total + number
        i = 1 + i
print total
"""
fibNumbers = [1, 2]
total = 2
nextNumber = 3

while not (nextNumber > 4000000):
    if nextNumber % 2 == 0:
        total = total + nextNumber
    fibNumbers.append(nextNumber)
    nextNumber = fibNumbers[-1] + fibNumbers[-2]

print total

