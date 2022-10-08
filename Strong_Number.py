def fac(x):
    s=1
    for i in range(1,x+1):
        s*=i
    return s
n=int(input())
c,t=0,n
while n:
    c+=fac(n%10)
    n//=10
if c==t:print('The number {} is a strong number'.format(t))
else:print('The number {} is not a strong number'.format(t))