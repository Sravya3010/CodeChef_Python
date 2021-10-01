t = int(input())
for i in range(t):
    res=""
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    for i in range(len(l)):
        if k >= l[i]:
            res = res + "1"
            k = k - l[i]
        else:
            res = res + "0"
    print(res)