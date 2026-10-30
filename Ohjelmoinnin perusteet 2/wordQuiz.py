import random
words = {"auto":"bil",
           "leipä":"bröd", 
           "juusto":"ost", 
           "kakku":"kaka", 
           "kala":"fisk", 
           "lintu":"fågel",
           "porkkana":"morot", 
           "punajuuri":"rödbeta", 
           "silta":"bro", 
           "kirja":"bok"}

lives = 3
score = 0
while lives > 0:
    keysInList = list(words.keys())
    key = random.choice(keysInList)

    answer = input(f"Mikä on ruotsiksi sana {key}? ")
    if answer == words[key]:
        print("Oikein!")
        score += 1
    else:
        print(f"Väärin! Oikea vastaus olisi ollut {words[key]}")
        lives -= 1

# En nyt tehnyt sellaista kun tehtävässä mutta, 
# jos olisin halunnut tehdä kymmenen sanaa ja laskea oikeat ja väärät niin se olisi ollut melkein sama. 
# Halusin omaan käyttöön sopivamman ja muutenkin ehkä paremman version,
# jossa saa niiin monta kertaa koittaa kunnes menee 3 kertaa väärin.