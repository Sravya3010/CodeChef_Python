t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    c = 0
    if len(l) == 1:
        print("YES")
    else:
        for i in range(len(l)-1):
            if abs(l[i] - l[i+1]) <= 1:
                c = c + 1 
        if c + 1 == n:
            print("YES")
        else:
            print("NO")