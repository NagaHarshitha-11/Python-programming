class QUEUE:
    def __init__(self,maxSize):
        self.q1=[]
        self.maxSize=maxSize

    def IsFull(self):
        if len(self.q1) == self.maxSize:
            return True
        else:
            return False
    def IsEmpty(self):
        if len(self.q1) == 0:
            return True
        else:
            return False
    def Enqueue(self,val):
        if self.IsFull():
            print("queue is full")
        else:
            self.q1.append(val)

    def peek(self):
        if self.IsEmpty():
            print("no elements to peek")
        else:
            print("peek element is: ",self.q1[0])
    def display(self):
        if self.IsEmpty():
            print("no elements to display")
        else:
            print(self.q1)
    def dequeue(self):
        if self.IsEmpty():
            print("no elements to remove")
        else:
            self.q1.pop(0)

q=QUEUE(5)
print("Is queue is full",q.IsFull)      
    


