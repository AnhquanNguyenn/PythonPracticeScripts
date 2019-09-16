# O(n^3) Solution Checking each individual pair and seeing if they equal the sum desired 
def threeSum_On3(numbers):
    # holding a sublist for each individual triplet that passes a + b + c = 0
    tempSubArray = list()
    outputList = list()         # output list is a list of lists
    length = len(numbers)       # length of the input list, is the iteration limits
    
    # Starting from index 0 all the way to i only needs to be 2 away from the index at the end
    # j needs to only be 1 index from the end, and k can go to the end. 
    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                # Checking if subarray tripley equals 0, if it does append to the tempSubarray
                if (numbers[i] + numbers[j] + numbers[k] == 0):
                    tempSubArray.append([numbers[i], numbers[j], numbers[k]])  
    
    # adding each temp sub array in the output list
    for l in tempSubArray:
        outputList.append(l) 
    
    return outputList


# O(n^2) Solution by sorting the list, and creating a left and right index to check the values
def threeSum_On2(numbers):
    length = len(numbers)
    found = False
    tempSubArray = list()
    outputList = list()

    # Sorting the array
    numbers.sort()
    
    for i in range(0, length - 1):
        # Initializing indexes 
        left = i + 1
        right = length - 1

        while left < right:
            if numbers[i] + numbers[left] + numbers[right] == 0:
                tempSubArray.append([numbers[i], numbers[left], numbers[right]])
                found = True
                left += 1
                right -= 1
            
            # In a sorted list, we now need to just increase the left index to make it larger
            elif numbers[i] + numbers[left] + numbers[right] < 0:
                left += 1
            
            # In a sorted list, we need to decrease the right index to make the value smaller
            else:
                right -= 1
            
                
    if found == False:
        return "No Triplet Found"
    
    # adding each temp sub array in the output list
    for l in tempSubArray:
        outputList.append(l)

    return outputList
    

numbers = [1, -2, 1, 0, 5]
print(threeSum_On3(numbers))
numbers = [0, -1, 2, -3, 1]
print(threeSum_On3(numbers))
numbers = [1, -2, 1, 0, 5]
print(threeSum_On2(numbers))
numbers = [0, -1, 2, -3, 1]
print(threeSum_On2(numbers))


