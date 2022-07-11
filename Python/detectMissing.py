a = list(map(int, input("enter the list: ").split()))
a.sort()
for i in range(len(a)):
    if i+1 != a[i]:
        print(i+1)
    else: i = i+1

