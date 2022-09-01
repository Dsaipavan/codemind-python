n=int(input())
f=n*n
s=0
while f:
    r=f%10
    f//=10
    s+=r
if n == s:print('Neon Number')
else:print('Not Neon Number')