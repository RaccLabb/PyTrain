import os

def addBook(addbooks):
    isbn = input("Syötä kirjan ISBN: ")
    bookName = input("Syötä kirjan nimi: ") 
    author = input("Syötä kirjailijan nimi: ")
    amount = int(input("Syötä kirjojen määrä: "))
    
    addbooks[isbn] = {
        "otsikko" : bookName,
        "kirjailija" : author,
        "kappaleet" : amount
    }
    return addbooks

def deleteBook(delbooks):
    #ISBN
    bookCode = input("Syötä poistettavan kirjan ISBN: ")

    if bookCode in delbooks:
        del delbooks[bookCode]
        print(f"Kirja {bookCode} on poistettu.")
    else:
        print(f"Kirjaa {bookCode} ei löytynyt.")
    return delbooks

def printBooks(bookList):

    for book in bookList:
        print(f"{bookList[book]["otsikko"]}, {bookList[book]["kirjailija"]}")
        print(f"Kappaleet: {bookList[book]["kappaleet"]}\n\n")

def showAmoun(bookList):
    amounts = 0
    for isbn in bookList.values():
        amounts += isbn["kappaleet"]
    print(amounts)


if __name__=="__main__":
    #Kijroja testausta varten valmiina
    books = {    
        "978-0-306": {
        "otsikko": "Introduction to Algorithms",
        "kirjailija": "Thomas H. Cormen",
        "kappaleet": 5
    },
    "978-0-672": {
        "otsikko": "Python Crash Course",
        "kirjailija": "Eric Matthes",
        "kappaleet": 8
    },
    "978-0-07": {
        "otsikko": "Clean Code",
        "kirjailija": "Robert C. Martin",
        "kappaleet": 3
    },
    "978-1-491": {
        "otsikko": "Deep Learning",
        "kirjailija": "Ian Goodfellow",
        "kappaleet": 2
    },
    "978-0-321": {
        "otsikko": "The Pragmatic Programmer",
        "kirjailija": "Andrew Hunt",
        "kappaleet": 6
    }}

    while True:
        print("1. Kirjan lisäys \n 2. Poista kirja \n 3. Tarkastele listaa \n 4. Kirjojen kokonaismäärä \n 0. Poistu")
        command = int(input("Valitse toiminto"))

        if command == 1:
            os.system("cls")
            books = addBook(books)

        elif command == 2:
            os.system("cls")
            books = deleteBook(books)

        elif command == 3:
            os.system("cls")
            printBooks(books)

        elif command == 4:
            os.system("cls")
            showAmount(books)

        elif command == 0:
            break

        else:
            print("Virheellinen komento!")
            continue

