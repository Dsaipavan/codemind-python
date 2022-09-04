n=int(input())
c=n
s=0
l=len(str(n))
while n:
    r=n%10
    s+=r**l
    l-=1
    n//=10
print(s==c)