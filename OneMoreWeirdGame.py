#CodeChef
t = int(input())
for i in range(t):
    r,c = map(int,input().split())
    print((c - 1) + (r-1) * 1 + ((c-1) * 2)*(r-1))