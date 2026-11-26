import os
class product:
    def __init__(self, pName, pPrice, pNum):
        self.name = pName
        self.price = pPrice
        self.num = pNum
        
    def getPrice(self):#hakee tuotteen hinnan
        return self.price

    def setPrice(self, pPrice):#Asettaa tuotteen hinnan
        self.price = pPrice

def priceHandler(productlist, pNum):#Käsittelee hinnan muutosta
    productPrice = productlist[pNum].getPrice()
    while True:
        changedPrice = float(input(f"Vanha hinta: {productPrice}, Syötä uusi hinta: "))
        difference = abs(productPrice - changedPrice) / max(productPrice, changedPrice)
        if changedPrice <= 0.1 or difference > 0.1:
            print("Virheellinen hinta!\nHinta saa muuttua enintään 10% ja oltava vähintään 0.10€.")
            continue
        productlist[pNum].setPrice(changedPrice)
        print(f"Uusi hinta on {productlist[pNum].price}")
        break

def main():
    products = {}
    while True:
        os.system("cls")
        print("Tuote katalogi")
        for item in products.values():
            print(f"{item.name}")
            print(f"EAN: {item.num}")
            print(f"Hinta: {item.price}")
            print()

        command = int(input("1. Lisää tuote\n2. Muokkaa hintaa\n"))
        if command == 1:
            newName = input("Syötä tuotteen nimi: ")
            newPrice = float(input("Syötä tuotteen hinta: "))
            newNum = input("Syötä tuotteen numero: ")
            products[newNum] = product(newName, newPrice, newNum)
        elif command == 2:
            misClicks = 0 #Laskee virheelliset koodit
            while True:
                productNum = input("Syötä tuotteen numero: ")
                if productNum in products:                   
                    priceHandler(products, productNum)
                    break
                elif misClicks > 1:#Kolmannella heittää ulos loopista
                    break
                else: 
                    print("Virheellinen koodi")
                    misClicks += 1
                    continue
    
if __name__=="__main__":
    main()