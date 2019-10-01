def push(val):
    stack.append(val)
    
def pop():
    if stack == []:
        return None
    else:
        stack.pop()
        
        topElementIndex = len(stack) - 1
        topElement = stack[topElementIndex]
        
        return topElement

def maximum():
    if stack == []:
        return None
    else:
        maxElement = max(stack)
        return maxElement
    

stack = list()
print(pop())
print(maximum()) 
push(1)
push(2)
push(3)
push(4)
push(5)
print(stack)
print("The Largest Element In The List Is:", maximum())
print("Top Element On The Stack After Pop:", pop()) 
print(stack)
print("The Largest Element In The List Is:", maximum())
