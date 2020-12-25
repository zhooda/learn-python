# We can use the built-in input function to get
# input from a user :)

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

print(f"your name is {firstName} {lastName}")

# The input function always stores the users value
# as a string. You'll need to convert the data type
# if necessary

# Example 1: a simple calculator
print("This calculator just uses string input values :)")
num1 = input("Enter the first number:  ")
num2 = input("Enter the second number: ")
print(num1 + num2)
# without data type conversions, the input strings
# given by the user are just smushed together
# Check the data type of num1 and num2 with the "type()" function
print(type(num1), type(num2))

# In order to get numerical values from the user
# we need to convert the string inputs into numbers.
# We can use the "int()" function to convert strings to integers
print("\nThis calculator will convert user inputs to integers!")
num1 = int(input("Enter the first number:  "))
num2 = int(input("Enter the second number: "))
print(num1 + num2)
# Check the data type of num1 and num2 with the "type()" function
# hint: they should be integers now :)
print(type(num1), type(num2))