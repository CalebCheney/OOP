import random

class Insect:
    def __init__(self,wings,legs):
        self.wings = wings
        self.legs = legs
        self.miles = 0

    def flight(self):
        self.miles = random.randint(0,10)
    
    def get_flight(self):
        return self.miles

    def get_wings(self):
        return self.wings

    def get_legs(self): 
        return self.legs