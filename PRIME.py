a=int(input("enter lower range:"))
b=int(input("enter higher range"))
for i in range(a,b+1):
    c=0
    for j in range(2,i):
        if(i%j==0):
            c=c+1
    if(c==0):
        print(i,end="   ")