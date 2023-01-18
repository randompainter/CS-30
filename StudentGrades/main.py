# Place holder
import random
from tkinter import X

# Main Program Loop 
loop = True

grades = []
for i in range (0, 35):
  x = random.randrange(0, 101)
  grades.append(x)
while loop:
  # Print Student Grades Menu
  print("Student Grades Simulator Menu")

  print("1: Display All Grades")
  print("2: Display All Honours")
  print("3: Overall Stats")
  print("4: Randomize Grades")
  print("\n5: EXIT")

  selection = input("\nEnter Selection (1-5): ")

  if selection == "1":
    print("\nAll Student Grades")
    for x in grades: 
     print(str(x) + " %") 
  elif selection == "2":
    honour = 0
    for x in grades: 
      if x >= 80:
        honour += 1
        print(str(x),"%", "|Honour", honour)
  elif selection == "3":
      print ("Average STATS Of Students")
      print ("\nHigest Average: " + str(max(grades)) + " %")
      print ("\nLowest Average: " + str(min(grades)) + " %")
      print ("\nOverall Average: "+ str(round(sum(grades) / len(grades), 2)) + " %")
  elif selection == "4":

    print("GRADES HAVE BEEN RANDOMIZED")
    grades = []
    for i in range (0, 35):
     x = random.randrange(0, 101)
     grades.append(x)
     print(str(x) + " %") 
  elif selection == "5":
    print("\nStudent Grade Simulator Closing......")
    loop = False
  else:
    loop = True





