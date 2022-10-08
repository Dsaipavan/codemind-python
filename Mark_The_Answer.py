x,y=map(int,input().split())
z=list(map(int,input().split()))
m,c=0,0
for i in z:
    if i>y:
        m+=1
    if m>1:
        break
    if m<2 and i<=y:
        c+=1
print(c)