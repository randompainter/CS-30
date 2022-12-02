# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)

num_red_pink = 0
for color in color_data:
    family = color["family"]
    if family == "Red" or family == "Pink":
        num_red_pink += 1

print("There are a total of", str(num_red_pink), "red and pink color")