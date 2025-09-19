def kishore(a,b):
    if(a==1):
        return
    while(a%b!=0):
        b=b+1
    print(b,end=" ")
    kishore(a//b,b)
n=int(input("enter any num:"))
kishore(n,2)
