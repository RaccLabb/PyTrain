print("LASKIN /n")
play = True

while play:

    def sum_calc(num1, num2):
        print(f"{num1} + {num2} = {num1 + num2}")

    def multiplier_calc (num1, num2):
        print(f"{num1} * {num2} = {num1 * num2}")

    def div_calc(num1, num2):
        print(f"{num1} / {num2} = {num1 / num2}")
    correct = False
    while correct == False:
        calc = input("Anna lasku esim. 2 + 31: ")
        parts = calc.split()
        #Tarkastetaan että on kirjoitettu oikein
        if len(parts) == 3:
            num1, oper, num2 = calc.split()
            if oper == "+":
                sum_calc(float(num1), float(num2))
                correct = True
            elif oper == "*":
                multiplier_calc(float(num1), float(num2))
                correct = True
            elif oper == "/":
                div_calc(float(num1), float(num2))
                correct = True
            else:
                print("Lasku epäonnistui. Syötä lasku muodossa 14 * 5. Hyväksyttävät laskumerkt ovat + - * /")
                correct = False
        else:
            print("Lasku epäonnistui. Syötä lasku muodossa 7 / 2. Muista välit luvun ja laskumerkin välille!")    

    correct = False
    #Jatkamisen tarkastus
    while correct == False:
        playInp = input("Lasketanko vielä? Kyllä tai Ei: ")
        if playInp == "Ei" or playInp == "ei":
            correct = True
            play = False
            
        elif playInp == "Kyllä" or playInp == "kyllä":
            play = True
            correct = True
            
        else :
            print(f"Kirjoitit {playInp}. Tämä on väärin.")    
