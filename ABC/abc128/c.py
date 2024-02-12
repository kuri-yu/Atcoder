def generate01(n):
    return [format(i, f'0{n}b') for i in range(2**n)]

n, m = map(int, input().split())
k = []
s = []

for i in range(m):
    ks = list(map(int, input().split()))
    k.append(ks[0])
    s.append(ks[1:])

p = list(map(int, input().split()))

n01 = generate01(n)

ans = 0

for i in n01:
    judge = True
    for j in range(m):
        sum = 0
        for k in s[j]:
            sum += int(i[k-1])
        if sum%2!=p[j]:
            judge = False
    if judge:
        ans += 1

print(ans)