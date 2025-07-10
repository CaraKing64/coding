text = ""

if text == "":
    text = input("Text to display: ")

newtext = ""

for letter in text:
    if letter in "acbdefghijklmnopqrstuvwxyz":
        newtext += ":regional_indicator_" + letter + ":"
    if letter == " ":
        newtext += "  "

print(newtext)