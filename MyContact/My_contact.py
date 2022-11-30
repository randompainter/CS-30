# My Contacts List
import random
import json

# Main Program Loop 
loop = True

contacts = [
{
   "Name": "John",
   "Phone-Number": "102-421-612", 
   "Email": "JohnSoCool@email.com"
}, 
{
    "Name": "Sean", 
    "Phone-Number": "780-216-71724", 
    "Email": "Sean@email.com"
}, 
{
    "Name": "Joe", 
    "Phone-Number": "992-521-6125", 
    "Email": "Joe123@email.com"
}]

# Functions
def search_contacts(name):
    for i in range (len(contacts)):
        if contacts[i]["Name"] == name:
            return i
    # Else return -1 (Not Found)
    return -1

def display_names():
    for i in contacts:
        print(i["Name"])

def search_contact(): 
    selected_contact = input("Enter the contact you wish to find: ")
    search_contact = search_contacts(selected_contact.capitalize())
    if search_contact != -1:
        print("Closest Matching Results:")
        print("Name:", contacts[search_contact]["Name"]) 
        print("Phone-Number:", contacts[search_contact]["Phone-Number"]) 
        print("Email:", contacts[search_contact]["Email"])
    else:
        print("Contact was not found")   

def edit_contact():
    select_contact = input("Enter the contact name you wish to edit: ")
    edit = search_contacts(select_contact.capitalize())
    if edit != -1:
        contacts[edit]["Name"] = input("Enter a new name for the contact: ").capitalize()
        contacts[edit]["Phone-Number"] = input("Enter a new phone number for the contact: ")
        contacts[edit]["Email"] = input("Enter a new email for the contact: ")
    else:
        print("Contact not found")

def add_contact():
    add_name = input("Enter a name for this contact: ")
    add_number = input("Enter a new number for this contact: ")
    add_email = input("Enter a new email for the contact: ")
    print("Contact Added")
    newcontact = {
        "Name": add_name.capitalize(),
        "Phone-Number": add_number,
        "Email": add_email
    }
    contacts.append(newcontact)

def remove_contact():
    remove_selected = input("What is the name of the contact you would like to delete? ")
    remove = search_contacts(remove_selected.capitalize())
    if remove != -1:
        contacts.pop(remove)
        print("Contact Removed")
    else:
        print("Contact not found")

# Main Menu
loop = True 
while loop: 
    # Menu Options
    print("\n|MAIN MENU|")
    print("1. Display Contact Names")
    print("2. Search for Contact")
    print("3. Edit Contact")
    print("4. New Contact")
    print("5. Remove Contact")
    print("6. Exit")
    selection = input("\nSelect option (1-6): ")

    if selection == "1":
        display_names()
    elif selection == "2":
        search_contact()
    elif selection == "3":
        edit_contact()
    elif selection == "4":
        add_contact()
    elif selection == "5":
        remove_contact()
    elif selection == "6":
        loop = False
        print("Closing my contact...")
    else: 
        print("Please use a valid function(1-6) ")
