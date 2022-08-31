def pr(x):
    if x==1:return False
    if x==2:return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True
n1=int(input())
n2=int(input())
n3=n1+n2+1
while pr(n3)==False:
    n3+=1
print(n3-n1-n2)