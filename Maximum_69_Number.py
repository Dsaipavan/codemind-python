s=input()
x=[s]
for i in range(len(s)):
    if s[i]=='6':
        x.append(s[:i]+'9'+s[i+1:])
    if s[i]=='9':
        x.append(s[:i]+'6'+s[i+1:])
print(sorted(x)[-1])