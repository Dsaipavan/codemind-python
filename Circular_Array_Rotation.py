n,k,q=map(int,input().split())
x=list(map(int,input().split()))
z=x[n-k:]+x[:n-k]
for i in range(q):
    print(z[int(input())])