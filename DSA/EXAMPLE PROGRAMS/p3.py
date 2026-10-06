'''WAP TO ENQUEUE THE ELEMENTS TO QUEUE DATA STRUCTURE AND PUSH THE ENTIRE QUEUE TO STACK DATA STRUCTURE AND REMOVE THE ELEMENT BY USING RULES OF BOTH STACK AND QUEUE '''

class STACK:
    def __init__(self):
        self.s1 = []
    
    def push(self, val):
        self.s1.append(val)

    def display(self):
        for i in range(len(self.s1)-1,-1,-1):
            print(self.s1[i])

    def pop(self):
        if len(self.s1) == 0:
            return None
        return self.s1.pop()
    
class QueueStack:
    def __init__(self):
        self.stack1 = STACK()
        self.stack2 = STACK()

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        while len(self.stack1.s1):
            self.stack2.push(self.stack1.pop())
        res = self.stack2.pop()
        while len(self.stack2.s1):
            self.stack1.push(self.stack2.pop())
        return res

    def display(self):
        self.stack1.display()


qs = QueueStack()
print("---Enqueue Elements---")
qs.enqueue('A')
qs.enqueue('B')
qs.enqueue('C')
qs.enqueue('D')
qs.enqueue('E')
qs.display()
print()

print("Dequeue Operation")
print("Removed element : ",qs.dequeue())
qs.display()
print("Removed element : ",qs.dequeue())
qs.display()
print("Removed element : ",qs.dequeue())
qs.display()
print("Removed element : ",qs.dequeue())
qs.display()
print("Removed element : ",qs.dequeue())
qs.display()
print("Removed element : ",qs.dequeue())
qs.display()
print("Removed element : ",qs.dequeue())
qs.display()


# ---Enqueue Elements---
# E
# D
# C
# B
# A

# Dequeue Operation
# Removed element :  A
# E
# D
# C
# B
# Removed element :  B
# E
# D
# C
# Removed element :  C
# E
# D
# Removed element :  D
# E
# Removed element :  E
# Removed element :  None
# Removed element :  None