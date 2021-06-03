#CodeChef
t = int(input())
for i in range(t):
    n = int(input())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    k = [l1[i]*20 - (l2[i] * 10) for i in range(n)]
    if max(k) > 0:
        print(max(k))
    else:
        print(0)