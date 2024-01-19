n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n

dp[1] = a[0]

for i in range(2, n):
    dp[i] = min(dp[i-1] + a[i-1], dp[i-2] + b[i-2])

place = n-1
ans = [n]

while(place != 0):
    if dp[place - 1] + a[place - 1] == dp[place]:
        place -= 1
    else:
        place -= 2
    ans.append(place + 1)

ans = ans[::-1]

print(len(ans))
print(' '.join(map(str, ans)))