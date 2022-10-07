n=int(input())
x=[0,1]
while x[-1]<n:
    x.append(x[-1]+x[-2])
a,b=n-1,n+1
while True:
    if a in x:
        break
    a-=1
while True:
    if b in x:
        break
    b+=1
if abs(n-a)==abs(n-b):
    print(a,b)
elif abs(n-a)<abs(n-b):
    print(a)
else:
    print(b)