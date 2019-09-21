def count_invalid_parenthesis(parenthesisString):
    count = 0
    tempStack = list()
    index = 0
    
    for parenthesis in parenthesisString:
        tempStack.append(parenthesis)
        
        if tempStack[index] == ')' and tempStack[index - 1] == '(':
            tempStack.remove(')')
            tempStack.remove('(')
            index = -1 
            
        index += 1
    
    for i in tempStack:
        count += 1
    
    return count
    
input1 = "()())()"
print(count_invalid_parenthesis(input1))
