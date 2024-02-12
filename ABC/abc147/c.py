def generate01(n):
    return [format(i, f'0{n}b') for i in range(2**n)]

n = int(input())
mura = generate01(n)

say = [[] for i in range(n)]

for i in range(n):
    a = int(input())
    for j in range(a):
        x,y = map(int, input().split())
        say[i].append((x,y))

ans = 0
count = 0

for people in mura:
    judge = True
    for i in range(n):
        if people[i] == "1":
            for x,y in say[i]:
                if int(people[x-1]) != y:
                    judge = False
    if judge:
        count = 0
        for i in people:
            count += int(i)
        ans = max(ans, count)

print(ans)