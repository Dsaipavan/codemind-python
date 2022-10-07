x=input()
n=[]
m={}
for i in set(x):
    m[i]=x.count(i)
    n.append(m[i])
if max(n)==1:
    print(-1)
else:
    s=sorted(set(n))[-2]
    for i,j in m.items():
        if j==s:
            print(i)
            break
