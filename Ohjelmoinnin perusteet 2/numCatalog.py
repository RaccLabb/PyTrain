import json

def load_json():
        try:
            with open("contracts.json", "r", encoding="utf-8") as file:
                print("Tiedosto ladattu.")
                return json.load(file)
        except FileNotFoundError:
            with open("contracts.json", "w", encoding="utf-8") as file:
                 json.dump({}, file)
            print("Tiedostoa ei löytynyt.")
            return {}

def save_json(data):
    with open("contracts.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def getNum(catalog):
    name = input("Anna nimi: ")
    if name in catalog:
        print(catalog[name])
    else:
        print("Numeroa ei löytynyt!")

def printAll(catalog):
     print("Puhelinluettelo")
     print("." * 32)

     for name, num in catalog.items():#Printtaa dictionaryn hienommin
          print(f"{name:<20} {num}")

def addNum(catalog):
    name = input("Syötä nimi: ")
    num = input("Syötä numero: ")
    catalog[name] = num

def main():
    contract_Catalog = load_json()

    while True:
        print("1. Hae numero \n2.Lisää numero \n3.Tulosta kaikki \n4.Tallenna tiedot")
        command = int(input("Syötä toiminto: "))
        match command:
            case 1: #Hae numero
                  getNum(contract_Catalog)
            case 2: #Lisää numero
                  addNum(contract_Catalog) 
            case 3:
                  printAll(contract_Catalog)
            case 4:
                  save_json(contract_Catalog)
                
    
                  
if __name__=="__main__":
     main()   
