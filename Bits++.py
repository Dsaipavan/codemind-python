s=0
for _ in range(int(input())):
    z=input()
    if z=='X++' or z=='++X':s+=1
    elif z=='X--' or z=='--X':s-=1
print(s)