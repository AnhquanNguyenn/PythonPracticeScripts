class Queue:
    def __init__(self):
        self.mainStack = list()
        self.tempStack = list()
        
    def __show__(self):
        return str(self.mainStack)
    
    def enqueue(self, value):
        self.mainStack.append(value)
    
    def dequeue(self):
        # Empty Stacks
        if not self.mainStack:
            return None
        
        while self.mainStack:
            self.tempStack.append(self.mainStack.pop())
        value = self.tempStack.pop()
        
        while self.tempStack:
            self.mainStack.append(self.tempStack.pop())
        
        return value
    

q = Queue()
print(q.mainStack)
q.enqueue(1)
print("Enqueue a 1")
print(q.mainStack)
q.enqueue(2)
print("Enqueue a 2")
print(q.mainStack)
q.enqueue(3)
print("Enqueue a 3")
print(q.mainStack)
q.dequeue()
print("Dequeue a value")
print(q.mainStack)
q.dequeue()
print("Dequeue a value")
print(q.mainStack)
q.dequeue()
print("Dequeue a value")
print(q.mainStack)
q.dequeue()
print("Dequeue a value")
print(q.mainStack)
