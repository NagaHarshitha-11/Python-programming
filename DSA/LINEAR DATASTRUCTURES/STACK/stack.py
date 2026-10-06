#stack without limited size

# class STACK:
#     def __init__(self):
#         self.s1=[]

#     def display(self):
#         if len(self.s1) != 0:
#             for i in range(len(self.s1)-1,-1,-1):
#                 print(self.s1[i])
#         else:
#             print("No element present in stack")
#     def push(self,val):
#         self.s1.append(val)
#     def pop(self):
#         self.s1.pop()
#     def peek_ele(self):
#         print("Top most element present in a stack :",self.s1[-1])

# s1=STACK()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.display()
# print()
# s1.peek_ele()

# print()
# s1.pop()
# s1.display()

# o/p:
# 30
# 20
# 10

# Top most element present in a stack : 30

# 20
# 10


#stack with limited size
class STACK:
    def __init__(self,maxsize):
        self.s1=[]
        self.maxsize=maxsize
    
    def IsFull(self):
        if len(self.s1) == self.maxsize:
            return True
        else:
            return False
    def IsEmpty(self):
        if len(self.s1) == 0:
            return True
        else:
            return False
    def display(self):
        
        if self.IsEmpty():
            print("No elements present in a stack")
        else:
            for i in range(len(self.s1)-1,-1,-1):
                print(self.s1[i])
    def push(self,val):
        if self.IsFull():
            print("Stack is ful")
        else:
            self.s1.append(val)
    def pop(self):
        if self.IsEmpty():
            print("Stack is empty")
        else:
            self.s1.pop()
    def peek_ele(self):
        if self.IsEmpty():
            print("No elements present in a stack")
        else:
            print("Top element in a stack",self.s1[-1])
    
st=STACK(int(input("enter the size: ")))
while True:
    print("-------stack operations------")

    print("1.push\n2.pop\n3.display\n4.peek\n5.IsFull\n6.IsEmpty")
    opt=int(input("enter the option :"))
    match opt:
        case 1:
            val=input("Enter the element")
            st.push(val)
        case 2:
            st.pop()
        case 3:
            st.display()
        case 4:
            st.peek_ele()
        case 5:
            print("Is stck is full:",st.IsFull())
        case 6:
            print("Is stck is empty :6",st.IsEmpty())
        case _:
            print("Invalid Option")

# o/p:

# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :1
# Enter the element1
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :1
# Enter the element2
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :1
# Enter the element3
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :1
# Enter the element4
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :1
# Enter the element5
# Stack is ful
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :3
# 4
# 3
# 2
# 1
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :4
# Top element in a stack 4
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :5
# Is stck is full: True
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :6
# Is stck is empty :6 False
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :2
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :3
# 3
# 2
# 1
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :7
# Invalid Option
# -------stack operations------
# 1.push
# 2.pop
# 3.display
# 4.peek
# 5.IsFull
# 6.IsEmpty
# enter the option :


