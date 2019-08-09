def jumpingOnClouds(c):
    steps = 0
    index = 0
    length = len(c)
    while index < (length - 1):
        if (index + 2 <= length - 1 and c[index + 2] != 1):
            index += 2
        else:
            index += 1

        steps += 1

    return steps


testCase1 = [0, 0, 1, 0, 0, 1, 0]
testCase2 = [0, 0, 0, 1, 0, 0]

print(jumpingOnClouds(testCase1))
print(jumpingOnClouds(testCase2))
