def returnList(sentence, words):    
    wordSet = set(words)            # To convert our list, to a set of the words
    sentenceOutput = list()         # Creating an empty list to append values to
    length = len(sentence)          # To hold the length of the string, for iterative purposes
    
    # Any time we have don't have any words within our set, our any 
    # values for the string, return an empty string
    if not sentence or not words:
        return []
    
    # Looping through one letter at a time
    # check if t -> th -> the is in the list, since the is in the list, then we append that word
    # to the sentenceOutput, remove that same slice from the wordset, and recursively we call, 
    # our word removed sentence to find the next available word
    for i in range(length):
        if sentence[0: i + 1] in wordSet:
            sentenceOutput.append(sentence[0: i + 1])
            wordSet.remove(sentence[0: i + 1])
            sentenceOutput += returnList(sentence[i + 1:], wordSet)
            break
    
    return sentenceOutput


sentence = "thequickbrownfox"
words = ['quick', 'brown', 'the', 'fox']
print(returnList(sentence, words))
sentence = "bedbathandbeyond"
words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
print(returnList(sentence, words))


