# Sort Analyzer Assignment
import time

def bubbleSort(anArray):
    n = len(anArray)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if anArray[j] > anArray[j+1] :
               anArray[j], anArray[j+1] = anArray[j+1], anArray[j]

def selectionSort(anArray):
   for i in range(len(anArray)-1):
    
     min = i
     for j in range(i+1, len(anArray)):
         if anArray[min] > anArray[j]:
            min = j
            
     anArray[i], anArray[min] = anArray[min], anArray[i]


def insertionSort(anArray):
 
   for i in range(1, len(anArray)):
        current = anArray[i]
        j = i-1
        while j >=0 and current < anArray[j] :
               anArray[j+1] = anArray[j]
               j -= 1
        anArray[j+1] = current

def sort_data(sort_type, file_data_chosen):
        start = time.time()
        sort_type(file_data_chosen)
        end = time.time()
        return (end - start)



def main():
    # Load data files into variables
    randomData = loadDataArray("data-files/random-values.txt")
    reversedData = loadDataArray("data-files/reversed-values.txt")
    fewUniqueData = loadDataArray("data-files/few-unique-values.txt")
    nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")

    # Test file load
    #print(randomData[0:50])
    #print(reversedData[0:50])
    #print(fewUniqueData[0:50])
    #print(nearlySortedData[0:50])

    # Main Menu
    loop = True
    while loop:
        print("\nMain Menu")
        print("1: Sort All Data (Bubble Sort)")
        print("2: Sort All Data (Selection Sort)")
        print("3: Sort All Data (Insertion Sort)")
        print("4: Exit")
        # Print main menu and get user selection
        selection = input("Select options (1-4): ")

        # Process selection
        if (selection == "1"):
            print("\nBubble Sorting All Data")
            print("\nRandom Data: ",str(sort_data(bubbleSort, randomData)))
            print("Reversed Data:", str(sort_data(bubbleSort, reversedData)))
            print("Few Unique Data:", str(sort_data(bubbleSort, fewUniqueData)))
            print("Nearly Sorted Data:", str(sort_data(bubbleSort, nearlySortedData)))
        elif (selection == "2"):
            print("\nSelection Sorting All Data")
            print("\nRandom Data: ",str(sort_data(selectionSort, randomData)))
            print("Reversed Data:", str(sort_data(selectionSort, reversedData)))
            print("Few Unique Data:", str(sort_data(selectionSort, fewUniqueData)))
            print("Nearly Sorted Data:", str(sort_data(selectionSort, nearlySortedData)))
        elif (selection == "3"):
            print("\nInsertion Sorting All Data")
            print("\nRandom Data: ",str(sort_data(insertionSort, randomData)))
            print("Reversed Data:", str(sort_data(insertionSort, reversedData)))
            print("Few Unique Data:", str(sort_data(insertionSort, fewUniqueData)))
            print("Nearly Sorted Data:", str(sort_data(insertionSort, nearlySortedData)))
        elif (selection == "4"):
            loop = False
            print("Closing Analyzer")

def loadDataArray(fileName):
    # Return data from file as an array of integers.
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp



# Call main() to begin program
main()