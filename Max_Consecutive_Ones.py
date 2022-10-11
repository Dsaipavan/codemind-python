n=int(input())
x=input().split('0')
c=0
for i in x:
    c=max(c,i.count('1'))
print(c)