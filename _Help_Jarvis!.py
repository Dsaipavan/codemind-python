for _ in range(int(input())):
    s=input()
    z=sorted(s)
    n=0
    for i in range(len(z)-1):
        if int(z[i])+1!=int(z[i+1]):
            n=1
            print('NO')
            break
    if n==0:
        print('YES')