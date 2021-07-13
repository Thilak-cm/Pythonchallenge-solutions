# PYTHON CHALLENGE 5:
# To start off, click on banner.p in the page source
# that will take you to a site with seemingly rubbish characters 

import pickle  # peak hill sounds like pickle, the python serializing deserializing module
from urllib.request import urlopen

pickled_data = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(pickled_data)

for x in data:
    print("".join(key*value for key, value in x))
