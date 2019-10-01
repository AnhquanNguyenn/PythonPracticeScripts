# - Each employee begins with a bonus factor of 1x.
# - For each employee, if they perform better than the person sitting next to them, the employee is given + 1 
# higher bonus(and up to + 2 if they perform better than both people to their sides).

def bonus(numbers):
    bonusList = list()
    toTheLeft = 0
    toTheRight = 0
    index = 0
    
    for num in numbers:
        # for out initial first candidate, who doesn't have a left person to compare to
        if index < 1:
            # can only be a +1 or + 2, since they can only be higher than one other person
            if numbers[index] < numbers[index + 1]:
                bonusList.append(1)
                index += 1
            else:
                bonusList.append(2)
                index += 1
        # for the cases where all the employees will have a left and right person to compare to
        elif index >= 1 and index < len(numbers):
            index += 1
        elif index >= len(numbers):
            
                    
        
                
        
    return bonusList


numbers = [1, 2, 3, 2, 3, 5, 1]
print(bonus(numbers)) 
