#Types of operator
# Arithmetic 
# Comparision 
# Logical 

# Logical operator
# Logical operators = used on conditional statements

#               and = checks two or more conditions if True
#                or = checks if at least one condition is True
#               not = True if condition is False, and vice versa

# Temp = 25
# Sunny = True

# if Temp >= 20 and Temp <= 30:
#     print(f"Temp is too High")
# else:
#     print(f"Temp is low")

# if Temp <= 0 or Temp >= 30:
#     print(f"The Temp is bad")
# else:
#     print(f"The Temp is good")

# if not Sunny:
#     print(f"It is sunny outside")
# else:
#     print(f"It is sunny inside")


# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# #                          Pring or assign one of two values based on a condition
# #                          X if condition else Y

# num = 10
# a = 9
# b = 3
# print("Postive" if num>= 0 else "Negative")
# result= "EVEN" if num%2 else "ODD"
# maximum = "Max" if num >= a else "Min"

# print(result)
# print(maximum)

# name = input("Enter the name: ")
# age = int(input("Enter your age: "))

# result = len(name)
# result = name.find("n")
# result = name.rfind("n")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit().  #True only if only number is present otherwise False
# result = name.isalpha().    #vice versa of isdigit
# result = age.count("2")
# result = age.replace("3","6")
# print(result)

#--------------------------------------------------------------------------------------------
# Validate user input exercise
# 1. username is no more than 12 characters.
# 2. username must not contain spaces.
# 3. username must not contain digits.

# username = input("Enter the username")

# if len(username)>= 12:
#     print(f"The username is no more than 12 characters.")
# elif username.isdigit():
#     print(f"The username mudt not contain spaces.")
# elif username.isalpha():
#     print(f"The ussername must not contain digit.")
# else:
#     print(f"Welcome {username}")


# ---------------------------------------------------------------------------------
# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

# credit_number = "1234-5678-9012-3456"
# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-2])
# print(credit_number[::4])

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")
#----------------------------------------------------------------------------------
# Email slicer program (exercise)

# email = input("Enter your email: ")

# index = email.index("@")

# username = email[:index]
# domain = email[index+1:]

# print(f"Your username is {username} and domain is {domain}")
#-----------------------------------------------------------------------------------


# format specifiers = {value:flags} format a value based on what flags are inserted.

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

# price1 = 30000000000.14159
# price2 = -987.653
# price3 = 12.2343

# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:}")

#-------------------------------------------------------------------------------
# while loop = execute some code WHILE some condition remains true

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
#-------------------------------------------------------------------------
# age = int(input("Enter your age"))

# while age <0:
#     print(f"You did not enter your age: ")
#     age = int(input(f"Enter valid age"))

# print(f"you are {age} year old ")
#-------------------------------------------------------------------------
# food = input("Enter a food you like (q to quit): ").  #iska mtlb hua ki q hua to bye varna you like food wala statemnt

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")
#---------------------------------------------------------------------------
# num = int(input("Enter your number #between 1-10: "))

# while num<1 or num>10 :
#     print(f"Enter a valid number")
#     num = int(input("Enter your number #between 1-10: "))

# print(f"your number is {num}")
