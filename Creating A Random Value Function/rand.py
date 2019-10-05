import random

def rand5():
    return random.randint(1, 5)

def rand7():
    i = 5 * rand5() + rand5() - 5  # uniformly samples between 1-25
    if i < 22:
        return i % 7 + 1
    return rand7()

for i in range(10):
    print(rand7(), end=' ')
print('\n') 
