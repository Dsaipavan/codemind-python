def pr(x):
    for i in range(2,x):
        if x%i==0:
            return False
n=int(input())
s=2
for i in range(2,int(n/2)+1):
    if n%i==0 and pr(i)==False:
        s+=1
print(s)