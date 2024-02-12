card = []
for i in range(3):
    num = list(map(int, input().split()))
    card.append(num)

n = int(input())

for i in range(n):
    num = int(input())
    for j in range(3):
        for k in range(3):
            if card[j][k] == num:
                card[j][k] = -1

judge = False

for i in range(3):
    if card[i][0] == card[i][1] == card[i][2] == -1:
        judge = True
    if card[0][i] == card[1][i] == card[2][i] == -1:
        judge = True

if card[0][0] == card[1][1] == card[2][2] == -1:
    judge = True

if card[0][2] == card[1][1] == card[2][0] == -1:
    judge = True

print('Yes' if judge else 'No')