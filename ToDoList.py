import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#--------------------Funktiot---------------------
#Tallennus
def save_lists(): 
     with open("todo_lists.json", "w", encoding="utf-8") as file:
          json.dump(to_do_lists, file, ensure_ascii=False, indent=4)

print("To Do -List")
print("Tervetuloa konsolipohjaiseen To Do listaan! " \
"Voit navigoida valikossa käyttämällä annettuja numeroita. \n")
inApp = True

try:
     with open("todo_lists.json", "r", encoding="utf-8") as file:
          to_do_lists = json.load(file)
except FileNotFoundError:
     to_do_lists = {}

while inApp:
    print("Listat: ")
    for index, list_name in enumerate(to_do_lists):
        print(index + 1, list_name)

    print("")
    #Päävalikko
    print("Valitse Toiminto: ")
    print("1. Lisää Lista ")
    print("2. Poista Lista ")
    print("3. Avaa Lista ")
    print("4. Sulje Ohjelma")

    mainAction = int(input("Valitse toiminto: "))
    os.system("cls")

    if mainAction == 1:
        list_name = input("Anna listalle nimi: ")
        to_do_lists[list_name] = []
        save_lists()
        os.system("cls")

    elif mainAction == 2:
        for list_name in to_do_lists:
            print(list_name)

        list_to_del = input("Mikä lista poistetaan? Kirjoita listan nimi.")
        if list_to_del in to_do_lists:
            to_do_lists.pop(list_to_del)
            save_lists()
        os.system("cls")

    elif mainAction == 3:
        list_names = list(to_do_lists.keys())
        for index, list_name in enumerate(list_names):
            print(index + 1, list_name)

        choice = int(input("Mikä lista avataan: "))
        openList = list_names[choice - 1]
        os.system("cls")

        #Listan sisällä
        inList = True
        while  inList:   
            print(f"{openList}:") 
            for index, task in enumerate(to_do_lists[openList]):
                print(index + 1, task)
            print("")

            #Lista valikko
            print("Valitse toiminto:")
            print("1. Lisää tehtävä")
            print("2. Poista tehtävä")
            print("3. Näytä lista")
            print("4. Takaisin")
            action = int(input())

            os.system("cls")

            #Lisää Tehtävä
            if action == 1:
                print(f"{openList}:") 
                to_do_lists[openList].append(input("Anna Tehtävä: "))
                save_lists()
            elif action == 2:
                print(f"{openList}:") 
                task_to_del = int(input("Anna poistettavan tehtävän numero: "))
                to_do_lists[openList].pop(task_to_del - 1)
                save_lists()
            elif action == 4:
                break
            os.system("cls")
    elif mainAction == 4:
        break





    


