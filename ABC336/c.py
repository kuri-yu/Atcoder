from numpy import base_repr

n = int(input())
n = base_repr(n-1, 5)
s = str(n)

ans = []

for i in s:
    ans.append(int(i)*2)

print(''.join(map(str, ans)))