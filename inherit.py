# Inheritance = Allows a class to inherit attributes and methods from a different class
#               Helps with reusability and readability
#               class Child(Parent)

# class Animal:
#     def __init__(self,name,):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# class Mouse(Animal):
#     pass

# dog = Dog("Oroe")
# cat = Cat("Cookie")
# mouse = Mouse("Qui")

# dog.sleep()
# print(mouse.eat())


# Two types of Inheritance: 1. Multiple Inheritance, 2. Multilevel Inheritance.
# 1. Multiple Inheritance: Child class inherits from more than one parent class
# C (A, B).. Child (Parent1, Parent2)

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

# class calculator(self, a ,b):
#         self.a = a
#         self.b = b

#     def add(self):
#         print(f"Addition: {self.a + self.b}")

#     def sub(self):
#         print(f"Ssubtraction: {self.a - self.b}")

# a = int(input("Enter the value of a "))
# b = int(input("Enter the value of b"))

# calc1 =calculator(a ,b)

# calc1.add():
# calc1.sub():
# -------------------------------------------------
# MULTIPLY INHERITANCE:
# class prey:
#     def flee():
#         print("This animal is fleeing")

# class predator:
#     def hunt():
#         print("This animal is hunting")

# class Rabbit(prey):
#     pass

# class Hawk(predator):
#     pass

# class fish(prey, predator):
#     pass

# fish.hunt()
# Rabbit.flee()
# fish.flee()
# Hawk.hunt()

# # ---------------------------------------------
# MULTIYLEVEL INHERITANCE

class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
def show_class(self):
        print(f"The class of {self.name} is: {self.grade}")
        
    def print_age(self):
        print(f"The age of student is {self.age}")

class student1(Students):
    def read1(self):
        print("The student reads!!!")
        
class student2(student1):
    pass

# Students -> student1 -> student2
# Students -> student2
s1 = student2("Dhruv", 22, 4)


print(s1.age)


# super() function..    
 # Polymorphism


