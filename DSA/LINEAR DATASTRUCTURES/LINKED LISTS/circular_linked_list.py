class Node:
    def __init__(self, data):
        self.data = data
        self.addr = None

class Circular_Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_last(self, val):
        newNode=Node(val)
        if self.head is None:
            self.head = newNode
            self.head.addr = newNode
        else:
            temp = self.head
            while temp.addr != self.head:
                temp = temp.addr
            temp.addr = newNode
            newNode.addr = self.head

    def insert_at_first(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.head.addr = newNode
        else:
            temp = self.head
            while temp.addr != self.head:
                temp = temp.addr
            temp.addr = newNode
            newNode.addr = self.head
            self.head = newNode

    def insert_at_specified_loction(self, loc, val):
        newNode = Node(val)
        if loc <= 0:
            print("enter location above 0: ")
        elif  loc == 1:
            self.insert_at_first(val)
        elif loc == self.length()+1:
            self.insert_at_last(val)
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

    def length(self):
        if self.head is None:
            print("no nodes to count")

        else:
            temp = self.head
            cnt = 0
            while temp:
                cnt +=1
                
                temp = temp.addr 
                if temp == self.head:
                    break
            return cnt


    def display(self):
        if self.head is None:
            print("no nodes to display")

        else:
            temp = self.head
            while temp:
                print(temp.data,end="->")
                temp = temp.addr 
                if temp == self.head:
                    break
            print()
    def delete_at_last(self):
        if self.head is None:
            print("No nodes to remove")
        else:
            temp = self.head
            while temp.addr.addr != self.head:
                temp = temp.addr
            temp.addr = self.head

    def delete_at_first(self):
        if self.head is None:
            print("No nodes to remove")
        else:
            temp = self.head
            while temp.addr != self.head:
                temp = temp.addr
            temp.addr = self.head.addr
            self.head = self.head.addr
    # def delete_at_specified_location(self, val, loc):
    #     newNode = Node(val)
    #     if loc <=0:
    #         print("Enter location above 0 ")
    #     elif loc == 1:
    #         self.head = self.head.addr
    #     elif loc > self.length():
    #         print("Enter location lessthan ", self.length())
    #     else:




    



cll = Circular_Linked_List()
print("Insert at first")
cll.insert_at_first('D')
cll.display()
cll.insert_at_first('E')
cll.display()
print()

print("Insert at last")
cll.insert_at_last('A')
cll.insert_at_last('B')
cll.insert_at_last('C')
cll.display()
print("Total Nodes in circular linked list: ",cll.length())
print()

print("Insert at specified position")
cll.insert_at_specified_loction(1,'F')
cll.display()
print("Total Nodes in circular linked list: ",cll.length())
cll.insert_at_specified_loction(7,'G')
cll.display()
print("Total Nodes in circular linked list: ",cll.length())
cll.insert_at_specified_loction(3,'H')
cll.display()
print("Total Nodes in circular linked list: ",cll.length())


cll.delete_at_last()
cll.display()
print("Total Nodes in circular linked list: ",cll.length())

cll.delete_at_first()
cll.display()
print("Total Nodes in circular linked list: ",cll.length())
