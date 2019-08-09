def repeatedString(s, n):
    count = 0           # counter for the number of a's
    length = len(s)     # length of the string
    newStr = s

    # if we just have an a with any number n, then just return n
    if s == 'a':
        return n

    # testing if the length of the string and the repeated length are the same, no
    # need to add repeated strings
    if length == n:
        for i in range(n):
            if (s[i] == 'a'):
                count += 1
    else:
        # Create a new repeated substring that is of n length long
        remainder = n % length
        if remainder % length == 0:
            for i in range(n // length):
                newStr = ''.join((newStr, s))
            for i in range(n):
                if (newStr[i] == 'a'):
                    count += 1
        else:
            for i in range(n // length):
                newStr = ''.join((newStr, s))
            for j in range(remainder):
                newStr = ''.join((newStr, s[j]))
            for i in range(n):
                if (newStr[i] == 'a'):
                    count += 1

    return count

# Could also just get the number of a's and then multiply by the number of repeats


def repeatedString2(s, n):
    L = len(s)
    return(s.count('a') * (n // L) + s[:n % L].count('a'))


print(repeatedString("aba", 10))
print(repeatedString("abcda", 5))
print(repeatedString("a", 1000000))
print(repeatedString("abcda", 100))
print(repeatedString2("abcda", 100))
