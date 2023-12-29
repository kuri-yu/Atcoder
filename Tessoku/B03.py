n = int(input())
a = list(map(int, input().split()))

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(i+2,n):
            if a[i]+a[j]+a[k]==1000:
                exit(print('Yes'))

print('No')