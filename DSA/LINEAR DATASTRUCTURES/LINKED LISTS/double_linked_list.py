class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.previous = None
    
class Double_Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_last(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            newNode.previous = temp

    def display(self):
        if self.head is None:
            print("no nodes to display")

        else:
            temp = self.head
            while temp:
                print(temp.data,end=" <=> ")
                temp = temp.next 
            print()

    def length(self):
        if self.head is None:
            print("no nodes to count")
        else:
            temp = self.head
            cnt=0
            while temp:
                cnt +=1
                temp = temp.next 
            return cnt
        
    def insert_at_first(self, val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.previous=newNode
            self.head=newNode

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

    def delete_at_last(self):
        if self.head is None:
            print("No nodes to delete")
        elif self.length() == 1:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next.previous = None
            temp.next = None

    def delete_at_first(self):
        if self.head is None:
            print("No nodes to display")
        elif self.length() == 1:
            self.head = None
        else:
            self.head.next.previous = None
            self.head = self.head.next
            
    def delete_at_specified_loc(self,loc):
        if loc <= 0:
            print("Enter location above zero")
        elif loc == 1:
            self.delete_at_first()
        elif loc > self.length():
            print("Enter location lessthan ", self.length())

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
    def seaarch_the_element(self, val):
        if self.head is None:
            print("No Nodes")
        else:
            temp = self.head
            while temp.next != None:
                if temp.data == val:
                    print("value found")
                    print("previous value:" ,temp.previous.data if temp.previous!= None else "previous value is none")

                    print("Next value:" ,temp.next.data if temp.next!= None else "next value is none")

                    break
                temp = temp.next
            else:
                print("value no found")

dll = Double_Linked_list()
dll.insert_at_last(100)
dll.insert_at_last(200)
dll.insert_at_last(300)
dll.insert_at_last(400)
dll.insert_at_last(500)
dll.display()
print("Total nodes in DLL: ", dll.length())

dll.insert_at_first('A')
dll.display()
print("Total nodes in DLL: ", dll.length())

dll.insert_at_first(10)
dll.display()
print("Total nodes in DLL: ", dll.length())

dll.insert_at_specified_loc(69,2)
dll.display()
print("Total nodes in DLL: ", dll.length())

dll.delete_at_last()
dll.display()
print("Total nodes in DLL: ", dll.length())

dll.delete_at_first()
dll.display()
print("Total nodes in DLL: ", dll.length())

dll.delete_at_specified_loc(5)
dll.display()
print("Total nodes in DLL: ", dll.length())

dll.delete_at_specified_loc(5)
dll.display()
print("Total nodes in DLL: ", dll.length())

print()
print()
print()
print()
dll.seaarch_the_element(69)
