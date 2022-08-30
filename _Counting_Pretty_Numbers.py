for i in range(int(input())):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        s=j%10
        if s==2 or s==3 or s==9:
            c+=1
    print(c)