# Returns the numeric decimal value of a given roman numeral
def value(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == "C":
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1

def conversion(romanNumeral):
    res = 0
    index = 0
    
    # iterating through the roman numeral string
    while index < len(romanNumeral):
        # setting the initial roman numeral and getting the value of it
        # we simply need to check the value after to see if less than the next
        s1 = value(romanNumeral[index])
        
        # if the next character not the last character to check,
        # check if the character is less than or greater than
        if index + 1 < len(romanNumeral):
            s2 = value(romanNumeral[index + 1])
            
            # the sitauation when we have a simple situation where we just add numerics
            # like XI = 10 + 1 = 11
            if s1 >= s2:
                res += s1
                index += 1
            
            # The situation when we have a more complicated analysis, for like when
            # IX = 10 - 1 = 9
            else:
                res = res + s2 - s1
                index += 2 
        else:
            res += s1
            index += 1
    
    return res

romanNumeral = "IX"
print("The Decimal Conversion from Roman Numeral", romanNumeral, "is", conversion(romanNumeral))
romanNumeral = "VII"
print("The Decimal Conversion from Roman Numeral", romanNumeral, "is", conversion(romanNumeral))
romanNumeral = "MCMIV"
print("The Decimal Conversion from Roman Numeral", romanNumeral, "is", conversion(romanNumeral))


