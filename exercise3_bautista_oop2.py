#create object rectangle
class Rectangle():
    def __init__(self, length, width): # initialize the attributes
        self.length = length
        self.width = width
        
    def perimeter(self):
        return (2*self.length) + (2*self.width)
    
    def area(self):
        return self.length*self.width
 
#user input for the parameters    
l = float(input("enter the length: "))
w = float(input("enter the width: "))
#use the input for instances 
rect = Rectangle(l, w)

#print the result
print(f"The perimeter of the rectangle is: {rect.perimeter()}")
print(f"The area of the rectangle is: {rect.area()}")
        