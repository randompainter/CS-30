import re  # Needed for splitting text with a regular expression
import time

def linearSearch(anArray, item):
 for i in range(len(anArray)):
    if anArray[i] == item: 
      return i
 return -1

def binarySearch(anArray, item):
  lowerIndex = 0
  upperIndex = len(anArray) - 1

  while lowerIndex <= upperIndex: 
    middleIndex = (lowerIndex + upperIndex) // 2
    if (item == anArray[middleIndex]):
      return middleIndex
    elif (item < anArray[middleIndex]):
      upperIndex = middleIndex - 1
    else: 
      lowerIndex = middleIndex + 1

  return -1


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    # convert all words in alice to lower
    for word in range(len(aliceWords)):
      aliceWords[word] = aliceWords[word].lower()
    loop = True 
    while loop: 
      print("\nMAIN MENU")
      print("1: Spell Check a Word in dictionary (Linear Search)")
      print("2: Spell Check a Word in dictionary (Binary Search)")
      print("3: Spell Check Alice in Wonderland (Linear Search)")
      print("4: Spell Check Alice in Wonderland (Binary Search)")
      print("5: EXIT")

      # Get Menu Selection from User
      selection = input("Enter Selection (1-5): ")


      if selection == "1": 
        search_word = input("Search for a word: ")
        search_lower = search_word.lower()
        print("Linear search starting...")
        start = time.time()
        search_dictionary = linearSearch(dictionary, search_lower)
        if search_dictionary != -1:
          end = time.time()
          print(search_lower + " is in the dictionary at position", str(search_dictionary), "(" + str((end - start)) + " Seconds" + ")")
        else:
          print(search_lower, "Was not found in the dictionary")
      elif selection == "2":
        search_word = input("Please enter a word: ")
        search_lower = search_word.lower()
        print("Binary search starting...")
        start = time.time()
        search_dictionary = binarySearch(dictionary, search_lower)
        if search_dictionary != -1:
          end = time.time()
          print(search_lower + " is in the dictionary at search_dictionary " + str(search_dictionary), "(" + str((end - start)) + " seconds" + ")")
        else:
          print(search_lower, "Was not found in the dictionary")
      elif selection == "3": 
        print("Linear search starting...")
        word_counter = 0
        start = time.time()
        for words in aliceWords:
          search_alice = linearSearch(dictionary, words)
          if search_alice == -1:
            word_counter += 1
        end = time.time()
        print("Number of words not found in dictionary: " + str(word_counter), "(" + str((end - start)) + " Seconds" + ")")
      elif selection == "4": 
        print("Binary search starting...")
        word_counter = 0
        start = time.time()
        for words in aliceWords:
          search_alice = binarySearch(dictionary, words)
          if search_alice == -1:
            word_counter += 1
        end = time.time()
        print("Number of words not found in dictionary: " + str(word_counter), "(" + str((end - start)) + " Seconds" + ")")
      elif selection == "5":
        print("Exiting Spellcheck...")
        loop = False
      else: 
        print("Invalid selection choice please use (1-5)")
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

# Call main() to begin program
main()