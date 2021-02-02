import random
class Submarine():
    def __init__(self, name):
        self.name=name
        self.hp = 500
        self.armor = 800
        self.armorPercent =800
        self.numberOfNuces = 1
        self.numberOfJericho = 3
        self.numberOfTorpedoes = 6
        self.selfDefense = 1
        self.criticHit = 1
        pass


    def MissileBreak(self):
        Chance=random.randrange(0,21)
        if Chance==10:
            MissileCount=self.numberOfJericho
            self.numberOfJericho=0
            return MissileCount
        else:
            return 0
        pass
    def ShipFire(self ,round , breaked):
        if round >= 7:
            i = 0
            while (i == 0):
                if self.numberOfNuces <= 0:
                    print(f"We are out of Nuclear Missiles sir!!")
                    i += 1
                    continue

                else:
                    nuces = str(input("Sir do you want to fire Nuclear Missile [yes/no]....."))
                    if nuces.strip().lower() == "yes":
                        hit = 1000
                        percent = 0.5
                        hp, armor = hit * percent, hit * percent
                        print(
                            f"Firing Nuclear Missiles Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                        print(
                            "------------------------------------------------------------------------------------")
                        self.numberOfNuces -= 1
                        chance = random.randrange(1, 16)
                        if chance == 10:
                            hp = 0
                            armor = 0
                            self.hp -= 50
                            self.armor -= 150
                            print(
                                f"Fuck! Captain our Nuclear Missile explode unexpectedly\n{self.type}: {-50}hp {-150} armor")
                            print(
                                "------------------------------------------------------------------------------------")

                        i += 1
                        return (int(hp), int(armor), "Nuce")
                    elif nuces.strip().lower() == "no":
                        bulletType = str(
                            input(f"Select the bullet type {self.name}:\nTP(Torpedoes) ,JR(Jericho Missile)"))
                        if bulletType.strip().upper() == "TP":
                            self.numberOfTorpedoes -= 1
                            hit = 400
                            percent = random.randrange(0, 45) / 100
                            hp, armor = hit * percent, hit * (1 - percent)
                            i += 1
                            print(
                                f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                            print(
                                "------------------------------------------------------------------------------------")
                            return (int(hp), int(armor), "TP")
                        elif bulletType.strip().upper() == "JR":
                            self.numberOfJericho -= 1
                            hit = 500
                            hp = hit
                            i += 1
                            print(
                                f"Firing 1 Jericho Missiles out of {self.numberOfJericho} Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                            print(
                                "------------------------------------------------------------------------------------")
                            return (int(hp), 0, "JR")
                        else:
                            print("Waiting for your order....")

                    if self.numberOfJericho <= 0 and self.numberOfTorpedoes > 0:
                        print("Sir we are out of Jericho Missiles")
                        self.numberOfTorpedoes -= 1
                        hit = 400
                        percent = random.randrange(0, 45) / 100
                        hp, armor = hit * percent, hit * (1 - percent)
                        i += 1
                        print(
                            f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                        print(
                            "------------------------------------------------------------------------------------")
                        return (int(hp), int(armor), "TP")
                    elif self.numberOfTorpedoes <= 0 and self.numberOfJericho > 0:
                        print("Sir we are out of Torpedoes")
                        self.numberOfJericho -= 1
                        hit = 500
                        hp = hit
                        i += 1
                        print(
                            f"Firing 1 Jericho Missiles out of {self.numberOfJericho} Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                        print(
                            "------------------------------------------------------------------------------------")
                        return (int(hp), 0, "JR")
                    elif self.numberOfNuces <= 0 and self.numberOfJericho <= 0 and self.numberOfTorpedoes <= 0:
                        print(f"It was a pleasure to serve you sir {self.name}")
                        print(
                            "------------------------------------------------------------------------------------")
                    else:
                        print("Waiting for your order....")
        else:
            if self.numberOfJericho <= 0 and self.numberOfTorpedoes > 0:
                print("Sir we can't launch Jericho Missiles")
                self.numberOfTorpedoes -= 1
                hit = 400
                percent = random.randrange(0, 45) / 100
                hp, armor = hit * percent, hit * (1 - percent)
                print(
                    f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                print(
                    "------------------------------------------------------------------------------------")
                return (int(hp), int(armor), "TP")

            elif self.numberOfTorpedoes <= 0 and self.numberOfJericho > 0:
                print("Sir we are out of Torpedoes")
                self.numberOfJericho -= 1
                hit = 500
                hp = hit
                print(
                    f"Firing Jericho Missiles out of {self.numberOfJericho} Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                print(
                    "------------------------------------------------------------------------------------")
                return (int(hp), 0, "JR")
            elif self.numberOfNuces <= 0 and self.numberOfJericho <= 0:
                print(f"Sir we are out of everything but one chance in ROUND 9 {self.name}")
                print("------------------------------------------------------------------------------------")
                return (0, 0, "None")
            i = 0
            while (i == 0):
                bulletType = str(input(f"Select the bullet type {self.name}:\nTP(Torpedoes) ,JR(Jericho Missile)"))
                if bulletType.strip().upper() == "TP":
                    self.numberOfTorpedoes -= 1
                    hit = 400
                    percent = random.randrange(0, 45) / 100
                    hp, armor = hit * percent, hit * (1 - percent)
                    i += 1
                    print(
                        f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                    print(
                        "------------------------------------------------------------------------------------")
                    return (int(hp), int(armor), "TP")
                elif bulletType.strip().upper() == "JR":
                    self.numberOfJericho -= 1
                    hit = 500
                    hp = hit
                    i += 1
                    print(
                        f"Firing Jericho Missiles out of {self.numberOfJericho} Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), 0, "JR")
                else:
                    print("Waiting for your order....")
        pass


    def ShipDefense(self, hp, armor, round, bullet):
        if hp == 0 and armor==0:
            print("MISS SIR")
        else:
            if self.armor > 0:
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2:
                        print("MISS SIR")
                    else:
                        if self.selfDefense > 0:
                            loop = 0
                            while (loop == 0):
                                Defense = str(input(f"Want to dive {-820}ft\n+{hp}hp +{armor} armor\n[YES/NO]"))
                                if Defense.strip().lower()=="yes":
                                    print("Ballast tanks are filled with water ready to dive....")
                                    self.selfDefense-=1
                                    loop+=1
                                elif Defense.strip().lower()=="no":
                                    print("DIRECT HIT SIR")
                                    if bullet == "AP":
                                        self.hp -= hp
                                        self.armor -= armor
                                        loop += 1
                                    else:
                                        self.hp -= hp * (1 - (self.armor / self.armorPercent))
                                        loop+=1
                                        print(f"-{int(hp * (1 - (self.armor / self.armorPercent)))}hp")
                                        loop+=1
                                else:
                                    print("Waiting for your order....")
                        else:
                            print("DIRECT HIT SIR")
                            self.hp -= hp
                            self.armor -=armor
                            print(f"-{int(hp)}hp\n-{int(armor)} armor")

                elif bullet=="TP":
                    print("DIRECT HIT SIR")
                    self.hp-=hp
                    self.armor-=armor
                    print(f"-{int(hp)}hp\n-{int(armor)} armor")


            else:
                self.armor=0
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2 or chance==3:
                        print("MISS SIR")
                    else:
                        if self.selfDefense > 0:
                            loop = 0
                            while (loop == 0):
                                Defense = str(input(f"Want to dive {-820}ft\n+{hp}hp +{armor} armor\n[YES/NO]"))
                                if Defense.strip().lower()=="yes":
                                    print("Ballast tanks are filled with water ready to dive....")
                                    self.selfDefense-=1
                                    loop+=1
                                elif Defense.strip().lower()=="no":
                                    print("DIRECT HIT SIR")
                                    self.hp-=(hp+armor)
                                    print(f"-{int(hp)}hp\n-{int(armor)} armor")
                                    loop+=1
                                else:
                                    print("Waiting for your order....")
                        else:
                            print("DIRECT HIT SIR")
                            self.hp -= (hp+armor)
                            print(f"-{int(hp)}hp\n-{int(armor)} armor")

                elif bullet == "TP":
                    print("DIRECT HIT SIR")
                    self.hp -= (hp+armor)
                    print(f"-{int(hp)}hp\n-{int(armor)} armor")

        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        print("------------------------------------------------------------------------------------")
        return 0
        pass