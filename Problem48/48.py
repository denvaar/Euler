
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
# Find the last ten digits of the series,
# 1^1 + 2^2 + 3^3 + ... + 1000^1000

# Straight-forward solution.
s = 1
for i in range(2, 1001):
    s = (s + (i**i))
print str(s)[-10:]

