import random

class AircraftCarrier():
    def __init__(self, name):
        self.name=name
        self.type="AircraftCarrier"
        self.hp = 300
        self.armor = 500
        if self.armor<0:
            self.armor=0
        self.armorPercent =500
        self.selfDefense = 1
        self.numberOfStealth=1
        pass
    def ShipFire(self):
        pass
