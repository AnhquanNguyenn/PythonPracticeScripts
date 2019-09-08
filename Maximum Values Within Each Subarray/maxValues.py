def maxValues(numbers, k):
    maxElements = list()
    tempList = list()
    length = len(numbers)
    beginWindow = 0
    endWindow = 0
    count = 0
    
    while endWindow < length:
        # When we reach the maximum subarray count, we're gonna find the maximum within our
        # temp list and add that to our maxElements list for each subarray. We now move the 
        # begin window up 
        if count == k:
            maxElements.append(max(tempList))
            tempList = []
            beginWindow += 1
            endWindow = beginWindow
            count = 0 
        
        # Temp list has just been emptied and the next value to input is the index of beginWindow
        # else we have incremented the endwindow, and that now indexes the next value.
        if tempList == []:
            tempList.append(numbers[beginWindow])
        else:    
            tempList.append(numbers[endWindow])
        
        # Updating the end window point to move to the next value. If the endwindow reaches the max value 
        # in the list we have reached the end, we can simply just add the max value of the temp list, and 
        # get out of the loop
        if endWindow == length - 1:
            maxElements.append(max(tempList))
            break
        else:
            endWindow += 1
        count += 1
        
    return maxElements

print(maxValues([10, 5, 2, 7, 8 ,7], 3))
print(maxValues([10, 5, 2, 7, 8 ,7], 2))
print(maxValues([10, 5, 2, 7, 8, 7], 4))

'''
from collections import deque


def get_sliding_max(a, k):

    window_max_elements = list()

    if not a:
        return None
    if len(a) <= k:
        return max(a)

    dq = deque()

    for i in range(k):
        while dq and a[dq[-1]] < a[i]:
            dq.pop()
        dq.append(i)
    window_max_elements.append(a[dq[0]])

    for i in range(k, len(a)):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and a[dq[-1]] < a[i]:
            dq.pop()
        dq.append(i)

        window_max_elements.append(a[dq[0]])

    return window_max_elements


assert get_sliding_max([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert get_sliding_max([5, 2, 1], 2) == [5, 2]
'''
