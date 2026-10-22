import os
import time
import random

#Print stat list on start
def print_list():
        listLenght = len(nameList)
        i = 1
        while listLenght > 0:
            print(f"{i}. {nameList[listLenght - 1]} ajalla: {playTimeList[listLenght - 1]:.2f}s")
            listLenght -= 1
            i += 1


nameList = []
playTimeList = []
while True:
    if len(nameList) > 0:
        print_list()

    name = input("Anna nimimerkki: ")
    os.system("cls")
    
    #Difficulty
    print("Helppo")
    print("Keskivaikea")
    print("Vaikea")
    difficulty = input("Valitse vaikeustaso: ")
    os.system("cls")
    easyList = ["auto","kissa", "koira" , "tietokone", "lapio", "kaivinkone", "lentokone", "possu", "lista", "kettu", "pullo", "kulta", "hopea" , "jääkiekko", "jalkapallo"]
    mediumList = ["lentoemäntä", "ammattikorkeakoulu", "kvanttitietokone", "yliopistokahvila", "jääkärirykmentti", "apulaissheriffi", "sienirihmasto","kielitaidonhuoltaja"]
    hardList = ["Lentokoneenhuoltoajoneuvo", "Korkeakoulun opinto-ohjaaja", "Maanmittauslaitos", ]

    rounds = 1
    startTime = time.perf_counter()

        #Core game
    while rounds < 3:
        insertedWord = ""

        #Word lists for different difficulties
        if difficulty == "Helppo":
            word = random.choice(easyList)
        elif difficulty == "Keskivaikea":
            word = random.choice(mediumList)
        elif difficulty == "Vaikea":
            word = random.choice(hardList)

        print(word)
        while insertedWord != word:
            insertedWord = input("Kirjoita tähän: ")
        print("Oikein!")
        rounds += 1
        os.system("cls")

    endTime = time.perf_counter()
    playTime = endTime - startTime
    print(f"Pääsit pelin läpi ajassa {playTime:.2f}s")
    nameList.append(name)
    playTimeList.append(playTime)
    os.system("cls")

    #Asks player if it wants to try again
    while True:
        playagain = int(input("Pelataanko uudestaan 0 / 1: "))
        if playagain == 0 or playagain == 1:
            break
        else:
            continue
    if playagain == 0:
        break
    else:
        continue



