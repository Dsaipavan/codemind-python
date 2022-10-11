n=int(input())
x=list(map(int,input().split()))
c=0
j=0
for i in range(n):
    if x[i]-x[j]<0:
        j=i
    c=max(c,x[i]-x[j])
print(c)