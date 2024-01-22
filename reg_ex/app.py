import re

text = "the rain in spain"

x = re.search("spain$", text)

if x:
    print("we have a match")
else:
    print("not matching")
