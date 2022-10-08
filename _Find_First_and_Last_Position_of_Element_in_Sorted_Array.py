n=int(input())
x=list(map(int,input().split()))
c=int(input())
y=x[::-1]
if c in x:
    print(x.index(c),n-1-y.index(c))
else:
    print(-1,-1)