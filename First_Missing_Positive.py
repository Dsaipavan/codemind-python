n=int(input())
x=list(map(int,input().split()))
for i in range(1,n+1):
    if i not in x:
        print(i)
        break