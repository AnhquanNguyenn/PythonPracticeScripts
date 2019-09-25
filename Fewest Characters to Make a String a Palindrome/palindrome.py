def palindrome(word):
    if isPalindrome(word):
        return word
    
    # the first and last letters are equal recursively call the first letter plus the middle letters 
    # in between the first and last letters
    if word[0] == word[-1]:
        return word[0] + palindrome(word[1:-1]) + word[-1]
    else:
        palindrome1 = word[0] + palindrome(word[1:]) + word[0]
        palindrome2 = word[-1] + palindrome(word[:-1]) + word[-1]
        
        if len(palindrome1) > len(palindrome2):
            return palindrome2
        elif len(palindrome1) < len(palindrome2):
            return palindrome1
        else:
            if palindrome1 < palindrome2:
                return palindrome1
            else:
                return palindrome2


# Determines if a string or substring is a palindrome, by seeing if 
# the reverse of the word is equal to the original word
def isPalindrome(word):
    return word[::-1] == word

word = "race"
print(palindrome(word)) 
word = "google"
print(palindrome(word))
