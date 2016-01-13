"""
Create a vector x containing initial conditions to generate Fibonacci numbers
Create empty vector y to extract even Fibonacci numbers
"""
x= [1,2]
y= []
"Construct for loop to generate a Fibonacci sequence with F_n big enough"
for n in range(100):
    "Implement recursion of Fibonacci numbers and add to vector x"
    x.append(x[n]+x[n+1])
    "Impose even conditions and upper bound"
    if x[n]%2 is 0 and x[n]<4000000:
        "Add all values in x satisfying conditions to y"
        y.append(x[n])
    "Print sum"
print(sum(y))
