# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)

# 1
for i in color_data:
    print(i["name"], "(" + i["family"] + ")")

# 2
for i in color_data:
    if i["brightness"] >= 200:
     print(i["name"] + "," , str(i["brightness"]))

# 3 (Pink + Red = 15)
counter = 0
for i in color_data:
    if i["family"] == "Pink" or i["family"] == "Red":
      counter += 1
print("There are a total of", str(counter), "red and pink color")
    
# 4
counter = 0
user_input = input("Enter color family: ").capitalize()
for color in color_data:
    if user_input == color["family"]:
        print(color["name"], "(" + color["family"] + ")")
        counter += 1
print(counter, "Color found of this family")

# 5
letter_counter = 0
letter_input = input("Enter a letter: ").capitalize()
for color in color_data:
    if color["name"][0] == letter_input:
        print(color["name"])
        letter_counter += 1
print(letter_counter, "Colors that start with this letter ")




