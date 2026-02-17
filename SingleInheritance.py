class Parent_Class:
    def Parent_Method(self):
        print("Parent method is called.")
class Child_Class(Parent_Class):
    def Child_Method(self):
        print("Child method is called.")        
child=Child_Class()
child.Child_Method()
child.Parent_Method()