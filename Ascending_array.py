n=int(input())
x=list(map(int,input().split()))
a=0
for i in range(n-1):
    if x[i]>=x[i+1]:
        print('no')
        a=1
        break
if a==0:print('yes')