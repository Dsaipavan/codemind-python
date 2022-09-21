c=[]
n=int(input())
x=list(map(int,input().split()))
mn=0
mx=0
y=[i for i in x if i%2==0]
z=[i for i in x if i%2==1]
mn=min(len(y),len(z))
mx=max(len(y),len(z))
for i in range(mn):
    c.append(y[i])
    c.append(z[i])
if mx==len(y):d=c+y[mn:]
if mx==len(z):d=c+z[mn:]
if n%2==1:
    d.append(0)
    print(*d)
else:print(*d)