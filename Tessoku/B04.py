s = input()
num = len(s)
s = s[::-1]
ans = 0

for i in range(num):
    ans += 2**i*int(s[i])

print(ans)