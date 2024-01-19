n = int(input())
ans = 0
while n % 2 == 0:
    n //= 2
    ans += 1

print(ans)