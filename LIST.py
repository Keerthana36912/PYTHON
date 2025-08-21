a=["Ram","Sahith","Manish","Murali"]
b=[[45,23,78,56],[27,89,56,78],[23,67,89,12],[34,67,89,45]]
per=[]
for i in b:
    d=sum(i)//4
    per.append(d)
for i in range(4):
    print("{}.{}:{}%".format(i+1,a[i],per[i]))
    