# OOP Character Class Assignment

# character Class
class characters():
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0
    
    # make character say their catchphrases
    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.name + ":", self.phrase1)
        elif phraseNum == 2:
            print(self.name + ":", self.phrase2)
        else:
            print(self.name, "Only has 2 phrases available")

    # assign new level
    def setLevel(self, newLevel):
        self.level = newLevel
        print(self.name, "Set to level", self.level)

# character property
Spiderman = characters("Peter Parker", "With great power comes great responsibility", "Pizza time!")
Batman = characters("Bruce Wayne", "The night is darkest just before dawn", "A hero can be anyone")

# character tasks
Batman.speak(1)
Batman.setLevel(2)
Spiderman.speak(2)