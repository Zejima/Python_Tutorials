import random
import sys
import os

grocery_list=['Juice', 'Tomatoes'
              'Bananas', 'Potatoes']
# Can put any data-type into a list

grocery_list[0]="Green Juice"
print("First Term", grocery_list[0])

print(grocery_list[1:3])

other_events= ['Wash Car', 'Pick Up Kids', 'Cash Check']

to_do_list=[other_events, grocery_list] # 2D list

print((to_do_list[1][1]))
grocery_list.append("Onions")# adds new item at the end of the index
grocery_list.insert(4,"Pickle")# Places "Pickle" in the second position of the index
grocery_list.sort()# sorts items
grocery_list.reverse() # reverses items
grocery_list.remove("Pickle") # specifically gets rid of item

to_do_list2= other_events+ grocery_list # Combines strings inside of lists

print(len(to_do_list2)) # gets length of the list
print (max(to_do_list2)) # gets the first aphebetically
print (min(to_do_list2))  # gets the last aphebetically



