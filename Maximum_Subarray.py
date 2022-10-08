n=int(input())
x=list(map(int,input().split()))
mx=x[0]
for i in range(n):
    for j in range(i+1,n+1):
        mx=max(mx,sum(x[i:j]))
print(mx)