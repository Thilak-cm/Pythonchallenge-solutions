# PYTHONCHALLENGE 4
import re
from urllib.request import urlopen

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
next_nothing = 12345  # this  is the first nothing value
text = "" # done so that while loop condition does not throw an error for the first iteration

while "peak" not in text:
    f = urlopen(link.format(next_nothing))
    text = f.read().decode('utf-8') # reading content of link after decoding

    if "nothing" not in text :
        next_nothing = int(next_nothing) / 2 # Divide by two to get next nothing
        print(text.format(next_nothing))
        continue

    print(text)
    match = re.search("the next nothing is (\d+)", text)
    next_nothing = match.group(1)

print("Use this in the url and proceed to the next level!")
