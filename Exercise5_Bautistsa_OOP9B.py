#polymorphism

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Inherit attribute of a person        
class Student(Person):
    def traits(self):
        return f"studying, playing, dancing, singing"
        

class Teacher(Person):
    def traits(self):
        return f"teaching, socializing, participating"
        
student = Student("dale", 19)
teacher = Teacher("sayo", 29)

print("As a student, I do", student.traits() ) 
print("As a teacher, I do", teacher.traits())

#CHALLENGE 1
print("\n")
print("Challenge 1")
class Food():
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
        
class Pork(Food):
    def info(self):
        return f"I like {self.name} and it came from {self.origin}"
    
class Beef(Food):
    def info(self):
        return f"I like {self.name} and it came from {self.origin}"

class Chicken(Food):
    def info(self):
        return f"I like {self.name} and it came from {self.origin}"
    
customer1 = Pork("Adobo", "Philippines")
customer2 = Beef("Wagyu", "Japan")
customer3 = Chicken("KFC", "USA")

print(customer1.info())
print(customer2.info())
print(customer3.info())