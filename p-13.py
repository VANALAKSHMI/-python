#3
n=int(input("n="))
if(1<=n<=100000):
    l=[]
    m=[]
    c = 0
    print("enter your",n,"integers:")
    for i in range(0,n):
        a=int(input(""))
        l.append(a)
        if(i==l[i]):
            if(i>-1):
              m.append(i)
              c=c+1
    if(c>0):
       for i in range(0,c):
         print(m[i],end='')
    else:
        print(-1)
else:
    print("invalid input")
