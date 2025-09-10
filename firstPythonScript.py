# import random
# def get_choices():
#     player_choice = "rock"
#     computer_choice ="paper"

#     list_of_choices = ["rock","paper","seccor"]

#     return list_of_choices[random.randrange(0,list_of_choices.__len__())]

# print(get_choices())

# name =  input('Name: ')
# age = input('age: ')
# print("hello", name , "and you are", age )

# x = 9
# y=3
# result = x%y
# print(result)

# num = input('Number: ')
# print(int(num) -5)

# str = input('Enter string: ')
# print(str.lower() ,"in lower case")
# print(str.upper(), "in upper case")
# print(str.capitalize(), "this will capitalize the first letter in the first word")
# print(str.casefold())
# print(str.count('a'), "it counts the given  charecters in the string and it is case sensitive")

# tup = (11,33,44,22,"sd")
# list = [3423,323,22,4,2,243]

# for i in range(10):
#     print(i)

# for i  in range(len(list)):
#     print(i)

# for i , element in enumerate(tup):
#     print(i, element)

# range function has start stop and step where start is where you want to start and stop is where you want to end and step is how many times you want to increment elements
# by default range function takes stop if you give single number which means it starts from zero to the stop value that you have specified and this function returns a collection


# x =[0,1,2,3,4,5,6,7,8]
# y = ['hi','hello','goodbye','cya','sure']
# s="hello"

# sliced =x[0:4:2] starts at zero ends at 4 and jumps number by 2
# sliced =x[:4] starts at zero ends at 4
# sliced =x[0:] starts at zero ends at the end of the list
# sliced =x[:4:2] same as the first one
# sliced =x[::2] starts at zero ends at end of the list and jumps by 2
# sliced =x[::-1] it starts from end of the list and jumps back to start basically reversing the list.

# these slice operaters are work on string tuple aswell and on any collection


# print(sliced)

# x = set()  # this represent empty set
# s = {4,32,2,2} #this is a set of integer values
# s2= {4,2,11,44} #this is also the set of integer values
# print(s ,"s set")
# print(s2, "s2 set")
# print(s.union(s2), "union of s and s2")
# print(s.intersection(s2) ,"intersection of s and s2")
# print(s.difference(s2),"deference of s and s2")


# # comprehension
# x = [x for x in range(5)]


# def order_pizza(size, *toppings, **details):
#     print("Your Pizza size is", size)
#     print("Your Toppings are: ")
#     for topping in toppings:
#         print(topping)

#     if details["delivery"] == "door":
#         print("Your Pizza will be deliverd to your home")
#     elif details["delivery"] == "pickup":
#         print("Your Pizza is ready please collect from the counter")

#     if details["cost"] != None:
#         print("Total Price is:", details["cost"])


# order_pizza("large", "peperoni", "onion", "tomato", delivery="door", cost=400)
