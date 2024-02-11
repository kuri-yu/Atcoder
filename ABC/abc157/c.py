n,m = map(int, input().split())
ans = [-1] * n
num = ""
for i in range(m):
    s,c = map(int, input().split())
    if s==1 and c==0 and n != 1:
        print(-1)
        exit()
    if ans[s-1] != -1 and ans[s-1] != c:
        print(-1)
        exit() 
    else:
        ans[s-1] = c

for i in range(n):
    if i==0 and ans[i]==-1 and n != 1:
        num += str(1)
    elif ans[i]==-1:
        num += str(0)
    else:
        num += str(ans[i])
print(num)