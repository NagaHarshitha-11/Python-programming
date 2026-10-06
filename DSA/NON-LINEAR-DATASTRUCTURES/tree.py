class TREE:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    def insert_the_element(self,val):
        if self.data:
            if val < self.data:
                if self.left is None:
                    self.left = TREE(val)
                else:
                    self.left.insert_the_element(val)
            elif val > self.data:
                if self.right is None:
                    self.right = TREE(val)
                else:
                    self.right.insert_the_element(val)
    def display(self):
        if self.left:
            self.left.display()
        # print(self.data,end = '->')

        if self.right:
            self.right.display()
    def pre_order_traversal(self,root):
        if root:
            print(root.data, end = "->")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def In_order_traversal(self,root):
        if root:
            self.In_order_traversal(root.left)
            print(root.data, end = "->")
            self.pre_order_traversal(root.right)

    def Post_order_traversal(self,root):
        if root:
            self.Post_order_traversal(root.left)
            self.Post_order_traversal(root.right)
            print(root.data, end = "->")

    def Level_order_traversal(self,root,level):
        if root is None:
            return
        if level == 1:
            print(root.data, end = "->")
        else:
            self.Level_order_traversal(root.left,level-1)
            self.Level_order_traversal(root.right,level-1) 

    def search_the_element(self,val):
        if self.data == val:
            print("Element found")
        elif val < self.data and self.left:
            self.left.search_the_element(val)
        elif val > self.data and self.right:
            self.right.search_the_element(val)
        else:
            print("Element not found")

t=TREE(15)  #root node
t.insert_the_element(12)
t.insert_the_element(20)
t.insert_the_element(25)
t.insert_the_element(18)
t.insert_the_element(14)
t.insert_the_element(9)
t.insert_the_element(6)
t.insert_the_element(10)

t.display()   
print()

print("PRE-ORDER TRAVERSAL")
t.pre_order_traversal(t)
t.display()
print()

print("IN-ORDER TRAVERSAL")
t.In_order_traversal(t)
t.display()
print()

print("POST-ORDER TRAVERSAL")
t.Post_order_traversal(t)
t.display()
print()

print("LEVEL-ORDER OR ZIGZIG TRAVERSAL IN BFS:")
t.Level_order_traversal(t,1)
t.display()
print()
print("SEARCHING THE ELEMENT")
t.search_the_element(-987)
t.display()