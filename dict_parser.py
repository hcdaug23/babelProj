#algorithm to check a list or any string for if it contains english words

import requests
import re

word_list = ["list", "of", "words"] #currently I have it to where it can only do single words but working on compatibility for sentence str's
found_words = [] #empty list to put found words in from above list (this list is required)

for i, val in enumerate(word_list): #yk what this does
  word = word_list.pop() #pops last word off list
  url = (f'https://www.dictionary.com/browse/{word}') #puts that word on dictionary.com url
  r = requests.get(url) #gets the html file for that url 
  str = (r.text) #sets html file to a variable
  match = re.search(r'noun|pronoun|adverb|verb|adjective|interjection|conjunction|preposition', str) #checks that html file for a POS 
  if match:                    #{
    found_words.append(word)   #if html has a POS then its a word then adds to found_words (logic is that if it doesnt have a POS then its not a word)
  word_list.insert(0, word)    #}
  
print(found_words) #prints list of confirmed English Dictionary.com words 
