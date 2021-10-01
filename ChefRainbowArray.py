# Code Chef
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ref = [1,2,3,4,5,6,7]
    if list(set(l)) == ref and l == l[::-1]:
        print("yes")
    else:
        print("no")