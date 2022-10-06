for _ in range(int(input())):
    n,t=map(int,input().split())
    x=list(map(int,input().split()))
    c=0
    for i in range(n+1):
        for j in range(i+1,n+1):
            if sum(x[i:j])==t:
                c=1
                print(i+1,j)
                break
        if c==1:
            break
    if c==0:
        print(-1)