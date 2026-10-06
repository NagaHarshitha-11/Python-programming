class Node:
    def __init__(self,data):
        self.data=data
        self.addr=None

class Single_Linked_List:
    def __init__(self):
        self.head=None

    # implementation of insertion at last
    def insert_at_last(self, val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode

        else:
            temp = self.head
            while temp.addr != None:
                temp= temp.addr
            temp.addr = newNode

    # implementation of display
    def display(self):
        if self.head is None:
            print("no nodes to display")

        else:
            temp = self.head
            # while temp.addr != None:
            while temp:
                print(temp.data,end="->")
                temp = temp.addr 
            print()

    # implementation of length
    def length(self):
        if self.head is None:
            print("no nodes to count")
        else:
            temp = self.head
            cnt=0
            while temp:
                cnt +=1
                temp = temp.addr 
            return cnt
        
    def insert_at_first(self, val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            newNode.addr=self.head
            self.head=newNode

    def insert_at_specified_loc(self,val,loc):
        newNode = Node(val)
        if loc <= 0:
            print("enter location above 0: ")
        elif  loc == 1:
            newNode.addr=self.head
            self.head=newNode
        elif loc == self.length()+1:
            temp = self.head
            while temp.addr != None:
                temp= temp.addr
            temp.addr = newNode
        elif loc > self.length():
            print("enter location less than ->",self.length())
        else:
            temp=self.head
            cnt=1
            while temp.addr != None and cnt < loc - 1:
                temp = temp.addr
                cnt+=1
            newNode.addr = temp.addr
            temp.addr = newNode

    # implementation
    def delete_at_last(self):
        if self.head is None:
            print("no nodes to delete")
        elif self.length() == 1:
            self.head = None
        else:
            temp=self.head
            while temp.addr.addr != None:
                temp=temp.addr
            temp.addr = None

    def delete_at_first(self):
        if self.head is None:
            print("no nodes to delete")
        else:
            self.head = self. head.addr

    def delete_at_specified_loc(self,loc):
        if loc <= 0:
            print("Enter location above zero")
        elif loc == 1:
            self.head = self.head.addr
        elif loc > self.length():
            print("Enter location lessthan ", self.length())
        else:
            temp=self.head
            cnt=1
            while temp.addr != None and cnt < loc - 1:
                temp = temp.addr
                cnt+=1  
            temp.addr = temp.addr.addr

        
# object creation

sll=(int(input("enter the size: ")))
while True:
    print("----Single Linked List----")
    print("1.Insert at first\n2.insert at last\n3.insert at location\n4.display\n5.length\n6.deletion at first\n7.deletion at last\n8.deletion at position")
    option = int(input("Enter any option:"))
    match option:
        case 1:
            val=int(input("Enter values"))
            sll.insert_at_first(val)
        case 2:
            val=int(input("Enter values"))
            sll.insert_at_last(val)
        case 3:
                position = int(input("Enter location you want to insert."))
                sll.insert_at_specified_loc(position)
        case 4:
                sll.display()
        case 5:
                print("Total nodes present in linked list is ->",sll.length())
        case 6:

                sll.delete_at_first()
        case 7:

                sll.delete_at_last()
        case 8:
                loc=int(input("Enter location"))
                sll.delete_at_specified_loc(loc)
        case 9:
            print("Invalid option")
    
    
    
    
# sll.insert_at_last(10)
# sll.insert_at_last(20)
# sll.insert_at_last(30)
# sll.display()

# print("Total nodes in single linked list", sll.length())
# sll.insert_at_last(40)
# # sll.display()
# print("Total nodes in single linked list", sll.length())


# sll.insert_at_first(50)
# sll.display()
# print("Total nodes in single linked list", sll.length())


# # sll.insert_at_specified_loc(60,0)
# # sll.insert_at_specified_loc(60,-3)

# # sll.insert_at_specified_loc(60,1)
# # sll.display()
# # print(sll.length())

# # sll.insert_at_specified_loc(60,10)
# # sll.display()
# # print(sll.length())

# # sll.insert_at_specified_loc(70,5)
# # sll.display()
# # print(sll.length())

# # sll.insert_at_specified_loc(70,7)
# # sll.display()
# # print(sll.length())


# # sll.delete_at_last()
# # sll.display()
# # print(sll.length())

# # sll.delete_at_last()
# # sll.display()
# # print(sll.length())

# # sll.delete_at_last()
# # sll.display()
# # print(sll.length())

# # sll.delete_at_last()
# # sll.display()
# # print(sll.length())

# # sll.delete_at_last()
# # sll.display()
# # print(sll.length())

# # sll.delete_at_last()
# # sll.display()
# # print(sll.length())

# # sll.delete_at_last()
# # sll.display()
# # print(sll.length())

# # sll.delete_at_last()
# # sll.display()
# # print(sll.length())

# sll.delete_at_first()
# sll.display()
# print("Total nodes in single linked list", sll.length())

# sll.delete_at_specified_loc(3)
# sll.display()
# print("Total nodes in single linked list", sll.length())


