def camelCase(input):
    count = 1
    minimumASCIIValue = ord("A")
    maximumASCIIValue = ord("Z")
    
    for letters in input:
        if (ord(letters) >= minimumASCIIValue and ord(letters) <= maximumASCIIValue):
            count += 1

    return count

input = "saveChangesInTheEditor"
print(camelCase(input))
input = "minimumSpanningTree"
print(camelCase(input))
