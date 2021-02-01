import random ,os  ,Greeting
nameList=[]
typeList=[]
def Intro(index):
    ShipList = ("Destroyer", "Cruiser", "Armored", "Submarine")
    if index==1:
        print("Welcome to World of Warships")
        print(ShipList)
        i = 0
        while (i == 0):
            Info = str(input(
                "Do you want to learn more about BattleShips\nAdvice: Take time and read them carefully [yes/no]"))
            if Info.strip().lower() == "yes":
                f = open("BattleShips.txt", "r")
                print(f.read())
                i += 1
            elif Info.strip().lower() == "no":
                i += 1
            else:
                print("Please write yes or no")

    name = str(input(f"Can I have your name captain the {index}."))
    j=0
    while (j==0):
        print(ShipList)
        type=str(input("Now you can choose your ship from list"))
        if type.strip().capitalize() in ShipList:
            j += 1
            return (type.strip().capitalize() , name.capitalize().strip())
        else:
            print("Please choose appropriate ship type")
    pass

for i in range(1,3):
    type , name =Intro(i)
    nameList.append(name)
    typeList.append(type)
print("Now Let's Start The Battle")
print("------------------------------------------------------------------------------------")

class BattleShips:
    def __init__(self,type,name):
        self.type = type
        self.name = name
        if self.type=="Destroyer":
            self.hp=1200
            self.armor=100
            self.reloadTime=10
            self.numberOfCanons=4
            self.numberOfTorpedoes=6
        elif self.type=="Cruiser":
            self.hp=1400
            self.armor=200
            self.reloadTime=30
            self.numberOfCanons=6
        elif self.type=="Armored":
            self.hp=1600
            self.armor=400
            self.reloadTime=60
            self.numberOfCanons=8

        elif self.type=="Submarine":
            self.hp=300
            self.armor=800
            self.reloadTime=90
            self.numberOfNuces=1
            self.numberOfJericho=3
            self.numberOfTorpedoes=6
        pass


    def ShipFire(self,round):
        if self.type=="Destroyer":
            i=0
            while (i==0):
                if self.numberOfTorpedoes<=0:
                    #CANON BREAK
                    canon = self.numberOfCanons
                    Chance = random.randrange(0, 21)
                    if Chance == 10:
                        canon -= 2
                        print("Shit! Captain we lost 2 canons")
                    elif Chance == 5 or Chance == 20:
                        canon -= 1
                        print("Oh! Captain we lost 1 canon")

                    hp = 200 * (random.randrange(70, 101) / 100) * (canon / self.numberOfCanons)
                    i += 1
                    print(f"We are out of Torpedoes sir!!\nFiring HP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) ,0 , "Torpedoes")
                else:
                    bulletType = str(input(f"Select the bullet type {self.name}\nTP(Dealing Armor Damage ,HP(High-Spreader)"))
                    if bulletType.upper().strip()=="HP":
                        #CANON BREAK
                        canon = self.numberOfCanons
                        Chance = random.randrange(0, 21)
                        if Chance == 10:
                            canon -= 2
                            print("Shit! Captain we lost 2 canons")
                        elif Chance == 5 or Chance == 20:
                            canon -= 1
                            print("Oh! Captain we lost 1 canon")

                        hp = 200 * (random.randrange(70, 101) / 100) * (canon / self.numberOfCanons)
                        i += 1
                        print(f"Firing HP shells with {canon} out of {self.numberOfCanons} canons Captain {name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                        print("------------------------------------------------------------------------------------")
                        return (int(hp) ,0 , "TP")
                    elif bulletType.upper().strip()=="TP":
                        self.numberOfTorpedoes-=1
                        hit = 400 * (random.randrange(65, 91)/100)
                        percent=random.randrange(0,45)/100
                        hp , armor = hit*percent, hit*(1-percent)
                        i+=1
                        print(f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp+armor)} damage to the enemy ship!!")
                        print("------------------------------------------------------------------------------------")
                        return (int(hp) , int(armor) , "TP")

        elif self.type=="Cruiser":
            i=0
            while(i==0):
                bulletType=str(input(f"Select the bullet type {self.name}:\nAP(Armor-Piercing) ,HP(High-Spreader)"))
                # CANON BREAK
                canon = self.numberOfCanons
                Chance = random.randrange(0, 16)
                if Chance == 10:
                    canon -= 2
                    print("Shit! Captain we lost 2 canons")
                elif Chance == 5 or Chance == 15:
                    canon -= 1
                    print("Oh! Captain we lost 1 canon")

                if bulletType.upper() =="AP":
                    hit=200*(random.randrange(80,101)/100)*(canon/self.numberOfCanons)
                    percent=random.randrange(1,101)/100
                    hp , armor =hit*percent , hit*(1-percent)
                    i+=1
                    print(f"Firing AP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp+armor)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) , int(armor) , "AP")

                elif bulletType.upper() =="HP":
                    hp = 200 * (random.randrange(70, 101) / 100)*(canon/self.numberOfCanons)
                    i+=1
                    print(f"Firing HP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) , 0 , "HP")

        elif self.type=="Armored":
            i = 0
            while (i == 0):
                bulletType = str(input(f"Select the bullet type {self.name}:\nAP(Armor-Piercing) ,HP(High-Spreader)"))
                # CANON BREAK
                canon = self.numberOfCanons
                Chance = random.randrange(0, 26)
                if Chance == 10:
                    canon -= self.numberOfCanons
                    print("Shit! Captain we lost all canons")
                elif Chance == 5 or Chance == 10 or Chance==15 or Chance==20 or Chance==25:
                    canon -= 2
                    print("Oh! Captain we lost 2 canon")
                elif Chance == 2 or Chance == 4 or Chance == 6 or Chance==8 or Chance==10 or Chance==12:
                    canon -= 1
                    print("Captain we lost 1 canon")

                if bulletType.upper() == "AP":
                    hit = 400 * (random.randrange(80, 101) / 100) * (canon / self.numberOfCanons)
                    percent = random.randrange(1, 101) / 100
                    hp, armor = hit * percent, hit * (1 - percent)
                    i += 1
                    print(f"Firing AP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) , int(armor) , "AP")

                elif bulletType.upper() == "HP":
                    hp = 400 * (random.randrange(70, 101) / 100) * (canon / self.numberOfCanons)
                    i += 1
                    print(f"Firing HP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) , 0 , "HP")

        elif self.type=="Submarine":
            if self.numberOfNuces<=0:
                print(f"We are out of Nuclear Missiles sir!!\nTime to defend")
                print("------------------------------------------------------------------------------------")
                return (0, 0, "None")
            else:
                hit = 700 * (random.randrange(80, 101) / 100)
                percent=0.5
                hp , armor =hit*percent , hit*percent
                print(f"Firing Nuclear Missiles Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                print("------------------------------------------------------------------------------------")
                self.numberOfNuces-=1
                return (int(hp), int(armor),"Nuce")
        else:
           return False

    def ShipDefense(self,hp,armor ,round , bullet):
        if self.type == "Destroyer":
            print(f"DIRECT HIT SIR")
            if bullet=="AP" or bullet=="HP" or bullet=="Torpedoes":
                hp=hp * (random.randrange(90, 101) / 100)
                self.hp -= hp
                self.armor -= armor * (random.randrange(40, 61) / 100)
            elif bullet=="Nuce":
                self.hp -= hp
                self.armor = 0
            elif bullet=="Jericho":
                print(f"DIRECT HIT")
                hp=hp * (random.randrange(70, 81) / 100)
                self.hp -= hp
            print(f"-{int(hp)}hp\n-{int(armor)} armor")

        elif self.type == "Cruiser":
            if bullet == "AP" or bullet == "HP" or bullet == "Torpedoes":
                print(f"DIRECT HIT")
                hp=hp * (random.randrange(70, 91) / 100)
                armor=armor * (random.randrange(50, 71) / 100)
                self.hp -= hp
                self.armor -= armor
            elif bullet == "Nuce":
                self.hp -= hp
                self.armor = 0
            elif bullet=="Jericho":
                print(f"DIRECT HIT")
                hp=hp * (random.randrange(80, 91) / 100)
                self.hp -= hp
            print(f"-{int(hp)}hp\n-{int(armor)} armor")

        elif self.type == "Armored":
            if self.armor <= 0:
                self.hp -= hp
                self.armor=0
            else:
                self.hp -= hp * (random.randrange(50, 81) / 100)
                self.armor -= armor * (random.randrange(60, 81) / 100)
            print(f"-{int(hp)}hp\n-{int(armor)} armor")

        elif self.type == "Submarine":
            if bullet == "AP" or bullet == "HP" or bullet == "Torpedoes":
                print(f"DIRECT HIT")
                if self.armor <= 0:
                    self.hp -= hp
                    self.armor=0
                else:
                    hp=hp * (random.randrange(50, 81) / 100)
                    armor=armor * (random.randrange(70, 91) / 100)
                    self.hp -= hp
                    self.armor -= armor
            print(f"-{int(hp)}hp\n-{int(armor)} armor")
        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        print("------------------------------------------------------------------------------------")

        pass


Ship1 = BattleShips(typeList[0], nameList[0])
Ship2 = BattleShips(typeList[1], nameList[1])
ROUND=1
while not Ship1.hp<=0 or not Ship2.hp<=0 and not ROUND<=0:
    if Ship1.hp<=0:
        print(f"Captain {Ship2.name} is the ruler of the seas\nTHE END")
        ROUND = -1
        break
    elif Ship2.hp<=0:
        print(f"Captain {Ship1.name} is the ruler of the seas\nTHE END")
        ROUND=-1
        break
    print(f"~ROUND{ROUND}~")
    hp1 , armor1 , AMMUNATION=Ship1.ShipFire(ROUND)
    Ship2.ShipDefense(hp1 , armor1,ROUND , AMMUNATION)
    hp2, armor2 , AMMUNATION2=Ship2.ShipFire(ROUND)
    Ship1.ShipDefense(hp2,armor2,ROUND , AMMUNATION2)
    ROUND += 1

