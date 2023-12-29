n = int(input())
ans = ""

for i in range(10):
    ans += str(n//(2**i)%2)

print(ans[::-1])