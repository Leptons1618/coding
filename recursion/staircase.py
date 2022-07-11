n = int(input('n: '))
x = ' '
y = '#'
for i in range(n):
    print(x*(n-i-1) + y*(i+1))
        