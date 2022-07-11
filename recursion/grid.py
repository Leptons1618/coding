def grid(m, n):
    calls = 0
    if m == 1 or n ==1:
        return 1
    else:
        calls += 1
        return grid(m - 1, n) + grid(m, n - 1)
    
m, n = map(int, input().split())
print(grid(m, n))


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d={}

        def dfs(i,j):
            if (i,j) in d:return d[(i,j)]
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            
            d[(i,j)]=dfs(i+1,j)+dfs(i,j+1)
            
            return d[(i,j)]
        
        return dfs(0,0)