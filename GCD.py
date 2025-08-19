a= int(input("enter a  number:"))
b=int(input("enter b number:"))
while(b!=0):
    rem=a%b
    a=b
    b=rem
print(a)