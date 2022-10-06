for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    s=(n*(n+1))//2
    print(s-sum(x))