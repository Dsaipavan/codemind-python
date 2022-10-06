for _ in range(int(input())):
    z=0
    n=int(input())
    x=list(map(int,input().split()))
    for i in range(n):
        if sum(x[:i])==sum(x[i+1:]):
            print('YES')
            z=1
            break
    if z==0:
        print('NO')