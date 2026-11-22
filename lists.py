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
#----------------------------------

# Numpad 
# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #

num_pad = ((1,2,3),
            (4,5,6),
            (7,8,9),
            ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end =" ")
    print()   