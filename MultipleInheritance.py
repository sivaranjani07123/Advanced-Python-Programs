class B1_Class():
    def B1_Method(self):
        print("Base 1 method.")
class B2_Class():
    def B2_Method(self):
        print("Base 2 method.")
class D1_Class(B1_Class,B2_Class):
    def D1_Method(self):
        print("Derived 1 method.")
obj=D1_Class()
obj.D1_Method()
obj.B2_Method()
obj.B1_Method()