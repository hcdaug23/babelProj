import pybel
import random
import time
import PyDictionary
import tkinter
import skim
import pandas as pd
import re

#def numbers and letters variables for hexadecimal
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

hex = (random.choice(letters))+(random.choice(numbers)) #any combination of up to 3260 nums and/or lowercase letters
wall = str(random.randint(1, 4)) #1-4
shelf = str(random.randint(1, 5)) #1-5
volume = str(random.randint(1, 32)) #1-32

#puts the hex/wall/shelf/volume into a URL to find the source of the book printed into a variable to use for printing said URL later
sourceVar = str(f"Source: https://libraryofbabel.info/book.cgi?{hex}-w{wall}-s{shelf}-v{volume}")

with open('book.txt', 'w') as f:
    for i in range(1):
        f.write(pybel.getbook(hex, wall, shelf, volume))
        f.write(sourceVar)
        f.write('\n')

print(sourceVar)
print()


with open('book.txt') as file:
  line = file.readline()
  for lines in book.txt:
    step_1 = line.split(",")
    for idx, item in enumerate(step_1):
      print("Word {}: {}".format(idx, item))
  


#for each word in each line, check if word is in english, if so, print, else, don't, and make it repeat for each line in book.txt





