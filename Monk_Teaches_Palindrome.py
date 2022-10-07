for _ in range(int(input())):
    s=input()
    if s!=s[::-1]:print('NO')
    elif s==s[::-1] and len(s)%2==0:print('YES EVEN')
    else:print('YES ODD')