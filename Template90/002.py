def generate01(n):
    return [format(i, f'0{n}b') for i in range(2**n)]

def kakko(s):
    result = ''
    for char in s:
        if char == '0':
            result += '('
        elif char == '1':
            result += ')'
    return result

def judge(s):
    result = True
    left = 0
    right = 0
    for i in s:
        if i=="0":
            left+=1
        else:
            right+=1
        if right>left:
            result = False
    if result and left==right:
        print(kakko(s))
    
n = int(input())
n01 = generate01(n)

for i in n01:
    judge(i)