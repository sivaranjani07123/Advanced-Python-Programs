class Person:
    def __init__(self,name,age,weight,height):#__init__ is used to initialize objects and allocate memory space
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def display(self):
        print("------Person Detail-------")
        print(f"Name :{self.name}")
        print(f"Age :{self.age}")
        print(f"Weight :{self.weight}")
        print(f"Height :{self.height}")
p1=Person("Johan",25,70,5.9)
p1.display()        