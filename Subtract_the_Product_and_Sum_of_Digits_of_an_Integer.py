n=int(input())
p,s=1,0
while n:
    r=n%10
    n//=10
    p*=r
    s+=r
print(p-s)