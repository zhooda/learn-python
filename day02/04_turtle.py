# The turtle library is kinda useless imo
# but here it is anyways

# Importing the turtle module to extend pythons functionality
import turtle

# Now we're going to create a turtle which will go around the screen
# doing things for us
bob = turtle.Turtle()

# Make bob look like a turtle??
bob.shape("turtle")

# Change bobs color
bob.color("red")

# Make pen size larger
bob.pensize(7)

# Moving and turning
# I dont actually know what these functions do but thats what
# your course wants
bob.forward(50)
bob.left(45)
bob.forward(50)
bob.penup()
bob.left(45)
bob.forward(50)
bob.left(45)
bob.pendown()
bob.forward(50)
bob.left(45)
bob.forward(50)

# Where the turtle lives???
window = turtle.Screen()
# Exit window on click. This will wait for the screen to be clicked
# so that we can actually see what bob is doing. Otherwise it would
# exit too quickly for us to see anything
window.exitonclick()
