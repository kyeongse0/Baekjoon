T = input()
T = int(T)
result = []
for j in range(T):
    e = input().split()
    num = float(e[0])
    for i in range(len(e)):
        if i == 0: pass
        if e[i] == '@':
            num = num*3
        elif e[i] == '%':
            num = num+5
        elif e[i] == '#':
            num = num-7
    result.append(num)

for k in range(T):
    print(format(result[k], ".2f"))


