# Find the largest palindromic number from multiplying two 3-digit numbers.
l = []
for i in reversed(range(100, 1000)):
    for j in reversed(range(100,1000)):
        if str(i * j) == str(i * j)[::-1]:
            l.append(i*j)
print max(l)     
