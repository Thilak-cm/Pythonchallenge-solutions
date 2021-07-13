import zipfile
import re

# replace html with zip in the url, this will elicit the 
# downloading of a zipped file named channel.zip
# unzip it and you'll see a bunch of text files

f = zipfile.ZipFile("channel.zip")
print(f.read("readme.txt").decode())

next_nothing = "90052"

comments = []

while True:
    file_name = next_nothing + ".txt"
    content = f.read(file_name).decode()
    print(content)
    comments.append(f.getinfo(next_nothing + ".txt").comment.decode("utf-8"))
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    next_nothing = match.group(1)

print("".join(comments))

# you will see the word hockey 
# typing hockey in the url will lead you to another clue 
# telling you to look in the air, to look at the letters 
# each letter of hockeey comprises of characters which when 
# strung together form the word oxygen 

