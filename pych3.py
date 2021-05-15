import re
from urllib.request import urlopen

#url of the current pythonchallenge puzzle
link = "http://www.pythonchallenge.com/pc/def/equality.html"

#reading the contents of the page source
url = urlopen(link)
page_source = url.read().decode()

content = re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", page_source)
print("".join(content))