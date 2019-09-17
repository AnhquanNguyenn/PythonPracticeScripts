def encode(string):
    encodedString = ""          # output encoding
    length = len(string)        # length of the string, for iteration purposes
    count = 0                   # to handle the number of the same characters encountered
    
    for i, _ in enumerate(string):
        # To help with iteration purposes, and prevent out of bounds indexing
        if i == 0:
            count += 1
            continue
        
        # previous character is equal to the current character, then we can increase the count
        # else we have a difference, and the count must be reset for the next character, and we 
        # output the results to the encoded string, count then the character
        if string[i] == string[i - 1]:
            count += 1
        else:
            encodedString = encodedString + str(count) + string[i - 1]
            count = 1
            
        # for the last appending character yet to be added
        if i == length - 1:
            encodedString = encodedString + str(count) + string[i - 1]
            break
            
    return encodedString

def decode(encoding):
    decodedString = ""          # output for our decoded string
    length = len(encoding)      # length of the encoded string, iterative purposes
    count = 0                   # to hold how many iterations to print a specific character
    
    # checking each character. If it is a number, then we change the count to that number, else it 
    # is the character that we need. We add to decoded string the count of that specific character
    for char in encoding:
        if char.isdigit():
            count = int(char)
            continue
        
        else:    
            for i in range(count):
                decodedString = decodedString + char
            
            # resetting count for the next character
            count = 0
    
    return decodedString

# Test Cases
string = "AAAABBBCCDAA"
print("String before our encoding:", string)
encoding = encode(string)
print("String after we encode it: ", encoding)

print("String before our decoding:", encoding)
decoding = decode(encoding)
print("String after we decode it: ", decoding)
