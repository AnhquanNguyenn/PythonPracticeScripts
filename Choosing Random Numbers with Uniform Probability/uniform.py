import random

for i in range(1, 11):
    sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Attempt", i, ":", random.choices(sample))
    