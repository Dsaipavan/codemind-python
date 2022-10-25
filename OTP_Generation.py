a=input()
s=''
for i in a:
    n=int(i)
    if n%2 !=0:
        s+=str(n*n)
print(int(s))