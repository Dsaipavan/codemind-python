n=int(input())
s=n
e=o=0
while n:
    r=n%10
    if r%2==0:
        e+=1
    else:
        o+=1
    n//=10
if e==len(str(s)) and s%2==0:print('Even')
elif o==len(str(s)) and s%2==1:print('Odd')
else:print('Mixed')