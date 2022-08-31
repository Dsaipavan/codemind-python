for _ in range(int(input())):
    n=int(input())
    o=1
    while n:
        o*=n
        n-=1
    print(o)