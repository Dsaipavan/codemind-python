e,o=0,0
n=int(input())
x=list(map(int,input().split()))
for i in x:
    if i%2==0:
        e+=1
    else:o+=1
if e%2==0 and o%2==0:
    print(1)
else:
    print(0)