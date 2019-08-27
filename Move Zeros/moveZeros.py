def moveZeros(numbers):
    zerosList = []
    numbersList = []
    outputList = [] 
    
    for i, number in enumerate(numbers):
        if numbers[i] == 0:
            zerosList.append(numbers[i])
        else:
            numbersList.append(numbers[i])
    
    for i, output in enumerate(numbersList):
        outputList.append(numbersList[i])
    
    for i, outputs in enumerate(zerosList):
        outputList.append(zerosList[i])
    
    return outputList

input1 = [0, 1, 0, 3, 12]
input2 = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
print(input1, "->", moveZeros(input1))
print(input2, "->", moveZeros(input2))
