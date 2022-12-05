nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def selectionSort(anArray):
  # i indicates how many items were sorted
    for i in range(len(anArray)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(anArray)):
            # Update the min_index if the element at j is lower than it
            if anArray[j] < anArray[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        anArray[i], anArray[min_index] = anArray[min_index], anArray[i]
 
selectionSort(nums)
selectionSort(words)
 
print(nums)
print(words)