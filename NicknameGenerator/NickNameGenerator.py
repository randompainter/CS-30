# Nickname Generator 
import random

# Global Variables
loop = True

nick_name = ["Crusher", "Buster", "Buzz", "Bolter", "Mathematical-Genius", "Coder", "Clown Star", "Apex Predator", "Jester" ]

default_name = ("John Doe")

while loop:

  # Print Student Grades Menu
  print("\nMain Menu: " + "(" + default_name +")")

  print("1: Change Name")
  
  print("2: Generate Random Nickname")
  print("3: Display All Nickname")
  print("4: Add Nickname")
  print("5: Remove Nickname")
  print("\n6: EXIT")

  selection = input("\nEnter Selection (1-6): ")

  if selection == "1":
     first_name = str(input("\nPlease Enter Your First Name: "))
     last_name = str(input("Please Enter Your Last Name: "))
     default_name = first_name + " " + last_name
     print("\nCurrent name is: " + first_name +  " " + last_name)

  elif selection == "2":
        print("\nRANDOM NICKNAME")
        print("\n" + default_name + " The " + random.choice(nick_name))

  elif selection == "3":
    print("Display All Nickname")
    print("\nALL NICKNAMES")        
    for i in nick_name:
     print(default_name + " " + "The" + " " + i + " ")
        
  elif selection == "4":
    print("\nAdd New Nickname")
    new_nick_name = str(input("\n Please Enter A New Nickname: ")).title()

    if new_nick_name in nick_name: 
      print("This Nickname Already Exists")
    else:
      nick_name.append(new_nick_name)
      print(new_nick_name + " Has Been Added To The List Of Nicknames")

  elif selection == "5":
    print("Remove Nickname")

    nick_name_removal_selection = str(input("\nPlease Enter The Nickname You Wish To Remove: ")).title()

    if nick_name_removal_selection in nick_name: 
      nick_name.remove(nick_name_removal_selection)
      print(nick_name_removal_selection + " Has Been Removed From The List Of Nicknames")
    else:
      print(nick_name_removal_selection + " Is Not In The List O")
  elif selection == "6":
    print("Closing Nickname Generator.......")
    loop = False
  else:
    loop = True


