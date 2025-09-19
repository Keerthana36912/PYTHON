a=int(input("enter num1:"))
while(not (a>1000 and a<10000)):
    a=int(input("enter proper input"))
b=int(input("enter num2:"))
c=int(input("enter num3:"))
a1=[int(i) for i in str(a)]
b1=[int(i) for i in str(b)]
c1=[int(i) for i in str(c)]
key1=max(a1)+max(b1)+max(c1)
key2=min(a1)+min(b1)+min(c1)
print(key1-key2)