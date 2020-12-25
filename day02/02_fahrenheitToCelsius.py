# Defining constants
OFFSET = 32  # 32 ºF = 0 ºC
RATIO_CHANGE = 5 / 9

# Get temperature in fahrenheit from the user
sFahrenheit = input("Enter temperature in fahrenheit: ")

# Now we need to convert the string value to an integer
# so we can do math with it ;)

fFahrenheit = float(sFahrenheit)

# Now we can do some math
fCelsius = (fFahrenheit - OFFSET) * RATIO_CHANGE
print("The temperature in celsius is %.2f ºC" % fCelsius)
