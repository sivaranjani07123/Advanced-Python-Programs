class B1_Class():
    def B1_Method(self):
        print("Base 1 method.")
class B2_Class(B1_Class):
    def B2_Method(self):
        print("Base 2 method.")
class B3_Class(B1_Class):
    def B3_Method(self):
        print("Base 3 method.")
obj=B3_Class()
obj1=B2_Class()
obj.B3_Method()
obj1.B2_Method()
obj1.B1_Method()