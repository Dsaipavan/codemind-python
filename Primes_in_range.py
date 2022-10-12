def pr(x):
    if x==1:return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if pr(i):c+=1
print(c)