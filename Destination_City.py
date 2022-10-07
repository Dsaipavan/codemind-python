p=int(input())
x=[]
for i in range(p):
    x.append(list(map(str,input().split())))
a=[]
b=[]
for i in range(p):
    a.append(x[i][0])
    b.append(x[i][1])
for i in b:
    if i not in a:
        print(i)
        break