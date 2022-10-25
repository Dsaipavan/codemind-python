a=input()
s=''
c=0
k=[]
for i in a:
    if i in '0123456789':
        s+=i
for i in s:
    if i in '24680':
        c=1
        k.append(i)
if c==0:
    print(-1)
else:
    m=(sorted(set(s)))[::-1]
    if int(m[-1])%2!=0:
        m[-1],m[m.index(min(k))]=m[m.index(min(k))],m[-1]
    print(''.join(m))