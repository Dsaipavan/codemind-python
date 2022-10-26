s=input()
c=0
o=[]
for i in s:
    if i.lower() in 'aeiou':
        c+=1
    else:
        o.append(c)
        c=0
    o.append(c)
print(max(o))