import random
import os
import winsound

def checkTheWin(chosenIcons):
    moneyWon = 0.0
    global freeGames
    global playerMoney
    global multiplier


    if freeGames > 0: # Laksetaan vapaa pelien määrää
        freeGames -= 1
        wasFreegame = True
    else:
        wasFreegame = False
    #Valitaan oikea palkinto
    if chosenIcons.count("🍬") == 2:
        moneyWon = 0.10
    elif chosenIcons.count("🍬") == 3 or chosenIcons.count("🧹") == 2:
        moneyWon = 0.20
    elif chosenIcons.count("🧹") == 3 or chosenIcons.count("🫟") == 2:
        moneyWon = 1.00
    elif chosenIcons.count("🫟") == 3 or chosenIcons.count("🧛") == 2:
        moneyWon = 3.00
    elif chosenIcons.count("🧛") == 3 or chosenIcons.count("⚰️") == 2:
        moneyWon = 5.00
    elif chosenIcons.count("⚰️") == 3 or chosenIcons.count("🎃") == 2:
        moneyWon = 8.00
    elif chosenIcons.count("🎃") == 3:
        moneyWon = 10.00
    elif chosenIcons.count("☠️") == 3:
        freeGames += 10
        winsound.MessageBeep(winsound.MB_ICONHAND)
    elif chosenIcons.count("☠️") == 2:
        freeGames += 3
        winsound.MessageBeep(winsound.MB_ICONHAND)


    if moneyWon > 0.0:
        print(f"Voitit {moneyWon*multiplier} euroa!")
        if wasFreegame == False:
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
    else:
        print("Ei voittoa :(")
        if wasFreegame == False:
            winsound.MessageBeep(winsound.MB_ICONSTOP)


    playerMoney += moneyWon * multiplier
    playerMoney = round(playerMoney, 2)



def rollTheIcons(listOfIconlists):
        #"Pyöräyttää" pelin ikoneita
        chosenPossibility = []
        for iconList in listOfIconlists:
            icon = random.choice(iconList)
            chosenPossibility.append(icon)

        if freeGames == 0:
            os.system("cls")#Tyhjätään konsoli

        print(chosenPossibility)
        checkTheWin(chosenPossibility)



if __name__=="__main__":
    print("Tervetuloa pelaamaan Hedelmäpeliä. Halloween -Edition")

    listOfPossibilities = [["🍬","🧹","🎃","🫟", "🧛","⚰️","☠️"],["🍬","🧹","🎃","🫟", "🧛","⚰️","☠️"],["🍬","🧹","🎃","🫟", "🧛","⚰️","☠️"]]
    while True: #Ollaan luupissa kunnes annetaan sopiva summa
        playerMoney = float(input("Lisää rahaa vähintään 0.20€."))
        if playerMoney >= 0.2:
            break

        os.system("cls")#Tyhjätään konsoli

        print("Virheellinen rahasumma!")

    freeGames = 0
    multiplier = 1
    while True:
        if freeGames == 0: # jos ei ole vapaapelejä kysytään haluaako pelaaja pelata ja jos on niin ohitetaan kerroin vilpin vuoksi
            inputTextList = [f"Rahamäärä on {playerMoney}€.", f"Kerroin on {multiplier}X.", "2. Muuta kerroin", "1. Pyöräytä", "0. Lopeta peli"]
            for i in inputTextList:
                print(i)
            roll = input("Valitse toiminto: ") #Jos eri kuin 1 tai 0 kysyy uudelleen.

        if roll == "0" or playerMoney < 0.20: #Lopeta peli
            break

        elif roll == "1" or freeGames > 0:#Jatka peliä
            if playerMoney - 0.2 * multiplier >= 0:
                if freeGames == 0: # Jos ei vapaa pelejä, pelaaja joutuu maksamaan, muuten mennään vapaapeilin
                    playerMoney -= 0.2 * multiplier 
                rollTheIcons(listOfPossibilities)

            else: 
                print("Ei tarpeeksi rahaa!")

        elif roll == "2":
            while True:
                multiplier = int(input("Anna kerroin väliltä 1-10, vain kokonaisluvut sallittu: "))
                if multiplier >= 1 and multiplier <= 10 and multiplier % 1 == 0:
                    break #Tarkistetaan onko kerroin oikeanlainen
                else:
                    print("Anna sopiva kerroin!")
