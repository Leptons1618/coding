# n = int(input('n: '))
# for i in range(n):
#     print(n - i)

# n = int(input('n: '))
# x = ' '
# y = '#'
# for i in range(n):
#     print(x*(n-i-1) + y*(i+1))

# for _ in range(int(input())):
#     A, B, C, D = map(int, input().split())
#     if A > B or A == B:
#         B += C
#     else:
#         A += C
#     if A > B or A == B:
#         B += D
#     else:
#         A += D
#     if A > B or A == B:
#         print('N')
#     else:
#         print('S')

# import re

# for _ in range(int(input())):
#     N = int(input())
#     S = input()
#     match1 = re.search("code",S)
#     match2 = re.search("chef", S)
#     if match1.start() < match2.start():
#         print('AC')
#     else:
#         print('WA')
        
# for _ in range(int(input())):
#     N = int(input())
#     S = input()
#     s1 = 'code'
#     s2 = 'chef'
#     if S.find('code') < S.find('chef'):
#         print('AC')
#     else:
#         print('WA')


def extrema(a, i, n):
    if i == n:
        count = 0
        for i in range(1, n-1):
            if i+1 < n and i-1>0:
                count += (a[i] > a[i - 1] and a[i] > a[i + 1])
                count += (a[i] < a[i - 1] and a[i] < a[i + 1])
            return count
    fa=0;
    a[i]=0;
    fa+=extrema(a,i+1,n);
    a[i]=1; 
    fa+=extrema(a,i+1,n); 
    a[i]=2; 
    fa+=extrema(a,i+1,n); 
    return fa

for _ in range(int(input())):
    n = int(input())
    a = []*n
    print(extrema(a, 0, n))
    