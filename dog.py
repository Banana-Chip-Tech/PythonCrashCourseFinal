from pet import Pet

class Dog(Pet):
    def __init__(self,name=""):
        print("Hi! I'm your new dog!")
        super().__init__(name)

    def feedme(self):
        print("Roof! Roof! I'm hungry! Feed me!")
    def eat(self,food):
        print("Nom Nom ")
        super().eat(food)