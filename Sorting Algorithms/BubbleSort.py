# Bubble Sort Function Assignment
nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog", "at", "good", "eye", "cat", "ball", "fish"]
 
 
def bubbleSort(anArray):
   
  for i in range(len(anArray)):
 
    for j in range(0, len(anArray) - i - 1):
      if anArray[j] > anArray[j + 1]:
        anArray[j], anArray[j+1] = anArray[j+1], anArray[j]  
               
               
bubbleSort(nums)
bubbleSort(words)
 
print(nums)
print(words)