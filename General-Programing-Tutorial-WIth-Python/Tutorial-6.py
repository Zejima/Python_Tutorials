# I age is 5 Go to Kindergarten
# Ages 6 though 17 goes to grades 1 through 12
# If  age is greater than 17 say go to college
# Try to complete with 10 or less lines

# Asks user for age
age = eval(input("Enter your ages 5 and up"))

#If age is 5 go to kindergarten

if age==5:
    print("Go to kindergarten")
elif (age>=6) and (age <=17):
    grade=age-5
    print("Go to {} grade ".format(grade))
elif age>17:
    print("Go to college")
else:
    print("Go to college")
