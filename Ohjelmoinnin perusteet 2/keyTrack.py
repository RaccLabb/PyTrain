def checkAccess(roomList, room, key):
    for area in roomList:
        if area == room[0:2]:
            for R in roomList[area]:
                if R == room:
                    if key in roomList[area][R]:
                        print(f"Avaimella {key} pääsee huoneeseen {room}.")
                    else:
                        print(f"Avaimella {key} ei ole pääsyoikeutta huoneesee {room}.")
def main():
    rooms = {#Toinen vaihtoeto olisi luoda avain kohtaiset rakenteet dictionaryyn, riippuen siitä kumpaa mielummin halutaan hallita huonetta vai avainta.       
        "A1":{
            "A120":["123","321"],
            "A140":["123","321","456"],
            "A160":["123","321"],
            "A180":["123","321"]
        },
        "A2":{
            "A220":["123","321"],
            "A240":["123"],
            "A260":["456","321"],
            "A280":["123","321"]
        },
        "A3":{
            "A320":["123","321"],
            "A340":["123","321"],
            "A360":["123","321"],
            "A380":["123","321"]
        },
        "A4":{
            "A420":["123","321"],
            "A440":["123","321"],
            "A460":["123","321"],
            "A480":["123","321"]
        }
    }
    while True:
        chosenKey = input("Syötä avaimen id: ")
        chosenRoom = input("Syötä huoneen tunnus: ")
        checkAccess(rooms, chosenRoom, chosenKey)


if __name__=="__main__":
    main()