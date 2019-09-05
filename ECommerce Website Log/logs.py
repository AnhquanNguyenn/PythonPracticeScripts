def runLogs():
    record("001")
    record("002")
    record("003")
    record("004")
    record("005")
    get_last(1)
    get_last(3)
    get_last(5)
    
def get_last(i):
    print(recordItem[len(recordItem) - i])


# This Function adds a record ID number to a stack
def record(order_id):
    recordItem.append(order_id)
    print(recordItem)


recordItem = []
runLogs()
