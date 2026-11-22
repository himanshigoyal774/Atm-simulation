# Lists, Sets, and Tuples

#  list is a type of ordered collection.   
#Fruit list

# Fruits = ["Apple","Banana","cherry"]
# print(Fruits[0])

# Fruits.append("orange")
# print(Fruits)

# Fruits.remove("Banana")
# print(Fruits)

# Fruits[0] = "Lichi"
# print(Fruits)

# print(len(Fruits))
# print("cherr" in Fruits).  #isme hame true or falsse pta lagega ki voh list m hai ya nhi
#---------------------------------------------------------------------------------------------
#Shoppping cart
# cart = []
# while True:
#     item = input("Add an item: ")
#     if item.lower() == "done":
#         break
#     cart.append(item)

# print(f"your cart: {cart}")
# print(f"Total items: {len(cart)}")

# Sets: it is also a type of data collection.
# Sets are unordered
# Duplicates are not allowed in a set.

# colors = {"red", "green", "blue", "red"}
# colors.add("Yellow")
# colors.discard("green")

# print(colors)

# a = {1, 2, 3}
# b = {2, 3, 4}

# # Union ( | ), Intersection (&), Difference (-)
# print(a|b)
# print(a&b)
# print(a-b)


# Tuples.
# Ordered data collection type.
# Immutable datatypes: Cannot be changed
# Mutable datatypes: CAn be changed.
# Tuple is an immutable datatype.

# point = (3, 5)
# point[0] = 10

# List: []
# Set: {}
# Tuple: ()

# point = (3, 5, 6)
# print(point[0])

# x, y, z = point # Tuple unpacking.
# print(f"x={x}, y={y}, z={z}")



# Functions: It is a resuable piece of code.
# def min_max(numbers):
#     return min(numbers), max(numbers)

# low, high = min_max([4, 8, 15, 16, 23, 42])
# print(f"low={low}, high={high}") 
#-----------------------------------------------------
# 2D Lists: A list inside a list
# list = [list1, list2, list3]

# fruits = ["apple", "orange", "banana"]
# vegetables = ["okra", "spinach", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print(groceries)


# Iterating in 2D lists
# for x in groceries:
#     for y in x:
#         print(y, end = " ")
#     print()