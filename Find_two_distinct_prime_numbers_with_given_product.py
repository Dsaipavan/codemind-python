def pr(x):
    if x==1:return x!=1
    if x==2:return x==2
    for i in range(3,x):
        if x%i==0:
            return False
    return True
n=int(input())
x=[]
for i in range(1,n):
    if n%i==0 and pr(i)==True:
        x.append(i)
s=0
for i in x:
    for j in x:
        if i!=j and i*j==n:
            print(i,j)
            s=1
    break
if s==0:print(-1)