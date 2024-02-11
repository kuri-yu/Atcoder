h,w,n = map(int, input().split())

S = [["."] * w for _ in range(h)]
dir = [(0,-1), (1,0), (0,1), (-1,0)]

x = 0
y = 0
d = 0

for i in range(n):
    s = S[y][x]
    if s==".":
        S[y][x] = "#"
        d = (d + 1)%4
    else:
        S[y][x] = "."
        d = (d + 3)%4
    x = (x + dir[d][0])%w
    y = (y + dir[d][1])%h

for i in S:
    print(''.join(map(str, i)))