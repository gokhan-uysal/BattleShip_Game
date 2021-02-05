import random
class Destroyer():
    def __init__(self , name):
        self.type = "Destroyer"
        self.name = name
        self.hp = 1200
        self.armor = 200
        if self.armor<0:
            self.armor=0
        self.armorPercent =200
        self.numberOfCanons = 4
        self.numberOfTorpedoes = 3
        self.selfDefense = 1

    def CanonBreak(self):
        Chance = random.randrange(0, 21)
        if Chance == 10:
            self.numberOfCanons-= 2
            print("Shit! Captain we lost 2 canons")
            return 2
        elif Chance == 5 or Chance == 20:
            self.numberOfCanons -= 1
            print("Oh! Captain we lost 1 canon")
            return 1
        else:
            return 0
        pass

    def ShipFire(self, round , breaked):
        i = 0
        while (i == 0):
            if self.numberOfTorpedoes <= 0:
                hp = 200 * (self.numberOfCanons / (self.numberOfCanons+breaked))
                i += 1
                print(
                    f"We are out of Torpedoes sir!!\nFiring HP shells with {self.numberOfCanons} out of {self.numberOfCanons+breaked} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                print("------------------------------------------------------------------------------------")
                self.numberOfCanons+=breaked
                return (int(hp), 0, "HP")

            else:
                bulletType = str(input(f"Select the bullet type {self.name}\nTP(Torpedoes) ,HP(High-Spreader)"))
                if bulletType.upper().strip() == "HP":
                    hp = 200 * (self.numberOfCanons / (self.numberOfCanons+breaked))
                    i += 1
                    print(
                        f"Firing HP shells with {self.numberOfCanons} out of {self.numberOfCanons+breaked} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    self.numberOfCanons+=breaked
                    return (int(hp), 0, "HP")

                elif bulletType.upper().strip() == "TP":
                    self.numberOfTorpedoes -= 1
                    hit = 300
                    percent = random.randrange(0, 45) / 100
                    hp, armor = hit * percent, hit * (1 - percent)
                    i += 1
                    print(
                        f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), int(armor), "TP")

        pass


    def ShipDefense(self, hp, armor, round, bullet , location):
        if hp == 0 and armor == 0:
            print("THIS IS OUR CHANCE")
        else:
            if self.armor > 0:
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
                                    breakedCanon = Destroyer.CanonBreak(self)
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
                                            f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                                        print(
                                            "------------------------------------------------------------------------------------")

                                    else:
                                        self.hp -= hp*(1-((self.armor/1.5)/self.armorPercent))
                                        loop+=1
                                        print((f"-{int(hp*(1-((self.armor/1.5)/self.armorPercent)))}hp"))
                                        print(
                                            f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                                        print(
                                            "------------------------------------------------------------------------------------")
                                    return breakedCanon
                                else:
                                    print("Waiting for your order....")
                        else:
                            print("DIRECT HIT SIR")
                            breakedCanon = Destroyer.CanonBreak(self)
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
                                    f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                                print(
                                    "------------------------------------------------------------------------------------")
                            else:
                                self.hp -= hp*(1-((self.armor/1.5)/self.armorPercent))
                                print((f"-{int(hp*(1-((self.armor/1.5)/self.armorPercent)))}hp"))
                                print(
                                    f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                                print(
                                    "------------------------------------------------------------------------------------")
                            return breakedCanon

                elif bullet == "TP":
                    Chance = random.randrange(1, 8)
                    if Chance == 1:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        canonBreaked = Destroyer.CanonBreak(self)
                        if self.armor-armor<0:
                            self.hp-=(hp+armor-self.armor)
                            print((f"-{int(hp+armor-self.armor)}hp\n-{int(self.armor)} armor"))
                            self.armor=0
                        else:
                            self.hp -= hp
                            self.armor -= armor
                            print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                        print(
                            f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                        print("------------------------------------------------------------------------------------")
                        return canonBreaked

                elif bullet == "Nuce":
                    print("DIRECT HIT SIR")
                    canonBreaked = Destroyer.CanonBreak(self)
                    if self.armor-armor<0:
                        self.hp-=(hp+armor-self.armor)
                        print((f"-{int(hp+armor-self.armor)}hp\n-{int(self.armor)} armor"))
                    else:
                        self.hp -= hp
                        self.armor = 0
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                    print(
                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                    print("------------------------------------------------------------------------------------")
                    return canonBreaked
                elif bullet == "JR":
                    print("DIRECT HIT SIR")
                    canonBreaked = Destroyer.CanonBreak(self)
                    hp = hp * (random.randrange(50, 61) / 100)
                    self.hp -= hp
                    self.armor -= armor
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                    print(
                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                    print("------------------------------------------------------------------------------------")
                    return canonBreaked

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
                                    breakedCanon = Destroyer.CanonBreak(self)
                                    self.armor = 0
                                    self.hp -= (hp + armor)
                                    loop += 1
                                    print((f"-{int(hp + armor)}hp"))
                                    print(
                                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                                    print(
                                        "------------------------------------------------------------------------------------")
                                    return breakedCanon
                                else:
                                    print("Waiting for your order....")
                        else:
                            print("DIRECT HIT SIR")
                            breakedCanon = Destroyer.CanonBreak(self)
                            self.armor = 0
                            self.hp -= (hp + armor)
                            print((f"-{int(hp + armor)}hp"))
                            print(
                                f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                            print(
                                "------------------------------------------------------------------------------------")
                            return breakedCanon

                elif bullet == "TP":
                    Chance = random.randrange(1, 8)
                    if Chance == 1:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        canonBreaked = Destroyer.CanonBreak(self)
                        self.armor = 0
                        self.hp -= (hp + armor)
                        print((f"-{int(hp + armor)}hp"))
                        print(
                            f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                        print("------------------------------------------------------------------------------------")
                        return canonBreaked

                elif bullet == "Nuce":
                    print("DIRECT HIT SIR")
                    canonBreaked = Destroyer.CanonBreak(self)
                    self.hp -= hp
                    self.armor = 0
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                    print(
                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                    print("------------------------------------------------------------------------------------")
                    return canonBreaked

                elif bullet == "JR":
                    self.armor = 0
                    print("DIRECT HIT SIR")
                    canonBreaked = Destroyer.CanonBreak(self)
                    hp = hp * (random.randrange(50, 61) / 100)
                    self.hp -= (hp + armor)
                    print((f"-{int(hp + armor)}hp"))
                    print(
                        f"Captain {self.name} we have {int(self.hp)}hp , {int(self.armor)} armor and {self.numberOfTorpedoes} tp left.")
                    print("------------------------------------------------------------------------------------")
                    return canonBreaked
        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        print("------------------------------------------------------------------------------------")
        return 0
        pass
