'''A PERSON IS ARRANGING HIS BOOKS HELP HIM TO ARRAGE THE BOOKS IN THE FORM OF STACK DATA STRUCTURE
->ARRANGE THE BOOKS ON ABOVE ANOTHER AND IF IT IS REACHED LIMITED SIZE OF 5 THEN ADD THE BOOK IN A SECONF STACK AUTOMATICALLY, SO EACH STACK CONTAINS 5 BOOKS , ALL THE STACKS IS PRESENT IN A OUTER STACK ,SO INNER STACK HAS A LIMITED SIZE,OUTER STACK HAS NO LIMITED SIZE.
->CREATE A METHODS LIKE PUSH(), DISPLAY(), POP(), POPAT()'''

class STACK_OF_BOOKS:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.s1 = []
    
    def push(self, val):
        if len(self.s1) > 0 and len(self.s1[-1]) < self.maxSize:
            self.s1[-1].append(val)
        else:
            self.s1.append([val])

    def pushAt(self, val, stack_number):
        if stack_number <= len(self.s1):
            if len(self.s1[stack_number-1]) < self.maxSize:
                self.s1[stack_number-1].append(val)
            else:
                print("Stack reached its limit")
        else:
            print("No stack number")

    def pop(self):
        if self.s1 == 0:
            return None
        elif len(self.s1) and len(self.s1[-1]) > 0:
            self.s1[-1].pop()
        else:
            self.s1.pop()

    def popAt(self, stack_number):
        if len(self.s1) > 0 :
            if stack_number <= len(self.s1):
                self.s1[stack_number-1].pop()
            else:
                print("no stack is present in given number")

        else:
            print("stack is empty")

    def display(self):
        if len(self.s1) != 0:
            print(self.s1)
        else:
            print("No elements in stack")
            
    def peek(self):
        if len(self.s1) > 0:
            print(self.s1[-1][-1])

        else:
            print("Stack is Empty")

    def peekAt(self, stack_number):
        if len(self.s1) > 0 :
            if stack_number <= len(self.s1) and stack_number > 0:
                print(self.s1[stack_number-1][-1])
            else:
                print("no stack number")
        else:
            print("Stack has no elements")



b=STACK_OF_BOOKS(4)
b.push("C Programming")
b.push("C++")
b.push("C#")
b.push("Python")
b.push("SQL")
b.push("Django")
b.push("DSA")
b.push("API")
b.push("HTML")
b.push("CSS")
b.push("JS")
b.display()
print()

# b.pop()
# b.display()
# # b.pop()
# # b.display()
# # b.pop()
# # b.display()
# # b.pop()
# # b.display()

# print()
# # b.popAt(2)
# # b.display()

# # b.popAt(2)
# # b.display()

# # b.popAt(2)
# # b.display()

# b.popAt(7)
# b.display()
# print()


# b.peek()
# b.display()
# print()

# b.peekAt(2)
# b.display()

b.pushAt('Science',3)
b.display()

