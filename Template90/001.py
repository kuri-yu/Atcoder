n,l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
a.append(l)

dif = [a[0]]

for i in range(n):
    dif.append(a[i+1]-a[i])

def is_ok(x):
    length = 0
    cnt = 0
    for i in range(n+1):
        length += dif[i]
        if length>=x:
            length = 0
            cnt += 1
    if cnt>=k+1: return True 
    else: return False

def youkan():
    right = l+1
    left = 0
    while right-left>1:
        mid = (right + left)//2
        if is_ok(mid):
            left = mid
        else:
            right = mid
    return left

print(youkan())