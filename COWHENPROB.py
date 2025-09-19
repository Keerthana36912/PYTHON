legs=int(input("Enter the legs:"))
heads=int(input("Enter the heads:"))
flag=False
for cow in range(heads+1):
    hens=heads-cow
    if(cow*4+hens*2==legs):
        flag=True
        print("cows are:",cow)
        print("hens are:",hens)
if(flag==False):
    print("No solution...")
        

