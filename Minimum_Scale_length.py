n=int(input())
x=list(map(int,input().split()))
z=False
y=min(x)
while z==False:
    l=0
    for i in x:
        if i%y==0:
            l+=1
    if l==n:
        print(y)
        z=True
    y-=1