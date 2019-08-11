def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def staircase(n):
    return fib(n + 1)


print(staircase(1))
print(staircase(2))
print(staircase(3))
print(staircase(4))
print(staircase(5))


'''
if n == 1, (1)	1 way 
if n == 2, (1, 1) (2)	2 ways 
if n == 3, (1, 1, 1) (1, 2) (2, 1) 3 ways 
if n == 4, (1, 1, 1, 1) (1, 2, 1) (1, 1, 2) (2, 1, 1) (2, 2)	5 ways
'''

# Recursive function used by countWays


def countWaysUtil(n, m):
    res = [0 for x in range(n)]  # Creates list res with all elements 0
    res[0], res[1] = 1, 1

    for i in range(2, n):
        j = 1
        while j <= m and j <= i:
            res[i] = res[i] + res[i - j]
            j = j + 1
    return res[n - 1]

# Returns number of ways to reach s'th stair


def countWays(s, m):
    return countWaysUtil(s + 1, m)


# Driver Program
s, m = 5, 2
print("Number of ways =", countWays(s, m))
