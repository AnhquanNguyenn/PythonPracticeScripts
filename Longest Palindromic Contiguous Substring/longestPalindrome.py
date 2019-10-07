def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def longestPalindrome(word):
    if not word or isPalindrome(word):
        return word
    
    # After the first letter, and before the last letters
    substring1 = longestPalindrome(word[1:])
    substring2 = longestPalindrome(word[:-1])
    
    # find the longer of the substrings
    if len(substring1) > len(substring2):
        return substring1
    else:
        return substring2
    
word = "aabcdcb"
print(longestPalindrome(word))
word = "bananas"
print(longestPalindrome(word))


