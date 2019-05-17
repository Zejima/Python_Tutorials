# Enter Calculation: 5*6
# 5*6 =30

# Store the user input of two numbers and the operator of choice
num1,operator,num2=input('Enter Calculation').split()

# Convert the strings into integers
num1= int(num1)
num2= int(num2)

# if + then we need to provide output based on addition

if operator == "+":
    print(" {} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print(" {} - {} = {}".format(num1, num2, num1-num2))
elif operator == "/":
    print(" {} / {} = {}".format(num1, num2, num1/num2))
elif operator == "*":
    print(" {} * {} = {}".format(num1, num2, num1*num2))
else:
    print("User either + - * or / next time {space out inputs}")
# Print the result



#elif= else if
# everything is indented under if-else statements

