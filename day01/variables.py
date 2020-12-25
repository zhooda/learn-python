# Variables store data in a particular format (integer, string, floating point, boolean)
# A piece of memory on your computer is allocated to a specific variable
# The amount of memory / the size of the variable is determined by the variable type
# Variables go poof when the program terminates

# STANDARD PRIMITIVE TYPES

# Integer
a = 10

# Floating point (float)
b = 3.14

# String (string of characters)
c = 'Hello, World!'

# MAKING VARIABLES (pretty much identical to javascript)
# <variable name> = <data you want to store in the variable>
# String variables need to be surrounded by quotes
# (single or double is fine as long as the open and close quote are the same)
d = 'this is a valid string'
print(d)
d = "this is also a valid string"
print(d)

# You can find the type of a variable by using the built in "type" function
type_of_a = type(a)  # assigns the variable "type_of_a" to the result of the "type(a)" function
print(type_of_a)

# You can also nest functions so you don't have to worry about messy looking code
print(type(b))  # no variable is defined, but the type of b is still printed to the screen

# NAMING CONVENTIONS

# Most python programs use the snake_case naming convention
# In snake_case, all letters are lowercase and words are separated by "_"
this_is_a_variable = 100

# Other languages use the camelCase naming convention
# camelCase starts with a lowercase letter and capitalizes the first letter of each subsequent word
thisIsAVariable = 200

# Its always important to use meaningful variable names
# computers don't care about the names you use
Average = 10
Ave = 10
BobTheBuilder = 10
# are all the same to the computer, but to someone reading your code
# they can mean different things or introduce unnecessary ambiguity

# CONSTANTS
# In python, constants are just variables that dont change throughout the program
# You define a constant whereas you assign a variable (they're basically the same thing in python,
# its just the naming conventions that are different)
# Constants are usually named in ALL_CAPS with words separated by "_"
MY_CONSTANT = 100
PI = 3.141592653589793238462643383

# Since python doesn't really care about what programmers do, we could change MY_CONSTANT to whatever we want
MY_CONSTANT = 25  # however, this is very bad practice and can lead to errors down the line
# Your code editor will usually yell at you if you do this, even though python has no problem running this code

# EXPRESSIONS
# You probably know all about expressions from javascript and they're pretty much the same
# in python also

# Mathematical operands
# +, -, *, +
# ** (exponent or power)
# // (integer division)
# %  (remainder)


