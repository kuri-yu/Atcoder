n,s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False] * (s+1) for i in range(n+1)]

dp[0][0] = True

for i in range(1,n+1):
    for j in range(s+1):
        if dp[i-1][j] == True:
            dp[i][j] = True
            if j+a[i-1] <= s:
                dp[i][j+a[i-1]] = True

for i in range(n+1):
    if dp[i][s] == True:
        print('Yes')
        exit()

print('No')