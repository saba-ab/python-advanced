with open("text.txt", "w") as text:
    text.write("this is a test")

with open("text.txt", "r") as t:
    print(t.read())
