c='0123456789'
for _ in range(int(input())):
    x=input()
    print(''.join(sorted(set(x))) in c)