# Solution
# If n is odd, then initialize min and max to be the first element
# if n is even, then initialize min and max to be the first two elements respectively
# Rest of the elements go into pairs and then are compared respectively, as we 
# loop through we update the min and max
def findMinMax(numbers):
    n = len(numbers)
    
    # setting min and max values depending on array size, even or odd number of elements
    if n % 2 == 0:
        minimum = min(numbers[0], numbers[1])
        maximum = max(numbers[0], numbers[1])
        
        # starting index for even numbers
        i = 2
    else:
        minimum = maximum = numbers[0]
        
        # starting index for odd numbers
        i = 1
    
    # looping till the end of the array
    while i < n - 1:
        # the next number is larger, min and max need to be checked 
        if numbers[i] < numbers[i + 1]:
            minimum = min(minimum, numbers[i])
            maximum = max(maximum, numbers[i + 1])
        # the next number is smaller, min and max need to be checked
        else:
            minimum = min(minimum, numbers[i + 1])
            maximum = max(maximum, numbers[i])
            
        # going on to the next pair
        i += 2    
        
    return (minimum, maximum)


numbers = [3, 5, 1, 2, 4, 8]
print(findMinMax(numbers)) 
         
    
    
       
     
