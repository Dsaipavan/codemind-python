n=int(input())
x=list(map(int,input().split()))
t=sorted(x)[::-1]
i=0
while i<n-1:
    t[i],t[i+1]=t[i+1],t[i]
    i+=2
print(*t)