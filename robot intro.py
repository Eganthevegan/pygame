class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce(self):
        print(f"Hello! My name is {self.name}, and I am a {self.color} robot.")


robot1 = Robot(name="Tom", color="silver")
robot2 = Robot(name="Jerry", color="golden")


print("--- Robot Introductions ---")
robot1.introduce()
robot2.introduce()