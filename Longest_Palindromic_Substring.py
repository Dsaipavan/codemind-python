n=input()
l,k=[],[]
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        if n[i:j][::-1]==n[i:j]:
            l.append(n[i:j])
            k.append(len(n[i:j]))
print(l[k.index(max(k))])