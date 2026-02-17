class Car:
    def data(self,model,color):
        self.model=model
        self.color=color
    def show(self):
        print("Model is",self.model)
        print("Color is",self.color)
suzuki=Car()
suzuki.data("Swift","Blue")
suzuki.show()