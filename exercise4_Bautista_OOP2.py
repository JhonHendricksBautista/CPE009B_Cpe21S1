#example 1
class foo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b


foo_object = foo(3,4)
print(foo_object.add())

#example 2
class Counter:
    def __init__(self):
        self.current = 7
        
    def increment(self):
        self.current += 1
        
    def value(self):
        return self.current
    
    def reset(self):
        self.current = 0
        

counter = Counter()
counter.increment()
counter.increment()
counter.increment()

print(counter.value())

#example 3
class RegularPolygon:
    def __init__(self, side):
        self.side = side

class Square(RegularPolygon):
    def area(self):
        return self.side * self.side

class EquilateralTriangle(RegularPolygon):
    def area(self):
        return self.side * self.side * 0.433

obj1 = Square(5)
obj2 = EquilateralTriangle(3)

print("Area of Square:", obj1.area())
print("Area of Equilateral Triangle:", obj2.area())


#APPLICATION1
class Person:
    def __init__(self, name, pre, mid, fin):
        self.__name = name
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

class student1(Person):
    def grade(self):
        avg_grade = int((self._Person__pre + self._Person__mid + self._Person__fin)/3)
        print(f"Name: {self._Person__name} ")
        print(f"\tPrelim: {self._Person__pre}")
        print(f"\tMidterm: {self._Person__mid} ")
        print(f"\tFinal: {self._Person__fin}")
        print(f"\tAverage: {avg_grade} ")
        if avg_grade >= 50:
            print("\tPASS")
        else:
            print("\tFAIL")

    
    
class student2(Person):
    def grade(self):
        avg_grade = int((self._Person__pre + self._Person__mid + self._Person__fin)/3)
        print(f"Name: {self._Person__name} ")
        print(f"\tPrelim: {self._Person__pre}")
        print(f"\tMidterm: {self._Person__mid} ")
        print(f"\tFinal: {self._Person__fin}")
        print(f"\tAverage: {avg_grade} ")
        if avg_grade >= 50:
            print("\tPASS")
        else:
            print("\tFAIL")

    

class student3(Person):
    def grade(self):
        avg_grade = int((self._Person__pre + self._Person__mid + self._Person__fin)/3)
        print(f"Name: {self._Person__name} ")
        print(f"\tPrelim: {self._Person__pre}")
        print(f"\tMidterm: {self._Person__mid} ")
        print(f"\tFinal: {self._Person__fin}")
        print(f"\tAverage: {avg_grade} ")
        if avg_grade >= 50:
            print("\tPASS")
        else:
            print("\tFAIL")

    

Student1 = student1("jhon", 97, 99, 98)
Student2 = student2("kurt", 97, 99, 75)
Student3 = student3("dale", 97, 99, 67)

Student1.grade()     
Student2.grade()  
Student3.grade() 
        