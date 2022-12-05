# Insertion Sort Algorithm
nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def insertionSort(anArray):

    for i in range(1, len(anArray)):
        value = anArray[i]
        pos = i - 1
        
        # Compare value with each element on the left of it until an element smaller than it is found
        # For descending order, change value<anArray[pos] to value>anArray[pos].        
        while pos >= 0 and value < anArray[pos]:
            anArray[pos + 1] = anArray[pos]
            pos = pos - 1
        
        # Place value at after the element just smaller than it.
        anArray[pos + 1] = value

insertionSort(nums)
insertionSort(words)

print(nums)
print(words)
