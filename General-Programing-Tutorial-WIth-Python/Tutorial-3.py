# Ask the user to user 2 values and store them in variables num1 and num2
num1, num2= input('Enter 2 numbers:').split() #.split assigns tow variables


# Convert the strings into regular numbers
num1=int(num1)
num2=int(num2)
# Add the values  entered and store in sum
sum = num1 + num2

# Subtract values and store in difference
difference = num1 - num2 # Difference is different than "difference"

# Multiply the values and store in the product
product = num1 * num2

# Divide the values and store in the quotient
quotient = num1 / num2

# Use the modulus to find the remainder
remainder = num1 % num2

#Print the results
print("{} + {} = {})".format(num1, num2, sum))
print("{} - {} = {})".format(num1, num2, difference))
print("{} * {} = {})".format(num1, num2, product))
print("{} / {} = {})".format(num1, num2, quotient))
print("{} % {} = {})".format(num1, num2, remainder))

