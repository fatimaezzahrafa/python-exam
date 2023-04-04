#part I:
#The first code: 
# first thing the random module was imported 
#in order to generate random variables
#then the string was imported as well which contains 
#all ascii characters including whitespace, tab etc...
# a new function was created and it was given the 
#parameter length.
#a variable characters was created 
#return a list of characters and join them together

#The second code:
#the os module is used to provide easy function which 
#allows the programmer to get an access to the operating 
#system informations.
#re modules is also used on this code to 
# datetime module is used to deal dates and times







#part II:
import os
import random
from collections import Counter, defaultdict
from datetime import datetime
def create_file():
 """Create a new file with a random filename and some random contents."""
 filename = f'file_{datetime.now().strftime("%Y%m%d%H%M%S%f")}.txt'
 with open(filename, 'w') as f:
  for i in range(10):
   f.write(f'Line {i}: {random.randint(1, 100)}\n')
 return filename
def read_file(filename):
 """Read the contents of a file and return as a string."""
 with open(filename, 'r') as f:
  return f.read()
def count_numbers(text):
 lines = text.splitlines()
 counts = defaultdict(int)
 for line in lines:
  words = line.split()
 for word in words:
  if word.isdigit():
   counts[int(word)] += 1
 return Counter(counts)
if __name__ == '__main__':
 filename = create_file()
 text = read_file(filename)
 counts = count_numbers(text)
 print(f'Counts for file {filename}: {counts}')
 os.remove(filename)
 print(f'Total count: {sum(counts)}')



import webbrowser
import re
def search_google(query):
 """Search for the given query on Google and open the first result in a web
browser."""
 url = f'https://www.google.com/search?q={query}'
 response = webbrowser.open(url)
 if not response:
  return 'Unable to open web browser'
 html = webbrowser.get().open(url).real().decode('utf-8')
 pattern = re.compile(r'<a href="(https?://.*?)"')
 match = pattern.search(html)
 if not match:
  return 'No search results found'
 result_url = match.group(2)
 response = webbrowser.open(result_url)
 if not response:
  return 'Unable to open web browser'
 return 'Success'
if __name__ == '__main__':
 query = None
 result = search_google(query)
 print(result)

 #the first error in this code is on the line 69 

 

 #Part III:
 import random
 import datetime
 import collections



