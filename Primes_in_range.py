import math
def pr(x):
    if x==1:return False
    if x==2:return True
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if pr(i):
        c+=1
print(c)