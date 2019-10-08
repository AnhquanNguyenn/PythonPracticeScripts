def jump(numbers, startIndex, endIndex):
    minimum = float('inf')
    
    # If the initial index equals the last number in the list, we have reached the end
    if startIndex == endIndex:
        return 0
    
    if numbers[startIndex] == 0: 
        return float('inf')
    
    # checking for the minimum number of jumps necessary, 
    # if we have not reached the end with the current number of steps necessary, 
    # we should choose the largest overall gain within each subset
    for i in range(startIndex + 1, endIndex + 1):
        if i < startIndex + numbers[startIndex] + 1:
            jumps = jump(numbers, i, endIndex)
            if jumps != float('inf') and jumps + 1 < minimum:
                minimum = jumps + 1
        
    return minimum


numbers = [3, 2, 5, 1, 1, 9, 3, 4]
startIndex = 0
endIndex = len(numbers)
print(jump(numbers, startIndex, endIndex - 1))
numbers = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
startIndex = 0
endIndex = len(numbers)
print(jump(numbers, startIndex, endIndex - 1))
