n=int(input())
x=list(map(int,input().split()))
z=[]
j=0
for i in range(n):
    if x[i]-x[j]<0:
        j=i
    z.append(x[i]-x[j])
    j=i
print(sum(z))