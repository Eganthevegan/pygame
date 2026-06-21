class student:
    def __init__(self, name, id, class1, section):
        self.name = name
        self.id = id
        self.class1 = class1
        self.section = section

    def assignment(self):
        print("Assignment done!",self.name)

student1 = student("david", 7, 8, "green")
student1.assignment()
student2 = student("betty", 8, 9, "green")
student2.assignment()
        