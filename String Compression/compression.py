def compression(letters):
    compressedString = list()
    count = 1
    
    
    for i in range(1, len(letters)):
        # we have reached the end of the same consecutive letters
        if letters[i] != letters[i - 1]:
            compressedString.append(letters[i - 1])
            
            if count != 1:
                compressedString.append(count)
            count = 1
        else:
            count += 1
            
        if i == len(letters) - 1:
            compressedString.append(letters[i - 1])
            compressedString.append(count)
    
    
    
    return compressedString


letters = ['a', 'a', 'b', 'c', 'c', 'c']
print(compression(letters)) 