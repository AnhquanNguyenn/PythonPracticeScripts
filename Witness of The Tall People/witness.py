def witnesses(heights):
    i = 0
    count = 0
    length = len(heights)
    for height in heights:
        if (i == (length - 1) or (height > heights[i + 1])):
            count += 1
        i += 1
    return count

print(witnesses([3, 6, 3, 4, 1]))
