# s = 1+11+111+1111+.............+nth term
n = 5
a = s = 0
for i in range(n):
    e = 10**i + a
    s += e
    print("s: ",s)
    a = e
    print('a: ',a)
print(s)    