def detection(input):
    tempStack = list()
    i = 0
    
    for char in input:
        tempStack.append(char)
        
        # adding element by element to the temp list, if we find some kind of ending
        # brace, bracket, parenthesis, we immediately check the previous item in the list 
        # to see if its a opening. If it is we remove it and the ending from the list
        if char == ']' and tempStack[i - 1] == '[':
            tempStack.remove('[')
            tempStack.remove(']')
            i = len(tempStack) - 1
        
        if char == '}' and tempStack[i - 1] == '{':
            tempStack.remove('{')
            tempStack.remove('}')
            i = len(tempStack) - 1
        
        if char == ')' and tempStack[i - 1] == '(':
            tempStack.remove('(')
            tempStack.remove(')')
            i = len(tempStack) - 1
        
        i += 1
        
    if tempStack == []:
        return True
    else:
        return False


input1 = "([])[]({})"
print(detection(input1))
input1 = "([)]"
print(detection(input1))
input1 = "((()"
print(detection(input1))
