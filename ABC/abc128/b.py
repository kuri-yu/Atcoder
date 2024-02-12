n = int(input())
a = []
for i in range(n):
    n, k = input().split()
    k = int(k)
    a.append([n, -k, i+1])
a.sort()
for aa in a:
    print(aa[2])
