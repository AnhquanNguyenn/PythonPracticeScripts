def perfect(number):
    perfectNumber = (str)(number)
    
    toMakePerfect = 10 - number
    perfectNumber += (str)(toMakePerfect)
    
    return perfectNumber


number = 1
print(perfect(number))
number = 2
print(perfect(number))
