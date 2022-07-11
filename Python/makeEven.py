for _ in range(int(input())):
    n = input()
    if int(n) % 2 == 0:
        print(0)
    elif int(n[0]) % 2 == 0:
        print(1)
    else:
        flag = 0
        for i in n:
            if int(i) % 2 == 0:
                print(2)
                flag = 1
                break
        if flag == 0:
            print(-1)