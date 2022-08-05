# Users input
# Problem 1
# print("Problem 1")
# Write a program that asks the user to enter their name.
# Print a message that says hello to the user using his or her name.

User_name = input("Please Enter your name ""\n")
print("Hello", User_name)

#Problem 2
# print("Problem 2")
# Write a program that asks, What is your favorite color?. Assign the input to the variable named color.
# Print the following statement, "My favorite color is" where ____ is the value of the variable color.

favorite_color = input("what is your favorite color?""\n" )
print("your favorite", favorite_color)
#Problem 3
# print("Problem 3")
# Write Python code that asks, "What town do you live in?". Assign the input to the variable named town.
# Print the following statement, "I live in ____" where ____ is the value of the variable town.

users_town =  input("what town do live in?" "\n")
print("you live in", users_town)
# #Problem 4
# print("Problem 4")
# Write Python code that asks, "How many brothers do you have?".
# Assign the input to the variable named brothers.
# Print the following statement, "I have ____ brothers." where ____ is the value of the variable brothers.
number_of_brothers = int(input("How many brothers do you have? ""\n"))
print("You have ",number_of_brothers,"brothers")

# Next, ask, "How many sisters do you have?". Assign the input to the variable named sisters.
# Print the following statement, "I have ____ sisters." where ____ is the value of the variable sisters.
number_of_sister = int(input("How many sisters do you have?""\n"))
print("you have ", number_of_sister,"sisters")

# Assign the variable siblings to the sum of brothers and sisters.
# Print the following statement, "I have ____ siblings."
# sibling = int(input("How many siblings do you have ?""\n"))
# print("You have",sibling,"siblings")

# Assign the variable siblings to the sum of brothers and sisters.
# Print the following statement, "I have ____ siblings."

siblings = number_of_brothers + number_of_sister
print("wow! You have",siblings,"siblings in total.")

# print("Problem 5")
# Write a program that asks the user to enter the length and width of a room.
# Assign the variable area according to the formula.
length = int(input("what is the length of your room""\n"))
width = int(input("What is the width of your room ""\n"))
area = length  * width
print("The area of the rectangle is",area)
perimteter = (length *2) + (width * 2)
print("The perimeter of the room us", perimteter)

# print("Problem 6")
# Write Python code that asks, "What is the side of a square". Assign the input to the variable side.
# Assign the variable area according to the formula:
side = int(input("what is the side of a square ?""\n"))
area_side = side **2
print("the area of the a square is", area_side )
# perimeter
area_side1 = int(input("What is the side of a square?""\n"))
perimeter_side = side * 4
print("The perimeter is"perimeter_side)


