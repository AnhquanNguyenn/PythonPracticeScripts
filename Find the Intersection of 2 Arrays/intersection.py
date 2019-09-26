def intersection(list1, list2):
    outputList = list()
    
    for nums in list1:
        if nums in list2 and nums not in outputList:
            outputList.append(nums)
    return outputList

list1 = [1, 2, 2, 1]
list2 = [2, 2]
print(intersection(list1, list2))
list1 = [4, 9, 5]
list2 = [9, 4, 9, 8, 4]
print(intersection(list1, list2))
