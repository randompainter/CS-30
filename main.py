# Data management
import json

loop = True

friend_list = []
game_list = [{
    "Name": "Call Of The Goats",
    "Genre": "Horror",
    "Price": "40.99"
},
{
    "Name": "Forkknife",
    "Genre": "Puzzle",
    "Price": "53.78"
},
{
    "Name": "Lost In Woods",
    "Genre": "Action",
    "Price": "24.56"
},
{
    "Name": "Sleender Men",
    "Genre": "Mystery",
    "Price": "9.99"
},
{
    "Name": "Garbage Truck Simlator",
    "Genre": "Casual",
    "Price": "5.99"
},
{
    "Name": "Joe The Joker",
    "Genre": "Horror",
    "Price": "1.99$"
},
{
    "Name": "Not Finding Bigfoot",
    "Genre": "Shooter",
    "Price": "1.99"
},
{
    "Name": "Valor Rant",
    "Genre": "Open-World",
    "Price": "99"
},
{
    "Name": "Leauge Of Worthless",
    "Genre": "Battle Royale",
    "Price": "0.00"
},
{
    "Name": "Pokeman Beeps",
    "Genre": "Rhythm",
    "Price": "45.99"
}]

def display_game():
    for game in game_list:
        print(game["Name"])

def display_friends():
    for friend in friend_list:
        print(friend["Name"])

def search(list, name):
    for game in range(len(list)):
        if game_list[game]["Name"] == name:
            return game
    return -1
def search_game():
    select_game = input("\nEnter a game name: ").title()
    position = search(game_list, select_game)
    if position != -1:
        print("Closest Matching Result: ")
        print("Name:", game_list[position]["Name"])
        print("Genre:", game_list[position]["Genre"])
        print("Price:", game_list[position]["Price"])
    else:
        print("Game was not found")

def sort_game():
    for price in game_list:
        if price["Price"] >= 20:
            print(price["Name"], price["Price"])



# Main Menu
while loop: 
    # Menu Options
    print("\n|MAIN MENU|")
    print("1. Display List")
    print("2. Search for Game")
    print("3. Sort Games")
    print("4. New Contact")
    print("5. Remove Contact")
    print("6. Exit")
    selection = input("\nSelect option (1-6): ")

    if selection == "1":
        print("Game List = 1, Friend List = 2: ")
        display_list = input("Choose which list to display: ")
        if display_list == "1":
            print("\nAll Games: ")
            display_game()
        elif selection == "2": 
            print("All friends")
            display_friends()
        else:
            if len(friend_list) == 0:
                print("No contact found")

    elif selection == "2":
        print("Search for a game by name: ")
        search_game()
    elif selection == "3":
        sort_game()
    elif selection == "4":
        print("All avaliable games: ")
    elif selection == "5":
        print("All avaliable games: ")
    elif selection == "6":
        loop = False
        print("Closing my contact...")
    else: 
        print("Please use a valid function(1-6) ")