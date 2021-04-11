t = int(input())
for i in range(t):
    l =[input() for i in range(3)]
    if l[0][0] == l[1][0] == l[1][1] == 'l':
        print("yes")
    elif l[0][1] == l[1][1] == l[1][2] == 'l':
        print("yes")
    elif l[1][0] == l[2][0] == l[2][1] == 'l':
        print("yes")
    elif l[1][1] == l[2][1] == l[2][2] == 'l':
        print("yes")
    else:
        print("no")