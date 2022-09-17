m=int(input())
x=list(map(int,input().split()))
n=int(input())
y=list(map(int,input().split()))
o=int(input())
c=0
for i in range(m):
    if y[i]>=o and x[i]<=o:
        c+=1
print(c)