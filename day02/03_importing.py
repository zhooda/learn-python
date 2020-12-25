# Python provides many different modules
# that extend the functionality of the language.
# We can import those different modules with the "import" keyword
# followed by the module name

import math  # The math library contains useful functions and constants like trig functions and pi

# Example: Area of circle
radiusOfCircle = float(input("Enter circle radius: "))
areaOfCircle = math.pi * radiusOfCircle ** 2  # math.pi is a constant stored in the math library
print("The area of the circle is %.4f" % areaOfCircle)

# Example: Square root of a number
numberToRoot = float(input("Enter a number to square root: "))
squareRoot = math.sqrt(numberToRoot)  # math.sqrt() is function stored in the math library
print("The square root of %.2f is %.2f" % (numberToRoot, squareRoot))
