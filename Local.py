class Calculator:
    def add(self,x,y):
        result=x+y  #(Local variable)
        print(result)
    def sub(self,x,y):
        result=x-y
        print(result)
    def mul(self,x,y):
        result=x*y
        print(result)
    def div(self,x,y):
        result=x/y
        print(result)
    def rem(self,x,y):
        result=x%y
        print(result)
c=Calculator()
c.add(10,20)
c.sub(50,30)
c.mul(10,20)
c.div(80,20)
c.rem(10,5)        