from math import sqrt

n,d = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

ans = 0

for i in range(n-1):
    for j in range(i+1,n):
        num = 0
        for k in range(d):
            num += (grid[i][k] - grid[j][k])**2
        if int(sqrt(num))**2 == num:
            ans+=1

print(ans)