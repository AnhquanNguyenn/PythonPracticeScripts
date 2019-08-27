def validCharacter(chr):
    if chr > 26 or chr < 1:
        return 0
    else: 
        return 1


def decodedWays(str):
    numberOfWays = 0
    
    if '0' in str:
        return "String is Not Allowed"
    
    if len(str) == 1:
        numberOfWays = 1
    elif len(str) == 2:
        numberOfWays = 1 + validCharacter(int(str))
    else:
        numberOfWays = decodedWays(str[1:])
        if validCharacter(int(str[:2])):
            numberOfWays += decodedWays(str[2:])

    return numberOfWays


str1 = '111'
str2 = '001'
str3 = '81'
print(str1, "=", decodedWays(str1), "way(s) to decode")
print(str2, "=", decodedWays(str2))
print(str3, "=", decodedWays(str3), "way(s) to decode")
