# n = input()
# print(type(n))

# m = int(n)
# print(type(m))

# p = int(n[0])
# print(p)
# print(type(p))

# for i in n:
#     print(i)
#     print(type(i))

# list = [1, 2, 3, 4, 5]
# sum = 0
# for i in list:
#     sum += i
# print(sum)
# print(sum-min(list))

# for _ in range(int(input())):
#     n = int(input())
#     participants = list(map(int, input().split()))
#     money = 0
#     for i in participants:
#         money += i
#     print(money-min(participants))


# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     p = input()
#     cnt = 0
#     vowel = ['a', 'e', 'i', 'o', 'u']
#     S = []
#     P = []
#     for i in s:
#         S.append(i)
#     for j in p:
#         P.append(j)
#     for i in range(n):
#         if P[i] != S[i]:
#             if P[i] in vowel and S[i] in vowel:
#                 cnt += 2 
#             else:
#                 cnt += 1 
#     print(cnt)

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     c = list(input())
#     f = 0
#     k = 1
#     blue = []
#     red = []
#     for i in range(n):
#         if c[i] == "B":
#             blue.append(a[i])
#         else:
#             red.append(a[i])
#     blue.sort()
#     red.sort()
#     for i in range(len(blue)):
#         if blue[i] < k:
#             f = 1
#             break
#         k += 1
#     for i in range(len(red)):
#         if red[i] > k:
#             f = 1
#             break
#         k += 1
#     if f:
#         print('NO')
#     else:
#         print('YES')


# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = []
#     sum = 0
#     for i in range(n):
#         sum += a[i]


# my_set = {0, 'apple', 3.6}
# print(type(my_set))

# armstrong no or not
# n = int(input('Enter a digit: '))
# def isarmstrong(n):
#     order = len(str(n))
#     s = 0
#     temp = n
#     while temp != 0:
#         digit = temp % 10
#         s += digit ** order
#         temp //= 10
#     return (s == n)

# print(isarmstrong(n))


# Find all the strong number
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = int(input('Enter a digit: '))
# def isstrong(n):
#     s = 0
#     temp = n
#     while temp != 0:
#         digit = temp % 10
#         s += factorial(digit)
#         temp //= 10
#     return (s == n)
# print(isstrong(n))



def setMatrixZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = False
    col = False
    for i in range(m):
        if matrix[i][j] == 0:
            row = True
    for i in range(n):
        if matrix[i][j] == 0:
            col = True
    
    return matrix