def solution(array, k):
    for i in range(len(array)):
        target = k - array[i]
        if target in array:
            return True
    return False


def solution2(array, k):
    array.sort()
    j = len(array) - 1
    for i in range(len(array)):
        currentSum = array[i] + array[j]
        if currentSum < k:
            i += 1
        elif currentSum > k:
            j -= 1
        else:
            return True
    return False


array = [10, 15, 3, 7]
k = 17
l = 25
m = 13
n = 12
o = 8
p = 5

print("Solution 1")
print(solution(array, k))
print(solution(array, l))
print(solution(array, m))
print(solution(array, n))
print(solution(array, o))
print(solution(array, p))
print("Solution 2")
print(solution2(array, k))
print(solution2(array, l))
print(solution2(array, m))
print(solution2(array, n))
print(solution2(array, o))
print(solution2(array, p))
