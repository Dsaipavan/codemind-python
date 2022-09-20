a=int(input())
b=int(input())
c=0
d=[k for k in range(a,b+1)]
for i in range(len(d)):
    for j in range(i+1,len(d)+1):
        if sum(d[i:j])%2!=0:
            c+=1
print(c)