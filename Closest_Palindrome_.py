def rev(x):
    s,c=0,x
    p=10**(len(str(x))-1)
    while x:
        r=x%10
        x//=10
        s+=p*r
        p//=10
    return c==s
n=int(input())
a,b=n-1,n+1
while rev(a)==False:
    a-=1
while rev(b)==False:
    b+=1
if abs(n-a)==abs(n-b):
    print(a,b)
if abs(n-a)<abs(n-b):
    print(a)
if abs(n-a)>abs(n-b):
    print(b)