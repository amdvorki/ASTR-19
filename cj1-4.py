class Animal:
    lenArms = None
    lengthLegs = None
    numEyes = None
    hasTail = None
    isFurry = None
    def __init__(self, la, ll, ne, t, f):
        self.lenArms = la
        self.lengthLegs = ll
        self.numEyes = ne
        self.hasTail = t
        self.isFurry = f

    def printAttributes(self):
        print(f"Length of Arms: {self.lenArms} cm")
        print(f"Length of Legs: {self.lengthLegs} cm")
        print(f"Number of eyes: {self.numEyes} eyes")
        print(f"Has tail?: {self.hasTail}")
        print(f"Is Furry?: {self.isFurry}")


poodle = Animal(20.0,20.0,2,True,True)
poodle.printAttributes()



