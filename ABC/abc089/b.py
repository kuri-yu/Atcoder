n = int(input())
s = list(map(str, input().split()))

arare = set()

for i in s:
    arare.add(i)

print('Three' if len(arare)==3 else 'Four')