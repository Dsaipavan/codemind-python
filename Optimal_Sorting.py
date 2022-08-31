for _ in range(int(input())):    
    y=int(input())
    x=list(map(int,input().split()))
    if sorted(x)==x:
        print(0)
        continue
    else:
        print(sorted(x)[-1]-sorted(x)[0])