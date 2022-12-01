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




# 5

 


