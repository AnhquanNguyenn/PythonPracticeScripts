def findKthLargest(numbers, k):
    length = len(numbers)
    numbers.sort()
    index = length - k
    
    return numbers[index]

numbers = [3, 5, 2, 4, 6, 8]
k = 3
print(findKthLargest(numbers, k)) 