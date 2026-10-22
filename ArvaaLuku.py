import random

"""1. Arvaa numero

Harjoittelee: random, while, ehtolauseet

Tee ohjelma, joka:
Arpoo numeron 1–100 väliltä.
Pyytää käyttäjää arvaamaan.
Kertoo onko arvaus liian suuri vai pieni.
Lopettaa, kun numero löytyy.
Näyttää yritysten määrän.

Lisähaaste:
Lisää vaikeustasot."""
userName = input("Anna käyttäjänimi: ")
difficulty = input("Valitse vaikeustaso: Helppo, Keskivaikea tai Vaikea: ")
userNum = 0
pcNum = 0
if difficulty == "Helppo" or difficulty == "helppo":
    print(f"Tervetulo pelamaan {userName} numeronarvaus -peliä vaikeustasolla Helppo! Tämä on todella helppoa, arvaat vain luvun 1-10 väliltä. Sinulla on 4 yritystä.")

    #Arvaukset
    lives = 4
    #PC:n arpomaluku
    pcNum = random.randint(1,10)

    while lives > 0:
        userNum = int(input("Anna luku väliltä 1-10: "))
        if userNum == pcNum:
            print(f"Oikein! Arvauksia jäi jäljelle {lives - 1}")
            break
        lives -= 1
        print(f"Väärin! Arvauksia jäljellä {lives}")
        if lives == 0:
            print("Hävisti pelin!")
            break

if difficulty == "Keskivaikea" or difficulty == "keskivaikea":
    print(f"Tervetulo pelamaan {userName} numeronarvaus -peliä vaikeustasolla Helppo! Tämä on todella helppoa, arvaat vain luvun 1-10 väliltä. Sinulla on 4 yritystä.")

    #Arvaukset
    lives = 4
    #PC:n arpomaluku
    pcNum = random.randint(1,100)

    while lives > 0:
        userNum = int(input("Anna luku väliltä 1-100: "))
        if userNum == pcNum:
            print(f"Oikein! Arvauksia jäi jäljelle {lives - 1}")
            break
        lives -= 1
        print(f"Väärin! Arvauksia jäljellä {lives}")
        if lives == 0:
            print("Hävisti pelin!")
            break

if difficulty == "Vaikea" or difficulty == "vaikea":
    print(f"Tervetulo pelamaan {userName} numeronarvaus -peliä vaikeustasolla Helppo! Tämä on todella helppoa, arvaat vain luvun 1-1000 väliltä. Sinulla on 5 yritystä.")

    #Arvaukset
    lives = 5
    #PC:n arpomaluku
    pcNum = random.randint(1,1000)

    while lives > 0:
        userNum = int(input("Anna luku väliltä 1-1000: "))
        if userNum == pcNum:
            print(f"Oikein! Arvauksia jäi jäljelle {lives - 1}")
            break
        lives -= 1
        print(f"Väärin! Arvauksia jäljellä {lives}")
        if lives == 0:
            print("Hävisti pelin!")
            break

print(f"Kiitos pelaamisesta {userName}!")


    