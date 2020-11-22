a = int(input())
a1 = a//100
a2 = a//10 - a1*10
a3 = a%10
s = 0
if a1 == 3:
    s+= 1
if a2 == 3:
    s+= 1
if a3 == 3:
    s+= 1
print(s)