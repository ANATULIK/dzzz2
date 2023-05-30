dog = Pet("Baddies", "Dog")

dog.sleep()

dog.feed()

dog.play()

class Pet:
    def __init__(self, name, species):

        self.happy = None
        self.name = None
        self.hungry = None
        self.dog = Pet
        self.tired = None

    def feed(self):

        if self.hungry:

            print(f"{self.name} has been fed.")

            self.hungry = False

        else:

            print(f"{self.name} is not hungry")


    def sleep(self):

        if self.tired:

            print(f"{self.name} has gone to sleep")

            self.tired = False

        else:

            print(f"{self.name} is not tired")

    def play(self):

        if self.happy:

            print(f"{self.happy} is already playing")

        else:

            print(f"{self.happy} is playing now")

            self.happy = True


