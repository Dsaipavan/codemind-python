a,b=map(int,input().split())
c=0
x=list(map(int,input().split()))
for i in range(a):
    for j in range(i+1,a+1):
        if b==sum(x[i:j]):c+=1
print(c)