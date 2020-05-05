def findMissingNumbers(numbers):
    missingNumbers = list()
    
    for i in range(1, max(numbers) + 1):
        if i in numbers:
            continue
        else:
            missingNumbers.append(i)
    
    return missingNumbers


numbers = [4, 5, 2, 6, 8, 2, 1, 5]
print(findMissingNumbers(numbers))

numbers = [4, 6, 2, 6, 7, 2, 1]
print(findMissingNumbers(numbers))
