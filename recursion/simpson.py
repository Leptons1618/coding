def f(x):
    return 1/(1 + x**2)

def simp(a, b, n):
    h = (a + b)/n
    sum = f(a) + f(b)
    
    for i in range(1, n):
        s = a + i*h

        if i % 2 == 0:
            sum += 2 * f(s)
        else:
            sum += 4 * f(s)
        
    sum = sum * h/3
    return sum
a, b = map(float, input('Enter lower and upper limit: ').split())
n = int(input('Enter the sub_interval: '))

print('Integration result using Simpsons 1/3 method: ', simp(a, b, n))