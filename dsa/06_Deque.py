class Deque:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtFront(self,value):
        self.items.insert(0,value)
    
    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)
    
    def insertAtRear(self,value):
        self.items.append(value)
    
    def deleteAtRear(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop()

dq = Deque()
print(dq.isEmpty())
dq.insertAtFront(10)
dq.insertAtFront(20)
dq.insertAtRear(30)
dq.insertAtRear(40)
print(dq.isEmpty())
print(dq.deleteAtFront())
print(dq.deleteAtRear())
print(dq.deleteAtRear())
print(dq.deleteAtFront())
print(dq.deleteAtFront())
print(dq.deleteAtRear())