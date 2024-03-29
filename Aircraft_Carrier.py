import random

class AircraftCarrier():
    def __init__(self, name):
        self.name=name
        self.type="Carrier"
        self.hp = 300
        self.armor = 500
        if self.armor<0:
            self.armor=0
        self.armorPercent =500
        self.FireLocation=[1,2,3,4,5,6,7,8,9]
        self.numberOfAirStrike=30
        self.selfDefense = 1
        self.numberOfStealth=1
        self.Location=0
        if self.Location==0:
            AircraftCarrier.CurrentLocation(self)
        pass


    def AircraftBreak(self):
        Chance = random.randrange(0, 21)
        if Chance == 10:
            self.numberOfAirStrike -= 5
            print("Shit! Captain we lost 5 aircrafts")
            return 5
        elif Chance == 5 or Chance == 10 or Chance == 15 or Chance == 20:
            self.numberOfAirStrike -= 2
            print("Oh! Captain we lost 2 aircrafts")
            return 2
        elif Chance == 2 or Chance == 4 or Chance == 6 or Chance == 8 or Chance == 10:
            self.numberOfAirStrike -= 1
            print("Captain we lost 1 aircraft")
            return 1
        else:
            return 0
        pass

    def AircraftCount(self):
        loop=0
        while (loop==0):
            number=input("How many aircraft are you going to lift [0-5]")
            if number.isalpha():
                print(f"Sir {number} is not a number")
            else:
                if int(number)>5:
                    print("Sir we have 5 take-off ramps")
                else:
                    loop+=1
                    return int(number)
        pass

    def CurrentLocation(self):
        f = open("Carrier Air Strike Map", "r")
        print(f.read())
        loop = 0
        while (loop == 0):
            number = input(f"Select your position Captain {self.name}")
            if number.isalpha():
                print(f"Sir {number} is not a number")
            else:
                if int(number) > 9 or int(number) <= 0:
                    print(f"Sir {int(number)} is out of map")
                else:
                    loop += 1
                    self.location = int(number)
        pass

    def Location(self):
        loop=0
        while (loop==0):
            number=input(f"Select air strike coordinates Captain {self.name}")
            if number.isalpha():
                print(f"Sir {number} is not a number")
            else:
                if  int(number) > 9 or int(number)<=0:
                    print(f"Sir {int(number)} is out of map")
                else:
                    loop += 1
                    return int(number)
        print("------------------------------------------------------------------------------------")
        pass

    def ShipFire(self ,round , breaked):
        i=0
        self.numberOfAirStrike-=breaked
        while i==0:
            if self.numberOfStealth>0:
                craftSelect = str(input(f"Sir which plane are you going to lift\nST (Stealth capable aircraft) A2 (aircraft)"))
                if craftSelect.upper().strip()=="ST":
                    hp=150
                    i+=1
                    self.numberOfStealth-=1
                    print("Ready to take off")
                    print(f"Lifting B-2A Spirit Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), 0, "ST" , 0)

                elif craftSelect.upper().strip()=="A2":
                    f=open("Carrier Air Strike Map" , "r")
                    print(f.read())
                    Location=AircraftCarrier.Location(self)
                    number=AircraftCarrier.AircraftCount(self)
                    print(f"All {number}/{self.numberOfAirStrike} ready to take off!")
                    print(f"TARGET: {Location}")
                    hit = number * 50
                    percent = random.randrange(1, 41) / 100
                    hp, armor = hit * percent, hit * (1 - percent)
                    self.numberOfAirStrike-=number
                    print(f"Lifting A-10 Thunderbolt II Captain {self.name}.\nHopping to deal {int(hp+armor)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) , int(armor) , "A2" ,Location )

            elif self.numberOfStealth<=0:
                f = open("Carrier Air Strike Map", "r")
                print(f.read())
                Location = AircraftCarrier.Location(self)
                number = AircraftCarrier.AircraftCount(self)
                print(f"All {number}/{self.numberOfAirStrike} ready to take off!")
                print(f"TARGET: {Location}")
                hit = number * 50
                percent = random.randrange(1, 41) / 100
                hp, armor = hit * percent, hit * (1 - percent)
                self.numberOfAirStrike -= number
                print(
                    f"Lifting A-10 Thunderbolt II Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                print("------------------------------------------------------------------------------------")
                return (int(hp), int(armor), "A2", Location)

            elif self.numberOfStealth<=0 and self.numberOfAirStrike<=0:
                print(f"It was a pleasure to serve you sir {self.name}")
                print("------------------------------------------------------------------------------------")
        pass

    def ShipDefense(self, hp, armor, round, bullet ,  location):
        if hp == 0 and armor == 0:
            print("THIS IS OUR CHANCE")
        else:
            if self.armor > 0:
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2 or chance == 3:
                        print("MISS SIR")
                    else:
                        if self.selfDefense > 0:
                            loop = 0
                            while (loop == 0):
                                Defense = str(input(f"Want to use Phalanx CIWS\n+{hp}hp +{armor} armor\n[YES/NO]"))
                                if Defense.lower().strip() == "yes":
                                    print("BOOOM Thank God!")
                                    self.selfDefense -= 1
                                    loop += 1
                                elif Defense.lower().strip() == "no":
                                    aircraftBreak=AircraftCarrier.AircraftBreak(self)
                                    print("DIRECT HIT SIR")
                                    if bullet=="AP":
                                        if self.armor-armor<0:
                                            self.hp -= (hp+armor-self.armor)
                                            loop += 1
                                            print((f"-{int((hp+armor-self.armor))}hp\n-{self.armor} armor"))
                                            self.armor=0
                                        else:
                                            self.hp-=hp
                                            self.armor-=armor
                                            print((f"-{int((hp))}hp\n-{int(armor)} armor"))
                                        print(
                                            f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                                        print(
                                            "------------------------------------------------------------------------------------")

                                    else:
                                        self.hp -= hp*(1-((self.armor/1.2)/self.armorPercent))
                                        loop+=1
                                        print((f"-{int(hp*(1-((self.armor/1.2)/self.armorPercent)))}hp"))
                                        print(
                                            f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                                        print(
                                            "------------------------------------------------------------------------------------")
                                    return aircraftBreak
                                else:
                                    print("Waiting for your order....")
                        else:
                            print("DIRECT HIT SIR")
                            aircraftBreak=AircraftCarrier.AircraftBreak(self)
                            if bullet == "AP":
                                if self.armor - armor < 0:
                                    self.hp -= (hp+armor-self.armor)
                                    print((f"-{int((hp+armor-self.armor))}hp\n-{self.armor} armor"))
                                    self.armor = 0
                                else:
                                    self.hp -= hp
                                    self.armor -= armor
                                    print((f"-{int((hp))}hp\n-{int(armor)} armor"))
                                print(
                                    f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                                print(
                                    "------------------------------------------------------------------------------------")
                            else:
                                self.hp -= hp*(1-((self.armor/1.5)/self.armorPercent))
                                print((f"-{int(hp*(1-((self.armor/1.5)/self.armorPercent)))}hp"))
                                print(
                                    f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                                print(
                                    "------------------------------------------------------------------------------------")
                            return aircraftBreak

                elif bullet == "TP":
                    Chance = random.randrange(1, 8)
                    if Chance == 1:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        aircraftBreak = AircraftCarrier.AircraftBreak(self)
                        if self.armor-armor<0:
                            self.hp-=(hp+armor-self.armor)
                            print((f"-{int(hp+armor-self.armor)}hp\n-{int(self.armor)} armor"))
                            self.armor=0
                        else:
                            self.hp -= hp
                            self.armor -= armor
                            print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                        print(
                            f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                        print("------------------------------------------------------------------------------------")
                        return aircraftBreak

                elif bullet == "Nuce":
                    print("DIRECT HIT SIR")
                    aircraftBreak = AircraftCarrier.AircraftBreak(self)
                    if self.armor-armor<0:
                        self.hp-=(hp+armor-self.armor)
                        print((f"-{int(hp+armor-self.armor)}hp\n-{int(self.armor)} armor"))
                    else:
                        self.hp -= hp
                        self.armor = 0
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                    print(
                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                    print("------------------------------------------------------------------------------------")
                    return aircraftBreak

                elif bullet == "JR":
                    print("DIRECT HIT SIR")
                    aircraftBreak = AircraftCarrier.AircraftBreak(self)
                    hp = hp * (random.randrange(50, 61) / 100)
                    self.hp -= hp
                    self.armor -= armor
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                    print(
                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                    print("------------------------------------------------------------------------------------")
                    return aircraftBreak

            else:
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2 or chance == 3 or chance == 4:
                        print("MISS SIR")
                    else:
                        if self.selfDefense > 0:
                            loop = 0
                            while (loop == 0):
                                Defense = str(input(f"Want to use Phalanx CIWS\n+{hp}hp +{armor} armor\n[YES/NO]"))
                                if Defense.lower().strip() == "yes":
                                    print("BOOOM Thank God!")
                                    self.selfDefense -= 1
                                    loop += 1
                                elif Defense.lower().strip() == "no":
                                    print("DIRECT HIT SIR")
                                    aircraftBreak = AircraftCarrier.AircraftBreak(self)
                                    self.armor = 0
                                    self.hp -= (hp + armor)
                                    loop += 1
                                    print((f"-{int(hp + armor)}hp"))
                                    print(
                                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                                    print(
                                        "------------------------------------------------------------------------------------")
                                    return aircraftBreak
                                else:
                                    print("Waiting for your order....")
                        else:
                            print("DIRECT HIT SIR")
                            aircraftBreak = AircraftCarrier.AircraftBreak(self)
                            self.armor = 0
                            self.hp -= (hp + armor)
                            print((f"-{int(hp + armor)}hp"))
                            print(
                                f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                            print(
                                "------------------------------------------------------------------------------------")
                            return aircraftBreak

                elif bullet == "TP":
                    Chance = random.randrange(1, 8)
                    if Chance == 1:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        aircraftBreak = AircraftCarrier.AircraftBreak(self)
                        self.armor = 0
                        self.hp -= (hp + armor)
                        print((f"-{int(hp + armor)}hp"))
                        print(
                            f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                        print("------------------------------------------------------------------------------------")
                        return aircraftBreak

                elif bullet == "Nuce":
                    print("DIRECT HIT SIR")
                    aircraftBreak = AircraftCarrier.AircraftBreak(self)
                    self.hp -= hp
                    self.armor = 0
                    print((f"-{int(hp+armor)}hp"))
                    print(
                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                    print("------------------------------------------------------------------------------------")
                    return aircraftBreak

                elif bullet == "JR":
                    self.armor = 0
                    print("DIRECT HIT SIR")
                    aircraftBreak = AircraftCarrier.AircraftBreak(self)
                    hp = hp * (random.randrange(50, 61) / 100)
                    self.hp -= (hp + armor)
                    print((f"-{int(hp + armor)}hp"))
                    print(
                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfAirStrike} airStrike left.")
                    print("------------------------------------------------------------------------------------")
                    return aircraftBreak

        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        print("------------------------------------------------------------------------------------")
        return 0
        pass
        pass