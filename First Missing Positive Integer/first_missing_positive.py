def first_missing_positive(numbers):
    missing_number = None
    temp_list = list()
    
    for num in numbers:
        # Skipping negative numbers, since we don't need them
        if num <= 0:
            continue
        
        temp_list.append(num)
    
    # sorting the list for easier manipulation, and to cut the search 
    # to be smaller since we only need the smallest missing positive integer    
    temp_list.sort()
    
    # In the case that we have the maximum value as the first or only values 
    # we're going to make the max to be 1 + the previous max
    if max(temp_list) <= temp_list[0]:
        maximum = temp_list[0] + 1
    else:
        maximum = max(temp_list)
    
    # Iterating from 1 to the max, and checking if that value 
    # is in the temp list or not, if it is not then we have found 
    # the smallest positive missing number
    for i in range(1, maximum):
        if i in temp_list:
            continue
        else:
            missing_number = i
            return missing_number
    
    # In the case that we have all the numbers that are the same, we can just simply
    # add 1 to the first element and that should now be the lowest missing positive number 
    if missing_number == None:
        missing_number = temp_list[0] + 1
             
    return missing_number

numbers = [3, 4, -1, 1]
print(first_missing_positive(numbers)) 
numbers = [1, 1, 0, -1, -2]
print(first_missing_positive(numbers))
numbers = [2, 3, 7, 6, 8, -1, -10, 15]
print(first_missing_positive(numbers))
numbers = [2, 3, -7, 6, 8, 1, -10, 15]
print(first_missing_positive(numbers))
