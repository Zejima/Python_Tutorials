import random
import sys
import os

# functions are used to be reused and make more readable code

def addNumber(fNum,lnum): # def is to define a function, then a function name, then the parameters the function receives
    sumNum=fNum +lnum
    return sumNum
# What happens in these functions stays in these functions unless it is returned to us


print(addNumber(1,4)) # calling the function

print('What is your name')

name=sys.stdin.readline() # Gets input from the user

print('Hello', name)

