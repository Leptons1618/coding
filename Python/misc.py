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



# def setMatrixZeroes(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     row = False
#     col = False
#     for i in range(m):
#         if matrix[i][j] == 0:
#             row = True
#     for i in range(n):
#         if matrix[i][j] == 0:
#             col = True
   
#     return matrix

class Solution:
    def setZeroes(self, matrix) -> None:
        # Do not return anything, modify matrix in-place instead.
        
        m = len(matrix) # rows
        n = len(matrix[0]) # columns
        col = False
        for i in range(m):
            if matrix[i][0] == 0:
                col = True
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 # set row to 0 for all col in row i 
                    matrix[0][j] = 0 # set col to 0 for all row in col j    
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                if col:
                    matrix[i][j] = 0
        
        return matrix

matrix = [[-4,-2,6,-7,0],[-8,6,-8,-6,0],[2 ,2,-9,-6,-10]]
print(Solution().setZeroes(matrix))
print([[0,0,0,0,0],[0,0,0,0,0],[2147483647,2,-9,-6,0]])



# # Add two numbers and return the sum as a linked list.
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         dummy = ListNode(0)
#         curr = dummy
#         carry = 0
#         while l1 or l2 or carry:
#             if l1:
#                 carry += l1.val
#                 l1 = l1.next
#             if l2:
#                 carry += l2.val
#                 l2 = l2.next
#             curr.next = ListNode(carry % 10)
#             curr = curr.next
#             carry //= 10
#         return dummy.next
# s = Solution()
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
# res = s.addTwoNumbers(l1, l2)
# # res = s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
# while res:
#     print(res.val)
#     res = res.next
