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
