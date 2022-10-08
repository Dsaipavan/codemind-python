n=int(input())
x=list(map(int,input().split()))
p=1
for i in x:p*=i
z=[]
for i in x:z.append(p//i)
print(*z)