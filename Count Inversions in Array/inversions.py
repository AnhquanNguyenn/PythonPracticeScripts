def inversions_On2(array):
    inversionsCount = 0
    
    # checking every possible pair to determine if a value is larger than the other, if the previous
    # number is larger than we haev an inversion. 
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if (array[i] > array[j]):
                inversionsCount += 1
    return inversionsCount


def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr) // 2]
        b = arr[len(arr) // 2:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]


    return c, inversions


# Test cases for O(n^2) simple solution
array = [1, 2, 3, 4, 5]
print(inversions_On2(array))
print(mergeSortInversions(array))
array = [2, 1, 3, 4, 5]
print(inversions_On2(array))
print(mergeSortInversions(array))
array = [2, 4, 1, 3, 5]
print(inversions_On2(array))
print(mergeSortInversions(array))
array = [5, 4, 3, 2, 1]
print(inversions_On2(array))
print(mergeSortInversions(array))
