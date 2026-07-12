from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_info(self):
        print(self.name + " is a " + self.category + " instrument.")

    @abstractmethod
    def play_sound(self):
        pass

class Guitar(Instrument):
    def __init__(self, name, category):
        super().__init__(name, category)

    def play_sound(self):
        print("Strum strum!")

class Drum(Instrument):
    def __init__(self, name, category):
        super().__init__(name, category)

    def play_sound(self):
        print("Boom boom!")

class Flute(Instrument):
    def __init__(self, name, category):
        super().__init__(name, category)
        

    def play_sound(self):
        print("Toot toot!")

guitar = Guitar("Acoustic Guitar", "String")
drum = Drum("Snare Drum", "Percussion")
flute = Flute("Wood Flute", "Woodwind")

guitar.display_info()
guitar.play_sound()

drum.display_info()
drum.play_sound()

flute.display_info()
flute.play_sound()