
def lookAndSay(nth_term):
    # For the first two terms in the list we can simply return 
    # our base cases 
    if nth_term == 1:
        return "1"
    if nth_term == 2:
        return "11"
    # If we have a value greater than 2 we can now calculate the next
    # sequence based on the previous one
    
    # to hold the previous character to count
    output = "11"

    for i in range(3, nth_term + 1):
            # Dummy character ensured to the iteration goes one more than the one expected
        output += "$"
        length = len(output)
        count = 1       # matching characters within the string
        temp = ""       # nth term in the series, we add values to the string as we parse through
        for j in range(1, length):
            if output[j] != output[j - 1]:
                # Appending the count of a specific number to temp
                temp += str(count + 0)
                
                # Appending the value to temp
                temp += output[j - 1]
                
                # Resetting count
                count = 1
            else:
                count += 1
    
        output = temp
        
    return output


for nth_term in range(1, 16): 
    print("Term", nth_term, "=", lookAndSay(nth_term)) 

