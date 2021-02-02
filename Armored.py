import random
class Armored():
    def __init__(self, name):
        self.type="Armored"
        self.name=name
        self.hp = 1600
        self.armor = 400
        self.numberOfCanons = 8
        self.selfDefense = 2
        self.Round = 0
        pass

    def ShipFire(self,round):
        i = 0
        while (i == 0):
            bulletType = str(input(f"Select the bullet type {self.name}:\nAP(Armor-Piercing) ,HP(High-Spreader)"))
            # CANON BREAK
            canon = self.numberOfCanons
            Chance = random.randrange(0, 21)
            if Chance == 10:
                canon -= self.numberOfCanons
                print("Shit! Captain we lost all canons")
            elif Chance == 5 or Chance == 10 or Chance == 15 or Chance == 20 or Chance == 19:
                canon -= 2
                print("Oh! Captain we lost 2 canon")
            elif Chance == 2 or Chance == 4 or Chance == 6 or Chance == 8 or Chance == 10 or Chance == 12:
                canon -= 1
                print("Captain we lost 1 canon")

            if bulletType.upper() == "AP":
                hit = 300 * (canon / self.numberOfCanons)
                percent = random.randrange(1, 41) / 100
                hp, armor = hit * percent, hit * (1 - percent)
                i += 1
                print(
                    f"Firing AP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                print("------------------------------------------------------------------------------------")
                return (int(hp), int(armor), "AP")

            elif bulletType.upper() == "HP":
                hp = 250 * (canon / self.numberOfCanons)
                i += 1
                print(
                    f"Firing HP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                print("------------------------------------------------------------------------------------")
                return (int(hp), 0, "HP")

    def ShipDefense(self, hp, armor, round, bullet):
        if hp == 0:
            print("MISS SIR")
        else:
            if self.armor - armor > 0:
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= hp
                        self.armor -= armor
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "TP":
                    print("DIRECT HIT SIR")
                    self.hp -= hp
                    self.armor -= armor
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "Nuce":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                self.hp -= hp
                                self.armor = 0
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= hp
                        self.armor = 0
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "JR":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                hp = hp * (random.randrange(60, 71) / 100)
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        hp = hp * (random.randrange(60, 71) / 100)
                        self.hp -= hp
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))


            else:
                self.armor = 0

                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= (hp + armor)
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                elif bullet == "TP":
                    self.hp -= (hp + armor)
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "Nuce":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= hp
                        self.armor = 0
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "JR":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                hp = hp * (random.randrange(60, 71) / 100)
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        hp = hp * (random.randrange(60, 71) / 100)
                        self.hp -= hp
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        print("------------------------------------------------------------------------------------")
        pass