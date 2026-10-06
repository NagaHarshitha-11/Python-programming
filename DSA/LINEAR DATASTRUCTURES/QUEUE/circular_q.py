class Circular_Queue:
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.c1=[None] * maxSize
        self.front=-1
        self.rear=-1
    #isfull implementation
    def IsFull(self):
        if self.front == 0 and self.rear +1 ==self.maxSize:
            return True
        elif self.rear +1 == self.front:
            return True
        else:
            return False
        
    def IsEmpty(self):
        if self.rear ==-1 and self.front ==-1:
            return True
        else:
            return False
        
    def display(self):
        print(self.c1)
        print("front ->",self.front)
        print("rear ->",self.rear)

    
    #enqueue implementation
    def  enqueue(self,val):
        if self.IsFull():
            print("circular queue is full")
        else:
            if self.rear +1 == self.maxSize:
                self.rear=0
            else:
                self.rear+=1
                if self.front==-1:
                    self.front=0
        self.c1[self.rear] = val

    def dequeue(self,val):
        if self.IsEmpty():
            print("No elements present in CQ")
        else:
            index=self.front
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front + 1 == self.maxSize:
                self.front=0
            else:
                self.front += 1
            self.c1[index] = None

    def peek(self):
        if self.IsEmpty():
            print("no elements to peek")
        else:
            print("The peek element in CQ is: ",self.c1[self.front] )

cq=Circular_Queue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()
cq.dequeue(10)
cq.display()
cq.dequeue(10)
cq.display()
cq.enqueue(60)
cq.display()
cq.peek()

# print(cq.IsFull())
# print(cq.IsEmpty())

# o/p:
# [10, 20, 30, 40, 50]
# front -> 0
# rear -> 4
# [None, 20, 30, 40, 50]
# front -> 1
# rear -> 4
# [None, None, 30, 40, 50]
# front -> 2
# rear -> 4
# [60, None, 30, 40, 50]
# front -> 2
# rear -> 0
# The peek element in CQ is:  30


