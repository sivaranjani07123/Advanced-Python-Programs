class A:
    __privatecount=0
    def Sum(self):
        self.__privatecount+=1
        print(self.__privatecount)
a=A() 
a.Sum()
a.Sum()
print(a._A__privatecount)