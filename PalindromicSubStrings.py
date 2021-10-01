#CodeChef
alp = "abcdefghijklmnopqrstuvwxyz"
s1 = input()
s2 = input()
f = 0
for i in alp:
    if i in s1 and i in s2:
        f = 1
        break
if(f):
    print("Yes")
else:
    print("No")
    