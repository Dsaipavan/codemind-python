for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    s=sorted(x)
    c=0
    for i in range(n):
        for j in range(i,n):
            if i!=j and (x[i]+x[j] in x):
                c+=1
    if c==0:
        print(-1)
    else:
        print(c)