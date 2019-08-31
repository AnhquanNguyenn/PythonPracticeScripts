def merge(intervals):
    interval_start = set()
    interval_end = set()
    mergedList = list()
    currentActive = 0
    instantStatus = list([currentActive])
    start = None
    end = None
    
    for start, end in intervals: 
        interval_start.add(start)
        interval_end.add(end)
    
    min_start = min(interval_start)
    max_end = max(interval_end)
    
    for i in range(min_start, max_end + 1):
        if i in interval_end:
            currentActive -= 1
        if i in interval_start:
            currentActive += 1
        instantStatus.append(currentActive)
    
    for i in range(len(instantStatus)):
        if instantStatus[i] and not instantStatus[i - 1]:
            start = i
        if not instantStatus[i] and instantStatus[i - 1]:
            end = i
            mergedList.append((start, end))
            start = None
            end = None
    
    return mergedList

intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(merge(intervals))