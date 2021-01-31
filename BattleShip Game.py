import random ,os , pandas as pd ,Greeting
nameList=[]
typeList=[]
def Intro():
    print("Welcome to World of Warships")
    name = str(input("Can I have your name captain!!"))
    ShipList=("Destroyer","Cruiser","Armored")
    print(ShipList)
    i=0
    j=0
    while (i==0):
        Info=str(input("Do you want to learn more about BattleShips\nAdvice: Take time and read them carefully [yes/no]"))
        if Info.strip().lower()=="yes":
            f=open("BattleShips.txt","r")
            print(f.read())
            i+=1
        elif Info.strip().lower()=="no":
            i+=1
        else:
            print("Please write yes or no")

    while (j==0):
        print(ShipList)
        type=str(input("Now you can choose your ship from list"))
        if type.strip().capitalize() in ShipList:
            j += 1
            return (type.strip().capitalize() , name.capitalize())
        else:
            print("Please choose appropriate ship type")
    pass
for i in range(2):
    type , name =Intro()
    nameList.append(name)
    typeList.append(type)
print("Now Let's Start The Battle")
print("------------------------------------------------------------------------------------")

class BattleShips:
    def __init__(self,type,name):
        self.type = type
        self.name = name
        if type=="Destroyer":
            self.hp=800
            self.armor=100
            self.reloadTime=10
            self.numberOfCanons=4
            self.numberOfTorpedoes=4
        elif type=="Cruiser":
            self.hp=1400
            self.armor=200
            self.reloadTime=30
            self.numberOfCanons=6
        elif type=="Armored":
            self.hp=2000
            self.armor=400
            self.reloadTime=60
            self.numberOfCanons=8
        pass

    def ShipFire(self):

        def CanonBreak():
            numberOfCanons = self.numberOfCanons
            Chance = random.randrange(0, 21)
            if Chance == 10:
                numberOfCanons -= 2
                print("Shit! Captain we lost 2 canons")
            elif Chance == 5 or Chance == 20:
                numberOfCanons -= 1
                print("Oh! Captain we lost 1 canon")
            return numberOfCanons
            pass

        if self.type=="Destroyer":
            i=0
            while (i==0):
                if self.numberOfTorpedoes<=0:
                    numberOfCanons = CanonBreak()
                    hp = 200 * (random.randrange(70, 101) / 100) * (numberOfCanons / self.numberOfCanons)
                    i += 1
                    print(f"We are out of Torpedoes sir!!\nFiring HP shells with {numberOfCanons} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) ,0)
                else:
                    bulletType = str(input(f"Select the bullet type {self.name}\nTP(Dealing Armor Damage ,HP(High-Spreader)"))
                    if bulletType.upper().strip()=="HP":
                        numberOfCanons = CanonBreak()
                        hp = 200 * (random.randrange(70, 101) / 100) * (numberOfCanons / self.numberOfCanons)
                        i += 1
                        print(f"Firing HP shells with {numberOfCanons} out of {self.numberOfCanons} canons Captain {name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                        print("------------------------------------------------------------------------------------")
                        return (int(hp) ,0)
                    elif bulletType.upper().strip()=="TP":
                        self.numberOfTorpedoes=self.numberOfTorpedoes-1
                        hit = 400 * (random.randrange(65, 91)/100)
                        percent=random.randrange(0,45)/100
                        hp , armor = hit*percent, hit*(1-percent)
                        i+=1
                        print(f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp+armor)} damage to the enemy ship!!")
                        print("------------------------------------------------------------------------------------")
                        return (int(hp) , int(armor))

        elif self.type=="Cruiser":
            i=0
            while(i==0):
                bulletType=str(input(f"Select the bullet type {self.name}:\nAP(Armor-Piercing) ,HP(High-Spreader)"))
                if bulletType.upper() =="AP":
                    numberOfCanons=CanonBreak()
                    hit=200*(random.randrange(80,101)/100)*(numberOfCanons/self.numberOfCanons)
                    percent=random.randrange(1,101)/100
                    hp , armor =hit*percent , hit*(1-percent)
                    i+=1
                    print(f"Firing AP shells with {numberOfCanons} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp+armor)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) , int(armor))

                elif bulletType.upper() =="HP":
                    numberOfCanons = CanonBreak()
                    hp = 200 * (random.randrange(70, 101) / 100)*(numberOfCanons/self.numberOfCanons)
                    i+=1
                    print(f"Firing HP shells with {numberOfCanons} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) , 0)

        elif type=="Armored":
            i = 0
            while (i == 0):
                bulletType = str(input(f"Select the bullet type {self.name}:\nAP(Armor-Piercing) ,HP(High-Spreader)"))
                if bulletType.upper() == "AP":
                    numberOfCanons = CanonBreak()
                    hit = 200 * (random.randrange(80, 101) / 100) * (numberOfCanons / self.numberOfCanons)
                    percent = random.randrange(1, 101) / 100
                    hp, armor = hit * percent, hit * (1 - percent)
                    i += 1
                    print(f"Firing AP shells with {numberOfCanons} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) , int(armor))

                elif bulletType.upper() == "HP":
                    numberOfCanons = CanonBreak()
                    hp = 200 * (random.randrange(70, 101) / 100) * (numberOfCanons / self.numberOfCanons)
                    i += 1
                    print(f"Firing HP shells with {numberOfCanons} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp) , 0)

    def ShipDefense(self,hp,armor):

        if self.type == "Destroyer":
            self.hp -= hp * (random.randrange(90, 101) / 100)
            self.armor -= armor * (random.randrange(40, 61) / 100)
            print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        elif self.type == "Cruiser":
            self.hp -= hp * (random.randrange(70, 91) / 100)
            self.armor -= armor * (random.randrange(50, 71) / 100)
            print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        elif self.type == "Armored":
            self.hp -= hp * (random.randrange(50, 81) / 100)
            self.armor -= armor * (random.randrange(60, 81) / 100)
            print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        if self.hp <= 0:
            BattleShips(type, name).TheEnd()
            return "END"
        pass

    def TheEnd(self):
        print(f"Captains are the last to leave their ships\nTHE END")
        print("------------------------------------------------------------------------------------")
        return "END"

Ship1 = BattleShips(typeList[0], nameList[0])
Ship2 = BattleShips(typeList[1], nameList[1])
while not Ship1.hp<=0 or not Ship2.hp<=0:
    print(Ship1.hp,Ship2.hp)
    hp1 , armor1=Ship1.ShipFire()
    Ship2.ShipDefense(hp1 , armor1)
    hp2, armor2=Ship2.ShipFire()
    Ship1.ShipDefense(hp2,armor2)

