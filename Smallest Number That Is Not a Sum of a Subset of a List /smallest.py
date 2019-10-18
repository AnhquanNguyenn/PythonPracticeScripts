def findSmallest(numbersList):
    length = len(numbersList)
    res = 1

    for i in range(0, length - 1):
        if numbersList[i] <= res:
            res += numbersList[i]
        else:
            break
    
    return res
        
numbersList = [1, 2, 3, 8, 9, 10]
print(findSmallest(numbersList))
# 7
numbersList = [1, 3, 6, 10, 11, 15]
print(findSmallest(numbersList))
