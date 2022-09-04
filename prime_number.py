def pr(x):
    if x==1:return x!=1
    if x==2:return True
    for i in range(3,x):
        if x%i==0:
            return False
    return True
if pr(int(input())):print('prime')
else:print('not a prime')