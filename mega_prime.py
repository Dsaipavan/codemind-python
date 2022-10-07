def pr(x):
    if x==1:return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True
n=int(input())
z=0
if pr(n):
    while n:
        r=n%10
        if pr(r)==False:
            z=1
            print('Not Mega Prime')
            break
        n//=10
    if z==0:
        print('Mega Prime')
else:
    print('Not Mega Prime')