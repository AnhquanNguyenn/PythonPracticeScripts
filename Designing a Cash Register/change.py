import sys

nameValue = {0.01: 'PENNY', 0.05: 'NICKEL', 0.1: 'DIME',
             0.25: 'QUARTER', 0.5: 'HALF DOLLAR', 1.00: 'ONE', 2.00: 'TWO', 5.00: 'FIVE', 10.00: 'TEN', 20.00: 'TWENTY', 50.00: 'FIFTY', 100.00: 'ONE HUNDRED'}

# Array of Values holding each individual change value to loop through to find the change necesary
values = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]


def change(purchasePrice, cashGiven):
        # If you gave less cash then the purchase price, you still owe money, error
    if cashGiven < purchasePrice:
        print("ERROR")
        return
    # if you gave equal cash to the purchase price then there is no change
    elif purchasePrice == cashGiven:
        print("ZERO")
        return
    # you gave more cash than the purchase price, find change
    else:
        # The amount of change necessary is the amount of cash - price
        change = cashGiven - purchasePrice
        # empty set to hold which values we need to use with change
        results = set([])

        # looping through each change value to see if it fits within the change
        for value in values:
            while change >= value:
                results.add(value)
                change = change - value

        results = list(results)
        results = [nameValue[result] for result in results]

        results = sorted(results)
        print(",".join(results))
        return


# Tests
inputs = ["15.94;16.00", "17;16", "35;35", "45;50"]

for tests in inputs:
    purchasePrice, cashGiven = tests.split(";")
    purchasePrice = float(purchasePrice)
    cashGiven = float(cashGiven)
    change(purchasePrice, cashGiven)
    #change(purchasePrice, cashGiven)


'''
for line in sys.stdin:
    purchase_price, cashGiven = line.split(";")
    purchase_price, cashGiven = float(purchase_price), float(cash)
    change(purchase_price, cash)
'''


'''

Test 1
Test Input : 15.94;16.00
Expected Output : NICKEL,PENNY

Test 2
Test Input : 17;16
Expected Output : ERROR  

Test 3
Test Input : 35;35
Expected Output : ZERO  

Test 4
Test Input : 45;50
Expected Output : FIVE

'''
