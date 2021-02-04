import random


class Cruiser():
    def __init__(self, name):
        self.name = name
        self.type = "Cruiser"
        self.hp = 1400
        self.armor = 300
        if self.armor<0:
            self.armor=0
        self.armorPercent =300
        self.numberOfCanons = 6
        self.selfDefense = 2
        pass

    def CanonBreak(self):
        Chance = random.randrange(0, 16)
        if Chance == 10:
            self.numberOfCanons -= 2
            print("Shit! Captain we lost 2 canons")
            return 2
        elif Chance == 5 or Chance == 15:
            self.numberOfCanons -= 1
            print("Oh! Captain we lost 1 canon")
            return 1
        else:
            return 0
        pass

    def ShipFire(self, round, breaked):
        i = 0
        while (i == 0):
            bulletType = str(input(f"Select the bullet type {self.name}:\nAP(Armor-Piercing) ,HP(High-Spreader)"))
            if bulletType.upper() == "AP":
                hit = 250 * (self.numberOfCanons / (self.numberOfCanons + breaked))
                percent = random.randrange(1, 41) / 100
                hp, armor = hit * percent, hit * (1 - percent)
                i += 1
                print(
                    f"Firing AP shells with {self.numberOfCanons} out of {self.numberOfCanons + breaked} canons Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                print("------------------------------------------------------------------------------------")
                self.numberOfCanons += breaked
                return (int(hp), int(armor), "AP")

            elif bulletType.upper() == "HP":
                hp = 275 * (self.numberOfCanons / (self.numberOfCanons + breaked))
                i += 1
                print(
                    f"Firing HP shells with {self.numberOfCanons} out of {self.numberOfCanons+breaked} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                self.numberOfCanons += breaked
                print("------------------------------------------------------------------------------------")
                return (int(hp), 0, "HP")
        pass


    def ShipDefense(self, hp, armor, round, bullet):
        if hp == 0 and armor == 0:
            print("MISS SIR")
        else:
            if self.armor > 0:
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2 or chance == 3:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        canonBreaked = Cruiser.CanonBreak(self)
                        if bullet == "AP":
                            if self.armor-armor<0:
                                self.hp-=(hp+armor-self.armor)
                                print((f"-{int(hp+armor-self.armor)}hp\n-{self.armor} armor"))
                                self.armor=0
                            else:
                                self.hp -= hp
                                self.armor -= armor
                                print((f"-{int(hp)}hp\n-{self.armor} armor"))
                            print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                            print(
                                "------------------------------------------------------------------------------------")
                        else:
                            self.hp -= hp * (1 - ((self.armor/1.3) / self.armorPercent))
                            print((f"-{int(hp * (1 - ((self.armor/1.3) / self.armorPercent)))}hp"))
                            print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                            print("------------------------------------------------------------------------------------")
                        return canonBreaked

                elif bullet == "TP":
                    print("DIRECT HIT SIR")
                    canonBreaked = Cruiser.CanonBreak(self)
                    if self.armor-armor<0:
                        self.hp-=(hp+armor-self.armor)
                        print((f"-{int(hp+armor-self.armor)}hp\n-{self.armor} armor"))
                        self.armor=0
                    else:
                        self.hp -= hp
                        self.armor -= armor
                    print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                    print("------------------------------------------------------------------------------------")
                    return canonBreaked

                elif bullet == "Nuce":
                    if hp == 0:
                        print("MISS SIR")
                    else:
                        if self.selfDefense > 0 and hp > 0:
                            loop = 0
                            while (loop == 0):
                                Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                                if Defense.lower().strip() == "yes":
                                    print("BOOOM Thank God!")
                                    self.selfDefense -= 1
                                    loop += 1
                                elif Defense.lower().strip() == "no":
                                    print("DIRECT HIT SIR")
                                    canonBreaked = Cruiser.CanonBreak(self)
                                    if self.armor - armor < 0:
                                        self.hp -= (hp+armor-self.armor)
                                        print((f"-{int(hp+armor-self.armor)}hp\n-{self.armor} armor"))
                                        self.armor = 0
                                    else:
                                        self.hp -= hp
                                        self.armor -= armor
                                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                                    print(
                                        f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                                    print(
                                        "------------------------------------------------------------------------------------")
                                    return canonBreaked
                                else:
                                    print("Waiting for your order....")
                        else:
                            print("DIRECT HIT SIR")
                            canonBreaked = Cruiser.CanonBreak(self)
                            if self.armor - armor < 0:
                                self.hp -= (hp+armor-self.armor)
                                print((f"-{int(hp+armor-self.armor)}hp\n-{self.armor} armor"))
                                self.armor = 0
                            else:
                                self.hp -= hp
                                self.armor -= armor
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                            print(
                                "------------------------------------------------------------------------------------")
                            return canonBreaked

                elif bullet == "JR":
                    if self.selfDefense > 0 and hp > 0:
                        loop = 0
                        while (loop == 0):
                            hp = hp * (random.randrange(60, 71) / 100)
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1

                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                canonBreaked = Cruiser.CanonBreak(self)
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                                print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                                print(
                                    "------------------------------------------------------------------------------------")
                                return canonBreaked
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        canonBreaked = Cruiser.CanonBreak(self)
                        hp = hp * (random.randrange(60, 71) / 100)
                        self.hp -= hp
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                        print("------------------------------------------------------------------------------------")
                        return canonBreaked
            else:
                self.armor = 0
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2 or chance == 3:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        canonBreaked = Cruiser.CanonBreak(self)
                        self.hp -= (hp + armor)
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                        print("------------------------------------------------------------------------------------")
                        return canonBreaked

                elif bullet == "TP":
                    print("DIRECT HIT SIR")
                    canonBreaked = Cruiser.CanonBreak(self)
                    self.hp -= (hp + armor)
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                    print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                    print("------------------------------------------------------------------------------------")
                    return canonBreaked

                elif bullet == "Nuce":
                    if self.selfDefense > 0 and hp > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                canonBreaked = Cruiser.CanonBreak(self)
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                                print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                                print(
                                    "------------------------------------------------------------------------------------")
                                return canonBreaked
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        canonBreaked = Cruiser.CanonBreak(self)
                        self.hp -= hp
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                        print("------------------------------------------------------------------------------------")
                        return canonBreaked

                elif bullet == "JR":
                    if self.selfDefense > 0 and hp > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1

                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                canonBreaked = Cruiser.CanonBreak(self)
                                hp = hp * (random.randrange(60, 71) / 100)
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                                print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                                print(
                                    "------------------------------------------------------------------------------------")
                                return canonBreaked
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        canonBreaked = Cruiser.CanonBreak(self)
                        hp = hp * (random.randrange(60, 71) / 100)
                        self.hp -= hp
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
                        print("------------------------------------------------------------------------------------")
                        return canonBreaked
        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        print("------------------------------------------------------------------------------------")
        return 0
        pass
