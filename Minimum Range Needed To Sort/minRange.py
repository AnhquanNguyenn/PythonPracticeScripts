# as we go through the list, the numbers should be bigger than the previous, but less
# than the next. If it doesn't satisify either, then that specific value is out of order
# and we need to update the lowIndex and maxIndex
def minRange(numbersRange):
    length = len(numbersRange) 
    maxIndex = length - 1            # max should be the last number, till proven otherwise
    
    if numbersRange == list():
        return "The List is Empty, There is Nothing To Sort"
    
    # Used to find the minimum index value for the unsorted list.
    # it should be the first value in the list that is less than the previous number
    for minIndex in range(0, length - 1):
        if numbersRange[minIndex] > numbersRange[minIndex + 1]:
            break
        
    # Parsed through the list completely and nothing was out of order
    if minIndex == length - 2:
        return "The List is Completely Sorted"
    
    # finding the max index of the unsorted list
    while maxIndex > 0:
        if numbersRange[maxIndex] < numbersRange[maxIndex- 1]:
            break
        maxIndex -= 1
    
    # assigning min and max value placeholders
    min = numbersRange[minIndex]
    max = numbersRange[minIndex]
    
    # finding the lowest and highest values within the sub list
    for i in range (minIndex + 1, maxIndex + 1):
        if numbersRange[i] > max:
            max = numbersRange[i]
        if numbersRange[i] < min:
            min = numbersRange[i]
            
    # finding the minIndex
    for i in range(minIndex):
        if numbersRange[i] > min:
            minIndex = i
            break
    
    # finding the maxIndex
    i = length - 1
    while i >= maxIndex + 1:
        if numbersRange[i] < max:
            maxIndex = i
            break
        i -= 1
        
    return (minIndex, maxIndex)
    
numbersRange = [1, 7, 9, 5, 7, 8, 10]
print(minRange(numbersRange))
numbersRange = []
print(minRange(numbersRange))
numbersRange = [1, 2, 3, 4, 5, 6, 7]
print(minRange(numbersRange))
