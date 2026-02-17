class Car:
    def data(self):
        self.model=input("Enter the model:")
        self.color=input("Enter the color:  ")
    def show(self):
        print("Model is",self.model)
        print("Color is",self.color)
suzuki=Car()
suzuki.data()
suzuki.show()