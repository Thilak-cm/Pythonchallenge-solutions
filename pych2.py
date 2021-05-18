# PYTHONCHALLENGE LEVEL 2

from urllib.request import urlopen
import re

# url of the current pythonchallenge puzzle
link = "http://www.pythonchallenge.com/pc/def/ocr.html"

# reading the contents of the page source
f = urlopen(link)
page_source = f.read().decode()

# separates the commented part of the page source from the html part of the page source
data = re.findall("<!--(.*?)-->", page_source, re.DOTALL)[-1]
# this gives a two element list an an output; hence we take the last element
# as the first one contains the question ---> find rare characters in the mess below:

pattern = re.compile("[a-z]") # to find all the letters in data
rare_letters = pattern.findall(data)
print(rare_letters)

print("".join(rare_letters)) # joining all the elements of the list
# copy the output and paste it in the url to progress to the next level
