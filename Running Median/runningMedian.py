def runningMedian(numbers):
    medianList = list()
    tempList = list()
    medianIndex = 0
    currentMedian = 0
    upperboundIndex = 0
    lowerboundIndex = 0 
    
    for num in numbers:
        tempList.append(num)
        tempList.sort()
        
        # If we have an even length that is even, then we have a situation where a median value is in between 
        # 2 numbers. If the length is odd, then we have a discrete value for the median
        if len(tempList) % 2 == 0:
            upperboundIndex = (len(tempList) // 2)
            lowerboundIndex = upperboundIndex - 1
            currentMedian = (tempList[upperboundIndex] + tempList[lowerboundIndex]) / 2
            medianList.append(currentMedian)         
            
        else:
            # find the median index
            medianIndex = (len(tempList) // 2)
            currentMedian = tempList[medianIndex]
            medianList.append(currentMedian) 
    
    return medianList


numbers = [2, 1, 4, 7, 2, 0, 5]
print(runningMedian(numbers))
