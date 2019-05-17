import random
import sys
import os

# if else and elif are used to perform  different actions based
# of: == != > < <= >=

# if statement executes code if a condition is met

age= 21

if age > 16:
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')

if age <=21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not old enough to drive')

if ((age >=1) and (age<=18)):
    print("You get a birthday")
elif (age == 21) or (age >= 65):
    print("You get a birthday")
elif not(age==30):
    print('you do not get a birthday')
else:
    print("You get a birthday party yeah")

#-------Loooping-----

for x in range(0,10):
    print(x, '', end='')
print('\n')

grocery_list =['Juice','Tomatoes', 'Potatoes', 'Bananas']

for y in grocery_list:
    print(y)

for x in [2,4,6,8,10]:
    print (x)
num_list=[[1,2,3],[2,4,6],[3,6,9]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])


random_num=random.randrange(0,100) #Generates random number between 1 and 100

while (random_num != 15):
    print(random_num)
    random_num=random.randrange(0,100)

i=0 # creation of iterator

while(i <= 20):
    if i%2==0:
        print(i)
    elif i==9:
        break # ends the loop
    else:
        i+=1 # i = i+1
        continue # comes back into the while loop

    i+= 1

