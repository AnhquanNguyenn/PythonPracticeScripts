import sys

def buy_and_sell(array):
    buy = 0
    sell = 0
    length = len(array)
    arrayCopy = array.copy()
    arrayCopy.sort()
    cheapestCost = arrayCopy[0]
    tempArray = []
    
    cheapestCostIndex = 0
    for index, nums in enumerate(array):
        if cheapestCost == nums:
            cheapestCostIndex = index
            break
      
    for i in range(cheapestCostIndex, length):
        tempArray.append(array[i])
    
    tempArray.sort()
    buy = tempArray[0]
    sell = tempArray[len(tempArray) - 1]
    
    maxProfit = sell - buy
    
    
    return maxProfit


array = [9, 11, 8, 5, 7, 10]
array2 = [9, 11, 3, 5, 7, 11]
print(buy_and_sell(array))
print(buy_and_sell(array2))


def get_stock_profit(prices):
    if not prices or len(prices) < 2:
        return

    min_price = prices[0]
    max_diff = -sys.maxsize
    for price in prices[1:]:
        if price - min_price > max_diff:
            max_diff = price - min_price
        if price < min_price:
            min_price = price

    return max_diff


array = [9, 11, 8, 5, 7, 10]
array2 = [9, 11, 3, 5, 7, 11]
print(get_stock_profit(array))
print(get_stock_profit(array2))
