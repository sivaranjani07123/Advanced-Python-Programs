class B1_Class():
    def B1_Method(self):
        print("Base 1 method.")
class B2_Class(B1_Class):#  SINGLE INHERITANCE
    def B2_Method(self):
        print("Base 2 method.")
class B3_Class():
    def B3_Method(self):
        print("Base 3 method.")
class B4_Class(B2_Class,B3_Class):#MULTIPLE INHERITANCE 
    def B4_Method(self):
        print("Base 4 method.")
obj=B4_Class()
obj.B4_Method()
obj.B3_Method()
obj.B2_Method()
obj.B1_Method()