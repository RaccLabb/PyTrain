import random
import json

def load_english_json():
        try:
            with open("englishWords.json", "r", encoding="utf-8") as file:
                print("Tiedosto ladattu.")
                return json.load(file)
        except FileNotFoundError:
            with open("englishWords.json", "w", encoding="utf-8") as file:
                 json.dump({}, file)
            print("Tiedostoa ei löytynyt.")
            return {}

def load_swedish_json():
        try:
            with open("swedishWords.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            with open("swedishWords.json", "w", encoding="utf-8") as file:
                 json.dump({}, file)
            print("Tiedostoa ei löytynyt.")
            return {}
def main():
    language = int(input("Valitse kieli \n1. Englanti\n2. Ruotsi\n"))
    if language == 1:
         words = load_english_json()
         infoWord = "englanniksi"
    elif language == 2:
         words = load_swedish_json()
         infoWord = "ruotsiksi"

    lives = 3
    score = 0
    while lives > 0:
        keysInList = list(words.keys())
        key = random.choice(keysInList)

        answer = input(f"Mikä on {infoWord} sana {key}? ")
        if answer == words[key]:
            print("Oikein!")
            score += 1
        else:
            print(f"Väärin! Oikea vastaus olisi ollut {words[key]}")
            lives -= 1

if __name__=="__main__":
    main()