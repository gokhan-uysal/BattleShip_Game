import random, os, Greeting , pygame , sys
from Destroyer import Destroyer
from Cruiser import Cruiser
from Armored import Armored
from Submarine import Submarine

"""
nameList = ["Gökhan","Suhan"]
typeList = ["Cruiser","Armored"]
"""

nameList = []
typeList = []

def Intro(index):
    ShipList = ("Destroyer", "Cruiser", "Armored", "Submarine")
    if index == 1:
        print("Welcome to World of Warships")
        Greeting.Greetings("Captains")
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
    j = 0
    while (j == 0):
        print(ShipList)
        type = str(input("Now you can choose your ship from list"))
        if type.strip().capitalize() in ShipList:
            j += 1
            return (type.strip().capitalize(), name.capitalize().strip())
        else:
            print("Please choose appropriate ship type")
    pass


for i in range(1, 3):
    type, name = Intro(i)
    nameList.append(name)
    typeList.append(type)
print("Now Let's Start The Battle")
print("------------------------------------------------------------------------------------")


def main():
    if typeList[0]=="Destroyer":
        Ship1=Destroyer(nameList[0])
    elif typeList[0]=="Cruiser":
        Ship1 = Cruiser(nameList[0])
    elif typeList[0]=="Armored":
        Ship1 = Armored(nameList[0])
    elif typeList[0]=="Submarine":
        Ship1 = Submarine(nameList[0])

    if typeList[1] == "Destroyer":
        Ship2 = Destroyer(nameList[1])
    elif typeList[1] == "Cruiser":
        Ship2 = Cruiser(nameList[1])
    elif typeList[1] == "Armored":
        Ship2 = Armored(nameList[1])
    elif typeList[1] == "Submarine":
        Ship2 = Submarine(nameList[1])

    ROUND = 1
    while not Ship1.hp <= 0 or not Ship2.hp <= 0 and not ROUND <= 0:
        if ROUND==1:
            print(f"~ROUND{ROUND}~")
            hp1, armor1, AMMUNATION = Ship1.ShipFire(ROUND , 0 )
            breakCanon1 = Ship2.ShipDefense(hp1, armor1, ROUND, AMMUNATION)
            if Ship1.hp <= 0:
                print(f"Captain {Ship2.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            elif Ship2.hp <= 0:
                print(f"Captain {Ship1.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            hp2, armor2, AMMUNATION2 = Ship2.ShipFire(ROUND , breakCanon1)
            breakCanon2 = Ship1.ShipDefense(hp2, armor2, ROUND, AMMUNATION2)
            if Ship1.hp <= 0:
                print(f"Captain {Ship2.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            elif Ship2.hp <= 0:
                print(f"Captain {Ship1.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            ROUND += 1
        else:
            print(f"~ROUND{ROUND}~")
            hp1, armor1, AMMUNATION = Ship1.ShipFire(ROUND , breakCanon2)
            if Ship1.hp <= 0:
                print(f"Captain {Ship2.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            elif Ship2.hp <= 0:
                print(f"Captain {Ship1.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            breakCanon3 = Ship2.ShipDefense(hp1, armor1, ROUND, AMMUNATION)
            if Ship1.hp <= 0:
                print(f"Captain {Ship2.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            elif Ship2.hp <= 0:
                print(f"Captain {Ship1.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            hp2, armor2, AMMUNATION2 = Ship2.ShipFire(ROUND, breakCanon3)
            if Ship1.hp <= 0:
                print(f"Captain {Ship2.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            elif Ship2.hp <= 0:
                print(f"Captain {Ship1.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            breakCanon2 = Ship1.ShipDefense(hp2, armor2, ROUND, AMMUNATION2)
            if Ship1.hp <= 0:
                print(f"Captain {Ship2.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            elif Ship2.hp <= 0:
                print(f"Captain {Ship1.name} is the ruler of the seas\nTHE END")
                ROUND = -1
                break
            ROUND += 1


if __name__== "__main__":
    main()
