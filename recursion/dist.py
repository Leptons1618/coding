dists = list(map(int, input().split()))
for i in range(len(dists)-1):
    if dists[i] > dists[i+1]:
        dists[i] += dists[i+1]
    else:
        dists[i+1] += dists[i]
for i in range(len(dists)):
    if dists[i] == max(dists):
        print(i)
