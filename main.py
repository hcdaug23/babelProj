import pybel
import random
import ast
import re
import requests
from bs4 import BeautifulSoup as bs
import lxml

#def numbers and letters variables for hexadecimal
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#create an empty list to put the found words in
found_words = []
word_list = []

hex = (random.choice(letters))+(random.choice(numbers)) #any combination of up to 3260 nums and/or lowercase letters
wall = str(random.randint(1, 4)) #1-4
shelf = str(random.randint(1, 5)) #1-5
volume = str(random.randint(1, 32)) #1-32

#puts the hex/wall/shelf/volume into a URL to find the source of the book printed into a variable to use for printing said URL later
source_var = str(f"Source: https://libraryofbabel.info/book.cgi?{hex}-w{wall}-s{shelf}-v{volume}")
'''
with open('book.txt', 'w') as f:
    for i in range(1):
        f.write(pybel.getbook(hex, wall, shelf, volume))'''

print(source_var)
print()

with open('book.txt', 'r') as fp:
  lines = len(fp.readlines())
  print("parsing ", lines, " lines")

with open('book.txt', 'r') as file_object:
  for line in file_object:
    word_list = re.split(r'\s*[,.]\s*', line)
    for i, val in enumerate(word_list): 
      word = word_list.pop() 
      url = (f'https://www.dictionary.com/browse/{word}') 
      r = requests.get(url) 
      str = (r.text) 
      #soup = bs(r.content, "lxml")
      #pos = soup.findAll("span", {"class" : "luna-POS"})
      match = re.search(r'noun|pronoun|adverb|verb|adjective|interjection|conjunction|preposition', str) 
      if match:                   
        found_words.append(word)   
      word_list.insert(0, word)     
    
print(found_words)  
    
#9/27/22 fixed the line splitter so it should work to parse things now just need to fully make sure it works because it takes a long time
