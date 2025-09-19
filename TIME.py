def find(x,y,z):
    ht=0
    time=0
    step=1
    while(ht<x):
        if(step%2!=0):
            ht=ht+y
            time=time+1
            step=step+1
        else:
            ht=ht-z
            time=time+1
            step=step+1
    print("Total time is",time)
find(30,10,5)            
    