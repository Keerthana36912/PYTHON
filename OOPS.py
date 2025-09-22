class Rectangle:
    color = "Red"
    def set_dim(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def category(self):
        area= self.area()
        if area < 500:
            return "small"
        elif 500 <= area < 1000:
            return "medium"
        else:
            return "big"
    def display(self):
        print("rectangle color is: ", self.color)
        print("rectangle area is: ", self.area())
        print("rectangle perimeter is: ", self.perimeter())
        print("rectangle category is: ", self.category())
r1 = Rectangle()
r2 = Rectangle()
r3 = Rectangle()
length = 10
breadth = 20
r1.set_dim(length, breadth)
r2.set_dim(length + 10, breadth + 10)
r3.set_dim(length + 20, breadth + 20)
r1.display()
print("----------------------------")
r2.display()
print("----------------------------")
r3.display()
print("----------------------------")






