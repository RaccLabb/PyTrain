import os
class book:
    def __init__(self, isbn, bName, author, amount):
        self.isbn = isbn
        self.bName = bName
        self.author = author
        self.amount = amount

    
def addBook():
    isbn = input("Syötä kirjan ISBN: ")
    bookName = input("Syötä kirjan nimi: ") 
    author = input("Syötä kirjailijan nimi: ")
    amount = int(input("Syötä kirjojen määrä: "))
    global books
    books.append(book(isbn,bookName,author,amount))

def deleteBook():
    #ISBN
    bookCode = input("Syötä poistettavan kirjan ISBN: ")
    global books
    for book in books:
        if book.isbn == bookCode:
            books.remove(book)


if __name__=="__main__":

    books = [book("12345", "Saiman Salaisuus", "PetteriR", 12)]
    
    while True:
        print("1. Kirjan lisäys \n 2. Poista kirja \n 3. Tarkastele listaa \n 0. Poistu")
        command = int(input("Valitse toiminto"))

        if command == 1:
            os.system("cls")
            addBook()

        elif command == 2:
            os.system("cls")
            deleteBook()

        elif command == 3:
            os.system("cls")
            for book in books:
                print(f"ISBN: {book.isbn}\nBook name: {book.bName}\nAuthor: {book.author}\nAmount: {book.amount}\n")
                print()
                
        elif command == 0:
            break

        else:
            print("Virheellinen komento!")
            continue

