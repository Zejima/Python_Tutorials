import random
import sys
import os

# Dictionaries are basically maps
# Similar to lists, but you cannot join dictionaries together


super_villains={ 'Fiddler':'Issac Bowin', 'Scratchman' : 'Tim Timothy'}

print(super_villains['Fiddler'])

print(len(super_villains)) # number of supervillains

del super_villains ['Scratchman'] # delete supervillain

print(super_villains.get('Fiddler')) # get the value of the dictionary

print(super_villains.keys()) # get a list of supervillain keys

print(super_villains.values()) # gets values of the dictionary
