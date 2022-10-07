for _ in range(int(input())):
    a=[]
    s=input()
    if s[0] in '}])':print(False)
    for i in s:
        if i=='{' or i=='[' or i=='(':
            a.append(i)
        elif i=='}' and a[-1]=='{':
            a.pop(-1)
        elif i==']' and a[-1]=='[':
            a.pop(-1)
        elif i==')' and a[-1]=='(':
            a.pop(-1)
    print(len(a)==0)