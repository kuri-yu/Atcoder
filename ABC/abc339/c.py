from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

result = list(accumulate(a))
print(abs(min(0,min(result))) + result[-1])