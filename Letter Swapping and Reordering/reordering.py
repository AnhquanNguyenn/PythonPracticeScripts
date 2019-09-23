# Standard swapping mechanism within arrays, having a temporary variable to hold the
# the results of the swapping
def swapping(array, startIndex, endIndex):
    temp = array[startIndex]
    array[startIndex] = array[endIndex]
    array[endIndex] = temp

# Returns the last letter index once all the letters of a specific character are found
def pullToTheFront(array, startIndex, endIndex, letter):
    lastLetterIndex = -1
    
    while startIndex < endIndex:
        # we have found the letter, update start index and last letter indexes
        if array[startIndex] == letter:
            lastLetterIndex = startIndex
            startIndex += 1 
        # Just increment through to find letters that we need
        elif array[endIndex] != letter:
            endIndex -= 1
        # Swapping the letters once they have been organized properly
        else:
            lastLetterIndex = startIndex
            swapping(array, startIndex, endIndex)
    
    return lastLetterIndex 
            
# This method pulls to the front Rs, then Gs, and the remaining will be Bs
def reorder(array):
    # Rs will be pulled first 
    lastIndex = pullToTheFront(array, 0, len(array) - 1, 'R')
    
    # Gs will be next, but the starting point is the last index of all the Rs
    pullToTheFront(array, lastIndex + 1, len(array) - 1, 'G')
    
    return array


array = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(array)
print(reorder(array))
