n=int(input())
x=list(map(int,input().split()))
i,y,c=1,[],0
while i<=max(x):
    for j in x:
        if j%i==0:
            c+=1
            if c==n:y.append(i)
    i+=1
    c=0
print(max(y)) 