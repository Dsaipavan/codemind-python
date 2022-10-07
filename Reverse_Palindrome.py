n=int(input())
x=n+int(str(n)[::-1])
if str(x)[::-1]==str(x):
    print(x)
else:
    while str(x)[::-1]!=str(x):
        x+=int(str(x)[::-1])
    print(x)