import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def euler_series(n):
    sum = 1
    for i in range(1, n+1):
        sum += (1/factorial(i))
    return sum
print(euler_series(100))


