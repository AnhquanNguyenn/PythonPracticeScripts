def decodeString(inputString):
    integerStack = list()
    stringStack = list()
    temp = ""
    output = ""
    
    for i in range(len(inputString)):
        count = 0 
        
        # if the character is a number we converted it into an integer and
        # push it onto the integer stack
        if inputString[i] >= '0' and inputString[i] <= '9':
            while inputString[i] >= '0' and inputString[i] <= '9':
                count = count * 10 + ord(inputString[i]) - ord('0')
                i += 1
                
            i -= 1
            integerStack.append(count)
            
        elif inputString[i] == ']':
            count = 0
            temp = ""
            
            if len(integerStack) != 0:
                count = integerStack[-1]
                integerStack.pop()
                
            while len(stringStack) != 0 and stringStack[-1] != '[':
                temp = stringStack[-1] + temp
                stringStack.pop()
                
            if len(stringStack) != 0 and stringStack[-1] == '[':
                stringStack.pop()
            
            # repeating the temp string from the count
            for j in range(count):
                output = output + temp
            
            # pushing to char stack
            for j in range(len(output)):
                stringStack.append(output[j])
            
            output = ""
            
        elif inputString[i] == '[':
            # previous element of the opening brace must be a number, then we can add to the character stacks
            # that need to be repeated until an ending brace.
            if inputString[i - 1] >= '0' and inputString[i - 1] <= '9':
                stringStack.append(inputString[i])

            # we just repeat the element once if not a number found
            else:
                stringStack.append(inputString[i])
                integerStack.append(1)
        
        # A letter to be repeated
        else:
            stringStack.append(inputString[i])
       
    # remaining characters in the stack are simply outputted
    while len(stringStack) != 0:
        output = stringStack[-1] + output
        stringStack.pop()
    
    return output 
    
    


inputString = '2[a2[b]c]'
print(inputString, "decoded =", decodeString(inputString)) 
inputString = '3[abc]'
print(inputString, "decoded =", decodeString(inputString))
inputString = "1[b]"
print(inputString, "decoded =", decodeString(inputString))
inputString = "2[ab]"
print(inputString, "decoded =", decodeString(inputString))
inputString = "2[a2[b]]"
print(inputString, "decoded =", decodeString(inputString))
inputString = "3[b2[ca]]"
print(inputString, "decoded =", decodeString(inputString))
