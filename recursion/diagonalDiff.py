def diagonalDifference(arr):
    # Write your code here
    ld = rd = 0
    for i in range(n):
        ld += arr[i][i]
        rd += arr[i][n-1-i]
    diff = abs(ld - rd)
    
    return diff

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)