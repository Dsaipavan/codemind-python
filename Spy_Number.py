n=int(input())
p,s=1,0
while n:
    r=n%10
    n//=10
    s+=r
    p*=r
if p==s:print('Spy Number')
else:print('Not Spy Number')