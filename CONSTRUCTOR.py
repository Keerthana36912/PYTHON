class cog:
    comp_name="COGNIZANT"
    comp_profit=5000000
    tax_per=10
    def __init__(self,name,salary,sharepercent):
        self.name=name
        self.salary=salary
        self.sharepercent=sharepercent
        self.tax=0
        self.profitshare=0
    def cal_tax(self):
        self.tax=((self.tax_per*self.salary)/100)
    def cal_Share(self):
        self.profitshare=((self.comp_profit*self.sharepercent)/100)
    def display(self):
        print("enter name:",self.name)
        print("enter salary:",self.salary)
        self.cal_tax()
        self.cal_Share()
        print("tax to pay:",self.tax)
        print("share percentage:",self.profitshare)
s=int(input("enter no of employees:"))
emp=[]
for i in range(s):
    name=input("enter name:")
    salary=int(input("enter salary:"))
    sharepercent=int(input("enter sharepercent:"))
    s1=cog(name,salary,sharepercent)
    emp.append(s1)
for i in emp:
    i.display()
    
    
    
    
    
    
    
    
    
    
       

