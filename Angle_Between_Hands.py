def angle(h,m):
    ha=((h%12)+(m)/60)*30
    ma=m*6
    a=abs(ha-ma)
    return min(a,360-a)
s=input()
h=int(s[:2])
m=int(s[3:])
print(angle(h,m))