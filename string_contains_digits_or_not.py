x='1234567890'
n=0
for _ in range(int(input())):
    z=input()
    for i in x:
        if i in z:
            print('Yes')
            n=1
            break
    else:
        print('No')