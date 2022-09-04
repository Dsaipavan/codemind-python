def hap(x):
    s=0
    while x:
        r=x%10
        s+=r**2
        x//=10
    return s
n=int(input())
while hap(n)>9:
    n=hap(n)
print(hap(n)==1 or hap(n)==7)