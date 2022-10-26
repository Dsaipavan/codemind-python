for _ in range(int(input())):
    s=input()
    l=len(s)
    c=0
    for i in range(1,l):
        if s[i]==s[i-1]:
            c+=1
    print(c)