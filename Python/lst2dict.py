lst = [1, 2, 3, 1, 5, 3, 1]

def sol():
    lstD = {}
    for elem in lst:
        if elem not in lstD:
            lstD[elem] = 0
        lstD[elem] += 1
    return lstD

print(sol())
