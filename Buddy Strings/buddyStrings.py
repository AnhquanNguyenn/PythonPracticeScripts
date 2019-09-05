def buddyStrings(str1, str2):
    lengthStr1 = len(str1)
    lengthStr2 = len(str2)
    i = 0
    count = 0
    prev = -1
    curr = -1
     
    # If they are not equal lengths, they can never be equal despite swapping
    if lengthStr1 != lengthStr2:
        return False    
    
    # Loop through each individual array value till the end, we could have used either 
    # string length, doesn't matter they should be the same
    while i < lengthStr1:
        # If we have a difference in characters we need to increase the count
        if str1[i] != str2[i]:
            count += 1
            
            # We cannot have more than 2 difference for a swap 
            if count > 2:
                return False
            
            # Storing the current and previous characters to swap
            prev = curr
            curr = i
        
        
        # Moving on to the next character if they are the same in str1 and str2
        i += 1
    
    # If we looped through the entire string, and we don't see any differences, thus
    # we must have the case where all the characters are the same and the strings are 
    # both the same as well
    if (count == 0 and str1[0] == str1[1]):
        return True
    
    # checking the count must be 2, and the previous and current characters that were swapped
    # must now be the same after swap in respect to str1 and str2
    if (count == 2 and str1[prev] == str2[curr] and str1[curr] == str2[prev]):
        return True    
    
    return False   
    

str1 = "ab"
str2 = "ba"
print(buddyStrings(str1, str2))
str1 = "ab"
str2 = "ab"
print(buddyStrings(str1, str2))
str1 = ""
str2 = "aa"
print(buddyStrings(str1, str2))
str1 = "aa"
str2 = "aa"
print(buddyStrings(str1, str2))
str1 = "aaaaaaabc"
str2 = "aaaaaaacb"
print(buddyStrings(str1, str2))
