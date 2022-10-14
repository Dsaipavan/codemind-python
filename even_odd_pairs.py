n=int(input())
x=list(map(int,input().split()))
e=[]
o=[]
z=[]
for i in x:
    if i%2==0:e.append(i)
    else:o.append(i)
if len(e)>len(o):
    maxi=e
else:
    maxi=o
mn=min(len(e),len(o))
for i in range(mn):
    z.append(e[i])
    z.append(o[i])
z=z+maxi[mn:]
if n%2==0:
    print(*z)
else:
    z.append(0)
    print(*z)