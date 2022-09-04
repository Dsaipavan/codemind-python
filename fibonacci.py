n=int(input())
x=[0,1]
while len(x)<n:
    x.append(x[-1]+x[-2])
print(*x)