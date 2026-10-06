class string:
    def __init__(self,name,age):
        self.name = name
        self.age=age

    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}"
obj=string("john",34)
print(obj)