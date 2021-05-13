#PYTHONCHALLENGE LEVEL 2

from urllib.request import urlopen
from collections import Counter
import re

#url of the current pythonchallenge puzzle
link = "http://www.pythonchallenge.com/pc/def/ocr.html"

#reading the contents of the page source
f = urlopen(link)
page_source = f.read().decode()

#separates the commented part of the page source from the html part of the page source
data = re.findall("<!--(.*?)-->", page_source, re.DOTALL)[-1]
#this gives a two element list an an output; hence we take the last element
# as the first one contains the question ---> find rare characters in the mess below:

frequency = Counter(data).most_common()
frequency = tuple(frequency)
#converted to its tuple form so as to enable tuple matching done below

rare_letters = []
i = 0
#using tuple unpacking in for loop 
for str1, f in frequency:
    i += 1
    if f == 1:
        rare_letters.append(frequency[i-1][0])

print("".join(rare_letters))
#copy the output and paste it in the url to progress to the next level
