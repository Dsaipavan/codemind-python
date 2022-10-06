n=int(input())
x=list(map(int,input().split()))
mn=max(x)
mx=mn
while True:
    z=0
    for i in x:
        if mn%i==0:
            z+=1
        else:break
    if z==n:
        print(mn)
        break
    mn+=mx