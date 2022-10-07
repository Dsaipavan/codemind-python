n=int(input())
x=list(map(int,input().split()))
s=sum(x)
for i in range(n,0,-1):
    if s%i==0:
        print(i)
        break