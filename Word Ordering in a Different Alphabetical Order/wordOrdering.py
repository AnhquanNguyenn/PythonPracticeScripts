def wordOrdering(words, order):
    # Creating a dictionary 
    orderIndex = {c: i for i, c in enumerate(order)}
    
    for i in range(len(words) - 1):
        # we can only compare two words at a time
        word1 = words[i]
        word2 = words[i + 1]
        
        # Iterate through until the minimum length of either word. 
        # if one word is longer than the other and has the same letters as the
        # other word then we assume that it is larger
        for k in range(min(len(word1), len(word2))):
            # Checking letter by letter if the words are the same, if not, 
            # Check the order index and if that index is larger in word1 than word2,
            # its not in order
            if word1[k] != word2[k]:
                if orderIndex[word1[k]] > orderIndex[word2[k]]:
                    return False
                break
                
            else:
                # in the case that all the letters are the same, up to certain letter, and the 
                # loop ends, we need to check if one word is longer than the other, and if the first 
                # word is longer then it is not in order
                if len(word1) > len(word2):
                    return False
                    
    return True


# Test Case 1 
words = ["abcd", "efgh"]
order = "zyxwvutsrqponmlkjihgfedcba"
print(wordOrdering(words, order))

# Test Case 2
words = ["zyx", "zyxw", "zyxwy"]
order = "zyxwvutsrqponmlkjihgfedcba"
print(wordOrdering(words, order))
