#102
n=int(input(""))
if(1<=n<=100000):
    s=0
    while(n>0):
        a=n%10
        b=a*a
        s=s+b
        n=n//10
    print(s)
