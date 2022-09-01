def ch(x):
    s,c=0,x
    while x:
        r=x%10
        x//=10
        if r!=0:
            if c%r==0:
                s+=1
    return s==len(str(c))
m=int(input())
n=int(input())
for i in range(m,n+1):
    if ch(i):
        print(i,end=' ')