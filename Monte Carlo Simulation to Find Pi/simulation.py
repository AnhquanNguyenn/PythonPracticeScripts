from random import random


# pi = 4 * (number of values that can define a circle / the total number of simulations)

def simulation(numberOfTests, radius):
    counter = 0
    rsquared = radius ** 2
    for _ in range(numberOfTests):
        xRand = random() * radius
        yRand = random() * radius
        
        if (xRand ** 2) + (yRand ** 2) <= rsquared:
            counter += 1 
    return round(4 * (counter / numberOfTests ), 3)

numberOfTests = 10000
radius = 1
print(simulation(numberOfTests, radius))