def overlap(intervals):
    overlapCount = 0
    tempOverlapCount = 0
    startTime = dict()
    endTime = dict() 
    
    # Creating a dictonary for our start times, and end times
    for start, end in intervals:
        if start not in startTime:
            startTime[start] = 0
        startTime[start] += 1
        
        if end not in endTime:
            endTime[end] = 0
        endTime[end] += 1
    
    # Indicating our minimum and maximum bounds
    earlestStartTime = min(startTime)
    latestEndTime = max(endTime)
    
    # Counting the times as they are in the list, if they overlap we can
    # take that interval out of consideration
    for i in range(earlestStartTime, latestEndTime):
        if i in startTime:
            tempOverlapCount += startTime[i]
            if tempOverlapCount > overlapCount:
                overlapCount = tempOverlapCount
        if i in endTime:
            tempOverlapCount -= endTime[i]
    
    return overlapCount

intervals = [(30, 75), (0, 50), (60, 150)]
print(overlap(intervals))
intervals = [(30, 75), (0, 50), (60, 150), (160, 170)]
print(overlap(intervals))
intervals = [(30, 75), (0, 50), (60, 150), (40, 150)]
print(overlap(intervals))
intervals = [(30, 75), (0, 50)]
print(overlap(intervals))
intervals = [(30, 75)]
print(overlap(intervals))
