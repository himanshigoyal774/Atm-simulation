# Python Object Oriented Programming
# Object: A "bundle" of related attributes (variables) and methods (functions)
# You need a class to define objects
# Class: (Blueprint) used to design the structure and layout of an object

# class Car:
#     def __init__(self, model, year, color, for_sale): # Constructor
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
        
#     def drive(self): # functions defined inside a class are called methods
#         print("You are driving the car")
    
#     def stop(self):
#         print("You stopped the car")
        
#     def printname(self,model):
#         print(f"The name of the car {model}")
        
# car1 = Car("Mustang", 2009, "red", False)
# car2 = Car("Corvette", 2023, "blue", True)

#----------------------------------------
# 1. Inheritance -> Multiple inheritance, Multi level inheritance.
# 2. Polymorphism
# 3. Abstraction
# 4. Encapsulation

# Four pillars of OOP

# class Student:
#     class_marks = 99

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# student1 = Student("Riya" ,"20")
# student2 = Student("Gimu" ,"25")

# print(student1.name)
# print(student2.age)



# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True

#         def eat(self):
#             print(f"{self.name} is eating")

#         def sleep(self):
#             print(f"{self.name} is sleeping")

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# class Mouse(Animal):
#     pass


# dog = Dog("Rockey")
# cat = Cat("Meow")
# mouse = Mouse("Mickeyy") 

# print(cat.eat())



# class variables = these are instances shared among class and its objects
#                   Defined outside the constructor
#                   Allows you to share data among all objects created from that class

class Student:

    class_year = 2026

    def __init__(self,name, age):
        self.name = name
        self.age = age

student1 = Student("Spongebob" , "23")
student2 = Student("dudu" ,"21")

print(student1.name)
print(student2.age)
print(student1.class_year)
print(student2.class_year)
