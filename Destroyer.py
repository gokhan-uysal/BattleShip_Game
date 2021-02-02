import random
class Destroyer():
    def __init__(self , name):
        self.type = "Destroyer"
        self.name = name
        self.hp = 1200
        self.armor = 100
        self.numberOfCanons = 4
        self.numberOfTorpedoes = 3
        self.selfDefense = 2
    def ShipFire(self,round):
        i = 0
        while (i == 0):
            if self.numberOfTorpedoes <= 0:
                # CANON BREAK
                canon = self.numberOfCanons
                Chance = random.randrange(0, 21)
                if Chance == 10:
                    canon -= 2
                    print("Shit! Captain we lost 2 canons")
                elif Chance == 5 or Chance == 20:
                    canon -= 1
                    print("Oh! Captain we lost 1 canon")

                hp = 200 * (canon / self.numberOfCanons)
                i += 1
                print(
                    f"We are out of Torpedoes sir!!\nFiring HP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                print("------------------------------------------------------------------------------------")
                return (int(hp), 0, "HP")

            else:
                bulletType = str(input(f"Select the bullet type {self.name}\nTP(Torpedoes) ,HP(High-Spreader)"))
                if bulletType.upper().strip() == "HP":
                    # CANON BREAK
                    canon = self.numberOfCanons
                    Chance = random.randrange(0, 21)
                    if Chance == 10:
                        canon -= 2
                        print("Shit! Captain we lost 2 canons")
                    elif Chance == 5 or Chance == 20:
                        canon -= 1
                        print("Oh! Captain we lost 1 canon")

                    hp = 200 * (canon / self.numberOfCanons)
                    i += 1
                    print(
                        f"Firing HP shells with {canon} out of {self.numberOfCanons} canons Captain {name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), 0, "HP")

                elif bulletType.upper().strip() == "TP":
                    self.numberOfTorpedoes -= 1
                    hit = 400
                    percent = random.randrange(0, 45) / 100
                    hp, armor = hit * percent, hit * (1 - percent)
                    i += 1
                    print(
                        f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), int(armor), "TP")

    def ShipDefense(self, hp, armor, round, bullet):
        if hp == 0 and armor == 0:
            print("MISS SIR")
        else:
            if self.armor - armor > 0:
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2 or chance == 3 or chance == 4:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        if self.selfDefense > 0:
                            loop = 0
                            while (loop == 0):
                                Defense = str(input(f"Want to use Phalanx CIWS\n+{hp}hp +{armor} armor\n[YES/NO]"))
                                if Defense.lower().strip() == "yes":
                                    print("BOOOM Thank God!")
                                    self.selfDefense -= 1
                                    loop += 1
                                elif Defense.lower().strip() == "no":
                                    self.hp -= hp
                                    self.armor -= armor
                                    loop += 1
                                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                                else:
                                    print("Waiting for your order....")
                        else:
                            self.hp -= hp
                            self.armor -= armor
                            print((f"-{int(hp)}hp\n-{int(armor)} armor"))

                elif bullet == "TP":
                    print("DIRECT HIT SIR")
                    self.hp -= hp
                    self.armor -= armor
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                elif bullet == "Nuce":
                    print("DIRECT HIT SIR")
                    self.hp -= hp
                    self.armor = 0
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                elif bullet == "JR":
                    print("DIRECT HIT SIR")
                    hp = hp * (random.randrange(50, 61) / 100)
                    self.hp -= hp
                    self.armor -= armor
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))

            else:
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2 or chance == 3 or chance == 4:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        if self.selfDefense > 0:
                            loop = 0
                            while (loop == 0):
                                Defense = str(input(f"Want to use Phalanx CIWS\n+{hp}hp +{armor} armor\n[YES/NO]"))
                                if Defense.lower().strip() == "yes":
                                    print("BOOOM Thank God!")
                                    self.selfDefense -= 1
                                    loop += 1
                                elif Defense.lower().strip() == "no":
                                    self.armor = 0
                                    self.hp -= (hp + armor)
                                    loop += 1
                                    print((f"-{int(hp + armor)}hp"))
                                else:
                                    print("Waiting for your order....")
                        else:
                            self.armor = 0
                            self.hp -= (hp + armor)
                            print((f"-{int(hp + armor)}hp"))
                elif bullet == "TP":
                    print("DIRECT HIT SIR")
                    self.armor = 0
                    self.hp -= (hp + armor)
                    print((f"-{int(hp + armor)}hp"))
                elif bullet == "Nuce":
                    print("DIRECT HIT SIR")
                    self.hp -= hp
                    self.armor = 0
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                elif bullet == "JR":
                    self.armor = 0
                    print("DIRECT HIT SIR")
                    hp = hp * (random.randrange(50, 61) / 100)
                    self.hp -= (hp + armor)
                    print((f"-{int(hp + armor)}hp"))
        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        print("------------------------------------------------------------------------------------")
        pass