n=int(input())
x=list(map(int,input().split()))
for i in range(n-1):x[i]=max(x[i+1:n])
x[-1]=-1
print(*x)