n=int(input())
x=list(map(int,input().split()))
a=[]
c=[]
if x.count(0)==0:print(-1)
elif x.count(1)==0:print(-1)
else:
    for i in range(n):
        for j in range(i+1,n+1):
            b=x[i:j]
            if b.count(0)==b.count(1):
                a.append(i)
                a.append(j-1)
                c.append(j-i)
    l=c.index(max(c))+1
    print(a[(l*2)-2],a[(l*2)-1])