def sortingColors(colors):
    sortedColorsList = list()
    count0 = 0
    count1 = 0
    count2 = 0
    
    # Keeping a count for each of the three colors, and then we will append each 
    # color at a time for each of those counts
    for color in colors:
        if color == 0:
            count0 += 1
        elif color == 1:
            count1 += 1
        else:
            count2 += 1
    
    while count0 > 0:
        sortedColorsList.append(0)
        count0 -= 1
    
    while count1 > 0:
        sortedColorsList.append(1)
        count1 -= 1
    
    while count2 > 0:
        sortedColorsList.append(2)
        count2 -= 1
        
    return sortedColorsList 

colors = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sorting: ")
print(colors)

afterSort = sortingColors(colors)
print("After Sorting: ")
print(afterSort)

