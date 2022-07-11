from typing import Counter

n = int(input('which element?: '))
lst = [1, 2, 3, 1, 5, 3, 1]

# def sol(n):
#     cnt = 0
#     for el in lst:
#         if el == n:
#             cnt += 1
#     print(cnt)

# # x = list(map(sol, lst))
# # print(x)
# sol(n)


freq = {ele:lst.count(ele) for ele in lst}
print(freq.get(n))

