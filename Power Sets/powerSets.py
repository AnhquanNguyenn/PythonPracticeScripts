def powerSets(inputSet):
    outputSet = list()
    
    # If we have an empty set, then the only power set is the empty set itself
    if len(inputSet) == 0: 
        return [set()]
    
    
    currentNumber =  inputSet[0]
    childPowerSet = powerSets(inputSet[1:])
    outputSet.extend(childPowerSet)
    
    for childSet in childPowerSet:
        newSet = childSet.copy()
        newSet.add(currentNumber)
        outputSet.append(newSet) 
    
    outputSet = sorted(outputSet)
    return outputSet

inputSet = ([1, 2, 3])
print(powerSets(inputSet))
inputSet = ([])
print(powerSets(inputSet))
inputSet = ([1, 2])
print(powerSets(inputSet))
inputSet = ([1, 2, 3, 4, 5, 6])
print(powerSets(inputSet))

