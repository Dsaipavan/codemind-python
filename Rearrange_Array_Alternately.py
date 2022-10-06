for _ in range(int(input())):
    op=[]
    n=int(input())
    x=list(map(int,input().split()))
    o=x[:n//2]
    e=(x[n//2:])[::-1]
    for i in range(n//2):
        op.append(e[i])
        op.append(o[i])
    if n%2==1:
        op.append(x[(n//2)])
        print(*op)
    else:
        print(*op)