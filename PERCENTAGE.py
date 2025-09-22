class Student:
    dept="CSE"
    def set_dim(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.total=m1+m2+m3
        self.percentage=self.total//3
    def dispaly(self):
        print(f"Name: {self.name}")
        print(f"Marks: [{self.m1}, {self.m2}, {self.m3}]")
        print(f"Percentage: {self.percentage:}%")
students = []
for i in range(10):
    print("department:",self.dept)
    print(f"\nEnter details of student {i+1}:")
    name = input("Enter name: ")
    m1 = int(input("Enter marks for Subject 1: "))
    m2 = int(input("Enter marks for Subject 2: "))
    m3 = int(input("Enter marks for Subject 3: "))
    student=Student(name, m1, m2, m3)
    students.append(student)
    print(f"Percentage: {student.percentage:.2f}%")
print("------------------------------")
for student in students:
    student.display()

        
    
    
    