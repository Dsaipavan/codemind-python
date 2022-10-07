n=int(input())
x=bin(n)[2:]
if x.count('1')==1:
    print(0)
else:
    a=2**len(x)
    b=2**(len(x)-1)
    print(min(abs(n-a),abs(n-b)))