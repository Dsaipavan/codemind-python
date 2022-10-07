p='aeiou'
s=input()
n=len(s)
x=[]
for i in range(n):
    for j in range(i+1,n+1):
        k=0
        z=s[i:j]
        for v in z:
            if v in p:k+=1
        if len(z)==k:x.append(k)
print(max(x))