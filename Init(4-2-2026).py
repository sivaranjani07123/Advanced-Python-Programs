class Car:
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def show(self):
        print("Model is",self.model)
        print("Color is",self.color)
toyota=Car("Innova","Grey")
toyota.show()