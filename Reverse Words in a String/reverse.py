def reverse(sentence):
    # Keep a variable for storing the reversed words in each strign
    reversedString = ""
    
    # splitting the sentence into individual words
    words = sentence.split(' ')
    
    # Iterating through each loop and joining the reversed version of each word to the 
    # reversedString along with a space to separate each word. 
    for word in words:
        reversedString += ("".join(reversed(word)))
        reversedString += ("".join(" "))
            
    return reversedString


sentence = "The cat in the hat"
print(sentence)
print(reverse(sentence))
