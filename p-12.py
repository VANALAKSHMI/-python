#2
n=int(input("n="))
if(1<=n<=100000):
    l=[]
    m=[]
    print("enter your",n,"integers:")
    for i in range(0,n):
        a=int(input())
        l.append(a)
        m.append(sorted(l))
    c=m[-1]
    k=c[::-1]
    for i in range(0,n):
         print(k[i],end='')
else:
    print("invalid input")
