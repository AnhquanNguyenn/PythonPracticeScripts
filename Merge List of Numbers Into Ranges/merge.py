def merge(numbers):
    outputList = list()     # output list to store our parsed strings
    subList = list()        # sublist to store each individual pair of consecutive elements
    index = -1              # Temporary value to hold the current index as value come in 
    
    # iterating through the numbers in the list
    for number in numbers:
        # We shouldn't do any comparisions if a list is smaller than 2 elements, because there is nothing 
        # to compare, and we would access elements outside the list
        if len(subList) <= 1:
            subList.append(number)
            index += 1
            
            # secondary condition to check when we have already had an element in the list, we need to check
            # if the element is in consistence with the consecutive numbers rule
            if subList[index] - 1 != subList[index - 1] and len(subList) >= 2:
                # remove the index we just added, due to it being not consecutive, update index to current max index value
                # and then update the ouput list with 
                subList.remove(subList[index])
                index -= 1
                minimum = subList[0]
                maximum = subList[index]
                outputString = str(minimum) + "->" + str(maximum)
                outputList.append(outputString)
                subList = list()
                subList.append(number)
                index = 0
            continue 
    
        elif (subList[index] - 1) == subList[index - 1] and (number == subList[index] + 1):
            subList.append(number)
            index += 1
            continue
        # if we ever encounter a number that is the same as the largest number in the sublist, 
        # it just doesn't get added, just continue on with the loop
        elif (number == subList[index]):
            continue
        #  When we reach an element that is non in consecutive order, we output the current min and max of the list, add it to the output list,
        # the current value being processed is then put back in to the list to iterate again
        else:
            minimum = subList[0]
            maximum = subList[index]
            outputString = str(minimum) + "->" + str(maximum)
            outputList.append(outputString)
            subList = list()
            subList.append(number)
            index = 0
    
    # To handle the very last value if there is any units that apply
    minimum = subList[0]
    maximum = subList[index]
    outputString = str(minimum) + "->" + str(maximum)
    outputList.append(outputString)
    
    return outputList
        
# Test Cases
numbers = [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
print(merge(numbers))
numbers = [0, 1, 2, 3, 4, 5, 7, 8, 9, 9, 10, 11, 15]
print(merge(numbers))
