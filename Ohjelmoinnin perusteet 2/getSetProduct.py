import os
class product:
    def __init__(self, pName, pPrice, pNum):
        self.name = pName
        self.__price = pPrice
        self.num = pNum
    @property    
    def price(self):#hakee tuotteen hinnan
        return self.__price

    @price.setter
    def price(self, pPrice):#Asettaa tuotteen hinnan
        difference = abs(self.price - pPrice) / max(self.price, pPrice)
        if pPrice >= 0.1 or difference < 0.1:
            self.__price = pPrice
            

def priceHandler(productlist, pNum):#Käsittelee hinnan muutosta
    productPrice = productlist[pNum].price
    while True:
        changedPrice = float(input(f"Vanha hinta: {productPrice}, Syötä uusi hinta: "))
        productlist[pNum].price = changedPrice
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