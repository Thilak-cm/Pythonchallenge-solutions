# PYTHONCHALLENGE 4
import re
from urllib.request import urlopen

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
next_nothing = 12345  # this  is the first nothing value


# this value reads contents of the link
def read_content(url: str) -> str:
    f = urlopen(url)
    page_source = f.read().decode()
    return page_source


while True:
    content = read_content(link.format(next_nothing))

    # this if case covers the possibility of the content having no numbers in it
    if re.search("\d+", content) == None:

        # this if case checks if html is in the content, because if it is, then we have reached our answer
        if "html" in content:
            print(content)
            break

        print(content)
        next_nothing = int(next_nothing) // 2  # content of this link says Divide by two to get next nothing
        link.format(next_nothing)
        print("and the next nothing is " + str(next_nothing))
        continue

    match = re.search("next nothing is (\d+)", content)
    next_nothing = match.group(1)
    link.format(next_nothing)
    print("and the next nothing is " + next_nothing)

# Take the output and past it in the url to progress to the next level
