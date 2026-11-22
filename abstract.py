# Abstract classes: A class that cannot be instantiated on its own. These classes are meant to be subclassed
# The can contain abstract methods,  which are declared but have no implemenation
# Benefits:
# 1. Prevents instantiation of the class itself
# 2. Requires Children to use inherited abstract methods

# from abc import ABC , abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def go(self):
#         print(f"The car is driven")

#     def stop(self):
#         print(f"Stop the car")

# car = Car()

# car.go()
# car.stop()
        
# class Motorcycle(Vehicle):
#     def go(self):
#         print("Driving")

#     def stop(self):
#         print("STOP!")

# M1 = Motorcycle()

# M1.go()
# M1.stop()

# --------------------------------------------
# Abstract class, add sub div.. 
# 2 child classes,.. add_cal
#-------------------------------------------------
# from abc import ABC , abstractmethod

# class Calculator(ABC):

#     @abstractmethod
#     def add(self):
#         pass

#     @abstractmethod
#     def sub(self):
#         pass
    
#     @abstractmethod
#     def divi(self):
#         pass

# class cal1(Calculator):
#     def __init__(self,num1 , num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         print(f"Addition: {self.num1+self.num2}")

#     def sub(self):
#         print(f"Subtraction: {self.num1 - self.num2}")

#     def divi(self):
#         print(f"Division: {self.num1 / self.num2}")

# calc1 = cal1(21,7)

# calc1.add()
# calc1.divi()
# ----------------------------------------------------------------
# super(): Function used in a child class to call methods from a parent class 
# # Allows you to extend the functionality of child classes

    
# class Shape:
#     def __init__(self,color,is_filled):
#         self.color = color
#         self.is_filled = is_filled

#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self,color,is_filled,radius):
#         self.color = color
#         self.is_fillled = is_filled
#         self.radius = radius

#     def describe(self):
#         print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")

# class Square(Shape):
#     def __init__(self,color,is_filled,width):
#         self.color = color
#         self.is_filled =is_filled
#         self.width = width

#     def describe(self):
#           print(f"IT is a square with area of {self.width * self.width} cm^2")

# class Triangle(Shape):
#     def __init__(self,color,is_filled,height,width):
#         self.color = color
#         self.is_filled = is_filled
#         self.height = height
#         self.width = width

#     def describe(self):
#          print(f"IT is a triange with area of {self.width * self.height / 2} cm^2")
        

# circle = Circle(color =  "red" , is_filled = True ,radius = 5)
# square = Square(color = "Blue", is_filled = False , width = 8)
# triangle = Triangle(color = "yellow" , is_filled = True , height = 9 ,width = 8)

# circle.describe()
# triangle.describe()
#----------------------------------------------------------------------------------------------------
# PolyMorphism = Greek word that means to "same name -> have may forms"
# We have two ways to implement PolyMorphism:
# 1. Inheritance = An object could be treated as the same type as the parent class
# 2. Duck Typing

