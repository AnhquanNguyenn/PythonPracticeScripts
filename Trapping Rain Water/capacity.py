def capacity(puddles):
    amountOfWater = 0
    length = len(puddles)
    
    # To find the current maxes at a specific iteration, at the moment default set to 0
    leftMax = 0
    rightMax = 0
    
    # To iterate through each index value, one starting at the beginning, and one at the end 
    lowIndex = 0
    highIndex = length - 1
    
    # looping through as long as the two windows don't intersect one another
    while lowIndex <= highIndex:
        if puddles[lowIndex] < puddles[highIndex]:
            # updating the left max if we find a value larger than it 
            if puddles[lowIndex] > leftMax:
                leftMax = puddles[lowIndex]
            # We now have a puddle, so we add the amount of water puddles there is
            # The difference between the maximum height and the current shorter height
            else: 
                amountOfWater += leftMax - puddles[lowIndex]
            # moving on to the next element from the left
            lowIndex += 1
        else: 
            # updating the right max if we find a value larger than it
            if puddles[highIndex] > rightMax:
                rightMax = puddles[highIndex]
            # we have found a puddle, add the amounts
            else:
                amountOfWater += rightMax - puddles[highIndex]
            # moving on to the next element from the right
            highIndex -= 1
    return amountOfWater  
    
puddles = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
puddles2 = [2, 0, 2]
puddles3 = [3, 0, 0, 2, 0, 4]
puddles4 = [3, 0, 1, 3, 0, 5]
print(capacity(puddles))
print(capacity(puddles2))
print(capacity(puddles3))
print(capacity(puddles4))
