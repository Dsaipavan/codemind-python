n=int(input())
x=list(map(int,input().split()))
m=int(input())
if m>n:
    m=m%n
z=x[-m:]+x[:-m]
print(*z)