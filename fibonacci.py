# Fibonacci Sequence Program:

n = int(input("Input: "))
a, b = 0, 1
fib = []

for i in range(n):
    fib.append(a)
    a, b = b, a + b

print("Output:", fib)

