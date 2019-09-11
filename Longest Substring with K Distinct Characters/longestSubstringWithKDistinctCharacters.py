'''
def longestSubstringWithKDistinctChacters(substring, k):
    uniqueCharacterCount = 1
    maxCount = 0
    length = len(substring)
    #tempList = list()
    startWindow = 0
    endWindow = startWindow + 1
    index = 0
    
    while endWindow < length:
        if uniqueCharacterCount == k:
            maxCount = max(substringCount, maxCount)
            startWindow += 1
            uniqueCharacterCount -= 1
            substringCount = len(substring[startWindow:endWindow])
            if endWindow == length:
                return substringCount
            continue
        
        if substring[endWindow] != substring[endWindow - 1]:
            uniqueCharacterCount += 1
        
        substringCount = len(substring[startWindow:endWindow + 1])
        endWindow += 1

    return substringCount
'''
MAX_CHARS = 26

# Determines if we have a valid number of unique characters in a given substring
def isValid(count, k):
    val = 0
    for i in range(MAX_CHARS):
        if count[i] > 0:
            val += 1

    return (k >= val)

# Finds the maximum substring with exactly k unique characters
def longestSubstringWithKDistinctCharacters(substring, k):
    # to store our output values into a single list
    outputList = list()
    uniqueCharacters = 0    
    length = len(substring)

    # Associative array to store the count
    count = [0] * MAX_CHARS

    # Tranverse the string, fills the associative array
    # count[] and count number of unique characters
    for i in range(length):
        if count[ord(substring[i]) - ord('a')] == 0:
            uniqueCharacters += 1
        count[ord(substring[i]) - ord('a')] += 1

    # If there are not enough unique characters, show
    # an error message.
    if uniqueCharacters < k:
        print("Not enough unique characters")
        return

    # Otherwise take a window with first element in it.
    # start and end variables.
    currentStart = 0
    currentEnd = 0

    # Also initialize values for result longest window
    maxWindowSize = 1
    maxWindowStart = 0

    # Initialize associative array count[] with zero
    count = [0] * len(count)

    count[ord(substring[0]) - ord('a')] += 1    # put the first character

    # Start from the second character and add
    # characters in window according to above
    # explanation
    for i in range(1, length):
        # Add the character 's[i]' to current window
        count[ord(substring[i]) - ord('a')] += 1
        currentEnd += 1

        # If there are more than k unique characters in
        # current window, remove from left side
        while not isValid(count, k):
            count[ord(substring[currentStart]) - ord('a')] -= 1
            currentStart += 1

        # Update the max window size if required
        if currentEnd - currentStart + 1 > maxWindowSize:
            maxWindowSize = currentEnd - currentStart + 1
            maxWindowStart = currentStart

    outputList.append(maxWindowSize) 
    outputList.append(maxWindowStart)
    return outputList


# Driver function
substring = "aabcdefff"
k = 3
outputList = longestSubstringWithKDistinctCharacters(substring, k)
max_window_start = outputList[1]
max_window_size = outputList[0]
print("The Longest substring for", substring, "is", substring[max_window_start:], "of length", max_window_size)

substring = "aabacbebebe"
k = 3
outputList = longestSubstringWithKDistinctCharacters(substring, k)
max_window_start = outputList[1]
max_window_size = outputList[0]
print("The Longest substring for", substring, "is",
      substring[max_window_start:], "of length", max_window_size)

substring = "aaabbb"
k = 3
outputList = longestSubstringWithKDistinctCharacters(substring, k)
if (outputList):
    max_window_start = outputList[1]
    max_window_size = outputList[0]
    print("The Longest substring for", substring, "is",
          substring[max_window_start:], "of length", max_window_size)

    
