def maxValues(numbers, k):
    maxElements = list()
    tempList = list()
    length = len(numbers)
    beginWindow = 0
    endWindow = 0
    count = 0
    
    while endWindow < length:
        # When we reach the maximum subarray count, we're gonna find the maximum within our
        # temp list and add that to our maxElements list for each subarray. We now move the 
        # begin window up 
        if count == k:
            maxElements.append(max(tempList))
            tempList = []
            beginWindow += 1
            endWindow = beginWindow
            count = 0 
        
        # Temp list has just been emptied and the next value to input is the index of beginWindow
        # else we have incremented the endwindow, and that now indexes the next value.
        if tempList == []:
            tempList.append(numbers[beginWindow])
        else:    
            tempList.append(numbers[endWindow])
        
        # Updating the end window point to move to the next value. If the endwindow reaches the max value 
        # in the list we have reached the end, we can simply just add the max value of the temp list, and 
        # get out of the loop
        if endWindow == length - 1:
            maxElements.append(max(tempList))
            break
        else:
            endWindow += 1
        count += 1
        
    return maxElements

print(maxValues([10, 5, 2, 7, 8 ,7], 3))
print(maxValues([10, 5, 2, 7, 8 ,7], 2))
print(maxValues([10, 5, 2, 7, 8, 7], 4))
