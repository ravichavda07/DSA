class Node():
    def __init__(self,value=None):
        self.data = value
        self.next = None
        self.prev = None

class doublyLinkedList():
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        t1 = self.head
        while(t1.next != None):
            t1 = t1.next
        t1.next = temp
        temp.prev = t1
    
    def insertAtBeg(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
    
    def insertAtMid(self,value,x):
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                break
            else:
                t1 = t1.next
        temp = Node(value)
        temp.next = t1.next
        t1.next.prev = temp
        t1.next = temp
        temp.prev = t1
    
    def delete(self,value):
        if(self.head == None):
            print("LinkedList is empty")
            return
        t1 = self.head
        if(t1.data == value):
            self.head = t1.next
            self.head.prev = None
            return
        while(t1.next != None):
            if(t1.data == value):
                t1.prev.next = t1.next 
                t1.next.prev = t1.prev
                return
            else:
                t1 =t1.next
        if(t1.data == value):
            t1.prev.next = None
    
    def printDLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end=" <=> ")
            t1 = t1.next
        print(t1.data)
        
obj = doublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtMid(40,20)
obj.delete(20)
obj.printDLL()