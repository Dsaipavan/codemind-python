n=int(input())
x=[0,1]
while x[-1]<n:
    x.append(x[-1]+x[-2])
print(x[-1]==n)