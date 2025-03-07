import math
h, m = input().split()
x= input()
h = int(h)
m = int(m)
x = int(x) # 분단위로 주어짐 (0~1000)

if (x==0):
    p = 0 # h에 더할 값
    q = 0 # m에 더할 값
else:
    p= math.floor(x/60)
    q= x%60
    
h = h+p
m = m+q

if (m == 60):
    h+=1
    m=0
elif (m>60):
    h+=1
    m=m-60
else:
    pass

if (h==24):
    h=0
elif(h>24):
    h= h-24

print(h, m)