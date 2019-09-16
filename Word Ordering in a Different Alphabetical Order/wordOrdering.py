def wordOrdering(words, order):
    # Creating a dictionary 
    # {'z': 0, 'y': 1, 'x': 2, 'w': 3, 'v': 4, 'u': 5, 't': 6, 's': 7, 'r': 8, 'q': 9, 'p': 10, 
    # 'o': 11, 'n': 12, 'm': 13, 'l': 14, 'k': 15, 'j': 16, 'i': 17, 'h': 18, 'g': 19, 'f': 20, 
    # 'e': 21, 'd': 22, 'c': 23, 'b': 24, 'a': 25}
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
