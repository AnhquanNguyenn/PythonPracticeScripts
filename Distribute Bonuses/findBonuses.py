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
            else:
                bonusList.append(2)
            
            index += 1
            
        # for the cases where all the employees will have a left and right person to compare to
        elif index >= 1 and index < (len(numbers) - 1):
            toTheLeft = index - 1
            toTheRight = index + 1
            
            if numbers[index] > numbers[toTheLeft]:
                if numbers[index] > numbers[toTheRight]:
                    bonusList.append(3)
                else:
                    bonusList.append(2)
            else:
                if numbers[index] > numbers[toTheRight]:
                    bonusList.append(2)
                else:
                    bonusList.append(1)
                     
            index += 1
            
        # for the case of the last number in the list where there is no right person to compare to. 
        elif index == len(numbers) - 1:
            toTheLeft = index - 1
            
            if numbers[index] > numbers[toTheLeft]:
                bonusList.append(2)
            else:
                bonusList.append(1)
            
    return bonusList


numbers = [1, 2, 3, 2, 3, 5, 1]
print(bonus(numbers)) 
