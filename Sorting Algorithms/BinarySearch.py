import random
import math

nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]
 
def binarySearch(anArray, value):
    # lower and upper index
    lower_Index = 0
    # length of array -1 to get index
    upper_Index = len(anArray) - 1

    while upper_Index >= lower_Index:
        middle_Index = (math.floor(lower_Index + upper_Index) // 2)

        # Check if value value equals middle index value
        if (anArray[middle_Index] == value):
            return middle_Index
        elif (value < anArray[middle_Index]):
            upper_Index = middle_Index -1
        elif (value > anArray[middle_Index]):
           lower_Index = middle_Index +1


    # Else if value not found
    return -1
    

  

print(binarySearch(nums, 100))
print(binarySearch(nums, 75))
print(binarySearch(words, "fish"))
print(binarySearch(words, "at"))
print(binarySearch(unsorted, 70))