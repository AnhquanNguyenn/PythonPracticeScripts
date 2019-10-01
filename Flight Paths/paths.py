def paths(unorderedPaths, startingPoint, currentPath):
    completePath = None
    
    # Returning the most up to date path if there are no more paths that correlate
    if not unorderedPaths: 
        return currentPath + [startingPoint]
    
    # Enumerating through each of the lists and once we find the path, we try to find the next path available
    # by taking the current path off and looking through the others.
    for index, (city1, city2) in enumerate(unorderedPaths):
        if city1 == startingPoint:
            nextPath = paths(unorderedPaths[:index] + unorderedPaths[index + 1:], city2, currentPath + [city1])
            
            # Making sure there is a path after the current path we are on, or if there is a lexigraphically 
            # Smaller path to consider if there are multple valid paths.
            if nextPath:
                if not completePath or "".join(nextPath) < "".join(completePath):
                    completePath = nextPath

    return completePath

currentPath = []
unorderedPaths = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
startingPoint = 'YUL'
print(paths(unorderedPaths, startingPoint, currentPath))
currentPath = []
unorderedPaths = [('SFO', 'COM'), ('COM', 'YYZ')]
startingPoint = 'COM'
print(paths(unorderedPaths, startingPoint, currentPath))
currentPath = []
unorderedPaths = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
startingPoint = 'A'
print(paths(unorderedPaths, startingPoint, currentPath))
