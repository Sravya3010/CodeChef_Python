t = int(input())
for i in range(t):
    k1=[]
    l1=[]
    n,k  = map(int,input().split())
    l = list(map(str,input().split()))
    for _ in range(k):
        l1 += list(map(str,input().split()))
    for i in l:
        if i in l1:
            k1.append("YES")
        else:
            k1.append("NO")
    for i in k1:
        print(i,end=" ")
    print()