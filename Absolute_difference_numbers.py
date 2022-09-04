a,n=map(int,input().split())
e=str(a)[:n]
f=str(a)[len(str(a))-n:]
print(abs(int(e)-int(f)))