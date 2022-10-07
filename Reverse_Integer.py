def rev(x):
    l=len(str(x))-1
    s=0
    while x:
        s+=(x%10)*(10**l)
        x//=10
        l-=1
    return s
n=int(input())
if n<0:print(-1*rev(abs(n)))
else:print(rev(n))