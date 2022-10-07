a=int(input())
b=int(input())
def fac(x):
    s=0
    for i in range(1,(x//2)+1):
        if x%i==0:
            s+=i
    return s
if fac(a)==b and fac(b)==a:print('Amicable')
else:print('Not Amicable')