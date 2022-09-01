def ch(x):
    return len(set(x.lower()))==len(x)
x=input()
f,n=[],[]
for i in range(len(x)):
    for j in range(i+1,len(x)+1):
        if ch(x[i:j]):
            f.append(x[i:j])
            n.append(len(x[i:j]))
if max(n)<=2:print(-1)
else:print(f[n.index(max(n))])