import zipfile
import re

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
