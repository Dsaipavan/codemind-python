s=input()
c=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if len(set(s[i:j]))==1:
            c.append(len(s[i:j]))
print(max(c))