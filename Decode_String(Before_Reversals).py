for _ in range(int(input())):
    a,b=map(int,input().split())
    x=input()
    for i in range(b,0,-1):
        z=x[:i]
        x=z[::-1]+x[i:]
    print(x)