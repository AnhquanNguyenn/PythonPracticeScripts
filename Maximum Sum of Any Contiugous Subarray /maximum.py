def maximum(numbers):
    # if the maximum number in the list is less than 0, then we simply 
    # output a zero, or if we have an empty list as well
    if not numbers or max(numbers) < 0:
        return 0
    
    # Setting temporary max values, and change them as we progress 
    # through the array
    currentMax = numbers[0]
    overallMax = numbers[0]
    
    # iterating through the list, to find the current and overall max as 
    # we add numbers to the current max, and compare it to the overall max
    for num in numbers[1:]:
        currentMax = max(num, currentMax + num)
        overallMax = max(overallMax, currentMax)
 
    return overallMax
 

numbers = [34, -50, 42, 14, -5, 86]
print(maximum(numbers))
numbers = [-5, -1, -8, -9]
print(maximum(numbers))

     
