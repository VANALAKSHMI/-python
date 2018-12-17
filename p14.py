#4
n=int(input("a="))
if(1<=n<=100000):
    l=[]
    c=0
    print("enter your", n ,"integers")
    for i in range(1,n+1):
        a= int(input(""))
        l.append(a)
    print(l)
    for x in range(0,len(l)):
        c=0
        for y in range(0,len(l)):
            if(l[x]==l[y]):
                c=c+1

        if(c==1):
            print(l[x])
else:
    print("invalid size")
