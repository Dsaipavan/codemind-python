def prime(x):
    c=0
    for i in range(2,x):
        if x%i==0:
            c+=1
    if c==0:
        return (True)
    else:
        return (False)
def check(x):
    a=x
    b=x
    while(prime(a)==False):
        a=a-1
    while(prime(b)==False):
        b=b+1
    if (abs(x-a)>abs(x-b)):
        return b
    else :
        return a
n=int(input())
for i in range(n):
    x=int(input())
    print(check(x))