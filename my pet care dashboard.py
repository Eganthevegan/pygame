class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health  

    def set_health(self, new_health):  
        if 0 <= new_health <= 100: self.__health = new_health

    def show_info(self):
        print(f"Pet: {self.name} | Health: {self.__health}%")

    def care_action(self):
        pass

class Dog(Pet):
    def care_action(self): print(f" Take {self.name} for a walk!")

class Cat(Pet):
    def care_action(self): print(f" Give {self.name} some treats!")

class Rabbit(Pet):
    def care_action(self): print(f" Clean {self.name}'s hutch!")

pets = [Dog("Buddy", 80), Cat("Whiskers", 90), Rabbit("Fluffy", 75)]

for pet in pets:
    pet.show_info()
    pet.care_action()