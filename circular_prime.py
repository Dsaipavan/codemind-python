def pr(x):
    if x==1:return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True
n=int(input())
z=int(str(n)[::-1])
if pr(n) and pr(z):
    print('circular prime')
elif pr(n):
    print('prime but not a circular prime')
else:
    print('not prime')