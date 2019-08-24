def solution(inputArray):
    # Empty lists to hold product sums
    product = 1
    rightProductArray = list()
    for num in inputArray:
        product *= num
        rightProductArray.append(product)

    # print(rightProductArray)

    product = 1
    leftProductArray = list()
    for num in inputArray[::-1]:
        product *= num
        leftProductArray.append(product)
    leftProductArray = leftProductArray[::-1]

    # print(leftProductArray)

    outputArray = list()
    for i in range(len(inputArray)):
        num = None
        if i == 0:
            num = leftProductArray[i + 1]
        elif i == len(inputArray) - 1:
            num = rightProductArray[i - 1]
        else:
            num = leftProductArray[i + 1] * rightProductArray[i - 1]
        outputArray.append(num)

    return outputArray


input1 = [1, 2, 3, 4, 5]
input2 = [3, 2, 1]
print(solution(input1))
print(solution(input2))
