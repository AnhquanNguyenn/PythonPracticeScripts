def distance(s1, s2, lengths1, lengths2):
    # When s1's length is zero then the number of changes necessary to equal s2 is
    # the length of s2
    if lengths1 == 0:
        return lengths2

    # When s2's length is zero then the number of changes necessary to equal s2 is
    # the length of s1
    if lengths2 == 0:
        return lengths1

    # When the last two values in each string are equal, then we can just continue
    # going through the strings to test
    if s1[lengths1 - 1] == s2[lengths2 - 1]:
        return distance(s1, s2, lengths1 - 1, lengths2 - 1)

    # last characters are not the same, determine if we need to insert, remove, or replace
    # Insert lengths1, lengths2 - 1
    # Delete lengths1 - 1, lengths2
    # Substitute lengths1 - 1, lengths2 - 1

    return 1 + min(distance(s1, s2, lengths1, lengths2 - 1),
                   distance(s1, s2, lengths1 - 1, lengths2),
                   distance(s1, s2, lengths1 - 1, lengths2 - 1))

# Dyanmic Programming Approach


def distance_faster(s1, s2, lengths1, lengths2):
        # Creating a temporary array to hold return values
    dp = [[0 for x in range(lengths2 + 1)] for x in range(lengths1 + 1)]

    for i in range(lengths1 + 1):
        for j in range(lengths2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] == i
            elif s1[lengths1 - 1] == s2[lengths2 - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],
                                   dp[i - 1][j],
                                   dp[i - 1][j - 1])


str1 = 'biting'
str2 = 'sitting'
str3 = str1
print("Using Recursion:", distance(str1, str2, len(str1), len(str2)))
print("Using Dynamic Programming:", distance(str1, str2, len(str1), len(str2)))
print("Using Recursion:", distance(str1, str3, len(str1), len(str3)))
print("Using Dynamic Programming:", distance(str1, str3, len(str1), len(str3)))
