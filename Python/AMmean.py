for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    if abs((a + c - (2 * b)))%3 == 0:
        print(0)
    else:
        print(1)
