class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.previous = None
    
class Circular_Double_Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_last(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            newNode.previous = newNode
            newNode.next = newNode
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.previous = temp
            newNode.next = self.head 
            self.head.previous = newNode

    def display(self):
        if self.head is None:
            print("no nodes to display")

        else:
            temp = self.head
            while temp:
                print(temp.data,end=" <=> ")
                temp = temp.next 
                if temp == self.head:
                    break
            print()

    def length(self):
        if self.head is None:
            print("no nodes to count")

        else:
            temp = self.head
            cnt = 0
            while temp:
                cnt +=1
                
                temp = temp.next 
                if temp == self.head:
                    break
            return cnt
        
    def insert_at_first(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            newNode.previous = newNode
            newNode.next = newNode
        else:
            temp = self.head
            while temp.next != self.head:
                    temp = temp.next
            temp.next = newNode
            newNode.next = self.head
            newNode.previous = temp
            self.head.previous = newNode
            self.head = newNode

    def insert_at_specified_loc(self,val,loc):
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
            while temp.next != None and cnt < loc - 1:
                temp = temp.next
                cnt+=1
            temp.next.previous = newNode
            newNode.next = temp.next
            newNode.previous = temp
            temp.next = newNode
    # def delete_at_first(self):
    #     if self.head is None:
    #         print("No nodes to display")
    #     elif self.length() == 1:
    #         self.head = None
    #     else:
    #         self.head.next.previous = None
    #         self.head = self.head.next
            
    def delete_at_last(self):
        if self.head is None:
            print("No nodes to delete")
        elif self.length() == 1:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head
            self.head.previous = temp

    def delete_at_first(self):
        if self.head is None:
            print("No nodes to display")
        elif self.length() == 1:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head.next.previous = temp 
            self.head = self.head.next

    def delete_at_specified_loc(self,loc):
        if loc <= 0:
            print("Enter location above zero")
        elif loc == 1:
            self.delete_at_first()
        elif loc > self.length():
            print("Enter location lessthan: ", self.length())
        elif loc == self.length():
            self.delete_at_last()
        else:
            temp=self.head
            cnt=1
            while temp.next != None and cnt < loc - 1:
                temp = temp.next
                cnt+=1  
            temp.next = temp.next.next
            temp.next.previous = temp
cdll= Circular_Double_Linked_list()
cdll.insert_at_last('A')
cdll.insert_at_last('B')
cdll.insert_at_last('C')
cdll.insert_at_last('D')
cdll.insert_at_last('E')

cdll.display()
print("Total Nodes are: ", cdll.length())

cdll.insert_at_first(10)
cdll.display()
print("Total Nodes are: ", cdll.length())

cdll.insert_at_specified_loc('f',7)
cdll.display()
print("Total Nodes are: ", cdll.length())

cdll.insert_at_specified_loc('h',8)
cdll.display()
print("Total Nodes are: ", cdll.length())

cdll.delete_at_last()
cdll.display()
print("Total Nodes are: ", cdll.length())

# cdll.delete_at_last()
# cdll.display()
# print("Total Nodes are: ", cdll.length())
# cdll.delete_at_last()
# cdll.display()
# print("Total Nodes are: ", cdll.length())
# cdll.delete_at_last()
# cdll.display()
# print("Total Nodes are: ", cdll.length())
# cdll.delete_at_last()
# cdll.display()
# print("Total Nodes are: ", cdll.length())

# cdll.delete_at_last()
# cdll.display()
# print("Total Nodes are: ", cdll.length())
# cdll.delete_at_last()
# cdll.display()
# print("Total Nodes are: ", cdll.length())
# cdll.delete_at_last()
# cdll.display()
# print("Total Nodes are: ", cdll.length())

cdll.delete_at_first()
cdll.display()
print("Total Nodes are: ", cdll.length())
cdll.delete_at_specified_loc(1)
cdll.display()
print("Total Nodes are: ", cdll.length())

cdll.delete_at_specified_loc(3)
cdll.display()
print("Total Nodes are: ", cdll.length())

cdll.delete_at_specified_loc(4)
cdll.display()
print("Total Nodes are: ", cdll.length())