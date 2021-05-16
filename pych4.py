#PYTHONCHALLENGE 4

import re
from urllib.request import urlopen

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

#this function obtains the next nothing value
def get_nothing(content, i):
    current_nothing = re.search("\d+", link)
    next_nothing = re.search("next nothing is (\d+)", content)
    next_nothing = re.search("\d+", next_nothing.group())



    return current_nothing.group(), next_nothing.group()

#this value reads contents of the link
def read_content(link):
    f = urlopen(link)
    content = f.read().decode()
    return content

i = 0
while True:
    content = read_content(link)
    
    #this if case covers the possibility of the content having no numbers in it 
    #this occurs twice before we reach the answer
    if re.search("\d+" ,content) == None:
        print("in if loop")
        current_nothing = re.search("\d+", link)
        next_nothing = int(current_nothing.group()) // 2
        link = link.replace(current_nothing.group(), str(next_nothing))
        print("and the next nothing is " + str(next_nothing))
        
        #this if case checks if html is in the content, because if it is, then we have reached our answer 
        if "html" in content:
            print(content)
            break
        i +=1
        continue

    current_nothing, next_nothing = get_nothing(content, i)
    link = link.replace(current_nothing, next_nothing)
    print("and the next nothing is " + next_nothing)

    print(f"ith iteration:{i}")
    i +=1

#Take the output and past it in the url to progress to the next level