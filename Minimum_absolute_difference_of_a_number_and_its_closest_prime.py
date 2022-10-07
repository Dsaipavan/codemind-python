def pr(x):
    if x==1:return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True
n=int(input())
if pr(n):
    print(0)
else:
    a,b=n+1,n-1
    while pr(a)==False:
        a+=1
    while pr(b)==False:
        b-=1
    print(min(abs(n-a),abs(n-b)))